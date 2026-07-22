# GitHub Report — Helpdesk Ticket Project

Repository: Mehran-Tasawar-202505010519-Python
Branch: main

## Summary of work performed
- Implemented and tested a simple Helpdesk Ticket Registration System (Week 9 assignment).
- Created a `week_9` module with `main.py`, `ticket.py`, `display.py`, `README.md`, and `REPORT.md`.
- Implemented a launcher for the repository `main.py` and made it executable.
- Ran and passed unit tests for the `food_order` functionality (6 tests passed).

## Files added or modified
- Added: [week_9/main.py](week_9/main.py)
- Added: [week_9/ticket.py](week_9/ticket.py)
- Added: [week_9/display.py](week_9/display.py)
- Added: [week_9/README.md](week_9/README.md)
- Added: [week_9/REPORT.md](week_9/REPORT.md)
- Added: [GITHUB_REPORT.md](GITHUB_REPORT.md)
- Modified: [main.py](main.py) — switched to call ticket flow (can be reverted)
- Existing: [food_order.py](food_order.py), [test_food_order.py](test_food_order.py), [disply.py](disply.py), [ticket.py](ticket.py)

## How to run
Run the project `main.py` (root) interactively:

```bash
python3 main.py
```

Or run the Week 9 version:

```bash
python3 week_9/main.py
```

Run non-interactively (example):

```bash
printf "izzad\n12345678910\nblue screen pc\nlab 101 level 1\n1\n" | python3 week_9/main.py
```

Run unit tests:

```bash
python -m pytest -q
```

## Test Results
- `test_food_order.py`: 6 passed (verified during session).

## Example output (sample inputs shown above)

=== IT Helpdesk Ticket ===
Student Name : 
Student ID   : 
Issue        : 
Location     : 
Priority Level
1. High
2. Medium
3. Low
Choose (1/2/3): 

========== HELPDESK TICKET ==========
Student Name : izzad
Student ID   : 12345678910
Issue        : blue screen pc
Location     : lab 101 level 1
Priority     : High
Technician   : Ahmad
Status       : Pending
=====================================

## Notes and next steps
- Option: rename `disply.py` to `display.py` in root for consistency.
- Add input validation and saving tickets to a file (CSV/JSON).
- Optionally, create a small CLI flag to choose between `food_order` demo and `ticket` demo.

## Actions performed in this session
- Inspected project files
- Installed `pytest` and ran tests
- Made `main.py` executable and created a launcher in `~/bin`
- Implemented ticket flow and created `week_9` package
- Created `GITHUB_REPORT.md` and `week_9/REPORT.md`

If you want, I can open a pull request with these changes, or revert the root `main.py` back to the original food-order behavior — tell me which you prefer.
