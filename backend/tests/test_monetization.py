"""Backend tests for monetization layer: admin, settings, reviews, payments, chat limit."""
import os
import uuid
import hmac
import hashlib
import pytest
import requests

BASE_URL = os.environ.get("REACT_APP_BACKEND_URL", "https://excel-helper-20.preview.emergentagent.com").rstrip("/")
API = f"{BASE_URL}/api"

ADMIN_EMAIL = os.environ.get("ADMIN_EMAIL")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
USER_EMAIL = "test@example.com"
USER_PASSWORD = "test123"


def _login_or_signup(email: str, password: str, name: str = "User"):
    r = requests.post(f"{API}/auth/login", json={"email": email, "password": password})
    if r.status_code != 200:
        requests.post(f"{API}/auth/signup", json={"email": email, "password": password, "name": name})
        r = requests.post(f"{API}/auth/login", json={"email": email, "password": password})
    assert r.status_code == 200, f"login failed for {email}: {r.text}"
    return r.json()


@pytest.fixture(scope="module")
def admin_data():
    if not ADMIN_EMAIL or not ADMIN_PASSWORD:
        pytest.skip("Admin credentials not configured. Set ADMIN_EMAIL and ADMIN_PASSWORD in the environment.")
    return _login_or_signup(ADMIN_EMAIL, ADMIN_PASSWORD, "Rajel Admin")


@pytest.fixture(scope="module")
def admin_headers(admin_data):
    return {"Authorization": f"Bearer {admin_data['token']}", "Content-Type": "application/json"}


@pytest.fixture(scope="module")
def user_data():
    return _login_or_signup(USER_EMAIL, USER_PASSWORD, "Test User")


@pytest.fixture(scope="module")
def user_headers(user_data):
    return {"Authorization": f"Bearer {user_data['token']}", "Content-Type": "application/json"}


# ============= AUTH / ADMIN PROMOTION =============
class TestAdminPromotion:
    def test_admin_login_is_admin_true(self, admin_data):
        assert admin_data["user"]["email"] == ADMIN_EMAIL
        assert admin_data["user"].get("is_admin") is True

    def test_user_login_is_admin_false(self, user_data):
        assert user_data["user"].get("is_admin") is False

    def test_me_returns_flags(self, admin_headers, user_headers):
        r1 = requests.get(f"{API}/auth/me", headers=admin_headers)
        assert r1.status_code == 200
        u1 = r1.json()
        assert u1["is_admin"] is True
        assert "is_pro" in u1

        r2 = requests.get(f"{API}/auth/me", headers=user_headers)
        assert r2.status_code == 200
        u2 = r2.json()
        assert u2["is_admin"] is False
        assert u2["is_pro"] is False


# ============= ADMIN STATS =============
class TestAdminStats:
    def test_stats_forbidden_for_non_admin(self, user_headers):
        r = requests.get(f"{API}/admin/stats", headers=user_headers)
        assert r.status_code == 403

    def test_stats_unauthorized_no_auth(self):
        r = requests.get(f"{API}/admin/stats")
        assert r.status_code in (401, 403)

    def test_stats_admin_ok(self, admin_headers):
        r = requests.get(f"{API}/admin/stats", headers=admin_headers)
        assert r.status_code == 200
        data = r.json()
        for f in ["total_users", "pro_users", "free_users", "total_chats",
                  "total_reviews", "avg_rating", "total_revenue_inr"]:
            assert f in data, f"missing stat field {f}"
        assert data["total_users"] >= 1


# ============= ADMIN USERS / REVIEWS =============
class TestAdminLists:
    def test_users_admin_only(self, user_headers):
        r = requests.get(f"{API}/admin/users", headers=user_headers)
        assert r.status_code == 403

    def test_users_admin_ok(self, admin_headers):
        r = requests.get(f"{API}/admin/users", headers=admin_headers)
        assert r.status_code == 200
        users = r.json()
        assert isinstance(users, list) and len(users) >= 1
        for u in users:
            assert "password_hash" not in u
            assert "_id" not in u

    def test_admin_reviews_admin_only(self, user_headers, admin_headers):
        r1 = requests.get(f"{API}/admin/reviews", headers=user_headers)
        assert r1.status_code == 403
        r2 = requests.get(f"{API}/admin/reviews", headers=admin_headers)
        assert r2.status_code == 200
        assert isinstance(r2.json(), list)


