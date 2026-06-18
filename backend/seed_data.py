"""Seed Excel functions and tutorials into MongoDB."""

# visual_example shape:
#   data: list of [cellRef, value] rows (the sample input cells)
#   formula_cell: where the formula sits (e.g., "B1")
#   formula: the formula string
#   result: the displayed result
# OR for text/date/single-input functions:
#   data: list of [label, value]  — used as a small key/value block
#   formula_cell, formula, result same

EXCEL_FUNCTIONS = [
    # ============= MATH =============
    {"name": "SUM", "category": "Math", "syntax": "=SUM(number1, [number2], ...)", "description": "Adds all the numbers in a range of cells.", "example": "=SUM(A1:A10) returns the sum of values in A1 through A10.", "use_case": "Calculate totals, like total sales or expenses.",
     "visual_example": {"data": [["A1", 10], ["A2", 20], ["A3", 30]], "formula_cell": "B1", "formula": "=SUM(A1:A3)", "result": 60}},
    {"name": "AVERAGE", "category": "Math", "syntax": "=AVERAGE(number1, [number2], ...)", "description": "Returns the arithmetic mean of the arguments.", "example": "=AVERAGE(B1:B5) returns the average of cells B1 to B5.", "use_case": "Find the average score, average price, or average performance.",
     "visual_example": {"data": [["A1", 80], ["A2", 90], ["A3", 70], ["A4", 60]], "formula_cell": "B1", "formula": "=AVERAGE(A1:A4)", "result": 75}},
    {"name": "MIN", "category": "Math", "syntax": "=MIN(number1, [number2], ...)", "description": "Returns the smallest number in a set of values.", "example": "=MIN(A1:A20) returns the smallest value in A1:A20.", "use_case": "Find the lowest price or smallest measurement.",
     "visual_example": {"data": [["A1", 45], ["A2", 12], ["A3", 78], ["A4", 23]], "formula_cell": "B1", "formula": "=MIN(A1:A4)", "result": 12}},
    {"name": "MAX", "category": "Math", "syntax": "=MAX(number1, [number2], ...)", "description": "Returns the largest number in a set of values.", "example": "=MAX(A1:A20) returns the largest value in the range.", "use_case": "Find the peak revenue or top score.",
     "visual_example": {"data": [["A1", 45], ["A2", 12], ["A3", 78], ["A4", 23]], "formula_cell": "B1", "formula": "=MAX(A1:A4)", "result": 78}},
    {"name": "ROUND", "category": "Math", "syntax": "=ROUND(number, num_digits)", "description": "Rounds a number to a specified number of digits.", "example": "=ROUND(3.14159, 2) returns 3.14.", "use_case": "Round monetary values to 2 decimal places.",
     "visual_example": {"data": [["A1", 3.14159]], "formula_cell": "B1", "formula": "=ROUND(A1, 2)", "result": 3.14}},
    {"name": "ROUNDUP", "category": "Math", "syntax": "=ROUNDUP(number, num_digits)", "description": "Rounds a number up, away from zero.", "example": "=ROUNDUP(3.2, 0) returns 4.", "use_case": "Always round up shipping counts.",
     "visual_example": {"data": [["A1", 3.2]], "formula_cell": "B1", "formula": "=ROUNDUP(A1, 0)", "result": 4}},
    {"name": "ROUNDDOWN", "category": "Math", "syntax": "=ROUNDDOWN(number, num_digits)", "description": "Rounds a number down, towards zero.", "example": "=ROUNDDOWN(3.9, 0) returns 3.", "use_case": "Truncate decimals when computing whole units.",
     "visual_example": {"data": [["A1", 3.9]], "formula_cell": "B1", "formula": "=ROUNDDOWN(A1, 0)", "result": 3}},
    {"name": "MOD", "category": "Math", "syntax": "=MOD(number, divisor)", "description": "Returns the remainder after a number is divided by a divisor.", "example": "=MOD(10, 3) returns 1.", "use_case": "Identify even/odd rows or alternating patterns.",
     "visual_example": {"data": [["A1", 10], ["A2", 3]], "formula_cell": "B1", "formula": "=MOD(A1, A2)", "result": 1}},
    {"name": "ABS", "category": "Math", "syntax": "=ABS(number)", "description": "Returns the absolute value of a number.", "example": "=ABS(-7) returns 7.", "use_case": "Compute distance or magnitude regardless of sign.",
     "visual_example": {"data": [["A1", -7]], "formula_cell": "B1", "formula": "=ABS(A1)", "result": 7}},
    {"name": "POWER", "category": "Math", "syntax": "=POWER(number, power)", "description": "Returns the result of a number raised to a power.", "example": "=POWER(2, 10) returns 1024.", "use_case": "Compound interest, exponential growth.",
     "visual_example": {"data": [["A1", 2], ["A2", 10]], "formula_cell": "B1", "formula": "=POWER(A1, A2)", "result": 1024}},
    {"name": "SQRT", "category": "Math", "syntax": "=SQRT(number)", "description": "Returns the square root of a number.", "example": "=SQRT(16) returns 4.", "use_case": "Engineering and statistical calculations.",
     "visual_example": {"data": [["A1", 16]], "formula_cell": "B1", "formula": "=SQRT(A1)", "result": 4}},
    {"name": "SUMIF", "category": "Math", "syntax": "=SUMIF(range, criteria, [sum_range])", "description": "Sums the cells specified by a given criteria.", "example": "=SUMIF(A1:A10, \">100\") sums values greater than 100.", "use_case": "Sum sales above threshold or by category.",
     "visual_example": {"data": [["A1", 50], ["A2", 150], ["A3", 80], ["A4", 200]], "formula_cell": "B1", "formula": "=SUMIF(A1:A4, \">100\")", "result": 350}},
    {"name": "SUMIFS", "category": "Math", "syntax": "=SUMIFS(sum_range, criteria_range1, criteria1, ...)", "description": "Sums based on multiple criteria.", "example": "=SUMIFS(C:C, A:A, \"East\", B:B, \">50\")", "use_case": "Multi-condition aggregations.",
     "visual_example": {"data": [["A1=East, B1=100", "—"], ["A2=West, B2=80", "—"], ["A3=East, B3=60", "—"]], "formula_cell": "C1", "formula": "=SUMIFS(B1:B3, A1:A3, \"East\")", "result": 160}},

    # ============= LOGICAL =============
    {"name": "IF", "category": "Logical", "syntax": "=IF(logical_test, value_if_true, value_if_false)", "description": "Returns one value if a condition is true and another if false.", "example": "=IF(A1>50, \"Pass\", \"Fail\")", "use_case": "Conditional grading, status flags.",
     "visual_example": {"data": [["A1", 75]], "formula_cell": "B1", "formula": "=IF(A1>50, \"Pass\", \"Fail\")", "result": "Pass"}},
    {"name": "IFS", "category": "Logical", "syntax": "=IFS(test1, value1, test2, value2, ...)", "description": "Checks multiple conditions and returns the value for the first TRUE.", "example": "=IFS(A1>=90, \"A\", A1>=80, \"B\", A1>=70, \"C\", TRUE, \"F\")", "use_case": "Cleaner alternative to nested IFs.",
     "visual_example": {"data": [["A1", 85]], "formula_cell": "B1", "formula": "=IFS(A1>=90,\"A\", A1>=80,\"B\", A1>=70,\"C\", TRUE,\"F\")", "result": "B"}},
    {"name": "AND", "category": "Logical", "syntax": "=AND(logical1, logical2, ...)", "description": "Returns TRUE if all arguments are true.", "example": "=AND(A1>0, B1>0)", "use_case": "Compound conditions inside IF.",
     "visual_example": {"data": [["A1", 5], ["B1", 10]], "formula_cell": "C1", "formula": "=AND(A1>0, B1>0)", "result": "TRUE"}},
    {"name": "OR", "category": "Logical", "syntax": "=OR(logical1, logical2, ...)", "description": "Returns TRUE if any argument is true.", "example": "=OR(A1=\"Yes\", B1=\"Yes\")", "use_case": "Either-or conditional checks.",
     "visual_example": {"data": [["A1", "No"], ["B1", "Yes"]], "formula_cell": "C1", "formula": "=OR(A1=\"Yes\", B1=\"Yes\")", "result": "TRUE"}},
    {"name": "NOT", "category": "Logical", "syntax": "=NOT(logical)", "description": "Reverses the logic of its argument.", "example": "=NOT(A1=B1)", "use_case": "Invert a boolean condition.",
     "visual_example": {"data": [["A1", 5], ["B1", 5]], "formula_cell": "C1", "formula": "=NOT(A1=B1)", "result": "FALSE"}},
    {"name": "IFERROR", "category": "Logical", "syntax": "=IFERROR(value, value_if_error)", "description": "Returns a custom value if a formula produces an error.", "example": "=IFERROR(A1/B1, 0)", "use_case": "Suppress #DIV/0! and other errors.",
     "visual_example": {"data": [["A1", 100], ["B1", 0]], "formula_cell": "C1", "formula": "=IFERROR(A1/B1, 0)", "result": 0}},
    {"name": "IFNA", "category": "Logical", "syntax": "=IFNA(value, value_if_na)", "description": "Returns custom value when a formula returns #N/A.", "example": "=IFNA(VLOOKUP(A1,B:C,2,FALSE), \"Not Found\")", "use_case": "Cleaner VLOOKUP error handling.",
     "visual_example": {"data": [["A1", "Mango"], ["B-list", "Apple, Banana"]], "formula_cell": "C1", "formula": "=IFNA(VLOOKUP(A1,B1:B2,1,FALSE),\"Not Found\")", "result": "Not Found"}},

    # ============= LOOKUP =============
    {"name": "VLOOKUP", "category": "Lookup", "syntax": "=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])", "description": "Looks up a value in the leftmost column and returns a value from a column you specify.", "example": "=VLOOKUP(\"Apple\", A2:C100, 3, FALSE)", "use_case": "Match records by ID, name, or product code.",
     "visual_example": {"data": [["A1: Apple", "B1: 50"], ["A2: Banana", "B2: 30"], ["A3: Cherry", "B3: 80"], ["E1 (lookup)", "Banana"]], "formula_cell": "F1", "formula": "=VLOOKUP(E1, A1:B3, 2, FALSE)", "result": 30}},
    {"name": "HLOOKUP", "category": "Lookup", "syntax": "=HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])", "description": "Searches for a value in the top row and returns a value in the same column from a row you specify.", "example": "=HLOOKUP(\"Q1\", A1:E5, 3, FALSE)", "use_case": "Horizontal lookup tables.",
     "visual_example": {"data": [["A1:D1", "Q1, Q2, Q3, Q4"], ["A2:D2", "100, 200, 150, 300"]], "formula_cell": "B5", "formula": "=HLOOKUP(\"Q3\", A1:D2, 2, FALSE)", "result": 150}},
    {"name": "XLOOKUP", "category": "Lookup", "syntax": "=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode])", "description": "Modern replacement for VLOOKUP/HLOOKUP. Searches a range and returns a corresponding item.", "example": "=XLOOKUP(\"A102\", A:A, C:C, \"Not found\")", "use_case": "Bidirectional lookups with default values.",
     "visual_example": {"data": [["A1: A101", "C1: $50"], ["A2: A102", "C2: $80"], ["A3: A103", "C3: $30"]], "formula_cell": "E1", "formula": "=XLOOKUP(\"A102\", A1:A3, C1:C3, \"Not found\")", "result": "$80"}},
    {"name": "INDEX", "category": "Lookup", "syntax": "=INDEX(array, row_num, [column_num])", "description": "Returns a value at a given position in a range or array.", "example": "=INDEX(A1:C10, 3, 2)", "use_case": "Powerful when paired with MATCH.",
     "visual_example": {"data": [["A1:C1", "10, 20, 30"], ["A2:C2", "40, 50, 60"], ["A3:C3", "70, 80, 90"]], "formula_cell": "E1", "formula": "=INDEX(A1:C3, 3, 2)", "result": 80}},
    {"name": "MATCH", "category": "Lookup", "syntax": "=MATCH(lookup_value, lookup_array, [match_type])", "description": "Returns the relative position of an item in a range.", "example": "=MATCH(\"Bob\", A1:A100, 0)", "use_case": "Find the row of an item, used with INDEX.",
     "visual_example": {"data": [["A1", "Alice"], ["A2", "Bob"], ["A3", "Charlie"]], "formula_cell": "B1", "formula": "=MATCH(\"Bob\", A1:A3, 0)", "result": 2}},
    {"name": "INDIRECT", "category": "Lookup", "syntax": "=INDIRECT(ref_text, [a1])", "description": "Returns the reference specified by a text string.", "example": "=INDIRECT(\"A\" & 5) returns the value in A5.", "use_case": "Dynamic sheet references.",
     "visual_example": {"data": [["A5", 99]], "formula_cell": "B1", "formula": "=INDIRECT(\"A\" & 5)", "result": 99}},
    {"name": "OFFSET", "category": "Lookup", "syntax": "=OFFSET(reference, rows, cols, [height], [width])", "description": "Returns a reference offset from a given starting point.", "example": "=OFFSET(A1, 2, 3) returns the value in D3.", "use_case": "Dynamic ranges for charts.",
     "visual_example": {"data": [["A1", "start"], ["D3", 555]], "formula_cell": "B1", "formula": "=OFFSET(A1, 2, 3)", "result": 555}},
    {"name": "CHOOSE", "category": "Lookup", "syntax": "=CHOOSE(index_num, value1, [value2], ...)", "description": "Picks a value from a list based on its position.", "example": "=CHOOSE(2, \"Red\", \"Blue\", \"Green\") returns \"Blue\".", "use_case": "Switch-style selection.",
     "visual_example": {"data": [["A1", 2]], "formula_cell": "B1", "formula": "=CHOOSE(A1, \"Red\", \"Blue\", \"Green\")", "result": "Blue"}},

    # ============= TEXT =============
    {"name": "CONCAT", "category": "Text", "syntax": "=CONCAT(text1, [text2], ...)", "description": "Combines text from multiple ranges or strings.", "example": "=CONCAT(\"Hello \", A1)", "use_case": "Build sentences or composite IDs.",
     "visual_example": {"data": [["A1", "World"]], "formula_cell": "B1", "formula": "=CONCAT(\"Hello \", A1)", "result": "Hello World"}},
    {"name": "TEXTJOIN", "category": "Text", "syntax": "=TEXTJOIN(delimiter, ignore_empty, text1, ...)", "description": "Joins text with a delimiter, optionally skipping empties.", "example": "=TEXTJOIN(\", \", TRUE, A1:A5)", "use_case": "Comma-separated lists from a column.",
     "visual_example": {"data": [["A1", "Apple"], ["A2", "Banana"], ["A3", "Cherry"]], "formula_cell": "B1", "formula": "=TEXTJOIN(\", \", TRUE, A1:A3)", "result": "Apple, Banana, Cherry"}},
    {"name": "LEFT", "category": "Text", "syntax": "=LEFT(text, [num_chars])", "description": "Returns leftmost characters of a string.", "example": "=LEFT(\"Excel\", 2) returns \"Ex\".", "use_case": "Extract prefixes or codes.",
     "visual_example": {"data": [["A1", "Excel"]], "formula_cell": "B1", "formula": "=LEFT(A1, 2)", "result": "Ex"}},
    {"name": "RIGHT", "category": "Text", "syntax": "=RIGHT(text, [num_chars])", "description": "Returns rightmost characters.", "example": "=RIGHT(\"Excel\", 3) returns \"cel\".", "use_case": "Extract suffixes.",
     "visual_example": {"data": [["A1", "Excel"]], "formula_cell": "B1", "formula": "=RIGHT(A1, 3)", "result": "cel"}},
    {"name": "MID", "category": "Text", "syntax": "=MID(text, start_num, num_chars)", "description": "Returns characters from the middle of a string.", "example": "=MID(\"Excel\", 2, 3) returns \"xce\".", "use_case": "Parse substrings from fixed positions.",
     "visual_example": {"data": [["A1", "Excel"]], "formula_cell": "B1", "formula": "=MID(A1, 2, 3)", "result": "xce"}},
    {"name": "LEN", "category": "Text", "syntax": "=LEN(text)", "description": "Returns the number of characters in a string.", "example": "=LEN(\"Hello\") returns 5.", "use_case": "Validate input length.",
     "visual_example": {"data": [["A1", "Hello"]], "formula_cell": "B1", "formula": "=LEN(A1)", "result": 5}},
    {"name": "TRIM", "category": "Text", "syntax": "=TRIM(text)", "description": "Removes extra spaces from text.", "example": "=TRIM(\"  Hello  World  \") returns \"Hello World\".", "use_case": "Clean imported data.",
     "visual_example": {"data": [["A1", "  Hello  World  "]], "formula_cell": "B1", "formula": "=TRIM(A1)", "result": "Hello World"}},
    {"name": "UPPER", "category": "Text", "syntax": "=UPPER(text)", "description": "Converts text to uppercase.", "example": "=UPPER(\"hello\") returns \"HELLO\".", "use_case": "Standardize codes or IDs.",
     "visual_example": {"data": [["A1", "hello"]], "formula_cell": "B1", "formula": "=UPPER(A1)", "result": "HELLO"}},
    {"name": "LOWER", "category": "Text", "syntax": "=LOWER(text)", "description": "Converts text to lowercase.", "example": "=LOWER(\"HELLO\") returns \"hello\".", "use_case": "Normalize email addresses.",
     "visual_example": {"data": [["A1", "HELLO"]], "formula_cell": "B1", "formula": "=LOWER(A1)", "result": "hello"}},
    {"name": "PROPER", "category": "Text", "syntax": "=PROPER(text)", "description": "Capitalizes the first letter of each word.", "example": "=PROPER(\"hello world\") returns \"Hello World\".", "use_case": "Format names properly.",
     "visual_example": {"data": [["A1", "hello world"]], "formula_cell": "B1", "formula": "=PROPER(A1)", "result": "Hello World"}},
    {"name": "SUBSTITUTE", "category": "Text", "syntax": "=SUBSTITUTE(text, old_text, new_text, [instance_num])", "description": "Replaces specific text in a string.", "example": "=SUBSTITUTE(\"abc-123\", \"-\", \"\")", "use_case": "Strip dashes from phone numbers.",
     "visual_example": {"data": [["A1", "abc-123"]], "formula_cell": "B1", "formula": "=SUBSTITUTE(A1, \"-\", \"\")", "result": "abc123"}},
    {"name": "FIND", "category": "Text", "syntax": "=FIND(find_text, within_text, [start_num])", "description": "Finds the position of text within text (case-sensitive).", "example": "=FIND(\"@\", A1)", "use_case": "Locate the @ in an email.",
     "visual_example": {"data": [["A1", "jane@work.com"]], "formula_cell": "B1", "formula": "=FIND(\"@\", A1)", "result": 5}},
    {"name": "SEARCH", "category": "Text", "syntax": "=SEARCH(find_text, within_text, [start_num])", "description": "Finds the position of text within text (case-insensitive, supports wildcards).", "example": "=SEARCH(\"world\", \"Hello World\")", "use_case": "Case-insensitive search.",
     "visual_example": {"data": [["A1", "Hello World"]], "formula_cell": "B1", "formula": "=SEARCH(\"world\", A1)", "result": 7}},
    {"name": "TEXT", "category": "Text", "syntax": "=TEXT(value, format_text)", "description": "Formats a number with a specific format string.", "example": "=TEXT(1234.5, \"$#,##0.00\")", "use_case": "Format numbers as currency or dates in text.",
     "visual_example": {"data": [["A1", 1234.5]], "formula_cell": "B1", "formula": "=TEXT(A1, \"$#,##0.00\")", "result": "$1,234.50"}},

    # ============= DATE/TIME =============
    {"name": "TODAY", "category": "Date/Time", "syntax": "=TODAY()", "description": "Returns the current date.", "example": "=TODAY()", "use_case": "Calculate age, due dates.",
     "visual_example": {"data": [["—", "no input"]], "formula_cell": "A1", "formula": "=TODAY()", "result": "2026-02-07"}},
    {"name": "NOW", "category": "Date/Time", "syntax": "=NOW()", "description": "Returns the current date and time.", "example": "=NOW()", "use_case": "Timestamp records.",
     "visual_example": {"data": [["—", "no input"]], "formula_cell": "A1", "formula": "=NOW()", "result": "2026-02-07 15:42"}},
    {"name": "DATE", "category": "Date/Time", "syntax": "=DATE(year, month, day)", "description": "Constructs a date from year/month/day.", "example": "=DATE(2026, 2, 15)", "use_case": "Build dates programmatically.",
     "visual_example": {"data": [["A1 (year)", 2026], ["B1 (month)", 2], ["C1 (day)", 15]], "formula_cell": "D1", "formula": "=DATE(A1, B1, C1)", "result": "2026-02-15"}},
    {"name": "DAY", "category": "Date/Time", "syntax": "=DAY(serial_number)", "description": "Returns the day of the month.", "example": "=DAY(TODAY())", "use_case": "Extract day component.",
     "visual_example": {"data": [["A1", "2026-02-15"]], "formula_cell": "B1", "formula": "=DAY(A1)", "result": 15}},
    {"name": "MONTH", "category": "Date/Time", "syntax": "=MONTH(serial_number)", "description": "Returns the month of a date.", "example": "=MONTH(\"2026-02-15\") returns 2.", "use_case": "Group data by month.",
     "visual_example": {"data": [["A1", "2026-02-15"]], "formula_cell": "B1", "formula": "=MONTH(A1)", "result": 2}},
    {"name": "YEAR", "category": "Date/Time", "syntax": "=YEAR(serial_number)", "description": "Returns the year of a date.", "example": "=YEAR(TODAY())", "use_case": "Annual summaries.",
     "visual_example": {"data": [["A1", "2026-02-15"]], "formula_cell": "B1", "formula": "=YEAR(A1)", "result": 2026}},
    {"name": "WEEKDAY", "category": "Date/Time", "syntax": "=WEEKDAY(serial_number, [return_type])", "description": "Returns the day of the week as a number.", "example": "=WEEKDAY(TODAY(), 2)", "use_case": "Identify weekends.",
     "visual_example": {"data": [["A1", "2026-02-07 (Sat)"]], "formula_cell": "B1", "formula": "=WEEKDAY(A1, 2)", "result": 6}},
    {"name": "DATEDIF", "category": "Date/Time", "syntax": "=DATEDIF(start_date, end_date, unit)", "description": "Returns the difference between two dates in years, months, or days.", "example": "=DATEDIF(A1, TODAY(), \"Y\")", "use_case": "Compute age or tenure.",
     "visual_example": {"data": [["A1 (start)", "2020-01-01"], ["B1 (end)", "2026-02-07"]], "formula_cell": "C1", "formula": "=DATEDIF(A1, B1, \"Y\")", "result": 6}},
    {"name": "EOMONTH", "category": "Date/Time", "syntax": "=EOMONTH(start_date, months)", "description": "Returns the last day of the month, n months away.", "example": "=EOMONTH(TODAY(), 0)", "use_case": "Month-end reporting.",
     "visual_example": {"data": [["A1", "2026-02-07"]], "formula_cell": "B1", "formula": "=EOMONTH(A1, 0)", "result": "2026-02-28"}},
    {"name": "NETWORKDAYS", "category": "Date/Time", "syntax": "=NETWORKDAYS(start_date, end_date, [holidays])", "description": "Returns the number of working days between two dates.", "example": "=NETWORKDAYS(A1, B1)", "use_case": "Project planning.",
     "visual_example": {"data": [["A1 (start)", "2026-02-02 Mon"], ["B1 (end)", "2026-02-13 Fri"]], "formula_cell": "C1", "formula": "=NETWORKDAYS(A1, B1)", "result": 10}},

    # ============= STATISTICAL =============
    {"name": "COUNT", "category": "Statistical", "syntax": "=COUNT(value1, [value2], ...)", "description": "Counts cells that contain numbers.", "example": "=COUNT(A1:A100)", "use_case": "Count numeric entries.",
     "visual_example": {"data": [["A1", 10], ["A2", "text"], ["A3", 30], ["A4", ""]], "formula_cell": "B1", "formula": "=COUNT(A1:A4)", "result": 2}},
    {"name": "COUNTA", "category": "Statistical", "syntax": "=COUNTA(value1, [value2], ...)", "description": "Counts non-empty cells.", "example": "=COUNTA(A1:A100)", "use_case": "Count any filled rows.",
     "visual_example": {"data": [["A1", 10], ["A2", "text"], ["A3", 30], ["A4", ""]], "formula_cell": "B1", "formula": "=COUNTA(A1:A4)", "result": 3}},
    {"name": "COUNTIF", "category": "Statistical", "syntax": "=COUNTIF(range, criteria)", "description": "Counts cells matching a criterion.", "example": "=COUNTIF(A1:A100, \">50\")", "use_case": "Count items by condition.",
     "visual_example": {"data": [["A1", 30], ["A2", 60], ["A3", 75], ["A4", 40]], "formula_cell": "B1", "formula": "=COUNTIF(A1:A4, \">50\")", "result": 2}},
    {"name": "COUNTIFS", "category": "Statistical", "syntax": "=COUNTIFS(range1, criteria1, ...)", "description": "Counts cells matching multiple criteria.", "example": "=COUNTIFS(A:A, \"East\", B:B, \">100\")", "use_case": "Multi-criteria counting.",
     "visual_example": {"data": [["A1=East, B1=120", "—"], ["A2=West, B2=80", "—"], ["A3=East, B3=150", "—"]], "formula_cell": "C1", "formula": "=COUNTIFS(A1:A3,\"East\", B1:B3,\">100\")", "result": 2}},
    {"name": "MEDIAN", "category": "Statistical", "syntax": "=MEDIAN(number1, [number2], ...)", "description": "Returns the median.", "example": "=MEDIAN(A1:A20)", "use_case": "Robust central value.",
     "visual_example": {"data": [["A1", 10], ["A2", 20], ["A3", 30], ["A4", 40], ["A5", 50]], "formula_cell": "B1", "formula": "=MEDIAN(A1:A5)", "result": 30}},
    {"name": "MODE", "category": "Statistical", "syntax": "=MODE(number1, [number2], ...)", "description": "Returns the most frequent value.", "example": "=MODE(A1:A20)", "use_case": "Most common rating.",
     "visual_example": {"data": [["A1", 4], ["A2", 5], ["A3", 4], ["A4", 3], ["A5", 4]], "formula_cell": "B1", "formula": "=MODE(A1:A5)", "result": 4}},
    {"name": "STDEV", "category": "Statistical", "syntax": "=STDEV(number1, [number2], ...)", "description": "Estimates standard deviation based on a sample.", "example": "=STDEV(A1:A100)", "use_case": "Measure data spread.",
     "visual_example": {"data": [["A1", 10], ["A2", 12], ["A3", 14], ["A4", 11]], "formula_cell": "B1", "formula": "=STDEV(A1:A4)", "result": 1.71}},
    {"name": "RANK", "category": "Statistical", "syntax": "=RANK(number, ref, [order])", "description": "Returns the rank of a number in a list.", "example": "=RANK(A1, A1:A100, 0)", "use_case": "Leaderboard rankings.",
     "visual_example": {"data": [["A1", 90], ["A2", 75], ["A3", 85]], "formula_cell": "B1", "formula": "=RANK(A1, A1:A3, 0)", "result": 1}},

    # ============= FINANCIAL =============
    {"name": "PMT", "category": "Financial", "syntax": "=PMT(rate, nper, pv, [fv], [type])", "description": "Calculates loan payment based on constant payments and interest rate.", "example": "=PMT(0.05/12, 60, -10000)", "use_case": "Calculate monthly mortgage.",
     "visual_example": {"data": [["A1 (rate/mo)", 0.00417], ["A2 (months)", 60], ["A3 (loan)", -10000]], "formula_cell": "B1", "formula": "=PMT(A1, A2, A3)", "result": "$188.71"}},
    {"name": "FV", "category": "Financial", "syntax": "=FV(rate, nper, pmt, [pv], [type])", "description": "Returns the future value of an investment.", "example": "=FV(0.06/12, 120, -100)", "use_case": "Project savings growth.",
     "visual_example": {"data": [["A1 (rate/mo)", 0.005], ["A2 (months)", 120], ["A3 (pmt)", -100]], "formula_cell": "B1", "formula": "=FV(A1, A2, A3)", "result": "$16,387.93"}},
    {"name": "PV", "category": "Financial", "syntax": "=PV(rate, nper, pmt, [fv], [type])", "description": "Returns the present value of an investment.", "example": "=PV(0.05, 10, -1000)", "use_case": "Discounted cash flow.",
     "visual_example": {"data": [["A1 (rate/yr)", 0.05], ["A2 (years)", 10], ["A3 (pmt)", -1000]], "formula_cell": "B1", "formula": "=PV(A1, A2, A3)", "result": "$7,721.73"}},
    {"name": "NPV", "category": "Financial", "syntax": "=NPV(rate, value1, [value2], ...)", "description": "Net present value of cash flows.", "example": "=NPV(0.1, A1:A10)", "use_case": "Investment evaluation.",
     "visual_example": {"data": [["A1", 1000], ["A2", 2000], ["A3", 3000]], "formula_cell": "B1", "formula": "=NPV(0.1, A1:A3)", "result": "$4,815.93"}},
    {"name": "IRR", "category": "Financial", "syntax": "=IRR(values, [guess])", "description": "Returns the internal rate of return.", "example": "=IRR(A1:A10)", "use_case": "Return on a series of cash flows.",
     "visual_example": {"data": [["A1", -10000], ["A2", 3000], ["A3", 4200], ["A4", 6800]], "formula_cell": "B1", "formula": "=IRR(A1:A4)", "result": "16.32%"}},
]

TUTORIALS = [
    {
        "title": "Mastering VLOOKUP: From Beginner to Pro",
        "category": "Lookup",
        "level": "Intermediate",
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
        "title": "INDEX + MATCH: The VLOOKUP Killer",
        "category": "Lookup",
        "level": "Advanced",
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
        "title": "Cleaning Messy Data Fast",
        "category": "Data Cleaning",
        "level": "Beginner",
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
        "title": "Charts That Actually Communicate",
        "category": "Visualization",
        "level": "Intermediate",
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
        "title": "Fixing #DIV/0!, #N/A, and #VALUE! Errors",
        "category": "Troubleshooting",
        "level": "Beginner",
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
]
