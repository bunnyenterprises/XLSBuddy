"""Seed Excel functions and tutorials into MongoDB."""

_HINDI_EXPLANATIONS = {
    "SUM": "मान लो तुम्हारे पास अलग-अलग गुल्लकों में सिक्के हैं। SUM सभी गुल्लकों के सिक्के जोड़कर कुल बताता है!",
    "AVERAGE": "अगर 4 दोस्तों के नंबर 80, 90, 70 और 60 हैं, तो AVERAGE बताता है कि बराबर बांटने पर सबको कितने मिलते — यानी 75!",
    "MIN": "जैसे क्लास में सबसे छोटे बच्चे को ढूंढना — MIN सभी नंबरों में से सबसे छोटा ढूंढता है!",
    "MAX": "जैसे क्लास में सबसे लंबे बच्चे को ढूंढना — MAX सभी नंबरों में से सबसे बड़ा ढूंढता है!",
    "ROUND": "अगर जवाब 3.14159 है लेकिन 2 decimal चाहिए, तो ROUND इसे 3.14 कर देता है — जैसे अतिरिक्त हिस्सा काट देना!",
    "ROUNDUP": "ROUNDUP हमेशा ऊपर जाता है — 3.1 भी 4 हो जाता है! जैसे होटल जो 61 मिनट के लिए भी पूरे घंटे का चार्ज करे!",
    "ROUNDDOWN": "ROUNDDOWN हमेशा नीचे जाता है — 3.9 भी 3 हो जाता है! जैसे सिर्फ पूरे सेब गिनना, आधे खाए सेब नहीं!",
    "MOD": "10 मिठाइयां 3 दोस्तों में बांटो — सबको 3 मिले और 1 बच जाए। MOD वही बचा हुआ remainder बताता है!",
    "ABS": "ABS माइनस का निशान हटा देता है! चाहे ₹7 दो या ₹7 मिलें, ABS हमेशा '7' कहेगा। यह हमेशा positive होता है!",
    "POWER": "POWER किसी नंबर को खुद से कई बार गुणा करता है। POWER(2,10) मतलब 2×2×2×2×2×2×2×2×2×2 = 1024!",
    "SQRT": "SQRT वह नंबर ढूंढता है जिसे खुद से गुणा करने पर तुम्हारा नंबर मिले। SQRT(16)=4 क्योंकि 4×4=16!",
    "SUMIF": "SUMIF एक नियम के साथ जोड़ता है! 'सिर्फ 100 से बड़े नंबर जोड़ो।' SUMIF तुम्हारा नियम मानता है!",
    "SUMIFS": "SUMIFS कई नियमों के साथ जोड़ता है! 'East region की और 50 से ऊपर की sales जोड़ो।' एक साथ दो नियम!",
    "IF": "IF ट्रैफिक लाइट जैसा है! अगर नंबर 50 से ज्यादा है तो 'Pass' दिखाओ, नहीं तो 'Fail'। एक नियम — दो जवाब!",
    "IFS": "IFS एक-एक करके कई नियम जांचता है — जैसे grading: 90 से ऊपर = A, 80 = B, 70 = C। जो पहले सच हो वही जवाब!",
    "AND": "AND मतलब 'दोनों सच होने चाहिए'। पार्क जाने के लिए: धूप हो AND वीकएंड हो। एक भी गलत तो जवाब गलत!",
    "OR": "OR मतलब 'कम से कम एक सच होना चाहिए'। मिठाई के लिए: सब्जी खाई हो OR जन्मदिन हो। एक काफी है!",
    "NOT": "NOT जवाब पलट देता है! NOT(TRUE) = FALSE। जैसे 'उल्टा दिन' — हर चीज़ उल्टी हो जाती है!",
    "IFERROR": "अगर formula गलत हो जाए (जैसे शून्य से भाग), तो IFERROR गलती पकड़कर backup जवाब दिखाता है!",
    "IFNA": "IFNA सिर्फ 'नहीं मिला' वाली गलती (#N/A) पकड़ता है। जब VLOOKUP कुछ न ढूंढे, IFNA 'नहीं मिला' दिखाता है!",
    "VLOOKUP": "जैसे फोन बुक! VLOOKUP को नाम दो, वह पहले column में ढूंढता है, फिर उसी row से दूसरे column की value लाता है!",
    "HLOOKUP": "VLOOKUP जैसा लेकिन आड़ा! HLOOKUP ऊपरी row में ढूंढता है, फिर नीचे तुम्हारी मनचाही row में जाता है!",
    "XLOOKUP": "VLOOKUP का सुपर अपग्रेड! XLOOKUP दाएं-बाएं दोनों तरफ खोज सकता है और 'नहीं मिला' का अपना संदेश दे सकता है!",
    "INDEX": "INDEX खज़ाने के नक्शे जैसा है। 'तीसरी पंक्ति, दूसरा column' — INDEX वहां जो है वह दे देता है!",
    "MATCH": "MATCH ढूंढता है कि कोई चीज़ list में कहां है। 'राहुल कहां है?' MATCH कहता है 'दूसरी जगह पर!' INDEX के साथ बेहतरीन!",
    "INDIRECT": "INDIRECT text में लिखा cell का पता पढ़कर वहां जाता है। जैसे 'तीसरा घर, Oak Street' पढ़कर वहां पहुंचना!",
    "OFFSET": "OFFSET एक cell से शुरू होकर हिलता है। 'A1 से 2 नीचे और 3 दाएं जाओ' — तुम D3 पर पहुंचोगे!",
    "CHOOSE": "CHOOSE list से नंबर के हिसाब से चुनता है। CHOOSE(2, 'लाल', 'नीला', 'हरा') — दूसरा यानी 'नीला' चुनता है!",
    "CONCAT": "CONCAT text जोड़ता है! CONCAT('नमस्ते ', 'दुनिया') = 'नमस्ते दुनिया'। जैसे दो कागज़ एक साथ चिपकाना!",
    "TEXTJOIN": "TEXTJOIN शब्दों की list को separator के साथ जोड़ता है। 'सेब, केला, चेरी' — बीच में comma लगाकर!",
    "LEFT": "LEFT शब्द के शुरू से अक्षर देता है। LEFT('Excel', 2) देता है 'Ex' — पहले 2 अक्षर!",
    "RIGHT": "RIGHT शब्द के अंत से अक्षर देता है। RIGHT('Excel', 3) देता है 'cel' — आखिरी 3 अक्षर!",
    "MID": "MID बीच से काटता है। MID('Excel', 2, 3) दूसरे अक्षर से 3 अक्षर लेता है: 'xce'!",
    "LEN": "LEN शब्द में अक्षरों की गिनती करता है। LEN('Hello') = 5 क्योंकि 5 अक्षर हैं। जैसे माला में मोती गिनना!",
    "TRIM": "TRIM text के extra spaces हटा देता है। जैसे बिखरे वाक्य को साफ करना — शुरू, अंत और बीच के extra gaps हटाना!",
    "UPPER": "UPPER सभी अक्षर CAPITAL बना देता है। UPPER('hello') = 'HELLO'। जैसे CAPS LOCK लगाना!",
    "LOWER": "LOWER सभी अक्षर छोटे बना देता है। LOWER('HELLO') = 'hello'। जैसे धीरे-धीरे बोलना!",
    "PROPER": "PROPER हर शब्द का पहला अक्षर CAPITAL बनाता है। 'john doe' बनता है 'John Doe' — नाम लिखने का तरीका!",
    "SUBSTITUTE": "SUBSTITUTE text में एक शब्द की जगह दूसरा रखता है। जैसे Find & Replace — लेकिन formula में!",
    "FIND": "FIND किसी अक्षर की position ढूंढता है। FIND('@', 'jane@work.com') = 5, क्योंकि @ पांचवें नंबर पर है!",
    "SEARCH": "SEARCH, FIND जैसा है लेकिन UPPER/lower case की परवाह नहीं करता। 'world' खोजो 'Hello World' में — मिल जाएगा!",
    "TEXT": "TEXT नंबर को मनचाहे रूप में दिखाता है। TEXT(1234.5, '₹#,##0.00') = '₹1,234.50' — नंबर को ड्रेस पहनाना!",
    "TODAY": "TODAY() आज की तारीख खुद-ब-खुद बताता है। हर बार Excel खोलो, यह update हो जाता है — जैसे स्मार्ट कैलेंडर!",
    "NOW": "NOW() अभी की तारीख AND समय बताता है। जैसे एक घड़ी जो तारीख भी दिखाए — एक ही cell में!",
    "DATE": "DATE तीन अलग नंबरों से तारीख बनाता है। DATE(2026, 6, 15) बनाता है 15 जून 2026 — तारीख के हिस्से जोड़ना!",
    "DAY": "DAY किसी तारीख से सिर्फ दिन का नंबर निकालता है। DAY('15 June 2026') = 15। कैलेंडर से सिर्फ दिन पढ़ना!",
    "MONTH": "MONTH किसी तारीख से सिर्फ महीने का नंबर निकालता है। MONTH('15 June 2026') = 6। जून 6वां महीना है!",
    "YEAR": "YEAR किसी तारीख से सिर्फ साल निकालता है। YEAR('15 June 2026') = 2026। कैलेंडर से सिर्फ साल पढ़ना!",
    "WEEKDAY": "WEEKDAY बताता है कि तारीख सप्ताह के किस दिन है। 15 जून सोमवार है या शुक्रवार? WEEKDAY नंबर में बताता है!",
    "DATEDIF": "DATEDIF दो तारीखों के बीच का अंतर बताता है। '2020 से 2026 में कितने साल?' DATEDIF कहता है 6! उम्र निकालने के लिए!",
    "EOMONTH": "EOMONTH महीने का आखिरी दिन बताता है। फरवरी 2026 के लिए 28 बताएगा। खुद जानता है हर महीने में कितने दिन!",
    "NETWORKDAYS": "NETWORKDAYS दो तारीखों के बीच सिर्फ काम के दिन (सोम-शुक्र) गिनता है, वीकएंड छोड़कर। Project deadline के लिए!",
    "COUNT": "COUNT सिर्फ नंबर वाले cells गिनता है। Text और blank को ignore करता है। सिर्फ नंबर वाले cells की गिनती!",
    "COUNTA": "COUNTA सभी भरे हुए cells गिनता है — नंबर हों, text हो, कुछ भी। जैसे form में कितनों ने नाम भरा!",
    "COUNTIF": "COUNTIF एक नियम से गिनता है। '50 से ज्यादा नंबर कितने हैं?' COUNTIF तुरंत बताता है — स्मार्ट tally counter!",
    "COUNTIFS": "COUNTIFS कई नियमों से एक साथ गिनता है। 'Class A के और 50 से ज्यादा नंबर वाले कितने?' दो नियम, एक जवाब!",
    "MEDIAN": "MEDIAN सभी नंबरों को क्रम में लगाने के बाद बीच वाला देता है। 10,20,30,40,50 में median = 30। बीच का नंबर!",
    "MODE": "MODE वह नंबर बताता है जो सबसे ज्यादा बार आया। 'सबसे ज्यादा छात्रों को कितने नंबर मिले?' सबसे लोकप्रिय जवाब!",
    "STDEV": "STDEV बताता है नंबर कितने अलग-अलग हैं। सबके 75 नंबर = STDEV 0। 10 से 100 तक = बड़ा STDEV!",
    "RANK": "RANK बताता है कि list में एक नंबर कहां खड़ा है। 90 नंबर मिले और बाकी सब कम = RANK कहता है #1!",
    "PMT": "PMT हर महीने loan की किस्त बताता है। ₹10,000 उधार 5% पर 5 साल के लिए? PMT बताएगा हर महीने कितना देना है!",
    "FV": "FV (Future Value) बताता है बचत कितनी बढ़ेगी। हर महीने ₹100 10 साल तक 6% ब्याज पर — FV दिखाएगा कुल कितना होगा!",
    "PV": "PV (Present Value) बताता है भविष्य का पैसा आज कितना है। 5 साल बाद ₹10,000 मिलेंगे — PV बताएगा आज उसकी value क्या है!",
    "NPV": "NPV किसी business के future मुनाफे को आज की value में जोड़ता है। 'क्या यह investment worth it है?' Positive NPV = हां!",
    "IRR": "IRR वह interest rate ढूंढता है जिस पर investment break-even करे। 'मेरे पैसे पर असल में कितना % return मिल रहा है?'",
}