# ============= ADMIN SETTINGS =============
class TestAdminSettings:
    def test_get_settings_admin_only(self, user_headers):
        r = requests.get(f"{API}/admin/settings", headers=user_headers)
        assert r.status_code == 403

    def test_get_settings_returns_all_fields(self, admin_headers):
        r = requests.get(f"{API}/admin/settings", headers=admin_headers)
        assert r.status_code == 200
        s = r.json()
        for f in ["razorpay_key_id", "razorpay_key_secret", "google_review_url",
                  "pro_price_inr", "free_daily_chat_limit"]:
            assert f in s

    def test_put_settings_persists(self, admin_headers):
        # Save current settings to restore later
        cur = requests.get(f"{API}/admin/settings", headers=admin_headers).json()
        new_url = f"https://g.page/test-{uuid.uuid4().hex[:6]}"
        payload = {
            "google_review_url": new_url,
            "pro_price_inr": 299,
            "free_daily_chat_limit": 5,
        }
        r = requests.put(f"{API}/admin/settings", headers=admin_headers, json=payload)
        assert r.status_code == 200, r.text
        updated = r.json()
        assert updated["google_review_url"] == new_url
        assert updated["pro_price_inr"] == 299
        assert updated["free_daily_chat_limit"] == 5

        # GET back to confirm persistence
        r2 = requests.get(f"{API}/admin/settings", headers=admin_headers)
        assert r2.status_code == 200
        assert r2.json()["google_review_url"] == new_url

        # Restore previous URL (don't leak test data)
        requests.put(f"{API}/admin/settings", headers=admin_headers,
                     json={"google_review_url": cur.get("google_review_url", "")})


# ============= PUBLIC CONFIG =============
class TestPublicConfig:
    def test_config_no_auth_required(self):
        r = requests.get(f"{API}/config")
        assert r.status_code == 200
        c = r.json()
        for f in ["razorpay_key_id", "razorpay_configured", "google_review_url",
                  "pro_price_inr", "free_daily_chat_limit"]:
            assert f in c, f"missing {f}"
        # Crucial: secret never leaks publicly
        assert "razorpay_key_secret" not in c
        assert isinstance(c["razorpay_configured"], bool)


# ============= REVIEWS =============
class TestReviews:
    def test_post_review_requires_auth(self):
        r = requests.post(f"{API}/reviews", json={"rating": 5, "comment": "nope"})
        assert r.status_code in (401, 403)

    def test_post_and_update_review(self, user_headers):
        r1 = requests.post(f"{API}/reviews", headers=user_headers,
                           json={"rating": 4, "comment": "Great app"})
        assert r1.status_code == 200, r1.text
        d1 = r1.json()
        assert d1["rating"] == 4
        assert d1["comment"] == "Great app"
        rid = d1["id"]

        # Same user posts again -> should UPDATE same review (one per user)
        r2 = requests.post(f"{API}/reviews", headers=user_headers,
                           json={"rating": 5, "comment": "Even better!"})
        assert r2.status_code == 200
        d2 = r2.json()
        assert d2["id"] == rid, "Expected same review id (update, not create)"
        assert d2["rating"] == 5
        assert d2["comment"] == "Even better!"

    def test_list_reviews_public(self):
        r = requests.get(f"{API}/reviews")
        assert r.status_code == 200
        assert isinstance(r.json(), list)

    def test_my_review(self, user_headers):
        r = requests.get(f"{API}/reviews/me", headers=user_headers)
        assert r.status_code == 200
        body = r.json()
        # After previous test, should have one
        assert "rating" in body or body == {}

    def test_review_rating_validation(self, user_headers):
        r = requests.post(f"{API}/reviews", headers=user_headers,
                          json={"rating": 6, "comment": "bad"})
        assert r.status_code == 422


