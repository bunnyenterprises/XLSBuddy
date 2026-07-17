"""
Curriculum seed data for XLSBuddy learning platform.
Run seed_curriculum() on startup to populate MongoDB if empty.
"""

CURRICULUM = [
    {
        "slug": "excel-basics",
        "title": "Excel Basics",
        "description": "Start from zero. Learn how Excel works, navigate confidently, and write your first formulas.",
        "level": "beginner",
        "order": 1,
        "emoji": "📗",
        "is_pro": False,
        "estimated_hours": 3,
        "modules": [
            {
                "slug": "getting-started",
                "title": "Getting Started",
                "order": 1,
                "description": "Understand the Excel interface and how data is organized.",
                "lessons": [
                    {
                        "slug": "what-is-excel",
                        "title": "What is Excel?",
                        "order": 1,
                        "xp_value": 10,
                        "estimated_minutes": 4,
                        "content": """## What is Excel?

Microsoft Excel is a **spreadsheet application** — a grid of rows and columns where you store, organize, and analyze data.

### Why Excel Matters
- Used by **over 750 million people** worldwide
- Standard tool in finance, HR, marketing, operations, and data analysis
- Employers expect Excel skills — it appears on 80% of job listings

### The Grid
Excel's workspace is called a **workbook**. Each workbook has **sheets** (tabs at the bottom). Each sheet is a grid of:
- **Columns** — labeled A, B, C ... Z, AA, AB ...
- **Rows** — numbered 1, 2, 3 ...
- **Cells** — the intersection of a column and row. Cell **B3** = column B, row 3.

### The Formula Bar
At the top of the screen, the **formula bar** shows what's inside the selected cell — a number, text, or formula.

### Quick Example
Click cell A1 and type `Hello`. Press Enter. You just added data to Excel!
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "What is the address of the cell in column C, row 5?",
                            "options": ["C5", "5C", "Row5Col3", "3,5"],
                            "answer": "C5",
                            "hints": ["Cell addresses combine the column letter and row number.", "Column comes first, then row number."],
                            "explanation": "Cell addresses always put the column letter first, then the row number. Column C, row 5 = C5.",
                        },
                    },
                    {
                        "slug": "navigating-excel",
                        "title": "Navigating the Interface",
                        "order": 2,
                        "xp_value": 10,
                        "estimated_minutes": 5,
                        "content": """## Navigating the Excel Interface

### The Ribbon
The **Ribbon** is the toolbar at the top. It has tabs:
- **Home** — formatting, font, alignment, number format
- **Insert** — charts, tables, pivot tables
- **Formulas** — formula library, name manager
- **Data** — sort, filter, data validation
- **View** — zoom, freeze panes, split

### Moving Around
| Key | Action |
|-----|--------|
| Arrow keys | Move one cell |
| Ctrl + Arrow | Jump to last filled cell in direction |
| Ctrl + Home | Go to cell A1 |
| Ctrl + End | Go to last used cell |
| Tab | Move right |
| Enter | Move down |

### Selecting Ranges
- Click and drag to select a range
- Click A1, Shift+Click C5 to select A1:C5
- Ctrl+A to select all cells

### The Name Box
Top-left corner shows your current cell address. You can also **type a cell address** here and press Enter to jump directly to it.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "Which keyboard shortcut takes you back to cell A1 from anywhere in the sheet?",
                            "options": ["Ctrl + Home", "Ctrl + A", "Ctrl + Arrow", "Alt + Home"],
                            "answer": "Ctrl + Home",
                            "hints": ["Think of 'Home' as going to the beginning.", "It's the Ctrl key plus the Home key."],
                            "explanation": "Ctrl + Home always navigates to cell A1, no matter where you are in the spreadsheet.",
                        },
                    },
                    {
                        "slug": "entering-data",
                        "title": "Entering and Editing Data",
                        "order": 3,
                        "xp_value": 10,
                        "estimated_minutes": 5,
                        "content": """## Entering and Editing Data

### Three Types of Data
1. **Numbers** — 42, 3.14, -100. Used in calculations.
2. **Text** — "Sales", "Raj Kumar". Labels and descriptions.
3. **Formulas** — Always start with `=`. Excel calculates the result.

### How to Enter Data
1. Click a cell
2. Type your data
3. Press **Enter** (moves down) or **Tab** (moves right) to confirm

### Editing a Cell
- **Double-click** the cell to edit inside it
- **F2** key also enters edit mode
- **Delete** key clears a cell's content
- **Escape** cancels editing without saving

### AutoFill
Type January in A1. Click the small green square at the bottom-right of the cell (called the **fill handle**) and drag down — Excel automatically fills February, March, April...

AutoFill also works with numbers: type 1 in A1 and 2 in A2, select both, then drag the fill handle to continue the series.

### Undo / Redo
- **Ctrl+Z** — undo your last action
- **Ctrl+Y** — redo what you undid
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "What key do you press to start editing the content of a cell you've already selected?",
                            "options": ["F2", "F4", "Enter", "Space"],
                            "answer": "F2",
                            "hints": ["It's a function key.", "F2 puts the cursor inside the cell for editing."],
                            "explanation": "F2 enters edit mode for the selected cell, placing your cursor at the end of the cell's content.",
                        },
                    },
                    {
                        "slug": "basic-formatting",
                        "title": "Basic Formatting",
                        "order": 4,
                        "xp_value": 10,
                        "estimated_minutes": 5,
                        "content": """## Basic Formatting

Good formatting makes your data readable and professional.

### Font Formatting (Home tab)
- **Bold** — Ctrl+B
- *Italic* — Ctrl+I
- Underline — Ctrl+U
- Font size, font color, fill color

### Number Formats
Excel stores numbers as plain values but can **display** them differently:
| Format | Example |
|--------|---------|
| General | 1234.5 |
| Number | 1,234.50 |
| Currency | ₹1,234.50 |
| Percentage | 12.35% |
| Date | 17-Jul-2026 |

Select cells → Home tab → Number group → choose format.

### Alignment
- Left / Center / Right align text
- **Merge & Center** — combines multiple cells into one (great for headers)
- **Wrap Text** — makes long text visible inside a cell without spilling over

### Column Width & Row Height
- Double-click the column border in the header to auto-fit the width
- Right-click a column/row header → "Column Width" or "Row Height"

### Borders
Home → Font group → Borders dropdown. Add borders around cells to create table-like layouts.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "Which number format would display 0.1234 as 12.34%?",
                            "options": ["Percentage", "Number", "Currency", "General"],
                            "answer": "Percentage",
                            "hints": ["The format name literally matches what you want to display.", "It multiplies by 100 and adds a % sign."],
                            "explanation": "The Percentage format multiplies the cell value by 100 and displays it with a % sign. So 0.1234 becomes 12.34%.",
                        },
                    },
                    {
                        "slug": "saving-and-files",
                        "title": "Saving, Sheets & File Types",
                        "order": 5,
                        "xp_value": 10,
                        "estimated_minutes": 4,
                        "content": """## Saving, Sheets & File Types

### Saving Your Work
- **Ctrl+S** — save (overwrites the current file)
- **Ctrl+Shift+S** — Save As (save with a new name or location)
- Excel auto-recovers unsaved work every 10 minutes by default

### File Formats
| Format | Extension | Use When |
|--------|-----------|----------|
| Excel Workbook | .xlsx | Default format — use this always |
| Excel 97-2003 | .xls | Only for very old Excel versions |
| CSV | .csv | Sharing data with other apps/databases |
| PDF | .pdf | Sharing a read-only view |

**Always save as .xlsx** unless someone specifically needs another format.

### Working with Sheets
- **Add a sheet** — click the + button next to sheet tabs
- **Rename a sheet** — double-click the tab name
- **Delete a sheet** — right-click tab → Delete
- **Move a sheet** — drag the tab left or right
- **Copy a sheet** — right-click → Move or Copy → check "Create a copy"

### Referencing Other Sheets
To use data from another sheet in a formula: `=Sheet2!A1`
The `!` separates the sheet name from the cell address.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You need to share an Excel file that others can open in any app or database. Which format should you use?",
                            "options": ["CSV (.csv)", ".xlsx", ".xls", ".pdf"],
                            "answer": "CSV (.csv)",
                            "hints": ["This format stores data as plain text with commas.", "Almost every app and database can import this format."],
                            "explanation": "CSV (Comma-Separated Values) is the universal data exchange format. Any spreadsheet app, database, or programming language can read it.",
                        },
                    },
                ],
            },
            {
                "slug": "first-formulas",
                "title": "Your First Formulas",
                "order": 2,
                "description": "Learn how formulas work and master the most-used Excel functions.",
                "lessons": [
                    {
                        "slug": "understanding-formulas",
                        "title": "How Formulas Work",
                        "order": 1,
                        "xp_value": 10,
                        "estimated_minutes": 5,
                        "content": """## How Formulas Work

Every formula in Excel starts with an **equals sign** `=`.

### Formula Anatomy
```
= SUM ( A1 : A10 )
↑  ↑    ↑    ↑
= Function  Arguments (inputs)
```

- **`=`** — tells Excel this is a formula, not plain text
- **Function name** — what operation to perform (SUM, AVERAGE, IF...)
- **Arguments** — the inputs the function needs, inside parentheses
- **Range** — A1:A10 means all cells from A1 to A10 (the colon means "through")

### Order of Operations
Excel follows BODMAS/PEMDAS:
1. Brackets / Parentheses
2. Exponents (^ symbol)
3. Multiplication and Division
4. Addition and Subtraction

`=2+3*4` → gives **14** (not 20), because 3×4=12 first, then +2

Use parentheses to control order: `=(2+3)*4` → **20**

### Cell References
Instead of typing numbers directly, reference cells:
- `=A1+B1` adds the values in A1 and B1
- When you change A1, the formula result updates **automatically**

### Formula Errors
| Error | Meaning |
|-------|---------|
| #N/A | Value not found |
| #VALUE! | Wrong data type |
| #DIV/0! | Dividing by zero |
| #REF! | Cell reference deleted |
| #NAME? | Function name not recognized |
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a formula that adds the values in cells A1 and A2.",
                            "answer": "=A1+A2",
                            "hints": ["All formulas start with =", "Use + to add two cell references together"],
                            "explanation": "=A1+A2 adds the values in cells A1 and A2. Both cell references are separated by the + operator.",
                        },
                    },
                    {
                        "slug": "sum-average",
                        "title": "SUM and AVERAGE",
                        "order": 2,
                        "xp_value": 10,
                        "estimated_minutes": 5,
                        "content": """## SUM and AVERAGE

### SUM — Add a Range of Numbers
```
=SUM(A1:A10)
```
Adds every number from A1 to A10. No matter how many rows — one formula.

**Multiple ranges:** `=SUM(A1:A5, C1:C5)` adds both ranges together.

**With numbers directly:** `=SUM(A1:A10, 100)` adds the range plus 100.

### AVERAGE — Calculate the Mean
```
=AVERAGE(B1:B20)
```
Adds all values in B1:B20, then divides by the count of numbers. **Blank cells are ignored** — they don't count as zero.

### Real Example
| | A | B |
|--|---|---|
| 1 | Sales | Jan |
| 2 | Delhi | 45000 |
| 3 | Mumbai | 62000 |
| 4 | Pune | 38000 |
| 5 | **Total** | **=SUM(B2:B4)** |
| 6 | **Average** | **=AVERAGE(B2:B4)** |

SUM(B2:B4) = 145000
AVERAGE(B2:B4) = 48333

### Keyboard Shortcut for SUM
Select a cell below a column of numbers and press **Alt + =** — Excel automatically inserts `=SUM(...)` with the range filled in!
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a formula to find the average of all values in cells C1 through C50.",
                            "answer": "=AVERAGE(C1:C50)",
                            "hints": ["The function name is AVERAGE", "The range goes from C1 to C50, written as C1:C50"],
                            "explanation": "=AVERAGE(C1:C50) calculates the mean of all numeric values in cells C1 to C50, ignoring any blank cells.",
                        },
                    },
                    {
                        "slug": "min-max-count",
                        "title": "MIN, MAX and COUNT",
                        "order": 3,
                        "xp_value": 10,
                        "estimated_minutes": 5,
                        "content": """## MIN, MAX and COUNT

### MIN — Find the Smallest Value
```
=MIN(A1:A100)
```
Returns the lowest number in the range. Useful for finding the minimum salary, lowest price, earliest date.

### MAX — Find the Largest Value
```
=MAX(A1:A100)
```
Returns the highest number. Useful for finding the top performer, maximum score, latest date.

### COUNT — Count Cells with Numbers
```
=COUNT(A1:A100)
```
Counts only cells that contain **numbers**. Skips text and blank cells.

### COUNTA — Count Non-Empty Cells
```
=COUNTA(A1:A100)
```
Counts cells that contain **anything** — numbers, text, dates. Only skips blanks.

### COUNTBLANK — Count Empty Cells
```
=COUNTBLANK(A1:A100)
```
Counts cells that are completely empty.

### Practical Example
You have exam scores in B2:B51 (50 students):
- `=COUNT(B2:B51)` → 47 (3 students didn't submit)
- `=MAX(B2:B51)` → 98 (top score)
- `=MIN(B2:B51)` → 23 (lowest score)
- `=AVERAGE(B2:B51)` → 71.4 (class average, calculated from 47 scores)
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a formula to find the highest value in the range D2:D100.",
                            "answer": "=MAX(D2:D100)",
                            "hints": ["The function that finds the largest value is MAX", "The range is D2 through D100"],
                            "explanation": "=MAX(D2:D100) scans all cells from D2 to D100 and returns the highest numeric value found.",
                        },
                    },
                    {
                        "slug": "if-function",
                        "title": "The IF Function",
                        "order": 4,
                        "xp_value": 15,
                        "estimated_minutes": 6,
                        "content": """## The IF Function

IF lets Excel **make decisions** — if a condition is true, show one thing; otherwise show another.

### Syntax
```
=IF(condition, value_if_true, value_if_false)
```

### Simple Example
```
=IF(A2 > 50, "Pass", "Fail")
```
- If A2 is greater than 50 → shows "Pass"
- Otherwise → shows "Fail"

### Comparison Operators
| Operator | Meaning |
|----------|---------|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `=` | Equal to |
| `<>` | Not equal to |

### Using Numbers Instead of Text
```
=IF(B2 >= 90, 100, 0)
```
Awards 100 bonus points if score is 90+, otherwise 0.

### Nested IF (Multiple Conditions)
```
=IF(A2 >= 90, "A", IF(A2 >= 75, "B", IF(A2 >= 60, "C", "Fail")))
```
Checks conditions one by one until one is true.

### Tip
Always use quotes around text values inside IF: `"Pass"` not `Pass`. Numbers don't need quotes: `100` not `"100"`.
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write an IF formula: if cell B2 is greater than 100, show \"High\", otherwise show \"Low\".",
                            "answer": '=IF(B2>100,"High","Low")',
                            "hints": [
                                "Syntax: =IF(condition, true_value, false_value)",
                                'Text values need quotes: "High" and "Low"',
                                "The condition is: B2 > 100",
                            ],
                            "explanation": '=IF(B2>100,"High","Low") checks if B2 is greater than 100. If yes, it shows "High". If no, it shows "Low".',
                        },
                    },
                    {
                        "slug": "basic-math",
                        "title": "Math Operators & ROUND",
                        "order": 5,
                        "xp_value": 10,
                        "estimated_minutes": 5,
                        "content": """## Math Operators & ROUND

### Basic Math in Formulas
| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Add | `=A1+B1` |
| `-` | Subtract | `=A1-B1` |
| `*` | Multiply | `=A1*B1` |
| `/` | Divide | `=A1/B1` |
| `^` | Power/Exponent | `=A1^2` (squares A1) |
| `%` | Percentage | `=A1*10%` (10% of A1) |

### Calculating Percentages
```
=B2/B12   → gives 0.25
```
Format the cell as Percentage to display it as 25%.

**Percentage increase:**
```
=(New - Old) / Old
```

### ROUND — Control Decimal Places
```
=ROUND(A1, 2)     → rounds to 2 decimal places
=ROUND(A1, 0)     → rounds to nearest whole number
=ROUND(A1, -1)    → rounds to nearest 10
=ROUNDUP(A1, 2)   → always rounds up
=ROUNDDOWN(A1, 2) → always rounds down
```

### Why ROUND Matters
`=10/3` gives 3.333333... — ugly in reports. `=ROUND(10/3, 2)` gives 3.33.

Also prevents the problem where totals don't match because of hidden decimal places.
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a formula to multiply cells A1 and B1, then round the result to 2 decimal places.",
                            "answer": "=ROUND(A1*B1,2)",
                            "hints": ["Use ROUND to control decimals", "The first argument is the value to round: A1*B1", "The second argument is the number of decimal places: 2"],
                            "explanation": "=ROUND(A1*B1,2) first multiplies A1 by B1, then rounds the result to exactly 2 decimal places.",
                        },
                    },
                ],
            },
            {
                "slug": "working-with-data",
                "title": "Working with Data",
                "order": 3,
                "description": "Sort, filter, and organize data like a professional.",
                "lessons": [
                    {
                        "slug": "sorting-data",
                        "title": "Sorting Data",
                        "order": 1,
                        "xp_value": 10,
                        "estimated_minutes": 4,
                        "content": """## Sorting Data

Sorting arranges your data in a specific order — alphabetical, numerical, or by date.

### Quick Sort
1. Click any cell inside the column you want to sort by
2. Home tab → Sort & Filter → **Sort A to Z** (ascending) or **Sort Z to A** (descending)

Excel automatically expands the selection to include all connected data — your rows stay together.

### Custom Sort (Multiple Levels)
**Data tab → Sort** opens the Sort dialog:
1. **Sort by** — primary column (e.g., Department)
2. **Then by** — secondary column (e.g., Salary)

Example: Sort by Department A→Z, then within each department, by Salary high→low.

### Sort Options
- **Sort A to Z** — alphabetical for text, smallest first for numbers, oldest first for dates
- **Sort Z to A** — reverse of above
- **Custom List** — sort by a custom order (e.g., Mon, Tue, Wed instead of alphabetical)

### Important: Always Have a Header Row
Excel uses the first row as headers if your data has them. Enable "My data has headers" in the Sort dialog so your header row doesn't get sorted into the data.

### Tip: Add a Row Number Column Before Sorting
If you might want to restore the original order, add a column with 1, 2, 3, 4... first. Sort by that column to restore the original order.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You want to sort a list of employees first by Department (A-Z), then by Salary (high to low) within each department. Which Excel feature do you use?",
                            "options": ["Custom Sort with multiple levels", "Sort A to Z button", "Filter", "AutoFill"],
                            "answer": "Custom Sort with multiple levels",
                            "hints": ["You need two sorting criteria.", "This feature is in the Data tab → Sort dialog."],
                            "explanation": "Custom Sort (Data tab → Sort) lets you add multiple sort levels. Level 1: Department A-Z. Level 2: Salary largest-to-smallest.",
                        },
                    },
                    {
                        "slug": "filtering-data",
                        "title": "Filtering Data",
                        "order": 2,
                        "xp_value": 10,
                        "estimated_minutes": 5,
                        "content": """## Filtering Data

Filtering hides rows that don't match your criteria — the data is still there, just hidden.

### Enable AutoFilter
Click any cell in your data → **Data tab → Filter** (or Ctrl+Shift+L).
Dropdown arrows appear on every column header.

### Using a Filter
1. Click the dropdown arrow on the column you want to filter
2. Uncheck **Select All**
3. Check only the values you want to see
4. Click OK

The row numbers turn blue, and a filter icon appears on the column header.

### Number Filters
For number columns, the dropdown offers **Number Filters**:
- Greater than, Less than, Between
- Top 10 (shows the top N values)
- Above/Below Average

### Text Filters
For text columns:
- Contains, Does Not Contain
- Begins With, Ends With

### Filter by Color
If you've color-coded cells, you can filter to show only cells of a specific color.

### Clear a Filter
- Click the filter dropdown → Clear Filter
- Or Data tab → Clear to remove all filters at once
- Ctrl+Shift+L again to turn off AutoFilter completely

### Filter vs Sort
| Filter | Sort |
|--------|------|
| Hides rows | Rearranges rows |
| Data is still there | Order permanently changes (until you re-sort) |
| Multiple criteria easy | Multiple levels via Custom Sort |
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "After applying a filter, what happens to the rows that don't match the filter criteria?",
                            "options": ["They are hidden but still in the spreadsheet", "They are deleted permanently", "They move to another sheet", "They turn red"],
                            "answer": "They are hidden but still in the spreadsheet",
                            "hints": ["Filtering is non-destructive.", "You can always clear the filter to see all rows again."],
                            "explanation": "Filtering only hides rows temporarily. The data is still there — you can see this because row numbers skip (e.g., 1, 3, 7...). Clear the filter to show all rows again.",
                        },
                    },
                    {
                        "slug": "tables",
                        "title": "Excel Tables",
                        "order": 3,
                        "xp_value": 15,
                        "estimated_minutes": 5,
                        "content": """## Excel Tables

Converting a data range into an **Excel Table** is one of the most useful things you can do.

### Create a Table
1. Click any cell in your data
2. Press **Ctrl+T** (or Insert → Table)
3. Confirm the range and check "My table has headers"
4. Click OK

### What Tables Give You Automatically
- **Filter dropdowns** on every column header
- **Striped rows** for readability
- **Auto-expand** — add a row below the table, it joins the table
- **Structured references** — formulas use column names instead of cell addresses

### Structured References
Instead of `=SUM(B2:B100)`, a table formula writes:
```
=SUM(Table1[Sales])
```
This is clearer and automatically includes new rows added to the table.

### Total Row
Table Design tab → check **Total Row** — adds a row at the bottom with sum/average/count dropdowns for each column.

### Table Name
By default tables are named Table1, Table2... Rename them in the Table Design tab to something meaningful like `SalesData`.

### Convert Back to Range
Table Design tab → Convert to Range — removes table formatting but keeps the data.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "What is the keyboard shortcut to convert a data range into an Excel Table?",
                            "options": ["Ctrl+T", "Ctrl+Table", "Alt+T", "Ctrl+Shift+T"],
                            "answer": "Ctrl+T",
                            "hints": ["It's a Ctrl key shortcut.", "T stands for Table."],
                            "explanation": "Ctrl+T instantly converts a selected data range into a formatted Excel Table with auto-filter, striped rows, and structured references.",
                        },
                    },
                    {
                        "slug": "find-replace",
                        "title": "Find, Replace & Go To",
                        "order": 4,
                        "xp_value": 10,
                        "estimated_minutes": 4,
                        "content": """## Find, Replace & Go To

### Find (Ctrl+F)
Search for any value, text, or formula in your spreadsheet.
- **Find Next** — jumps to each match one by one
- **Find All** — lists every match at once
- Options: Match Case, Match Entire Cell Contents, Look in Formulas/Values

### Replace (Ctrl+H)
Find a value and replace it with something else.
- Replace **one** at a time — Replace
- Replace **all** at once — Replace All

**Example:** Replace all instances of "Mumbai" with "Bombay" across 500 rows — one click.

### Wildcards in Find
- `*` — matches any number of characters. `Mar*` finds March, Marketing, Marvel
- `?` — matches one character. `B?g` finds Bag, Big, Bug, Bog

### Go To Special (Ctrl+G → Special)
This hidden gem lets you select specific types of cells:
- **Blanks** — select all empty cells (then type a value and press Ctrl+Enter to fill them all)
- **Formulas** — see which cells have formulas vs plain values
- **Last cell** — find the extent of your data
- **Constants** — find cells with hard-coded numbers

### Find & Replace for Formatting
Advanced Find (expand Options) lets you find cells by format (background color, font, borders).
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You want to replace every instance of 'Old Company Name' with 'New Company Name' across a 1000-row spreadsheet. What's the fastest way?",
                            "options": ["Ctrl+H → Replace All", "Manually edit each cell", "Ctrl+F → Find Next and retype", "Use a formula"],
                            "answer": "Ctrl+H → Replace All",
                            "hints": ["This is the Find & Replace shortcut.", "'Replace All' does every replacement in one click."],
                            "explanation": "Ctrl+H opens Find & Replace. Type the old text in 'Find what', the new text in 'Replace with', then click 'Replace All' to update every instance instantly.",
                        },
                    },
                    {
                        "slug": "basic-charts",
                        "title": "Creating Your First Chart",
                        "order": 5,
                        "xp_value": 15,
                        "estimated_minutes": 6,
                        "content": """## Creating Your First Chart

Charts turn numbers into visuals that people actually understand.

### Create a Chart in 3 Clicks
1. Select your data (including headers)
2. Press **Alt+F1** — inserts a chart on the same sheet
   Or **F11** — inserts chart on a new sheet
3. Change the chart type if needed

### Chart Types — Which to Use?
| Chart Type | Best For |
|-----------|----------|
| **Column/Bar** | Comparing categories (sales by city) |
| **Line** | Trends over time (monthly revenue) |
| **Pie/Doughnut** | Parts of a whole (market share) |
| **Scatter** | Relationship between two variables |
| **Area** | Cumulative totals over time |

**Rule of thumb:** Use column/bar charts for almost everything. They're the clearest.

### Customizing Charts
Click the chart to select it, then:
- **Chart Design tab** — change chart type, switch rows/columns, add data
- **Format tab** — colors, fonts, layout
- Click directly on chart elements (title, legend, axis) to edit them

### Chart Title
Click the default "Chart Title" text and type your own. Always add a title.

### The 3 Buttons Next to a Selected Chart
- **+** (Chart Elements) — add/remove title, legend, data labels, gridlines
- 🎨 (Chart Styles) — quick color and style presets
- ▽ (Chart Filters) — show/hide specific data series

### Sparklines — Mini Charts Inside Cells
Insert → Sparklines → Line/Column/Win-Loss — creates a tiny chart inside a single cell. Great for dashboards.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You want to show how monthly sales have changed over 12 months. Which chart type is most appropriate?",
                            "options": ["Line chart", "Pie chart", "Scatter chart", "Doughnut chart"],
                            "answer": "Line chart",
                            "hints": ["This chart is best for showing change over time.", "The x-axis would show months, y-axis would show sales."],
                            "explanation": "A Line chart is ideal for showing trends over time. Each month is a point on the x-axis, and the line connecting them shows the trend clearly.",
                        },
                    },
                ],
            },
        ],
    },
    {
        "slug": "excel-intermediate",
        "title": "Intermediate Excel",
        "description": "Master lookup functions, logical formulas, and text/date manipulation — the skills that separate beginners from professionals.",
        "level": "intermediate",
        "order": 2,
        "emoji": "📘",
        "is_pro": False,
        "estimated_hours": 4,
        "modules": [
            {
                "slug": "lookup-functions",
                "title": "Lookup Functions",
                "order": 1,
                "description": "Find and retrieve data from large tables automatically.",
                "lessons": [
                    {
                        "slug": "vlookup",
                        "title": "VLOOKUP",
                        "order": 1,
                        "xp_value": 20,
                        "estimated_minutes": 8,
                        "content": """## VLOOKUP — Vertical Lookup

VLOOKUP searches for a value in the **leftmost column** of a table and returns a value from another column in the same row.

### Syntax
```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

| Argument | What it means |
|----------|--------------|
| `lookup_value` | What you're searching for (e.g., employee ID, product code) |
| `table_array` | The table to search in (select the whole table) |
| `col_index_num` | Which column to return (1=first, 2=second...) |
| `range_lookup` | FALSE for exact match, TRUE for approximate |

### Real Example
You have an employee table in A1:C100 with columns: ID, Name, Salary.
To find the salary for employee ID "E005":
```
=VLOOKUP("E005", A1:C100, 3, FALSE)
```
- Searches column A for "E005"
- Returns the value from column 3 (Salary)
- FALSE = exact match required

### Common Mistake
The lookup value **must be in the first column** of your table array. If it's not, VLOOKUP won't work — use INDEX MATCH instead.

### VLOOKUP Returns #N/A
This means the lookup value wasn't found. Wrap with IFERROR:
```
=IFERROR(VLOOKUP(A2, Table, 2, FALSE), "Not Found")
```

### Absolute References
When copying VLOOKUP down a column, **lock the table reference** with $:
```
=VLOOKUP(A2, $B$1:$D$100, 2, FALSE)
```
Without $, the table range shifts as you copy the formula down.
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a VLOOKUP to find the value in column 2 of the table B1:D50, searching for the value in cell A2. Use exact match.",
                            "answer": "=VLOOKUP(A2,B1:D50,2,FALSE)",
                            "hints": [
                                "Syntax: =VLOOKUP(lookup_value, table, col_number, FALSE)",
                                "The lookup value is A2",
                                "The table range is B1:D50",
                                "Column 2 = second column of the table",
                                "FALSE = exact match",
                            ],
                            "explanation": "=VLOOKUP(A2,B1:D50,2,FALSE) searches for A2's value in the first column of B1:D50, then returns the value from the 2nd column of that table.",
                        },
                    },
                    {
                        "slug": "xlookup",
                        "title": "XLOOKUP — The Modern Lookup",
                        "order": 2,
                        "xp_value": 20,
                        "estimated_minutes": 7,
                        "content": """## XLOOKUP — VLOOKUP's Successor

XLOOKUP was introduced in Excel 2019/365 and fixes all of VLOOKUP's limitations.

### Syntax
```
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

### Compared to VLOOKUP
| Feature | VLOOKUP | XLOOKUP |
|---------|---------|---------|
| Search direction | Left column only | Any column |
| Return column | Column number (fragile) | Direct range reference |
| Not found | Returns #N/A error | Custom message built-in |
| Multiple returns | No | Yes (select multiple columns) |
| Search order | Top-to-bottom only | Can search bottom-to-top |

### Example: Same as our VLOOKUP
```
=XLOOKUP("E005", A1:A100, C1:C100, "Not Found")
```
- Searches A1:A100 for "E005"
- Returns the matching value from C1:C100
- Shows "Not Found" if not found (no IFERROR needed!)

### Search in Any Direction
```
=XLOOKUP(A2, D1:D100, A1:A100)
```
This searches column D and returns from column A — VLOOKUP can't do this.

### Return Multiple Columns
```
=XLOOKUP("E005", A1:A100, B1:D100)
```
Returns Name, Department, and Salary all at once (spills into 3 columns).

### If Not Available
XLOOKUP requires Excel 2019, Microsoft 365, or Excel for the web. For older Excel, use VLOOKUP or INDEX MATCH.
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write an XLOOKUP that searches for cell A2's value in the range E1:E100, returns from F1:F100, and shows \"Missing\" if not found.",
                            "answer": '=XLOOKUP(A2,E1:E100,F1:F100,"Missing")',
                            "hints": [
                                "Syntax: =XLOOKUP(lookup, search_range, return_range, if_not_found)",
                                'The if_not_found argument is "Missing" — in quotes',
                            ],
                            "explanation": '=XLOOKUP(A2,E1:E100,F1:F100,"Missing") searches E1:E100 for A2\'s value, returns the matching value from F1:F100, and shows "Missing" if not found.',
                        },
                    },
                    {
                        "slug": "index-match",
                        "title": "INDEX + MATCH",
                        "order": 3,
                        "xp_value": 25,
                        "estimated_minutes": 8,
                        "content": """## INDEX + MATCH

INDEX MATCH is the professional's alternative to VLOOKUP. It's two functions combined.

### MATCH — Find the Position
```
=MATCH(lookup_value, lookup_array, 0)
```
Returns the **row number** where the value is found. The `0` means exact match.

Example: `=MATCH("Raj", A1:A100, 0)` → returns 5 if "Raj" is in row 5.

### INDEX — Get a Value by Position
```
=INDEX(array, row_number)
```
Returns the value at a specific position in a range.

Example: `=INDEX(C1:C100, 5)` → returns the value in C5.

### Combined: INDEX MATCH
```
=INDEX(C1:C100, MATCH("Raj", A1:A100, 0))
```
1. MATCH finds the row where "Raj" is in column A
2. INDEX gets the value from that same row in column C

### Why Use INDEX MATCH Over VLOOKUP?
1. **No column counting** — reference the exact return column directly
2. **Looks in any direction** — can look right-to-left
3. **Doesn't break** when you insert columns (VLOOKUP's column number shifts)
4. **Faster** on very large datasets

### Two-Way Lookup
```
=INDEX(B2:E10, MATCH(A14, A2:A10, 0), MATCH(B14, B1:E1, 0))
```
Finds both the row and column position — like looking up a value in a 2D table.
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write an INDEX MATCH formula: search for cell A2 in column B (B1:B100), and return the matching value from column D (D1:D100).",
                            "answer": "=INDEX(D1:D100,MATCH(A2,B1:B100,0))",
                            "hints": [
                                "Structure: =INDEX(return_range, MATCH(lookup, search_range, 0))",
                                "MATCH goes inside INDEX as the row number argument",
                                "0 at the end of MATCH = exact match",
                            ],
                            "explanation": "=INDEX(D1:D100,MATCH(A2,B1:B100,0)) — MATCH finds what row A2 is in within B1:B100, then INDEX returns the value from that same row in D1:D100.",
                        },
                    },
                    {
                        "slug": "iferror",
                        "title": "IFERROR & Error Handling",
                        "order": 4,
                        "xp_value": 15,
                        "estimated_minutes": 5,
                        "content": """## IFERROR & Error Handling

Nothing looks worse in a professional spreadsheet than a column full of #N/A errors. IFERROR fixes that.

### IFERROR Syntax
```
=IFERROR(formula, value_if_error)
```
If the formula produces any error, show the fallback value instead.

### Common Use Cases
```
=IFERROR(VLOOKUP(A2,B:C,2,0), "Not Found")
=IFERROR(A1/B1, 0)
=IFERROR(INDEX(D:D, MATCH(A2,B:B,0)), "-")
```

### Excel Error Types
| Error | Cause | Common Fix |
|-------|-------|------------|
| `#N/A` | Value not found in lookup | IFERROR with "Not Found" |
| `#DIV/0!` | Dividing by zero | IFERROR with 0 |
| `#VALUE!` | Wrong data type | Check input format |
| `#REF!` | Cell referenced was deleted | Fix the formula |
| `#NAME?` | Typo in function name | Correct the spelling |
| `#NUM!` | Invalid numeric value | Check input range |

### IFNA — Only Catch #N/A
IFNA is like IFERROR but only catches #N/A errors, not all errors:
```
=IFNA(VLOOKUP(A2, Table, 2, 0), "Not in list")
```
Use IFNA when you want other errors (like #DIV/0!) to still show — they indicate real problems.

### ISERROR / ISERR / ISNA
These return TRUE/FALSE and can be used in IF statements:
```
=IF(ISERROR(VLOOKUP(A2,B:C,2,0)), "Not Found", VLOOKUP(A2,B:C,2,0))
```
(Old approach before IFERROR — IFERROR is simpler.)
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a formula that divides A1 by B1, but shows 0 instead of an error if B1 is zero.",
                            "answer": "=IFERROR(A1/B1,0)",
                            "hints": ["Use IFERROR to catch the division error", "The formula is A1/B1", "The fallback value is 0"],
                            "explanation": "=IFERROR(A1/B1,0) tries to divide A1 by B1. If B1 is 0, it would normally show #DIV/0! — IFERROR catches that and shows 0 instead.",
                        },
                    },
                    {
                        "slug": "sumif-countif",
                        "title": "SUMIF and COUNTIF",
                        "order": 5,
                        "xp_value": 20,
                        "estimated_minutes": 7,
                        "content": """## SUMIF and COUNTIF — Conditional Calculations

### COUNTIF — Count Rows Matching a Condition
```
=COUNTIF(range, criteria)
```
**Examples:**
```
=COUNTIF(B:B, "Delhi")         → count rows where city is Delhi
=COUNTIF(C:C, ">50000")        → count rows where salary > 50,000
=COUNTIF(A:A, "Raj*")          → count rows where name starts with "Raj"
=COUNTIF(D:D, "<>"&"")        → count non-empty cells
```

### SUMIF — Sum Rows Matching a Condition
```
=SUMIF(range, criteria, sum_range)
```
**Examples:**
```
=SUMIF(B:B, "Delhi", C:C)       → total sales only from Delhi
=SUMIF(C:C, ">50000", D:D)     → sum bonuses for employees earning >50k
=SUMIF(A:A, "Q1", B:B)         → sum of Q1 values
```

### COUNTIFS / SUMIFS — Multiple Conditions
Add an "S" to handle more than one condition:
```
=COUNTIFS(B:B, "Delhi", C:C, ">50000")
→ count rows where city=Delhi AND salary>50,000

=SUMIFS(D:D, B:B, "Delhi", C:C, "Manager")
→ sum column D where city=Delhi AND role=Manager
```

### Wildcards in Criteria
- `"*"` — any text. `"Del*"` matches Delhi, Delhivery, Deli
- `"?"` — any single character. `"R?j"` matches Raj, Roj

### AVERAGEIF / AVERAGEIFS
Same syntax as SUMIF but calculates an average:
```
=AVERAGEIF(B:B, "Delhi", C:C)   → average salary only from Delhi
```
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a SUMIF formula to add all values in column C where the corresponding value in column A equals \"Sales\".",
                            "answer": '=SUMIF(A:A,"Sales",C:C)',
                            "hints": [
                                "Syntax: =SUMIF(criteria_range, criteria, sum_range)",
                                "criteria_range = column A",
                                'criteria = "Sales" (in quotes)',
                                "sum_range = column C",
                            ],
                            "explanation": '=SUMIF(A:A,"Sales",C:C) looks through column A for cells that say "Sales", then adds up the corresponding values in column C.',
                        },
                    },
                ],
            },
            {
                "slug": "logical-functions",
                "title": "Logical & Text Functions",
                "order": 2,
                "description": "Build smart formulas that handle multiple conditions and manipulate text.",
                "lessons": [
                    {
                        "slug": "and-or",
                        "title": "AND, OR and Nested IF",
                        "order": 1,
                        "xp_value": 20,
                        "estimated_minutes": 7,
                        "content": """## AND, OR and Nested IF

### AND — All Conditions Must Be True
```
=AND(condition1, condition2, condition3...)
```
Returns TRUE only if **every** condition is true.
```
=AND(A2>18, B2="Active")    → TRUE only if age>18 AND status is Active
```

### OR — At Least One Condition Must Be True
```
=OR(condition1, condition2...)
```
Returns TRUE if **any** condition is true.
```
=OR(A2="Delhi", A2="Mumbai")  → TRUE if city is Delhi OR Mumbai
```

### Combining with IF
```
=IF(AND(A2>18, B2="Active"), "Eligible", "Not Eligible")
=IF(OR(A2="Manager", A2="Director"), "Senior", "Junior")
```

### IFS Function — Cleaner Than Nested IF
```
=IFS(
  A2>=90, "A",
  A2>=75, "B",
  A2>=60, "C",
  A2>=40, "D",
  TRUE, "Fail"
)
```
Much easier to read than:
```
=IF(A2>=90,"A",IF(A2>=75,"B",IF(A2>=60,"C",IF(A2>=40,"D","Fail"))))
```
The `TRUE` at the end is the "else" — catches everything that didn't match above.

### NOT Function
```
=NOT(A2="Delhi")    → TRUE if city is NOT Delhi
=IF(NOT(ISBLANK(A2)), "Has value", "Empty")
```
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write an IF formula that shows \"Approved\" if A2 is greater than 100 AND B2 equals \"Yes\", otherwise shows \"Rejected\".",
                            "answer": '=IF(AND(A2>100,B2="Yes"),"Approved","Rejected")',
                            "hints": [
                                "Use AND() inside IF() to check both conditions",
                                'Syntax: =IF(AND(cond1, cond2), "true_result", "false_result")',
                                'B2="Yes" checks if B2 contains the text Yes',
                            ],
                            "explanation": '=IF(AND(A2>100,B2="Yes"),"Approved","Rejected") — AND checks both conditions. If A2>100 AND B2="Yes" are both true, shows "Approved". Otherwise "Rejected".',
                        },
                    },
                    {
                        "slug": "text-functions",
                        "title": "Text Functions: LEFT, RIGHT, MID, LEN",
                        "order": 2,
                        "xp_value": 20,
                        "estimated_minutes": 7,
                        "content": """## Text Functions

### LEFT — Extract from the Left
```
=LEFT(text, num_chars)
=LEFT("EXCEL2024", 5)    → "EXCEL"
=LEFT(A2, 3)             → first 3 characters of A2
```

### RIGHT — Extract from the Right
```
=RIGHT(text, num_chars)
=RIGHT("EXCEL2024", 4)   → "2024"
=RIGHT(A2, 6)            → last 6 characters of A2
```

### MID — Extract from the Middle
```
=MID(text, start_position, num_chars)
=MID("EXCEL2024", 2, 4)  → "XCEL" (start at position 2, take 4 chars)
```

### LEN — Count Characters
```
=LEN("Excel")      → 5
=LEN(A2)           → number of characters in A2
```

### Practical Combinations
**Extract area code from phone number "022-45678901":**
```
=LEFT(A2, 3)             → "022"
```

**Extract last name from "Raj Kumar":**
```
=MID(A2, FIND(" ", A2)+1, LEN(A2))   → "Kumar"
```

**Check if a code starts with "INV":**
```
=IF(LEFT(A2,3)="INV", "Invoice", "Other")
```

### TRIM — Remove Extra Spaces
```
=TRIM(A2)
```
Removes spaces from the start, end, and collapses multiple internal spaces to one. This is the **#1 fix** when VLOOKUP returns #N/A — often caused by invisible spaces in data.

### UPPER, LOWER, PROPER
```
=UPPER("excel")       → "EXCEL"
=LOWER("EXCEL")       → "excel"
=PROPER("raj kumar")  → "Raj Kumar"
```
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a formula to extract the first 4 characters from cell A1.",
                            "answer": "=LEFT(A1,4)",
                            "hints": [
                                "Use the LEFT function",
                                "Syntax: =LEFT(text, number_of_characters)",
                                "You want 4 characters from the left side",
                            ],
                            "explanation": "=LEFT(A1,4) extracts the first 4 characters from the left side of whatever text is in cell A1.",
                        },
                    },
                    {
                        "slug": "textjoin-concat",
                        "title": "TEXTJOIN and CONCATENATE",
                        "order": 3,
                        "xp_value": 15,
                        "estimated_minutes": 5,
                        "content": """## TEXTJOIN and CONCATENATE

### The Old Way — & Operator
```
=A2 & " " & B2         → joins A2, a space, and B2
="Order: " & C2        → "Order: INV001"
```
Works fine for a few cells but gets messy with many.

### CONCATENATE (Legacy)
```
=CONCATENATE(A2, " ", B2, " ", C2)
```
Joins multiple items. Available in all Excel versions. Can't handle ranges.

### CONCAT (Modern)
```
=CONCAT(A2:D2)
```
Like CONCATENATE but accepts a range. No separator though.

### TEXTJOIN — Best for Multiple Cells
```
=TEXTJOIN(delimiter, ignore_empty, range)
=TEXTJOIN(", ", TRUE, A2:A10)   → "Raj, Priya, Amit, Neha, ..."
=TEXTJOIN(" - ", FALSE, B2:B5)  → joins with " - " separator
```
- First argument: the separator between values
- Second argument: TRUE = skip blank cells, FALSE = include blanks
- Third+ arguments: values or ranges to join

### Practical Example — Build Full Address
```
Columns: A=Street, B=City, C=State, D=PIN
=TEXTJOIN(", ", TRUE, A2, B2, C2, D2)
→ "42 MG Road, Pune, Maharashtra, 411001"
```

### TEXTSPLIT (Excel 365)
The reverse of TEXTJOIN — splits text into multiple cells:
```
=TEXTSPLIT("Raj,Priya,Amit", ",")   → splits into 3 columns
```
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a TEXTJOIN formula to combine all values in A1:A5, separated by a comma and space, skipping any blank cells.",
                            "answer": '=TEXTJOIN(", ",TRUE,A1:A5)',
                            "hints": [
                                'The separator is ", " (comma and space — in quotes)',
                                "TRUE means skip blank cells",
                                "The range is A1:A5",
                            ],
                            "explanation": '=TEXTJOIN(", ",TRUE,A1:A5) joins all non-blank values in A1:A5 with ", " between each value.',
                        },
                    },
                    {
                        "slug": "date-functions",
                        "title": "Date & Time Functions",
                        "order": 4,
                        "xp_value": 20,
                        "estimated_minutes": 7,
                        "content": """## Date & Time Functions

### Today's Date and Current Time
```
=TODAY()     → current date (updates daily)
=NOW()       → current date and time (updates on recalculation)
```

### Building Dates
```
=DATE(year, month, day)
=DATE(2026, 7, 17)   → 17-Jul-2026
=DATE(A2, B2, C2)    → date from separate year/month/day cells
```

### Extracting Parts of a Date
```
=YEAR(A2)    → extracts the year (e.g., 2026)
=MONTH(A2)   → extracts month number (1-12)
=DAY(A2)     → extracts day number (1-31)
=WEEKDAY(A2) → day of week (1=Sunday, 7=Saturday)
=TEXT(A2, "dddd")   → "Thursday" (full day name)
```

### Calculating Date Differences
```
=A2 - B2                    → number of days between two dates
=DATEDIF(start, end, "D")   → days between dates
=DATEDIF(start, end, "M")   → complete months between dates
=DATEDIF(start, end, "Y")   → complete years (age calculation!)
```

**Age calculation:**
```
=DATEDIF(B2, TODAY(), "Y")  → person's age in years
```

### Adding/Subtracting from Dates
```
=A2 + 30                    → date 30 days from A2
=EDATE(A2, 3)               → date 3 months from A2
=EOMONTH(A2, 0)             → last day of A2's month
=WORKDAY(A2, 10)            → 10 working days from A2 (skips weekends)
```

### Overdue Calculation
```
=IF(TODAY() > A2, "OVERDUE", "On Time")
```
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a formula to calculate a person's age in complete years, given their birthdate is in cell B2.",
                            "answer": '=DATEDIF(B2,TODAY(),"Y")',
                            "hints": [
                                "Use DATEDIF with TODAY() as the end date",
                                'The "Y" unit returns complete years',
                                "Syntax: =DATEDIF(start_date, end_date, unit)",
                            ],
                            "explanation": '=DATEDIF(B2,TODAY(),"Y") calculates the number of complete years between the birthdate in B2 and today — which is the person\'s age.',
                        },
                    },
                    {
                        "slug": "named-ranges",
                        "title": "Named Ranges & Data Validation",
                        "order": 5,
                        "xp_value": 15,
                        "estimated_minutes": 6,
                        "content": """## Named Ranges & Data Validation

### Named Ranges — Give Ranges Meaningful Names
Instead of `=SUM(B2:B100)`, write `=SUM(SalesData)`.

**Create a named range:**
1. Select the range B2:B100
2. Click the Name Box (top-left, shows "B2")
3. Type your name (e.g., `SalesData`) and press Enter

Or: Formulas tab → Name Manager → New.

**Rules for names:** No spaces, can't start with a number, not a cell address.

**Using named ranges in formulas:**
```
=SUM(SalesData)
=AVERAGE(Salaries)
=VLOOKUP(A2, EmployeeTable, 2, FALSE)
```
Much easier to read and maintain!

### Data Validation — Control What Users Enter
Data tab → Data Validation.

**Allow only numbers between 1 and 100:**
- Allow: Whole number
- Between: 1 and 100
- Error Alert: "Please enter a number between 1 and 100"

**Dropdown list:**
- Allow: List
- Source: `Delhi,Mumbai,Pune,Chennai` (comma-separated) or a range like `$F$1:$F$10`

**Date range:**
- Allow: Date
- Between: 01-01-2024 and 31-12-2026

### Input Message
Show a helpful hint when someone clicks the cell (like a tooltip).

### Circle Invalid Data
Data tab → Data Validation → Circle Invalid Data — draws a red circle around cells that don't meet the validation rules (useful after importing data).
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You want to ensure users can only enter a date in 2026 into cell A2. Which Excel feature do you use?",
                            "options": ["Data Validation", "Conditional Formatting", "Data Filter", "IFERROR"],
                            "answer": "Data Validation",
                            "hints": ["This feature controls what type of data can be entered into a cell.", "It's in the Data tab."],
                            "explanation": "Data Validation (Data tab → Data Validation) lets you restrict cell input to specific types, ranges, or lists. Set Allow: Date, Between: 01-01-2026 and 31-12-2026.",
                        },
                    },
                ],
            },
            {
                "slug": "advanced-basics",
                "title": "Power Data Tools",
                "order": 3,
                "description": "Conditional formatting, pivot tables, and dynamic arrays — the tools professionals use daily.",
                "lessons": [
                    {
                        "slug": "conditional-formatting",
                        "title": "Conditional Formatting",
                        "order": 1,
                        "xp_value": 20,
                        "estimated_minutes": 6,
                        "content": """## Conditional Formatting

Conditional formatting automatically changes a cell's appearance based on its value. Your spreadsheet becomes self-explanatory.

### Applying Conditional Formatting
Home tab → Conditional Formatting

### Highlight Cell Rules
- **Greater Than / Less Than / Between** — highlight numbers meeting a condition
- **Equal To** — highlight specific values
- **Text that Contains** — highlight text matches
- **A Date Occurring** — highlight dates (yesterday, last week, next month...)
- **Duplicate Values** — highlight or hide duplicates instantly

### Color Scales
Apply a gradient across a range:
- Green → Yellow → Red (good to bad)
- Values automatically get darker/lighter based on their relative value in the range

### Data Bars
Adds a bar chart inside each cell, proportional to the value. Great for quick visual comparison.

### Icon Sets
Adds icons (arrows, traffic lights, stars) based on thresholds.

### Custom Rule — Using Formulas
The most powerful option: highlight entire rows based on a condition.

Select the whole data range → New Rule → "Use a formula":
```
=$C2="Overdue"
```
(Note the $ before C but not before 2 — this locks the column but lets the row number change as it applies to each row.)

This highlights the entire row where column C says "Overdue".

### Managing Rules
Home → Conditional Formatting → Manage Rules — edit, delete, or reorder rules. Rules apply in order — the first matching rule wins.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You want to highlight entire rows in a dataset where column B says 'Overdue'. Which Conditional Formatting option do you use?",
                            "options": ["Use a formula to determine which cells to format", "Highlight Cell Rules > Text that Contains", "Color Scales", "Data Bars"],
                            "answer": "Use a formula to determine which cells to format",
                            "hints": ['You need to highlight whole rows, not just the cell that says "Overdue".', "The formula approach lets you reference another column to decide which rows to highlight."],
                            "explanation": 'Select the whole data range → New Rule → "Use a formula" → enter =$B2="Overdue". This highlights the entire row wherever column B says "Overdue".',
                        },
                    },
                    {
                        "slug": "pivot-tables",
                        "title": "Pivot Tables",
                        "order": 2,
                        "xp_value": 30,
                        "estimated_minutes": 8,
                        "content": """## Pivot Tables — Your Superpower

A Pivot Table summarizes thousands of rows of data in seconds, without writing a single formula.

### Creating a Pivot Table
1. Click any cell in your data
2. **Insert tab → PivotTable**
3. Choose: New Worksheet (recommended)
4. Click OK

### The Field List
On the right side, you'll see all your column names. Drag them to 4 areas:

| Area | Purpose |
|------|---------|
| **Rows** | Groups data by the values in this column (e.g., City) |
| **Columns** | Creates column headers for each unique value |
| **Values** | What to calculate (Sum, Count, Average...) |
| **Filters** | A filter dropdown above the pivot table |

### Example: Sales by City
- Drag **City** to Rows
- Drag **Sales** to Values
- Result: Total sales for each city, sorted automatically

### Change the Calculation
Click the Values field → Value Field Settings → choose Sum, Count, Average, Max, Min...

### Sorting and Filtering Inside Pivots
Click the dropdown arrows on Row Labels to sort or filter.

### Refresh a Pivot Table
When source data changes, right-click the pivot table → **Refresh**. Or Data tab → Refresh All.

### Slicers — Visual Filters
Insert tab → Slicer → select a field → clickable buttons filter your pivot. Great for presentations.

### Pivot Charts
Insert a chart based on a pivot table — it stays linked and updates when you change the pivot.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You've changed data in your source table. How do you update the Pivot Table to reflect the new data?",
                            "options": ["Right-click the pivot → Refresh", "Delete and recreate the pivot", "It updates automatically", "Press Ctrl+S"],
                            "answer": "Right-click the pivot → Refresh",
                            "hints": ["Pivot Tables don't auto-update when source data changes.", "There's a Refresh option accessible by right-clicking."],
                            "explanation": "Pivot Tables don't update automatically. Right-click anywhere on the pivot table and select Refresh to pull in the latest data from the source range.",
                        },
                    },
                    {
                        "slug": "dynamic-arrays",
                        "title": "Dynamic Arrays: UNIQUE, FILTER, SORT",
                        "order": 3,
                        "xp_value": 25,
                        "estimated_minutes": 7,
                        "content": """## Dynamic Arrays

Dynamic array functions return multiple results that automatically **spill** into adjacent cells. Enter the formula once — it fills as many cells as needed.

### UNIQUE — Remove Duplicates
```
=UNIQUE(A2:A100)
```
Returns a list with each value only once, sorted in first-occurrence order.

```
=UNIQUE(A2:A100, FALSE, TRUE)   → values that appear exactly once
```

### FILTER — Dynamic Filtering with a Formula
```
=FILTER(A2:C100, B2:B100="Delhi")
```
Returns all rows where column B = "Delhi". Updates automatically when data changes — unlike clicking the filter button.

**Multiple conditions:**
```
=FILTER(A2:C100, (B2:B100="Delhi") * (C2:C100>50000))
```
The `*` acts like AND for arrays.

```
=FILTER(A2:C100, (B2:B100="Delhi") + (B2:B100="Mumbai"))
```
The `+` acts like OR.

### SORT — Sort with a Formula
```
=SORT(A2:C100)               → sort by first column, ascending
=SORT(A2:C100, 2)            → sort by second column
=SORT(A2:C100, 2, -1)        → sort by second column, descending (-1)
```

### SORTBY — Sort by a Different Range
```
=SORTBY(A2:C100, B2:B100, -1)    → sort the table by column B, largest first
```

### Combining Dynamic Arrays
```
=SORT(UNIQUE(A2:A100))           → unique values, sorted
=SORT(FILTER(A2:C100, C2:C100>0), 3, -1)   → filter then sort
```

### Spill Error
If the spill range isn't empty, you get a #SPILL! error. Clear the cells in the spill range to fix it.
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a FILTER formula to return all rows from A2:C100 where the value in column B is greater than 1000.",
                            "answer": "=FILTER(A2:C100,B2:B100>1000)",
                            "hints": [
                                "Syntax: =FILTER(array, include_condition)",
                                "The array is A2:C100 (all 3 columns)",
                                "The condition checks column B: B2:B100>1000",
                            ],
                            "explanation": "=FILTER(A2:C100,B2:B100>1000) returns all rows from A2:C100 where the corresponding value in column B exceeds 1000. Results spill automatically.",
                        },
                    },
                    {
                        "slug": "keyboard-shortcuts",
                        "title": "Essential Keyboard Shortcuts",
                        "order": 4,
                        "xp_value": 15,
                        "estimated_minutes": 5,
                        "content": """## Essential Keyboard Shortcuts

Professionals never touch the mouse for common tasks. These shortcuts make you 3x faster.

### Navigation
| Shortcut | Action |
|----------|--------|
| Ctrl+Home | Go to A1 |
| Ctrl+End | Go to last used cell |
| Ctrl+Arrow | Jump to edge of data |
| Ctrl+Shift+Arrow | Select to edge of data |
| Ctrl+G or F5 | Go To dialog |

### Selection
| Shortcut | Action |
|----------|--------|
| Ctrl+A | Select all (press twice for whole sheet) |
| Ctrl+Space | Select entire column |
| Shift+Space | Select entire row |
| Ctrl+Shift+End | Select to last used cell |

### Editing
| Shortcut | Action |
|----------|--------|
| Ctrl+C / V / X | Copy / Paste / Cut |
| Ctrl+Z / Y | Undo / Redo |
| Ctrl+D | Fill Down (copies cell above) |
| Ctrl+R | Fill Right (copies cell to left) |
| Ctrl+; | Insert today's date |
| Ctrl+Enter | Fill selected range with same value |
| Alt+= | AutoSum |
| F4 | Toggle absolute/relative references ($) |

### Formatting
| Shortcut | Action |
|----------|--------|
| Ctrl+1 | Format Cells dialog |
| Ctrl+B / I / U | Bold / Italic / Underline |
| Ctrl+Shift+$ | Currency format |
| Ctrl+Shift+% | Percentage format |
| Alt+H+B | Add border |

### The Most Underused: F4
Press F4 while typing a formula to cycle through:
`A1` → `$A$1` → `A$1` → `$A1` → `A1`
Essential for fixing references when copying formulas.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You're writing a formula and want to lock both the row and column of cell B5 so it doesn't change when copied. What keyboard shortcut toggles this?",
                            "options": ["F4", "F2", "Ctrl+$", "Alt+F4"],
                            "answer": "F4",
                            "hints": ["This key cycles through the 4 types of cell references.", "Press it while your cursor is on the cell reference in the formula bar."],
                            "explanation": "F4 cycles between A1 (relative), $A$1 (absolute), A$1 (row locked), and $A1 (column locked). $B$5 locks both row and column so the reference never changes when copied.",
                        },
                    },
                    {
                        "slug": "paste-special",
                        "title": "Paste Special & Power Paste",
                        "order": 5,
                        "xp_value": 15,
                        "estimated_minutes": 5,
                        "content": """## Paste Special

Regular Ctrl+V pastes everything — format, formula, value. Paste Special lets you paste only what you need.

### Open Paste Special
- **Ctrl+Alt+V** after copying a cell
- Right-click → Paste Special

### Most Useful Options
| Option | What it does |
|--------|-------------|
| **Values** | Pastes the result of a formula, not the formula itself |
| **Formats** | Pastes only the formatting (colors, borders, fonts) |
| **Column Widths** | Copies column widths from one area to another |
| **Formulas** | Pastes formulas only, no formatting |
| **Transpose** | Rotates data — rows become columns, columns become rows |

### Paste Values — The Most Used
When you have a formula column and want to "freeze" the results:
1. Copy the formula cells
2. Paste Special → Values (Alt+H+V+V)
3. The formulas are replaced with their current values

This is essential before deleting the source data that formulas reference.

### Transpose — Flip Your Data
Data in rows but need it in columns?
1. Copy the row data
2. Click an empty area
3. Paste Special → Transpose

### Paste Special Operations
You can even do math while pasting:
- Copy a cell containing `1.1`
- Select all prices you want to increase by 10%
- Paste Special → Multiply
- All prices are multiplied by 1.1 instantly

### Quick Paste Buttons
After pasting, a small paste icon appears. Click it (or press Ctrl) to see paste options without opening the dialog.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "Column B has formulas that reference column A. You want to delete column A but keep column B's current values. What should you do first?",
                            "options": ["Copy B → Paste Special → Values → then delete A", "Delete A directly", "Save the file first", "Convert column B to text"],
                            "answer": "Copy B → Paste Special → Values → then delete A",
                            "hints": ["Deleting the source column will break any formulas that reference it.", "You need to replace the formulas with their current values before deleting column A."],
                            "explanation": "Copy column B, then Paste Special → Values on the same column. This replaces formulas with their current results. Now column B has no dependencies, and you can safely delete column A.",
                        },
                    },
                ],
            },
        ],
    },
    {
        "slug": "excel-advanced",
        "title": "Advanced Excel",
        "description": "Master the tools used by data analysts and Excel power users — dynamic arrays, power query, dashboard design, and advanced formula techniques.",
        "level": "advanced",
        "order": 3,
        "emoji": "📕",
        "is_pro": True,
        "estimated_hours": 5,
        "modules": [
            {
                "slug": "power-functions",
                "title": "Power Functions",
                "order": 1,
                "description": "Advanced formulas that handle complex, multi-dimensional problems.",
                "lessons": [
                    {
                        "slug": "let-function",
                        "title": "LET — Name Your Calculations",
                        "order": 1,
                        "xp_value": 30,
                        "estimated_minutes": 7,
                        "content": """## LET Function

LET lets you assign names to intermediate calculations inside a formula. This makes complex formulas readable and eliminates repeated calculations.

### Syntax
```
=LET(name1, value1, name2, value2, ..., calculation)
```

### Without LET (Hard to Read)
```
=IF((A2-B2)/B2>0.1, "Above Target by "&TEXT((A2-B2)/B2,"0%"), "Below Target by "&TEXT(ABS((A2-B2)/B2),"0%"))
```

### With LET (Clean)
```
=LET(
  actual,    A2,
  target,    B2,
  diff_pct,  (actual-target)/target,
  IF(diff_pct>0.1,
     "Above Target by "&TEXT(diff_pct,"0%"),
     "Below Target by "&TEXT(ABS(diff_pct),"0%")
  )
)
```

### Performance Benefit
Without LET, `(A2-B2)/B2` is calculated 3 times in the formula above. With LET, it's calculated once and stored in `diff_pct`. On large datasets, this is significantly faster.

### Combining LET with FILTER
```
=LET(
  data,     A2:D1000,
  filtered, FILTER(data, D2:D1000>0),
  SORT(filtered, 4, -1)
)
```
Name the intermediate results — filter first, then sort the filtered result.
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a LET formula that names cell A1 as 'price', multiplies it by 1.18 (adds 18% GST), and returns the result.",
                            "answer": "=LET(price,A1,price*1.18)",
                            "hints": [
                                "Syntax: =LET(name, value, calculation)",
                                "Name 'price' and assign it A1",
                                "The calculation uses the name: price*1.18",
                            ],
                            "explanation": "=LET(price,A1,price*1.18) names A1 as 'price', then uses that name in the calculation price*1.18 to return the GST-inclusive amount.",
                        },
                    },
                    {
                        "slug": "lambda",
                        "title": "LAMBDA — Build Your Own Functions",
                        "order": 2,
                        "xp_value": 35,
                        "estimated_minutes": 8,
                        "content": """## LAMBDA — Custom Reusable Functions

LAMBDA lets you create your own custom Excel functions — no VBA or macros required.

### Syntax
```
=LAMBDA(parameter1, parameter2, ..., calculation)
```

### Example: GST Calculator
```
=LAMBDA(price, gst_rate, price * (1 + gst_rate))
```

Used alone: `=LAMBDA(price, gst_rate, price*(1+gst_rate))(A2, 0.18)`

### Saving as a Named Function
The power of LAMBDA is saving it as a named range:
1. Formulas → Name Manager → New
2. Name: `ADDGST`
3. Refers to: `=LAMBDA(price, rate, price*(1+rate))`

Now you can use it anywhere: `=ADDGST(A2, 0.18)`

### Recursive LAMBDA (Advanced)
```
=LAMBDA(n, IF(n<=1, 1, n * SELF(n-1)))
```
SELF refers to the function itself — enables recursion for factorial, Fibonacci, etc.

### MAP, REDUCE, SCAN
These higher-order functions work with LAMBDA:
```
=MAP(A2:A10, LAMBDA(x, x*1.18))     → apply 18% to each value
=REDUCE(0, A2:A10, LAMBDA(acc, x, acc+x))   → custom sum
```

### When to Use LAMBDA
- When you repeat the same complex calculation in multiple places
- When a formula is so long it becomes unreadable
- When you want formula logic to be reusable like a named function
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You've created a LAMBDA function named DISCOUNT. To apply it to cell A2 with an argument of 0.1, what is the correct syntax?",
                            "options": ["=DISCOUNT(A2, 0.1)", "=LAMBDA(A2, 0.1)", "=APPLY(DISCOUNT, A2, 0.1)", "=A2.DISCOUNT(0.1)"],
                            "answer": "=DISCOUNT(A2, 0.1)",
                            "hints": ["Once named, LAMBDA functions work exactly like built-in Excel functions.", "Use the name you gave it, followed by arguments in parentheses."],
                            "explanation": "After saving a LAMBDA as a named function (e.g., DISCOUNT), you call it exactly like any Excel function: =DISCOUNT(A2, 0.1). The LAMBDA definition is stored in the Name Manager.",
                        },
                    },
                    {
                        "slug": "array-formulas",
                        "title": "Advanced Array Techniques",
                        "order": 3,
                        "xp_value": 30,
                        "estimated_minutes": 8,
                        "content": """## Advanced Array Techniques

### Arrays in Formulas
An array is a collection of values. Excel can operate on all of them at once.

### Inline Arrays
```
={1,2,3,4,5}     → horizontal array (use commas)
={1;2;3;4;5}     → vertical array (use semicolons)
```

### Array Constants in Formulas
```
=SUM(A1:A5 * {1,2,3,4,5})    → multiply each cell by its position, then sum
=MAX(IF(B2:B100="Delhi", C2:C100))   → max value only where city=Delhi
```
(The second one needs Ctrl+Shift+Enter in older Excel, but enters normally in Excel 365.)

### MAKEARRAY — Generate Arrays Programmatically
```
=MAKEARRAY(5, 3, LAMBDA(r, c, r*c))
```
Creates a 5×3 array where each cell = row number × column number. A multiplication table!

### CHOOSECOLS / CHOOSEROWS — Select Specific Columns/Rows
```
=CHOOSECOLS(A2:F100, 1, 3, 5)    → return only columns 1, 3, and 5
=CHOOSEROWS(A2:F10, 1, 3, 5)     → return only rows 1, 3, and 5
```

### HSTACK / VSTACK — Combine Arrays
```
=HSTACK(A2:B10, D2:E10)    → join side by side (horizontal)
=VSTACK(A2:B10, A15:B25)   → stack on top of each other (vertical)
```

### BYROW / BYCOL — Apply Function to Each Row/Column
```
=BYROW(A2:C10, LAMBDA(row, SUM(row)))   → row total for each row
=BYCOL(A2:C10, LAMBDA(col, AVERAGE(col)))  → average of each column
```

These replace the need for helper columns in many scenarios.
""",
                        "exercise": {
                            "type": "formula_input",
                            "question": "Write a formula using CHOOSECOLS to return only the 1st and 3rd columns from the range A1:E100.",
                            "answer": "=CHOOSECOLS(A1:E100,1,3)",
                            "hints": [
                                "Syntax: =CHOOSECOLS(array, col1, col2, ...)",
                                "The array is A1:E100",
                                "You want columns 1 and 3",
                            ],
                            "explanation": "=CHOOSECOLS(A1:E100,1,3) extracts only columns 1 and 3 from the range A1:E100, ignoring columns 2, 4, and 5. Results spill automatically.",
                        },
                    },
                    {
                        "slug": "power-query-intro",
                        "title": "Power Query — Transform Data at Scale",
                        "order": 4,
                        "xp_value": 35,
                        "estimated_minutes": 9,
                        "content": """## Power Query

Power Query is Excel's ETL (Extract, Transform, Load) tool. It connects to data sources, cleans and transforms data, and loads it into Excel — all without formulas.

### Opening Power Query
**Data tab → Get Data → From File / From Database / From Web...**

Or from an existing table: **Data tab → From Table/Range**

### The Query Editor
A separate window with its own ribbon. Every transformation you apply is recorded as a step.

### Common Transformations
| Task | Power Query Action |
|------|-------------------|
| Remove duplicates | Home → Remove Rows → Remove Duplicates |
| Filter rows | Click dropdown arrow on column header |
| Rename columns | Double-click column header |
| Change data type | Click type icon on column header |
| Split column | Transform → Split Column → By Delimiter |
| Merge columns | Add Column → Merge Columns |
| Pivot / Unpivot | Transform → Pivot Column / Unpivot Columns |
| Add calculated column | Add Column → Custom Column |

### Why Power Query Beats Formulas for Data Cleaning
- Handles 1M+ rows (formulas slow down)
- Steps are recorded and re-runnable
- Connect to the same source, click Refresh — all transformations reapply automatically
- No formulas needed for basic data cleaning

### M Language
Power Query uses a language called **M** behind the scenes. You can see/edit it: Home → Advanced Editor. You don't need to learn M to use Power Query effectively.

### Loading Back to Excel
Home → Close & Load → To Table, PivotTable, or Connection Only.

When source data changes: **Data tab → Refresh All** — all queries update.
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "You need to combine data from 12 monthly CSV files into one table, and do this every month automatically. What's the best approach?",
                            "options": ["Power Query — Connect to a folder, it auto-combines all files and refreshes", "Copy-paste each file manually", "VSTACK formula combining 12 ranges", "Macro to loop through files"],
                            "answer": "Power Query — Connect to a folder, it auto-combines all files and refreshes",
                            "hints": ["Power Query can connect to a folder and combine all files inside it.", "When you add a new monthly file to the folder, clicking Refresh updates the combined table."],
                            "explanation": "Power Query's 'From Folder' connector combines all files in a folder automatically. Each month, drop the new file in, click Refresh — done. No manual work after setup.",
                        },
                    },
                    {
                        "slug": "dashboard-design",
                        "title": "Dashboard Design Principles",
                        "order": 5,
                        "xp_value": 40,
                        "estimated_minutes": 10,
                        "content": """## Dashboard Design Principles

A dashboard communicates data at a glance. Good design is the difference between a spreadsheet people ignore and one they check every morning.

### The 3-Sheet Structure
1. **Data sheet** — raw data, imported or entered here only
2. **Calculations sheet** — all formulas, pivot tables, intermediate results
3. **Dashboard sheet** — visuals only, no raw data, references from Calculations

### Visual Hierarchy
Position items by importance:
- **Top-left** — most important KPIs (revenue, users, target vs actual)
- **Top-right** — secondary metrics
- **Bottom** — trends, breakdowns, detail tables

### KPI Cards
Use merged cells with large bold numbers for key metrics:
```
Revenue: ₹12.4L    ↑ 14% vs last month
```
Conditional formatting with UP/DOWN arrows using custom formats:
`[Green]▲ 0.0%;[Red]▼ 0.0%;0%`

### Chart Best Practices
- One message per chart — don't cram multiple stories into one visual
- Direct labels on bars/lines instead of a legend
- Remove gridlines, chart borders, and unnecessary formatting
- Use consistent colors across all charts
- Title every chart with the insight, not the data: "Delhi leads all regions" not "Sales by Region"

### Slicers for Interactivity
Add slicers that filter all connected pivot tables/charts at once:
- Insert → Slicer
- Right-click slicer → Report Connections → link to all relevant pivot tables

### Freeze Header Row
View → Freeze Panes → Freeze Top Row — keeps column headers visible when scrolling.

### Dashboard Checklist
- [ ] No raw data on dashboard sheet
- [ ] All charts titled with the insight
- [ ] Consistent color scheme (2-3 colors max)
- [ ] Source and date noted somewhere
- [ ] Mobile-friendly layout (left-to-right, no tiny text)
""",
                        "exercise": {
                            "type": "multiple_choice",
                            "question": "Which title is better for a chart showing sales by region where Delhi is highest?",
                            "options": ["Delhi leads all regions with ₹4.2L", "Sales by Region", "Regional Sales Data Q3", "Chart 1"],
                            "answer": "Delhi leads all regions with ₹4.2L",
                            "hints": ["A good chart title tells the viewer the insight, not just what data is shown.", "The reader should understand the point even before looking at the chart."],
                            "explanation": "Chart titles should communicate the insight, not just label the data. 'Delhi leads all regions with ₹4.2L' tells the story immediately. 'Sales by Region' just describes the data type.",
                        },
                    },
                ],
            },
        ],
    },
]