# Merge Hindi explanations into EXCEL_FUNCTIONS after list is defined (done at bottom of file)

# visual_example shape:
#   data: list of [cellRef, value] rows (the sample input cells)
#   formula_cell: where the formula sits (e.g., "B1")
#   formula: the formula string
#   result: the displayed result
# OR for text/date/single-input functions:
#   data: list of [label, value]  — used as a small key/value block
#   formula_cell, formula, result same

def _vurl(name):
    """LearnSkillsDaily channel search URL for a function."""
    return f"https://www.youtube.com/@learnskillsdaily/search?query=excel+{name}+function+tutorial"

def _hurl(name):
    """YouTube Hindi search URL for a function."""
    return f"https://www.youtube.com/results?search_query=excel+{name}+formula+in+hindi"

EXCEL_FUNCTIONS = [
    # ============= MATH =============
    {
        "name": "SUM", "category": "Math",
        "syntax": "=SUM(number1, [number2], ...)",
        "description": "Adds all the numbers in a range of cells.",
        "example": "=SUM(A1:A10) returns the sum of values in A1 through A10.",
        "use_case": "Calculate totals, like total sales or expenses.",
        "visual_example": {"data": [["A1", 10], ["A2", 20], ["A3", 30]], "formula_cell": "B1", "formula": "=SUM(A1:A3)", "result": 60},
        "simple_explanation": "Imagine you have coins in different piggy banks. SUM adds ALL the coins from every piggy bank and tells you the grand total!",
        "video_url": _vurl("SUM"),
        "video_url_hindi": _hurl("SUM"),
    },
    {
        "name": "AVERAGE", "category": "Math",
        "syntax": "=AVERAGE(number1, [number2], ...)",
        "description": "Returns the arithmetic mean of the arguments.",
        "example": "=AVERAGE(B1:B5) returns the average of cells B1 to B5.",
        "use_case": "Find the average score, average price, or average performance.",
        "visual_example": {"data": [["A1", 80], ["A2", 90], ["A3", 70], ["A4", 60]], "formula_cell": "B1", "formula": "=AVERAGE(A1:A4)", "result": 75},
        "simple_explanation": "If 4 friends scored 80, 90, 70 and 60, AVERAGE figures out what score they ALL get if marks were shared equally — that's 75!",
        "video_url": _vurl("AVERAGE"),
        "video_url_hindi": _hurl("AVERAGE"),
    },
    {
        "name": "MIN", "category": "Math",
        "syntax": "=MIN(number1, [number2], ...)",
        "description": "Returns the smallest number in a set of values.",
        "example": "=MIN(A1:A20) returns the smallest value in A1:A20.",
        "use_case": "Find the lowest price or smallest measurement.",
        "visual_example": {"data": [["A1", 45], ["A2", 12], ["A3", 78], ["A4", 23]], "formula_cell": "B1", "formula": "=MIN(A1:A4)", "result": 12},
        "simple_explanation": "Like finding the shortest kid in class — MIN looks at all numbers and picks the smallest one!",
        "video_url": _vurl("MIN"),
        "video_url_hindi": _hurl("MIN"),
    },
    {
        "name": "MAX", "category": "Math",
        "syntax": "=MAX(number1, [number2], ...)",
        "description": "Returns the largest number in a set of values.",
        "example": "=MAX(A1:A20) returns the largest value in the range.",
        "use_case": "Find the peak revenue or top score.",
        "visual_example": {"data": [["A1", 45], ["A2", 12], ["A3", 78], ["A4", 23]], "formula_cell": "B1", "formula": "=MAX(A1:A4)", "result": 78},
        "simple_explanation": "Like finding the tallest kid in class — MAX looks at all numbers and picks the biggest one!",
        "video_url": _vurl("MAX"),
        "video_url_hindi": _hurl("MAX"),
    },
    {
        "name": "ROUND", "category": "Math",
        "syntax": "=ROUND(number, num_digits)",
        "description": "Rounds a number to a specified number of digits.",
        "example": "=ROUND(3.14159, 2) returns 3.14.",
        "use_case": "Round monetary values to 2 decimal places.",
        "visual_example": {"data": [["A1", 3.14159]], "formula_cell": "B1", "formula": "=ROUND(A1, 2)", "result": 3.14},
        "simple_explanation": "If your answer is 3.14159 but you only need 2 decimal places, ROUND trims it neatly to 3.14 — like cutting the extra off!",
        "video_url": _vurl("ROUND"),
        "video_url_hindi": _hurl("ROUND"),
    },
    {
        "name": "ROUNDUP", "category": "Math",
        "syntax": "=ROUNDUP(number, num_digits)",
        "description": "Rounds a number up, away from zero.",
        "example": "=ROUNDUP(3.2, 0) returns 4.",
        "use_case": "Always round up shipping counts.",
        "visual_example": {"data": [["A1", 3.2]], "formula_cell": "B1", "formula": "=ROUNDUP(A1, 0)", "result": 4},
        "simple_explanation": "ROUNDUP always goes UP — even 3.1 becomes 4! Like a cinema that charges for the full hour even if the movie is 61 minutes.",
        "video_url": _vurl("ROUNDUP"),
        "video_url_hindi": _hurl("ROUNDUP"),
    },
    {
        "name": "ROUNDDOWN", "category": "Math",
        "syntax": "=ROUNDDOWN(number, num_digits)",
        "description": "Rounds a number down, towards zero.",
        "example": "=ROUNDDOWN(3.9, 0) returns 3.",
        "use_case": "Truncate decimals when computing whole units.",
        "visual_example": {"data": [["A1", 3.9]], "formula_cell": "B1", "formula": "=ROUNDDOWN(A1, 0)", "result": 3},
        "simple_explanation": "ROUNDDOWN always goes DOWN — even 3.9 becomes 3! Like counting only whole apples and ignoring the half-eaten ones.",
        "video_url": _vurl("ROUNDDOWN"),
        "video_url_hindi": _hurl("ROUNDDOWN"),
    },
    {
        "name": "MOD", "category": "Math",
        "syntax": "=MOD(number, divisor)",
        "description": "Returns the remainder after a number is divided by a divisor.",
        "example": "=MOD(10, 3) returns 1.",
        "use_case": "Identify even/odd rows or alternating patterns.",
        "visual_example": {"data": [["A1", 10], ["A2", 3]], "formula_cell": "B1", "formula": "=MOD(A1, A2)", "result": 1},
        "simple_explanation": "Share 10 candies among 3 friends equally — everyone gets 3 and there's 1 left over. MOD gives you that leftover remainder!",
        "video_url": _vurl("MOD"),
        "video_url_hindi": _hurl("MOD"),
    },
    {
        "name": "ABS", "category": "Math",
        "syntax": "=ABS(number)",
        "description": "Returns the absolute value of a number.",
        "example": "=ABS(-7) returns 7.",
        "use_case": "Compute distance or magnitude regardless of sign.",
        "visual_example": {"data": [["A1", -7]], "formula_cell": "B1", "formula": "=ABS(A1)", "result": 7},
        "simple_explanation": "ABS removes the minus sign! Whether you owe 7 rupees or have 7 rupees, ABS always says '7'. It's the positive version!",
        "video_url": _vurl("ABS"),
        "video_url_hindi": _hurl("ABS"),
    },
    {
        "name": "POWER", "category": "Math",
        "syntax": "=POWER(number, power)",
        "description": "Returns the result of a number raised to a power.",
        "example": "=POWER(2, 10) returns 1024.",
        "use_case": "Compound interest, exponential growth.",
        "visual_example": {"data": [["A1", 2], ["A2", 10]], "formula_cell": "B1", "formula": "=POWER(A1, A2)", "result": 1024},
        "simple_explanation": "POWER multiplies a number by itself many times. POWER(2,10) means 2×2×2×2×2×2×2×2×2×2 = 1024!",
        "video_url": _vurl("POWER"),
        "video_url_hindi": _hurl("POWER"),
    },
    {
        "name": "SQRT", "category": "Math",
        "syntax": "=SQRT(number)",
        "description": "Returns the square root of a number.",
        "example": "=SQRT(16) returns 4.",
        "use_case": "Engineering and statistical calculations.",
        "visual_example": {"data": [["A1", 16]], "formula_cell": "B1", "formula": "=SQRT(A1)", "result": 4},
        "simple_explanation": "SQRT finds the number that when multiplied by itself gives your number. SQRT(16) = 4 because 4×4 = 16!",
        "video_url": _vurl("SQRT"),
        "video_url_hindi": _hurl("SQRT"),
    },
    {
        "name": "SUMIF", "category": "Math",
        "syntax": "=SUMIF(range, criteria, [sum_range])",
        "description": "Sums the cells specified by a given criteria.",
        "example": "=SUMIF(A1:A10, \">100\") sums values greater than 100.",
        "use_case": "Sum sales above threshold or by category.",
        "visual_example": {"data": [["A1", 50], ["A2", 150], ["A3", 80], ["A4", 200]], "formula_cell": "B1", "formula": "=SUMIF(A1:A4, \">100\")", "result": 350},
        "simple_explanation": "Like SUM but with a rule! 'Add up all numbers, but ONLY if they are bigger than 100.' SUMIF follows your rule!",
        "video_url": _vurl("SUMIF"),
        "video_url_hindi": _hurl("SUMIF"),
    },
    {
        "name": "SUMIFS", "category": "Math",
        "syntax": "=SUMIFS(sum_range, criteria_range1, criteria1, ...)",
        "description": "Sums based on multiple criteria.",
        "example": "=SUMIFS(C:C, A:A, \"East\", B:B, \">50\")",
        "use_case": "Multi-condition aggregations.",
        "visual_example": {"data": [["A1=East, B1=100", "—"], ["A2=West, B2=80", "—"], ["A3=East, B3=60", "—"]], "formula_cell": "C1", "formula": "=SUMIFS(B1:B3, A1:A3, \"East\")", "result": 160},
        "simple_explanation": "Like SUMIF but with MANY rules! 'Add sales, but ONLY from East region AND ONLY above 50.' Two rules at once!",
        "video_url": _vurl("SUMIFS"),
        "video_url_hindi": _hurl("SUMIFS"),
    },

    # ============= LOGICAL =============
    {
        "name": "IF", "category": "Logical",
        "syntax": "=IF(logical_test, value_if_true, value_if_false)",
        "description": "Returns one value if a condition is true and another if false.",
        "example": "=IF(A1>50, \"Pass\", \"Fail\")",
        "use_case": "Conditional grading, status flags.",
        "visual_example": {"data": [["A1", 75]], "formula_cell": "B1", "formula": "=IF(A1>50, \"Pass\", \"Fail\")", "result": "Pass"},
        "simple_explanation": "IF is like a traffic light! IF the score is above 50, show 'Pass' (green); otherwise show 'Fail' (red). It checks a rule and picks an answer!",
        "video_url": _vurl("IF"),
        "video_url_hindi": _hurl("IF"),
    },
    {
        "name": "IFS", "category": "Logical",
        "syntax": "=IFS(test1, value1, test2, value2, ...)",
        "description": "Checks multiple conditions and returns the value for the first TRUE.",
        "example": "=IFS(A1>=90, \"A\", A1>=80, \"B\", A1>=70, \"C\", TRUE, \"F\")",
        "use_case": "Cleaner alternative to nested IFs.",
        "visual_example": {"data": [["A1", 85]], "formula_cell": "B1", "formula": "=IFS(A1>=90,\"A\", A1>=80,\"B\", A1>=70,\"C\", TRUE,\"F\")", "result": "B"},
        "simple_explanation": "IFS checks many rules one by one — like grading: above 90 = A, above 80 = B, above 70 = C. The first rule that's true wins!",
        "video_url": _vurl("IFS"),
        "video_url_hindi": _hurl("IFS"),
    },
    {
        "name": "AND", "category": "Logical",
        "syntax": "=AND(logical1, logical2, ...)",
        "description": "Returns TRUE if all arguments are true.",
        "example": "=AND(A1>0, B1>0)",
        "use_case": "Compound conditions inside IF.",
        "visual_example": {"data": [["A1", 5], ["B1", 10]], "formula_cell": "C1", "formula": "=AND(A1>0, B1>0)", "result": "TRUE"},
        "simple_explanation": "AND is like 'both must be true'. To go to the park: it must be sunny AND it must be weekend. If even one is false, the whole answer is false!",
        "video_url": _vurl("AND"),
        "video_url_hindi": _hurl("AND"),
    },
    {
        "name": "OR", "category": "Logical",
        "syntax": "=OR(logical1, logical2, ...)",
        "description": "Returns TRUE if any argument is true.",
        "example": "=OR(A1=\"Yes\", B1=\"Yes\")",
        "use_case": "Either-or conditional checks.",
        "visual_example": {"data": [["A1", "No"], ["B1", "Yes"]], "formula_cell": "C1", "formula": "=OR(A1=\"Yes\", B1=\"Yes\")", "result": "TRUE"},
        "simple_explanation": "OR is like 'at least one must be true'. You can eat dessert if you finished vegetables OR it's your birthday. Just one needs to be true!",
        "video_url": _vurl("OR"),
        "video_url_hindi": _hurl("OR"),
    },
    {
        "name": "NOT", "category": "Logical",
        "syntax": "=NOT(logical)",
        "description": "Reverses the logic of its argument.",
        "example": "=NOT(A1=B1)",
        "use_case": "Invert a boolean condition.",
        "visual_example": {"data": [["A1", 5], ["B1", 5]], "formula_cell": "C1", "formula": "=NOT(A1=B1)", "result": "FALSE"},
        "simple_explanation": "NOT flips the answer! NOT(TRUE) = FALSE and NOT(FALSE) = TRUE. Like saying 'opposite day' — everything gets reversed!",
        "video_url": _vurl("NOT"),
        "video_url_hindi": _hurl("NOT"),
    },
    {
        "name": "IFERROR", "category": "Logical",
        "syntax": "=IFERROR(value, value_if_error)",
        "description": "Returns a custom value if a formula produces an error.",
        "example": "=IFERROR(A1/B1, 0)",
        "use_case": "Suppress #DIV/0! and other errors.",
        "visual_example": {"data": [["A1", 100], ["B1", 0]], "formula_cell": "C1", "formula": "=IFERROR(A1/B1, 0)", "result": 0},
        "simple_explanation": "If a formula goes wrong (like dividing by zero), IFERROR catches the mistake and shows your backup answer instead of an ugly error!",
        "video_url": _vurl("IFERROR"),
        "video_url_hindi": _hurl("IFERROR"),
    },
    {
        "name": "IFNA", "category": "Logical",
        "syntax": "=IFNA(value, value_if_na)",
        "description": "Returns custom value when a formula returns #N/A.",
        "example": "=IFNA(VLOOKUP(A1,B:C,2,FALSE), \"Not Found\")",
        "use_case": "Cleaner VLOOKUP error handling.",
        "visual_example": {"data": [["A1", "Mango"], ["B-list", "Apple, Banana"]], "formula_cell": "C1", "formula": "=IFNA(VLOOKUP(A1,B1:B2,1,FALSE),\"Not Found\")", "result": "Not Found"},
        "simple_explanation": "IFNA is like IFERROR but only catches the 'not found' error. When VLOOKUP can't find something, IFNA shows 'Not Found' instead of #N/A!",
        "video_url": _vurl("IFNA"),
        "video_url_hindi": _hurl("IFNA"),
    },

    # ============= LOOKUP =============
    {
        "name": "VLOOKUP", "category": "Lookup",
        "syntax": "=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])",
        "description": "Looks up a value in the leftmost column and returns a value from a column you specify.",
        "example": "=VLOOKUP(\"Apple\", A2:C100, 3, FALSE)",
        "use_case": "Match records by ID, name, or product code.",
        "visual_example": {"data": [["A1: Apple", "B1: 50"], ["A2: Banana", "B2: 30"], ["A3: Cherry", "B3: 80"], ["E1 (lookup)", "Banana"]], "formula_cell": "F1", "formula": "=VLOOKUP(E1, A1:B3, 2, FALSE)", "result": 30},
        "simple_explanation": "Like a phonebook! You give VLOOKUP a name, it finds that name in the first column, then slides across to get the phone number from another column!",
        "video_url": _vurl("VLOOKUP"),
        "video_url_hindi": _hurl("VLOOKUP"),
    },
    {
        "name": "HLOOKUP", "category": "Lookup",
        "syntax": "=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])",
        "description": "Searches for a value in the top row and returns a value in the same column from a row you specify.",
        "example": "=HLOOKUP(\"Q1\", A1:E5, 3, FALSE)",
        "use_case": "Horizontal lookup tables.",
        "visual_example": {"data": [["A1:D1", "Q1, Q2, Q3, Q4"], ["A2:D2", "100, 200, 150, 300"]], "formula_cell": "B5", "formula": "=HLOOKUP(\"Q3\", A1:D2, 2, FALSE)", "result": 150},
        "simple_explanation": "Like VLOOKUP but sideways! HLOOKUP searches across the TOP ROW for a value, then slides DOWN to the row you want!",
        "video_url": _vurl("HLOOKUP"),
        "video_url_hindi": _hurl("HLOOKUP"),
    },
    {
        "name": "XLOOKUP", "category": "Lookup",
        "syntax": "=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode])",
        "description": "Modern replacement for VLOOKUP/HLOOKUP. Searches a range and returns a corresponding item.",
        "example": "=XLOOKUP(\"A102\", A:A, C:C, \"Not found\")",
        "use_case": "Bidirectional lookups with default values.",
        "visual_example": {"data": [["A1: A101", "C1: $50"], ["A2: A102", "C2: $80"], ["A3: A103", "C3: $30"]], "formula_cell": "E1", "formula": "=XLOOKUP(\"A102\", A1:A3, C1:C3, \"Not found\")", "result": "$80"},
        "simple_explanation": "The super-powered upgrade to VLOOKUP! XLOOKUP can search left AND right, shows a custom message when not found, and doesn't need column counting!",
        "video_url": _vurl("XLOOKUP"),
        "video_url_hindi": _hurl("XLOOKUP"),
    },
    {
        "name": "INDEX", "category": "Lookup",
        "syntax": "=INDEX(array, row_num, [column_num])",
        "description": "Returns a value at a given position in a range or array.",
        "example": "=INDEX(A1:C10, 3, 2)",
        "use_case": "Powerful when paired with MATCH.",
        "visual_example": {"data": [["A1:C1", "10, 20, 30"], ["A2:C2", "40, 50, 60"], ["A3:C3", "70, 80, 90"]], "formula_cell": "E1", "formula": "=INDEX(A1:C3, 3, 2)", "result": 80},
        "simple_explanation": "INDEX is like a treasure map grid. 'Go to row 3, column 2' — and INDEX gives you exactly what's in that spot on the grid!",
        "video_url": _vurl("INDEX"),
        "video_url_hindi": _hurl("INDEX"),
    },
    {
        "name": "MATCH", "category": "Lookup",
        "syntax": "=MATCH(lookup_value, lookup_array, [match_type])",
        "description": "Returns the relative position of an item in a range.",
        "example": "=MATCH(\"Bob\", A1:A100, 0)",
        "use_case": "Find the row of an item, used with INDEX.",
        "visual_example": {"data": [["A1", "Alice"], ["A2", "Bob"], ["A3", "Charlie"]], "formula_cell": "B1", "formula": "=MATCH(\"Bob\", A1:A3, 0)", "result": 2},
        "simple_explanation": "MATCH finds WHERE something is in a list. 'Where is Bob?' MATCH says 'He's at position 2!' Great helper when used with INDEX!",
        "video_url": _vurl("MATCH"),
        "video_url_hindi": _hurl("MATCH"),
    },
    {
        "name": "INDIRECT", "category": "Lookup",
        "syntax": "=INDIRECT(ref_text, [a1])",
        "description": "Returns the reference specified by a text string.",
        "example": "=INDIRECT(\"A\" & 5) returns the value in A5.",
        "use_case": "Dynamic sheet references.",
        "visual_example": {"data": [["A5", 99]], "formula_cell": "B1", "formula": "=INDIRECT(\"A\" & 5)", "result": 99},
        "simple_explanation": "INDIRECT reads a cell address written as text and goes there. Like reading '3rd house on Oak Street' as instructions and actually going there!",
        "video_url": _vurl("INDIRECT"),
        "video_url_hindi": _hurl("INDIRECT"),
    },
    {
        "name": "OFFSET", "category": "Lookup",
        "syntax": "=OFFSET(reference, rows, cols, [height], [width])",
        "description": "Returns a reference offset from a given starting point.",
        "example": "=OFFSET(A1, 2, 3) returns the value in D3.",
        "use_case": "Dynamic ranges for charts.",
        "visual_example": {"data": [["A1", "start"], ["D3", 555]], "formula_cell": "B1", "formula": "=OFFSET(A1, 2, 3)", "result": 555},
        "simple_explanation": "OFFSET starts at a cell and moves. 'Start at A1, move 2 rows down and 3 columns right' — you land on D3. Like following directions on a map!",
        "video_url": _vurl("OFFSET"),
        "video_url_hindi": _hurl("OFFSET"),
    },
    {
        "name": "CHOOSE", "category": "Lookup",
        "syntax": "=CHOOSE(index_num, value1, [value2], ...)",
        "description": "Picks a value from a list based on its position.",
        "example": "=CHOOSE(2, \"Red\", \"Blue\", \"Green\") returns \"Blue\".",
        "use_case": "Switch-style selection.",
        "visual_example": {"data": [["A1", 2]], "formula_cell": "B1", "formula": "=CHOOSE(A1, \"Red\", \"Blue\", \"Green\")", "result": "Blue"},
        "simple_explanation": "CHOOSE picks from a list by number. CHOOSE(2, 'Red', 'Blue', 'Green') picks the 2nd item: 'Blue'. Like a menu where you type a number and get that item!",
        "video_url": _vurl("CHOOSE"),
        "video_url_hindi": _hurl("CHOOSE"),
    },

    # ============= TEXT =============
    {
        "name": "CONCAT", "category": "Text",
        "syntax": "=CONCAT(text1, [text2], ...)",
        "description": "Combines text from multiple ranges or strings.",
        "example": "=CONCAT(\"Hello \", A1)",
        "use_case": "Build sentences or composite IDs.",
        "visual_example": {"data": [["A1", "World"]], "formula_cell": "B1", "formula": "=CONCAT(\"Hello \", A1)", "result": "Hello World"},
        "simple_explanation": "CONCAT glues text together! CONCAT('Hello ', 'World') makes 'Hello World'. Like taping two pieces of paper side by side!",
        "video_url": _vurl("CONCAT"),
        "video_url_hindi": _hurl("CONCAT"),
    },
    {
        "name": "TEXTJOIN", "category": "Text",
        "syntax": "=TEXTJOIN(delimiter, ignore_empty, text1, ...)",
        "description": "Joins text with a delimiter, optionally skipping empties.",
        "example": "=TEXTJOIN(\", \", TRUE, A1:A5)",
        "use_case": "Comma-separated lists from a column.",
        "visual_example": {"data": [["A1", "Apple"], ["A2", "Banana"], ["A3", "Cherry"]], "formula_cell": "B1", "formula": "=TEXTJOIN(\", \", TRUE, A1:A3)", "result": "Apple, Banana, Cherry"},
        "simple_explanation": "TEXTJOIN joins a list of words with a separator. Like stringing beads with a comma between each one: 'Apple, Banana, Cherry'!",
        "video_url": _vurl("TEXTJOIN"),
        "video_url_hindi": _hurl("TEXTJOIN"),
    },
    {
        "name": "LEFT", "category": "Text",
        "syntax": "=LEFT(text, [num_chars])",
        "description": "Returns leftmost characters of a string.",
        "example": "=LEFT(\"Excel\", 2) returns \"Ex\".",
        "use_case": "Extract prefixes or codes.",
        "visual_example": {"data": [["A1", "Excel"]], "formula_cell": "B1", "formula": "=LEFT(A1, 2)", "result": "Ex"},
        "simple_explanation": "LEFT cuts from the START of a word. LEFT('Excel', 2) gives 'Ex' — the first 2 letters. Like tearing the left side of a sticker!",
        "video_url": _vurl("LEFT"),
        "video_url_hindi": _hurl("LEFT"),
    },
    {
        "name": "RIGHT", "category": "Text",
        "syntax": "=RIGHT(text, [num_chars])",
        "description": "Returns rightmost characters.",
        "example": "=RIGHT(\"Excel\", 3) returns \"cel\".",
        "use_case": "Extract suffixes.",
        "visual_example": {"data": [["A1", "Excel"]], "formula_cell": "B1", "formula": "=RIGHT(A1, 3)", "result": "cel"},
        "simple_explanation": "RIGHT cuts from the END of a word. RIGHT('Excel', 3) gives 'cel' — the last 3 letters. Like tearing the right side of a sticker!",
        "video_url": _vurl("RIGHT"),
        "video_url_hindi": _hurl("RIGHT"),
    },
    {
        "name": "MID", "category": "Text",
        "syntax": "=MID(text, start_num, num_chars)",
        "description": "Returns characters from the middle of a string.",
        "example": "=MID(\"Excel\", 2, 3) returns \"xce\".",
        "use_case": "Parse substrings from fixed positions.",
        "visual_example": {"data": [["A1", "Excel"]], "formula_cell": "B1", "formula": "=MID(A1, 2, 3)", "result": "xce"},
        "simple_explanation": "MID cuts from the MIDDLE of a word. MID('Excel', 2, 3) starts at letter 2 and takes 3 letters: 'xce'. Like cutting a piece from the center of a ribbon!",
        "video_url": _vurl("MID"),
        "video_url_hindi": _hurl("MID"),
    },
    {
        "name": "LEN", "category": "Text",
        "syntax": "=LEN(text)",
        "description": "Returns the number of characters in a string.",
        "example": "=LEN(\"Hello\") returns 5.",
        "use_case": "Validate input length.",
        "visual_example": {"data": [["A1", "Hello"]], "formula_cell": "B1", "formula": "=LEN(A1)", "result": 5},
        "simple_explanation": "LEN counts how many letters are in a word. LEN('Hello') = 5 because there are 5 letters. Like counting beads on a necklace one by one!",
        "video_url": _vurl("LEN"),
        "video_url_hindi": _hurl("LEN"),
    },
    {
        "name": "TRIM", "category": "Text",
        "syntax": "=TRIM(text)",
        "description": "Removes extra spaces from text.",
        "example": "=TRIM(\"  Hello  World  \") returns \"Hello World\".",
        "use_case": "Clean imported data.",
        "visual_example": {"data": [["A1", "  Hello  World  "]], "formula_cell": "B1", "formula": "=TRIM(A1)", "result": "Hello World"},
        "simple_explanation": "TRIM removes all the extra spaces hiding in text. Like tidying a messy sentence — removes gaps at the start, end, and extra gaps in the middle!",
        "video_url": _vurl("TRIM"),
        "video_url_hindi": _hurl("TRIM"),
    },
    {
        "name": "UPPER", "category": "Text",
        "syntax": "=UPPER(text)",
        "description": "Converts text to uppercase.",
        "example": "=UPPER(\"hello\") returns \"HELLO\".",
        "use_case": "Standardize codes or IDs.",
        "visual_example": {"data": [["A1", "hello"]], "formula_cell": "B1", "formula": "=UPPER(A1)", "result": "HELLO"},
        "simple_explanation": "UPPER makes ALL letters CAPITAL. UPPER('hello') = 'HELLO'. Like pressing the CAPS LOCK key on the whole word!",
        "video_url": _vurl("UPPER"),
        "video_url_hindi": _hurl("UPPER"),
    },
    {
        "name": "LOWER", "category": "Text",
        "syntax": "=LOWER(text)",
        "description": "Converts text to lowercase.",
        "example": "=LOWER(\"HELLO\") returns \"hello\".",
        "use_case": "Normalize email addresses.",
        "visual_example": {"data": [["A1", "HELLO"]], "formula_cell": "B1", "formula": "=LOWER(A1)", "result": "hello"},
        "simple_explanation": "LOWER makes all letters small. LOWER('HELLO') = 'hello'. Like whispering everything very quietly — no more SHOUTING!",
        "video_url": _vurl("LOWER"),
        "video_url_hindi": _hurl("LOWER"),
    },
    {
        "name": "PROPER", "category": "Text",
        "syntax": "=PROPER(text)",
        "description": "Capitalizes the first letter of each word.",
        "example": "=PROPER(\"hello world\") returns \"Hello World\".",
        "use_case": "Format names properly.",
        "visual_example": {"data": [["A1", "hello world"]], "formula_cell": "B1", "formula": "=PROPER(A1)", "result": "Hello World"},
        "simple_explanation": "PROPER Capitalizes The First Letter Of Every Word. Like how you write people's names — 'john doe' becomes 'John Doe'!",
        "video_url": _vurl("PROPER"),
        "video_url_hindi": _hurl("PROPER"),
    },
    {
        "name": "SUBSTITUTE", "category": "Text",
        "syntax": "=SUBSTITUTE(text, old_text, new_text, [instance_num])",
        "description": "Replaces specific text in a string.",
        "example": "=SUBSTITUTE(\"abc-123\", \"-\", \"\")",
        "use_case": "Strip dashes from phone numbers.",
        "visual_example": {"data": [["A1", "abc-123"]], "formula_cell": "B1", "formula": "=SUBSTITUTE(A1, \"-\", \"\")", "result": "abc123"},
        "simple_explanation": "SUBSTITUTE finds a word inside text and swaps it with another. Like using Find & Replace — but inside a formula!",
        "video_url": _vurl("SUBSTITUTE"),
        "video_url_hindi": _hurl("SUBSTITUTE"),
    },
    {
        "name": "FIND", "category": "Text",
        "syntax": "=FIND(find_text, within_text, [start_num])",
        "description": "Finds the position of text within text (case-sensitive).",
        "example": "=FIND(\"@\", A1)",
        "use_case": "Locate the @ in an email.",
        "visual_example": {"data": [["A1", "jane@work.com"]], "formula_cell": "B1", "formula": "=FIND(\"@\", A1)", "result": 5},
        "simple_explanation": "FIND searches for a letter and tells you its position. FIND('@', 'jane@work.com') = 5 because @ is the 5th character. Like a treasure hunt that gives you the exact position!",
        "video_url": _vurl("FIND"),
        "video_url_hindi": _hurl("FIND"),
    },
    {
        "name": "SEARCH", "category": "Text",
        "syntax": "=SEARCH(find_text, within_text, [start_num])",
        "description": "Finds the position of text within text (case-insensitive, supports wildcards).",
        "example": "=SEARCH(\"world\", \"Hello World\")",
        "use_case": "Case-insensitive search.",
        "visual_example": {"data": [["A1", "Hello World"]], "formula_cell": "B1", "formula": "=SEARCH(\"world\", A1)", "result": 7},
        "simple_explanation": "Like FIND but friendlier — SEARCH doesn't care about UPPER or lower case. Searching 'world' in 'Hello World' still works perfectly!",
        "video_url": _vurl("SEARCH"),
        "video_url_hindi": _hurl("SEARCH"),
    },
    {
        "name": "TEXT", "category": "Text",
        "syntax": "=TEXT(value, format_text)",
        "description": "Formats a number with a specific format string.",
        "example": "=TEXT(1234.5, \"$#,##0.00\")",
        "use_case": "Format numbers as currency or dates in text.",
        "visual_example": {"data": [["A1", 1234.5]], "formula_cell": "B1", "formula": "=TEXT(A1, \"$#,##0.00\")", "result": "$1,234.50"},
        "simple_explanation": "TEXT dresses up a number in a custom outfit. TEXT(1234.5, '$#,##0.00') = '$1,234.50'. Makes numbers look exactly the way you want!",
        "video_url": _vurl("TEXT"),
        "video_url_hindi": _hurl("TEXT"),
    },

    # ============= DATE/TIME =============
    {
        "name": "TODAY", "category": "Date/Time",
        "syntax": "=TODAY()",
        "description": "Returns the current date.",
        "example": "=TODAY()",
        "use_case": "Calculate age, due dates.",
        "visual_example": {"data": [["—", "no input"]], "formula_cell": "A1", "formula": "=TODAY()", "result": "2026-06-19"},
        "simple_explanation": "TODAY() tells you today's date automatically. Every day you open Excel, it updates by itself — like a smart calendar that never goes out of date!",
        "video_url": _vurl("TODAY"),
        "video_url_hindi": _hurl("TODAY"),
    },
    {
        "name": "NOW", "category": "Date/Time",
        "syntax": "=NOW()",
        "description": "Returns the current date and time.",
        "example": "=NOW()",
        "use_case": "Timestamp records.",
        "visual_example": {"data": [["—", "no input"]], "formula_cell": "A1", "formula": "=NOW()", "result": "2026-06-19 15:42"},
        "simple_explanation": "NOW() gives you the current date AND time right now. Like a clock that also shows the date — all in one cell, updating live!",
        "video_url": _vurl("NOW"),
        "video_url_hindi": _hurl("NOW"),
    },
    {
        "name": "DATE", "category": "Date/Time",
        "syntax": "=DATE(year, month, day)",
        "description": "Constructs a date from year/month/day.",
        "example": "=DATE(2026, 2, 15)",
        "use_case": "Build dates programmatically.",
        "visual_example": {"data": [["A1 (year)", 2026], ["B1 (month)", 2], ["C1 (day)", 15]], "formula_cell": "D1", "formula": "=DATE(A1, B1, C1)", "result": "2026-02-15"},
        "simple_explanation": "DATE builds a date from three separate numbers. DATE(2026, 6, 15) creates June 15, 2026 — like assembling a date from its year, month, and day parts!",
        "video_url": _vurl("DATE"),
        "video_url_hindi": _hurl("DATE"),
    },
    {
        "name": "DAY", "category": "Date/Time",
        "syntax": "=DAY(serial_number)",
        "description": "Returns the day of the month.",
        "example": "=DAY(TODAY())",
        "use_case": "Extract day component.",
        "visual_example": {"data": [["A1", "2026-02-15"]], "formula_cell": "B1", "formula": "=DAY(A1)", "result": 15},
        "simple_explanation": "DAY pulls out just the day number from a date. DAY('June 15, 2026') = 15. Like reading only the day number from a calendar!",
        "video_url": _vurl("DAY"),
        "video_url_hindi": _hurl("DAY"),
    },
    {
        "name": "MONTH", "category": "Date/Time",
        "syntax": "=MONTH(serial_number)",
        "description": "Returns the month of a date.",
        "example": "=MONTH(\"2026-02-15\") returns 2.",
        "use_case": "Group data by month.",
        "visual_example": {"data": [["A1", "2026-02-15"]], "formula_cell": "B1", "formula": "=MONTH(A1)", "result": 2},
        "simple_explanation": "MONTH pulls out just the month number from a date. MONTH('June 15, 2026') = 6. June is the 6th month of the year!",
        "video_url": _vurl("MONTH"),
        "video_url_hindi": _hurl("MONTH"),
    },
    {
        "name": "YEAR", "category": "Date/Time",
        "syntax": "=YEAR(serial_number)",
        "description": "Returns the year of a date.",
        "example": "=YEAR(TODAY())",
        "use_case": "Annual summaries.",
        "visual_example": {"data": [["A1", "2026-02-15"]], "formula_cell": "B1", "formula": "=YEAR(A1)", "result": 2026},
        "simple_explanation": "YEAR pulls out just the year from a date. YEAR('June 15, 2026') = 2026. Like reading only the year from a calendar!",
        "video_url": _vurl("YEAR"),
        "video_url_hindi": _hurl("YEAR"),
    },
    {
        "name": "WEEKDAY", "category": "Date/Time",
        "syntax": "=WEEKDAY(serial_number, [return_type])",
        "description": "Returns the day of the week as a number.",
        "example": "=WEEKDAY(TODAY(), 2)",
        "use_case": "Identify weekends.",
        "visual_example": {"data": [["A1", "2026-02-07 (Sat)"]], "formula_cell": "B1", "formula": "=WEEKDAY(A1, 2)", "result": 6},
        "simple_explanation": "WEEKDAY tells you which day of the week a date falls on. Is June 15 a Monday or Friday? WEEKDAY answers with a number (1=Mon, 7=Sun)!",
        "video_url": _vurl("WEEKDAY"),
        "video_url_hindi": _hurl("WEEKDAY"),
    },
    {
        "name": "DATEDIF", "category": "Date/Time",
        "syntax": "=DATEDIF(start_date, end_date, unit)",
        "description": "Returns the difference between two dates in years, months, or days.",
        "example": "=DATEDIF(A1, TODAY(), \"Y\")",
        "use_case": "Compute age or tenure.",
        "visual_example": {"data": [["A1 (start)", "2020-01-01"], ["B1 (end)", "2026-06-19"]], "formula_cell": "C1", "formula": "=DATEDIF(A1, B1, \"Y\")", "result": 6},
        "simple_explanation": "DATEDIF calculates the gap between two dates. 'How many years between 2020 and 2026?' DATEDIF says 6! Perfect for calculating someone's age!",
        "video_url": _vurl("DATEDIF"),
        "video_url_hindi": _hurl("DATEDIF"),
    },
    {
        "name": "EOMONTH", "category": "Date/Time",
        "syntax": "=EOMONTH(start_date, months)",
        "description": "Returns the last day of the month, n months away.",
        "example": "=EOMONTH(TODAY(), 0)",
        "use_case": "Month-end reporting.",
        "visual_example": {"data": [["A1", "2026-02-07"]], "formula_cell": "B1", "formula": "=EOMONTH(A1, 0)", "result": "2026-02-28"},
        "simple_explanation": "EOMONTH finds the last day of a month. For February 2026 it gives Feb 28. It automatically knows how many days each month has — even leap years!",
        "video_url": _vurl("EOMONTH"),
        "video_url_hindi": _hurl("EOMONTH"),
    },
    {
        "name": "NETWORKDAYS", "category": "Date/Time",
        "syntax": "=NETWORKDAYS(start_date, end_date, [holidays])",
        "description": "Returns the number of working days between two dates.",
        "example": "=NETWORKDAYS(A1, B1)",
        "use_case": "Project planning.",
        "visual_example": {"data": [["A1 (start)", "2026-02-02 Mon"], ["B1 (end)", "2026-02-13 Fri"]], "formula_cell": "C1", "formula": "=NETWORKDAYS(A1, B1)", "result": 10},
        "simple_explanation": "NETWORKDAYS counts only working days (Mon–Fri) between two dates, automatically skipping weekends. Perfect for calculating project deadlines!",
        "video_url": _vurl("NETWORKDAYS"),
        "video_url_hindi": _hurl("NETWORKDAYS"),
    },

    # ============= STATISTICAL =============
    {
        "name": "COUNT", "category": "Statistical",
        "syntax": "=COUNT(value1, [value2], ...)",
        "description": "Counts cells that contain numbers.",
        "example": "=COUNT(A1:A100)",
        "use_case": "Count numeric entries.",
        "visual_example": {"data": [["A1", 10], ["A2", "text"], ["A3", 30], ["A4", ""]], "formula_cell": "B1", "formula": "=COUNT(A1:A4)", "result": 2},
        "simple_explanation": "COUNT counts only the cells with NUMBERS. If a column has numbers, text, and blanks — COUNT only counts the numbers and ignores everything else!",
        "video_url": _vurl("COUNT"),
        "video_url_hindi": _hurl("COUNT"),
    },
    {
        "name": "COUNTA", "category": "Statistical",
        "syntax": "=COUNTA(value1, [value2], ...)",
        "description": "Counts non-empty cells.",
        "example": "=COUNTA(A1:A100)",
        "use_case": "Count any filled rows.",
        "visual_example": {"data": [["A1", 10], ["A2", "text"], ["A3", 30], ["A4", ""]], "formula_cell": "B1", "formula": "=COUNTA(A1:A4)", "result": 3},
        "simple_explanation": "COUNTA counts ALL non-empty cells — numbers, text, anything! Like counting how many students filled in their name on a form (blank = not filled).",
        "video_url": _vurl("COUNTA"),
        "video_url_hindi": _hurl("COUNTA"),
    },
    {
        "name": "COUNTIF", "category": "Statistical",
        "syntax": "=COUNTIF(range, criteria)",
        "description": "Counts cells matching a criterion.",
        "example": "=COUNTIF(A1:A100, \">50\")",
        "use_case": "Count items by condition.",
        "visual_example": {"data": [["A1", 30], ["A2", 60], ["A3", 75], ["A4", 40]], "formula_cell": "B1", "formula": "=COUNTIF(A1:A4, \">50\")", "result": 2},
        "simple_explanation": "COUNTIF counts cells that match a rule. 'How many students scored above 50?' COUNTIF answers instantly — like a smart tally counter with a rule!",
        "video_url": _vurl("COUNTIF"),
        "video_url_hindi": _hurl("COUNTIF"),
    },
    {
        "name": "COUNTIFS", "category": "Statistical",
        "syntax": "=COUNTIFS(range1, criteria1, ...)",
        "description": "Counts cells matching multiple criteria.",
        "example": "=COUNTIFS(A:A, \"East\", B:B, \">100\")",
        "use_case": "Multi-criteria counting.",
        "visual_example": {"data": [["A1=East, B1=120", "—"], ["A2=West, B2=80", "—"], ["A3=East, B3=150", "—"]], "formula_cell": "C1", "formula": "=COUNTIFS(A1:A3,\"East\", B1:B3,\">100\")", "result": 2},
        "simple_explanation": "COUNTIFS counts with MANY rules at once. 'How many students from Class A scored above 50?' Two rules, one instant answer!",
        "video_url": _vurl("COUNTIFS"),
        "video_url_hindi": _hurl("COUNTIFS"),
    },
    {
        "name": "MEDIAN", "category": "Statistical",
        "syntax": "=MEDIAN(number1, [number2], ...)",
        "description": "Returns the median.",
        "example": "=MEDIAN(A1:A20)",
        "use_case": "Robust central value.",
        "visual_example": {"data": [["A1", 10], ["A2", 20], ["A3", 30], ["A4", 40], ["A5", 50]], "formula_cell": "B1", "formula": "=MEDIAN(A1:A5)", "result": 30},
        "simple_explanation": "MEDIAN finds the MIDDLE value when all numbers are sorted in order. With 10, 20, 30, 40, 50 — the median is 30. Not the average — the actual middle one!",
        "video_url": _vurl("MEDIAN"),
        "video_url_hindi": _hurl("MEDIAN"),
    },
    {
        "name": "MODE", "category": "Statistical",
        "syntax": "=MODE(number1, [number2], ...)",
        "description": "Returns the most frequent value.",
        "example": "=MODE(A1:A20)",
        "use_case": "Most common rating.",
        "visual_example": {"data": [["A1", 4], ["A2", 5], ["A3", 4], ["A4", 3], ["A5", 4]], "formula_cell": "B1", "formula": "=MODE(A1:A5)", "result": 4},
        "simple_explanation": "MODE finds the number that appears MOST OFTEN. Like asking 'what score did MOST students get?' The most popular answer wins!",
        "video_url": _vurl("MODE"),
        "video_url_hindi": _hurl("MODE"),
    },
    {
        "name": "STDEV", "category": "Statistical",
        "syntax": "=STDEV(number1, [number2], ...)",
        "description": "Estimates standard deviation based on a sample.",
        "example": "=STDEV(A1:A100)",
        "use_case": "Measure data spread.",
        "visual_example": {"data": [["A1", 10], ["A2", 12], ["A3", 14], ["A4", 11]], "formula_cell": "B1", "formula": "=STDEV(A1:A4)", "result": 1.71},
        "simple_explanation": "STDEV measures how SPREAD OUT numbers are. If everyone scored exactly 75, STDEV = 0. If scores range from 10 to 100, STDEV is large. Big STDEV = lots of variety!",
        "video_url": _vurl("STDEV"),
        "video_url_hindi": _hurl("STDEV"),
    },
    {
        "name": "RANK", "category": "Statistical",
        "syntax": "=RANK(number, ref, [order])",
        "description": "Returns the rank of a number in a list.",
        "example": "=RANK(A1, A1:A100, 0)",
        "use_case": "Leaderboard rankings.",
        "visual_example": {"data": [["A1", 90], ["A2", 75], ["A3", 85]], "formula_cell": "B1", "formula": "=RANK(A1, A1:A3, 0)", "result": 1},
        "simple_explanation": "RANK tells you where a number stands in a list. If you scored 90 and everyone else scored less, RANK says you're #1! Like a scoreboard position.",
        "video_url": _vurl("RANK"),
        "video_url_hindi": _hurl("RANK"),
    },

    # ============= FINANCIAL =============
    {
        "name": "PMT", "category": "Financial",
        "syntax": "=PMT(rate, nper, pv, [fv], [type])",
        "description": "Calculates loan payment based on constant payments and interest rate.",
        "example": "=PMT(0.05/12, 60, -10000)",
        "use_case": "Calculate monthly mortgage.",
        "visual_example": {"data": [["A1 (rate/mo)", 0.00417], ["A2 (months)", 60], ["A3 (loan)", -10000]], "formula_cell": "B1", "formula": "=PMT(A1, A2, A3)", "result": "$188.71"},
        "simple_explanation": "PMT calculates your monthly loan payment. Borrowed ₹10,000 at 5% for 5 years? PMT tells you exactly how much to pay each month — no guessing!",
        "video_url": _vurl("PMT"),
        "video_url_hindi": _hurl("PMT"),
    },
    {
        "name": "FV", "category": "Financial",
        "syntax": "=FV(rate, nper, pmt, [pv], [type])",
        "description": "Returns the future value of an investment.",
        "example": "=FV(0.06/12, 120, -100)",
        "use_case": "Project savings growth.",
        "visual_example": {"data": [["A1 (rate/mo)", 0.005], ["A2 (months)", 120], ["A3 (pmt)", -100]], "formula_cell": "B1", "formula": "=FV(A1, A2, A3)", "result": "$16,387.93"},
        "simple_explanation": "FV (Future Value) tells you how much your savings will grow. Save ₹100 every month for 10 years at 6% interest — FV shows the final total!",
        "video_url": _vurl("FV"),
        "video_url_hindi": _hurl("FV"),
    },
    {
        "name": "PV", "category": "Financial",
        "syntax": "=PV(rate, nper, pmt, [fv], [type])",
        "description": "Returns the present value of an investment.",
        "example": "=PV(0.05, 10, -1000)",
        "use_case": "Discounted cash flow.",
        "visual_example": {"data": [["A1 (rate/yr)", 0.05], ["A2 (years)", 10], ["A3 (pmt)", -1000]], "formula_cell": "B1", "formula": "=PV(A1, A2, A3)", "result": "$7,721.73"},
        "simple_explanation": "PV (Present Value) tells you what future money is worth TODAY. If someone promises ₹10,000 in 5 years, PV tells you what that's actually worth right now!",
        "video_url": _vurl("PV"),
        "video_url_hindi": _hurl("PV"),
    },
    {
        "name": "NPV", "category": "Financial",
        "syntax": "=NPV(rate, value1, [value2], ...)",
        "description": "Net present value of cash flows.",
        "example": "=NPV(0.1, A1:A10)",
        "use_case": "Investment evaluation.",
        "visual_example": {"data": [["A1", 1000], ["A2", 2000], ["A3", 3000]], "formula_cell": "B1", "formula": "=NPV(0.1, A1:A3)", "result": "$4,815.93"},
        "simple_explanation": "NPV adds up all future profits from a business and adjusts for time value. Like asking 'is this investment worth it TODAY?' — a positive NPV means yes!",
        "video_url": _vurl("NPV"),
        "video_url_hindi": _hurl("NPV"),
    },
    {
        "name": "IRR", "category": "Financial",
        "syntax": "=IRR(values, [guess])",
        "description": "Returns the internal rate of return.",
        "example": "=IRR(A1:A10)",
        "use_case": "Return on a series of cash flows.",
        "visual_example": {"data": [["A1", -10000], ["A2", 3000], ["A3", 4200], ["A4", 6800]], "formula_cell": "B1", "formula": "=IRR(A1:A4)", "result": "16.32%"},
        "simple_explanation": "IRR finds the interest rate that makes an investment break even. Like figuring out what percentage return you're ACTUALLY getting on your money!",
        "video_url": _vurl("IRR"),
        "video_url_hindi": _hurl("IRR"),
    },
]

