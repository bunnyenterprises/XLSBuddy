"""Backend integration tests for XLSBUDDY API."""
import os
import uuid
import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "https://excel-helper-20.preview.emergentagent.com").rstrip("/")
API = f"{BASE_URL}/api"

# Pre-seeded test user
TEST_EMAIL = "test@example.com"
TEST_PASSWORD = "test123"


@pytest.fixture(scope="session")
def api():
    s = requests.Session()
    s.headers.update({"Content-Type": "application/json"})
    return s


@pytest.fixture(scope="session")
def auth_token(api):
    r = api.post(f"{API}/auth/login", json={"email": TEST_EMAIL, "password": TEST_PASSWORD})
    if r.status_code != 200:
        # Try signup
        api.post(f"{API}/auth/signup", json={"email": TEST_EMAIL, "password": TEST_PASSWORD, "name": "Test User"})
        r = api.post(f"{API}/auth/login", json={"email": TEST_EMAIL, "password": TEST_PASSWORD})
    assert r.status_code == 200, f"Login failed: {r.text}"
    return r.json()["token"]


@pytest.fixture(scope="session")
def auth_headers(auth_token):
    return {"Authorization": f"Bearer {auth_token}", "Content-Type": "application/json"}


# ---------------- AUTH ----------------
class TestAuth:
    def test_signup_new_user(self, api):
        email = f"TEST_{uuid.uuid4().hex[:8]}@example.com"
        r = api.post(f"{API}/auth/signup", json={"email": email, "password": "pw12345", "name": "Tester"})
        assert r.status_code == 200, r.text
        data = r.json()
        assert "token" in data and isinstance(data["token"], str) and len(data["token"]) > 10
        assert data["user"]["email"] == email
        assert "password_hash" not in data["user"]

    def test_signup_duplicate(self, api):
        r = api.post(f"{API}/auth/signup", json={"email": TEST_EMAIL, "password": "x", "name": "x"})
        assert r.status_code == 400

    def test_login_valid(self, api):
        r = api.post(f"{API}/auth/login", json={"email": TEST_EMAIL, "password": TEST_PASSWORD})
        assert r.status_code == 200
        assert "token" in r.json()

    def test_login_invalid(self, api):
        r = api.post(f"{API}/auth/login", json={"email": TEST_EMAIL, "password": "wrong"})
        assert r.status_code == 401

    def test_me_requires_auth(self, api):
        r = api.get(f"{API}/auth/me")
        assert r.status_code in (401, 403)

    def test_me_returns_user(self, api, auth_headers):
        r = requests.get(f"{API}/auth/me", headers=auth_headers)
        assert r.status_code == 200
        u = r.json()
        assert u["email"] == TEST_EMAIL
        assert "password_hash" not in u


# ---------------- FUNCTIONS ----------------
class TestFunctions:
    def test_list(self, api):
        r = api.get(f"{API}/functions")
        assert r.status_code == 200
        data = r.json()
        assert isinstance(data, list)
        assert len(data) >= 60, f"Expected ~65 functions, got {len(data)}"
        assert "name" in data[0]

    def test_categories(self, api):
        r = api.get(f"{API}/functions/categories")
        assert r.status_code == 200
        cats = r.json()
        assert isinstance(cats, list)
        assert cats == sorted(cats)
        for expected in ["Math", "Logical", "Lookup", "Text", "Date/Time", "Statistical", "Financial"]:
            assert expected in cats, f"Missing category {expected}"

    def test_search_filter(self, api):
        r = api.get(f"{API}/functions", params={"search": "VLOOKUP"})
        assert r.status_code == 200
        data = r.json()
        assert any("VLOOKUP" in f["name"].upper() for f in data)

    def test_category_filter(self, api):
        r = api.get(f"{API}/functions", params={"category": "Math"})
        assert r.status_code == 200
        data = r.json()
        assert len(data) > 0
        for f in data:
            assert f["category"] == "Math"

    def test_get_one(self, api):
        all_funcs = api.get(f"{API}/functions").json()
        fid = all_funcs[0]["id"]
        r = api.get(f"{API}/functions/{fid}")
        assert r.status_code == 200
        assert r.json()["id"] == fid

    def test_get_404(self, api):
        r = api.get(f"{API}/functions/nope-id")
        assert r.status_code == 404


# ---------------- TUTORIALS ----------------
class TestTutorials:
    def test_list(self, api):
        r = api.get(f"{API}/tutorials")
        assert r.status_code == 200
        data = r.json()
        assert len(data) >= 8

    def test_search(self, api):
        r = api.get(f"{API}/tutorials", params={"search": "pivot"})
        assert r.status_code == 200

    def test_get_one(self, api):
        tuts = api.get(f"{API}/tutorials").json()
        tid = tuts[0]["id"]
        r = api.get(f"{API}/tutorials/{tid}")
        assert r.status_code == 200
        assert "content" in r.json()


# ---------------- CHAT ----------------
class TestChat:
    def test_message_requires_auth(self, api):
        r = api.post(f"{API}/chat/message", json={"content": "hi"})
        assert r.status_code in (401, 403)

    def test_send_message_creates_session(self, auth_headers):
        r = requests.post(
            f"{API}/chat/message",
            headers=auth_headers,
            json={"content": "What does VLOOKUP do? Reply briefly."},
            timeout=60,
        )
        assert r.status_code == 200, r.text
        data = r.json()
        assert "session_id" in data
        assert data["user_message"]["role"] == "user"
        assert data["assistant_message"]["role"] == "assistant"
        assert len(data["assistant_message"]["content"]) > 5
        TestChat._sid = data["session_id"]

    def test_list_sessions(self, auth_headers):
        r = requests.get(f"{API}/chat/sessions", headers=auth_headers)
        assert r.status_code == 200
        sessions = r.json()
        assert isinstance(sessions, list)
        assert len(sessions) >= 1

    def test_get_messages(self, auth_headers):
        sid = getattr(TestChat, "_sid", None)
        if not sid:
            pytest.skip("No session id")
        r = requests.get(f"{API}/chat/sessions/{sid}/messages", headers=auth_headers)
        assert r.status_code == 200
        msgs = r.json()
        assert len(msgs) >= 2

    def test_delete_session(self, auth_headers):
        sid = getattr(TestChat, "_sid", None)
        if not sid:
            pytest.skip("No session id")
        r = requests.delete(f"{API}/chat/sessions/{sid}", headers=auth_headers)
        assert r.status_code == 200
        # verify gone
        r2 = requests.get(f"{API}/chat/sessions/{sid}/messages", headers=auth_headers)
        assert r2.status_code == 404