async def seed_curriculum(db):
    """Seed learning paths, modules, and lessons if not already present."""
    existing = await db.learning_paths.count_documents({})
    if existing > 0:
        return

    for path_data in CURRICULUM:
        modules = path_data.pop("modules")
        path_data["total_xp"] = sum(
            lesson["xp_value"]
            for module in modules
            for lesson in module.get("lessons", [])
        )
        path_data["total_lessons"] = sum(
            len(module.get("lessons", [])) for module in modules
        )
        result = await db.learning_paths.insert_one(path_data)
        path_id = result.inserted_id

        for module_data in modules:
            lessons = module_data.pop("lessons")
            module_data["path_slug"] = path_data["slug"]
            module_data["path_id"] = path_id
            mod_result = await db.modules.insert_one(module_data)
            module_id = mod_result.inserted_id

            for lesson_data in lessons:
                lesson_data["path_slug"] = path_data["slug"]
                lesson_data["module_slug"] = module_data["slug"]
                lesson_data["path_id"] = path_id
                lesson_data["module_id"] = module_id
                lesson_data["is_pro"] = path_data["is_pro"]
                await db.lessons.insert_one(lesson_data)

    await db.learning_paths.create_index("slug", unique=True)
    await db.modules.create_index([("path_slug", 1), ("order", 1)])
    await db.lessons.create_index([("path_slug", 1), ("module_slug", 1), ("order", 1)])
    await db.user_progress.create_index([("user_id", 1), ("lesson_id", 1)], unique=True)