# Merge Hindi explanations into each function
EXCEL_FUNCTIONS = [
    {**f, "simple_explanation_hindi": _HINDI_EXPLANATIONS.get(f["name"], "")}
    for f in EXCEL_FUNCTIONS
]

TUTORIALS = [
    # ===== FREE TUTORIALS =====
    {
        "title": "Mastering VLOOKUP: From Beginner to Pro",
        "category": "Lookup",
        "level": "Intermediate",
        "is_pro": False,
        "summary": "Learn how to use VLOOKUP to find data across spreadsheets — including exact match, approximate match, and the most common errors.",
        "content": """## What is VLOOKUP?

VLOOKUP stands for "Vertical Lookup". It searches the **first column** of a range and returns a value in the same row from another column.

### Syntax
`=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`

### Step-by-step example
1. Suppose you have a table in `A2:C100` with: ID | Name | Salary.
2. To find a salary by ID, write: `=VLOOKUP(E2, A2:C100, 3, FALSE)`.
3. The `FALSE` ensures **exact match**.

### Common errors
- **#N/A**: lookup value not found. Wrap with `IFERROR` or `IFNA`.
- **#REF!**: column index is greater than columns in the array.
- VLOOKUP only searches **left to right**. Use XLOOKUP if you need right-to-left.

### Pro tip
Replace VLOOKUP with `XLOOKUP` whenever possible — it's faster, simpler, and supports defaults."""
    },
    {
        "title": "Pivot Tables Demystified",
        "category": "Data Analysis",
        "level": "Beginner",
        "is_pro": False,
        "summary": "Turn rows of raw data into instant insights using pivot tables.",
        "content": """## Why Pivot Tables?

Pivot tables let you **summarize, group, and analyze** thousands of rows in seconds — no formulas needed.

### Creating one
1. Select your data range (e.g., `A1:F1000`).
2. Go to **Insert > PivotTable**.
3. Drag fields into Rows, Columns, Values, and Filters.

### Real-world setup
- Drag `Region` to Rows
- Drag `Month` to Columns
- Drag `Sales` to Values (Sum)

You instantly see Sales by Region by Month.

### Tips
- Right-click any value → "Show Value As" → % of Total / Running Total.
- Use slicers (Insert > Slicer) for interactive dashboards.
- Refresh with Alt + F5 when source data changes."""
    },
    {
        "title": "Conditional Formatting Like a Designer",
        "category": "Formatting",
        "level": "Beginner",
        "is_pro": False,
        "summary": "Highlight trends, outliers, and rules with color — without macros.",
        "content": """## Make data jump off the page

Conditional Formatting applies color/style based on a rule.

### Quick recipes
- **Top 10**: Home > Conditional Formatting > Top/Bottom Rules > Top 10 Items.
- **Heatmap**: Color Scales (3-color: green-yellow-red).
- **Data bars**: in-cell mini bars proportional to value.
- **Custom formula**: `=$D2>1000` to highlight whole rows.

### Pro tip
Always anchor columns with `$` when applying formulas across whole rows."""
    },
    {
        "title": "Cleaning Messy Data Fast",
        "category": "Data Cleaning",
        "level": "Beginner",
        "is_pro": False,
        "summary": "TRIM, CLEAN, SUBSTITUTE, Flash Fill — your toolkit for messy spreadsheets.",
        "content": """## The 5-minute cleanup

### Whitespace
- `=TRIM(A1)` removes extra spaces.
- `=CLEAN(A1)` removes non-printable characters.

### Casing
- `=PROPER(A1)` for names: "JOHN doe" → "John Doe".

### Replace
- `=SUBSTITUTE(A1, "-", "")` to strip dashes.

### Flash Fill (Ctrl+E)
Type the desired output once, press **Ctrl+E**, and Excel infers the pattern. Magic for splitting names, formatting phone numbers, or extracting domains."""
    },
    {
        "title": "Fixing #DIV/0!, #N/A, and #VALUE! Errors",
        "category": "Troubleshooting",
        "level": "Beginner",
        "is_pro": False,
        "summary": "Decode every Excel error and squash them confidently.",
        "content": """## Error cheat sheet

- **#DIV/0!** — division by zero. Fix: `=IFERROR(A1/B1, 0)`.
- **#N/A** — value not found (lookups). Fix: `=IFNA(VLOOKUP(...), "Not Found")`.
- **#VALUE!** — wrong data type (text where number expected).
- **#REF!** — broken cell reference (deleted column).
- **#NAME?** — typo in function name or missing quotes around text.
- **#NUM!** — invalid numeric arg (e.g., negative under SQRT).
- **#NULL!** — wrong intersection operator (use `,` not space).

### General-purpose trap
`=IFERROR(your_formula, "")` returns blank instead of any error."""
    },
    {
        "title": "Keyboard Shortcuts That Save Hours",
        "category": "Productivity",
        "level": "Beginner",
        "is_pro": False,
        "summary": "The 25 shortcuts every Excel user must know.",
        "content": """## Navigation
- **Ctrl + Arrow** — jump to last filled cell.
- **Ctrl + Shift + Arrow** — select to last filled cell.
- **Ctrl + Home / End** — start / end of sheet.

## Editing
- **F2** — edit active cell.
- **Ctrl + ;** — insert today's date.
- **Ctrl + Shift + :** — insert current time.
- **Alt + =** — autosum.
- **Ctrl + D / Ctrl + R** — fill down / right.

## Power moves
- **Ctrl + T** — convert range to Table.
- **Ctrl + E** — Flash Fill.
- **Alt + N + V** — insert PivotTable.
- **Ctrl + Shift + L** — toggle filters.
- **Ctrl + 1** — Format Cells dialog."""
    },
    {
        "title": "IF Statements for Beginners",
        "category": "Logical",
        "level": "Beginner",
        "is_pro": False,
        "summary": "Master Excel's most useful function — the IF statement — with real examples.",
        "content": """## What is IF?

IF is Excel's decision-maker. It checks a condition and returns one value if TRUE, another if FALSE.

### Syntax
`=IF(condition, value_if_true, value_if_false)`

### Simple example
`=IF(A1>=50, "Pass", "Fail")`

If A1 is 75 → returns "Pass". If A1 is 30 → returns "Fail".

### Nested IF
You can put an IF inside an IF:
`=IF(A1>=90, "A", IF(A1>=80, "B", IF(A1>=70, "C", "F")))`

Better approach for many conditions: use `IFS`.

### Common uses
- Flag overdue invoices: `=IF(TODAY()>B2, "Overdue", "OK")`
- Apply discount: `=IF(C2>1000, C2*0.9, C2)`
- Mark duplicates: `=IF(COUNTIF(A:A,A2)>1, "Duplicate", "")`"""
    },
    {
        "title": "Excel Tables: Stop Using Plain Ranges",
        "category": "Productivity",
        "level": "Beginner",
        "is_pro": False,
        "summary": "Excel Tables auto-expand, auto-filter, and make formulas readable. Here's why you should use them.",
        "content": """## What is an Excel Table?

An Excel Table (Ctrl+T) is a structured range that automatically expands and includes built-in features.

### How to create
1. Click any cell in your data.
2. Press **Ctrl + T**.
3. Confirm the range and whether it has headers.

### Benefits
- **Auto-expand**: add a row below and the table grows automatically.
- **Structured references**: formulas use column names like `[@Sales]` instead of `C2`.
- **Built-in filter**: filter dropdowns appear automatically.
- **Total Row**: right-click → Table → Totals Row for quick sums.

### Structured reference example
Instead of `=C2/B2`, a table formula reads:
`=[@Sales]/[@Visits]` — much easier to understand!

### Naming your table
Table Design tab → Table Name → give it a meaningful name like `SalesData`. Then reference it as `SalesData[Sales]` from anywhere in the workbook."""
    },
    {
        "title": "SUMIF and COUNTIF Explained Simply",
        "category": "Math",
        "level": "Beginner",
        "is_pro": False,
        "summary": "Add or count with one condition — the building blocks of data analysis.",
        "content": """## COUNTIF — Count with a rule

`=COUNTIF(range, criteria)`

### Examples
- Count cells above 100: `=COUNTIF(B:B, ">100")`
- Count "Yes" responses: `=COUNTIF(C:C, "Yes")`
- Count a specific name: `=COUNTIF(A:A, "Rahul")`

## SUMIF — Add with a rule

`=SUMIF(range, criteria, sum_range)`

### Examples
- Sum all sales from "East": `=SUMIF(A:A, "East", C:C)`
- Sum amounts over 500: `=SUMIF(B:B, ">500")`

## Wildcard tricks
Use `*` for partial matches:
- `=COUNTIF(A:A, "Raj*")` counts all names starting with "Raj"
- `=SUMIF(B:B, "*Ltd*", C:C)` sums rows where B contains "Ltd"

## Multi-condition? Use SUMIFS / COUNTIFS
`=SUMIFS(C:C, A:A, "East", B:B, ">500")` — East region AND above 500."""
    },
    {
        "title": "Date Functions Every Excel User Needs",
        "category": "Date/Time",
        "level": "Beginner",
        "is_pro": False,
        "summary": "TODAY, DATEDIF, EOMONTH, NETWORKDAYS — master dates and never get confused again.",
        "content": """## The essential date toolkit

### Get today / now
- `=TODAY()` — current date (updates daily)
- `=NOW()` — current date + time

### Build a date
`=DATE(2026, 6, 15)` → June 15 2026

### Extract parts
- `=DAY(A1)` → day number
- `=MONTH(A1)` → month number
- `=YEAR(A1)` → year number

### Calculate age
`=DATEDIF(B2, TODAY(), "Y")` → years between B2 and today.
- "Y" = full years, "M" = full months, "D" = days

### Days until deadline
`=A2 - TODAY()` → days remaining (format cell as Number)

### End of month
`=EOMONTH(TODAY(), 0)` → last day of this month
`=EOMONTH(TODAY(), 1)` → last day of NEXT month

### Working days
`=NETWORKDAYS(A2, B2)` → business days between two dates
`=WORKDAY(TODAY(), 10)` → date 10 working days from today"""
    },
    {
        "title": "Data Validation: Control What Gets Typed",
        "category": "Productivity",
        "level": "Beginner",
        "is_pro": False,
        "summary": "Prevent wrong data entry with dropdown lists, number limits, and custom rules.",
        "content": """## Why Data Validation?

Data Validation stops users from typing invalid data — like text in a number column or a date outside a valid range.

### How to set up
1. Select the cells you want to validate.
2. Go to **Data > Data Validation**.
3. Choose a validation type and set rules.

### Common types

**Dropdown list**
- Allow: List
- Source: `Male,Female,Other` or select a range like `$F$1:$F$5`

**Number range**
- Allow: Whole number
- Between 1 and 100

**Date range**
- Allow: Date
- Greater than: `=TODAY()` (only future dates allowed)

**Custom formula**
- Allow: Custom
- Formula: `=LEN(A1)=10` (only 10-character entries)

### Input message
Add a helpful message that pops up when a cell is selected — great for guiding users.

### Error alert
Customize the error shown when someone enters invalid data. Set Style to "Stop" to completely block bad entries."""
    },

    # ===== PRO TUTORIALS =====
    {
        "title": "INDEX + MATCH: The VLOOKUP Killer",
        "category": "Lookup",
        "level": "Advanced",
        "is_pro": True,
        "summary": "A more flexible alternative that works left-to-right and right-to-left.",
        "content": """## Why INDEX/MATCH?

VLOOKUP only searches left-to-right. INDEX/MATCH works in any direction and is faster on large datasets.

### Syntax
`=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))`

### Example
To find a salary in column A by name in column C:
`=INDEX(A:A, MATCH("Bob", C:C, 0))`

### Why it's better
- Lookup column doesn't need to be the leftmost.
- Adding/removing columns won't break the formula.
- Faster on huge tables."""
    },
    {
        "title": "Charts That Actually Communicate",
        "category": "Visualization",
        "level": "Intermediate",
        "is_pro": True,
        "summary": "Pick the right chart type and remove the clutter.",
        "content": """## Chart-picking guide

| Goal | Chart |
|------|-------|
| Compare categories | Bar / Column |
| Trend over time | Line |
| Composition | Stacked Bar / Pie |
| Correlation | Scatter |
| Distribution | Histogram |

### Decluttering
- Delete gridlines.
- Use one accent color, grey for the rest.
- Add data labels only where they tell a story.
- Sort bars by value (not alphabetical).

### Sparklines
Tiny inline trends. Insert > Sparklines > Line. Perfect for dashboards."""
    },
    {
        "title": "XLOOKUP: The Modern VLOOKUP Replacement",
        "category": "Lookup",
        "level": "Intermediate",
        "is_pro": True,
        "summary": "XLOOKUP does everything VLOOKUP does — and more. Learn why you should switch today.",
        "content": """## XLOOKUP vs VLOOKUP

| Feature | VLOOKUP | XLOOKUP |
|---------|---------|---------|
| Direction | Left to right only | Any direction |
| If not found | Returns error | Custom message |
| Column counting | Manual | Not needed |
| Multiple results | No | Yes |

### Syntax
`=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`

### Basic example
`=XLOOKUP("Rahul", A:A, C:C, "Not found")`
Finds "Rahul" in column A, returns the value from column C. If not found, shows "Not found".

### Reverse lookup (right to left)
`=XLOOKUP("Rahul", C:C, A:A)` — searches column C, returns from A. VLOOKUP can't do this!

### Multiple return columns
`=XLOOKUP("Rahul", A:A, B:D)` — returns an entire row (B, C, D) at once!

### Wildcard search
`=XLOOKUP("Raj*", A:A, B:B, , 2)` — finds first name starting with "Raj".

### Last match instead of first
`=XLOOKUP("Raj", A:A, B:B, , , -1)` — searches from bottom up."""
    },
    {
        "title": "Power Query: Transform Data Without Formulas",
        "category": "Data Analysis",
        "level": "Advanced",
        "is_pro": True,
        "summary": "Import, clean, and reshape data from any source — automatically refresh with one click.",
        "content": """## What is Power Query?

Power Query (Data > Get & Transform) lets you import and transform data from files, databases, and web sources — without writing formulas.

### Getting started
1. Go to **Data > Get Data > From File > From Excel / CSV**.
2. Select your file and click **Transform Data**.
3. The Power Query Editor opens.

### Common transformations

**Remove blank rows**
Home > Remove Rows > Remove Blank Rows

**Split a column**
Select column → Transform > Split Column > By Delimiter

**Change data type**
Click the type icon at the top of a column header

**Filter rows**
Click the dropdown on any column header → filter like Excel

**Merge two tables (like VLOOKUP)**
Home > Merge Queries → choose the key column to join on

### Refresh
Once set up, click **Data > Refresh All** to re-run all transformations on fresh data.

### Why it's powerful
- No formulas to break
- Handles thousands of files at once
- Reproducible steps (every action is recorded)
- Works with CSV, Excel, SQL, SharePoint, Web, and more"""
    },
    {
        "title": "Dynamic Arrays: FILTER, SORT, UNIQUE, SEQUENCE",
        "category": "Data Analysis",
        "level": "Advanced",
        "is_pro": True,
        "summary": "The new Excel functions that automatically spill results across multiple cells.",
        "content": """## What are Dynamic Arrays?

Dynamic array functions return multiple results that **automatically spill** into neighbouring cells — no Ctrl+Shift+Enter needed.

### FILTER — extract matching rows
`=FILTER(A2:C100, B2:B100="East")`
Returns all rows where column B is "East". Add a third argument for "if empty": `=FILTER(A2:C100, B2:B100="East", "No results")`

### SORT — sort a range
`=SORT(A2:C100, 3, -1)` — sort by column 3, descending.

### UNIQUE — remove duplicates
`=UNIQUE(A2:A100)` — returns a list with duplicates removed.
Combine: `=SORT(UNIQUE(A2:A100))` — sorted unique list.

### SEQUENCE — generate number series
`=SEQUENCE(10)` → 1 to 10
`=SEQUENCE(5, 3)` → 5 rows × 3 columns grid
`=SEQUENCE(12, 1, 1, 1)` → months 1–12

### Combine them
`=SORT(FILTER(A2:C100, C2:C100>1000), 3, -1)` — filter rows where C > 1000, then sort by column 3 descending.

### The # reference
Once a formula spills, reference the whole spill range with `#`:
If your FILTER is in E2, use `E2#` to reference all spilled results."""
    },
    {
        "title": "Building a Sales Dashboard from Scratch",
        "category": "Data Analysis",
        "level": "Advanced",
        "is_pro": True,
        "summary": "Step-by-step: build a professional sales dashboard with charts, slicers, and KPI cards.",
        "content": """## Dashboard blueprint

A great dashboard has 3 layers:
1. **Raw data** (hidden sheet)
2. **Calculations** (helper sheet with pivot tables / formulas)
3. **Dashboard** (visual sheet — charts, KPI cards, slicers)

### Step 1: Structure your data as a Table
- Ctrl+T on your raw data
- Name it `SalesData`

### Step 2: Create Pivot Tables
- Insert > PivotTable from `SalesData`
- Create one PT for Sales by Region
- Create one PT for Sales by Month
- Create one PT for Top 10 Products

### Step 3: Build charts
- Click in each Pivot Table → Insert → choose chart type
- Use Column for region comparison
- Use Line for monthly trend
- Use Bar for top products

### Step 4: Add Slicers
- Click any Pivot Table → PivotTable Analyze > Insert Slicer
- Add slicers for Year, Region, Product Category
- Connect each slicer to all Pivot Tables:
  Right-click slicer → Report Connections → check all tables

### Step 5: KPI cards
Use text boxes linked to formula cells:
`="Total Sales: " & TEXT(SUM(SalesData[Amount]),"#,##0")`

### Step 6: Final polish
- Hide row/column headers (View > uncheck Headings)
- Lock the dashboard sheet (Review > Protect Sheet)
- Set a print area if needed"""
    },
    {
        "title": "Financial Modeling: Loan Amortization Schedule",
        "category": "Finance",
        "level": "Advanced",
        "is_pro": True,
        "summary": "Build a complete loan repayment schedule using PMT, IPMT, and PPMT functions.",
        "content": """## What is a Loan Amortization Schedule?

An amortization schedule shows each monthly payment broken down into interest and principal.

### Key functions
- `PMT(rate, nper, pv)` — total monthly payment
- `IPMT(rate, per, nper, pv)` — interest portion of payment #per
- `PPMT(rate, per, nper, pv)` — principal portion of payment #per

### Setup (enter in named cells)
| Cell | Name | Example |
|------|------|---------|
| B1 | LoanAmount | 500000 |
| B2 | AnnualRate | 8% |
| B3 | TermYears | 20 |

### Monthly rate
`=B2/12` (annual rate ÷ 12)

### Total payments
`=B3*12` (years × 12)

### Monthly payment (fixed)
`=PMT(B2/12, B3*12, -B1)`

### Build the schedule (row by row)
| Col | Formula |
|-----|---------|
| A (Period) | 1, 2, 3 ... |
| B (Payment) | `=PMT($B$2/12, $B$3*12, -$B$1)` |
| C (Interest) | `=IPMT($B$2/12, A2, $B$3*12, -$B$1)` |
| D (Principal) | `=PPMT($B$2/12, A2, $B$3*12, -$B$1)` |
| E (Balance) | Previous balance − D |

### Add a conditional format
Highlight rows where cumulative principal > 50% of loan — shows the midpoint of repayment."""
    },
    {
        "title": "Macros & VBA: Automate Repetitive Tasks",
        "category": "Automation",
        "level": "Advanced",
        "is_pro": True,
        "summary": "Record and edit macros to automate formatting, reports, and data tasks in seconds.",
        "content": """## What is a Macro?

A macro is a recorded sequence of actions that you can replay with one click. VBA (Visual Basic for Applications) is the language behind macros.

### Record your first macro
1. Go to **View > Macros > Record Macro** (or Developer tab if visible).
2. Give it a name (no spaces) and optionally a shortcut key.
3. Perform your actions (format cells, sort data, etc.).
4. Click **Stop Recording**.

### Run the macro
View > Macros > View Macros > select yours > Run.
Or press your shortcut key.

### Edit with VBA
Press **Alt + F11** to open the VBA editor.

### Useful VBA snippets

**Select last row**
```
Dim lastRow As Long
lastRow = Cells(Rows.Count, 1).End(xlUp).Row
```

**Loop through rows**
```
For i = 2 To lastRow
    If Cells(i, 3).Value > 1000 Then
        Cells(i, 4).Value = "High"
    End If
Next i
```

**Auto-format a table**
```
Range("A1").CurrentRegion.Select
Selection.AutoFormat Format:=xlRangeAutoFormatTable3
```

### Save as macro-enabled
Always save macro files as **.xlsm** (Excel Macro-Enabled Workbook) — otherwise macros are lost."""
    },
]