# ============= PAYMENTS =============
class TestPayments:
    def test_create_order_503_when_not_configured(self, user_headers, admin_headers):
        # Ensure razorpay keys are empty
        requests.put(f"{API}/admin/settings", headers=admin_headers,
                     json={"razorpay_key_id": "", "razorpay_key_secret": ""})
        r = requests.post(f"{API}/payments/create-order",
                          headers=user_headers, json={"plan": "pro_monthly"})
        assert r.status_code == 503, r.text
        assert "configured" in r.text.lower() or "razorpay" in r.text.lower()

    def test_create_order_requires_auth(self):
        r = requests.post(f"{API}/payments/create-order", json={"plan": "pro_monthly"})
        assert r.status_code in (401, 403)

    def test_verify_invalid_signature(self, user_headers, admin_headers):
        # Configure a fake secret so the verify path runs (not 503)
        fake_secret = "test_secret_key_123"
        requests.put(f"{API}/admin/settings", headers=admin_headers,
                     json={"razorpay_key_id": "rzp_test_fakekey", "razorpay_key_secret": fake_secret})
        try:
            r = requests.post(f"{API}/payments/verify", headers=user_headers, json={
                "razorpay_order_id": "order_test_123",
                "razorpay_payment_id": "pay_test_123",
                "razorpay_signature": "deadbeef" * 8,  # invalid
            })
            assert r.status_code == 400
            assert "signature" in r.text.lower()
        finally:
            # Reset to empty so other tests still see 503
            requests.put(f"{API}/admin/settings", headers=admin_headers,
                         json={"razorpay_key_id": "", "razorpay_key_secret": ""})

    def test_verify_valid_signature_promotes_pro(self, admin_headers):
        # Create a fresh user so we can mark them pro safely
        email = f"TEST_pay_{uuid.uuid4().hex[:6]}@example.com"
        sd = requests.post(f"{API}/auth/signup",
                           json={"email": email, "password": "pw12345", "name": "Pay"}).json()
        h = {"Authorization": f"Bearer {sd['token']}", "Content-Type": "application/json"}

        fake_secret = "verify_secret_xyz"
        requests.put(f"{API}/admin/settings", headers=admin_headers,
                     json={"razorpay_key_id": "rzp_test_v", "razorpay_key_secret": fake_secret})
        try:
            order_id = "order_verify_1"
            payment_id = "pay_verify_1"
            msg = f"{order_id}|{payment_id}".encode()
            sig = hmac.new(fake_secret.encode(), msg, hashlib.sha256).hexdigest()
            r = requests.post(f"{API}/payments/verify", headers=h, json={
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": sig,
            })
            assert r.status_code == 200, r.text
            assert r.json().get("is_pro") is True
            # Confirm via /me
            me = requests.get(f"{API}/auth/me", headers=h).json()
            assert me["is_pro"] is True
        finally:
            requests.put(f"{API}/admin/settings", headers=admin_headers,
                         json={"razorpay_key_id": "", "razorpay_key_secret": ""})


# ============= CHAT USAGE / LIMIT =============
class TestChatLimit:
    def test_chat_usage_pro_admin(self, admin_headers):
        r = requests.get(f"{API}/chat/usage", headers=admin_headers)
        assert r.status_code == 200
        u = r.json()
        # admin treated as pro from limit perspective per spec
        assert "is_pro" in u
        assert "used" in u and "limit" in u and "remaining" in u

    def test_chat_usage_free_user(self, user_headers):
        r = requests.get(f"{API}/chat/usage", headers=user_headers)
        assert r.status_code == 200
        u = r.json()
        assert u["is_pro"] is False
        assert u["limit"] == 5
        assert u["used"] >= 0
        assert u["remaining"] == max(0, 5 - u["used"])
