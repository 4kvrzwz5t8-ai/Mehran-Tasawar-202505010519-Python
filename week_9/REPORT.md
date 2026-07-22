# Week 9 — Helpdesk Ticket Report

## Purpose
Build a simple Helpdesk Ticket Registration System using modular Python. The application collects student report details, assigns a priority and technician, and displays a formatted helpdesk ticket.

## Files
- `week_9/main.py` — entry point that runs the ticket flow.
- `week_9/ticket.py` — `create_ticket()` collects inputs and assigns priority/technician.
- `week_9/display.py` — `display_ticket()` shows the formatted ticket.
- `week_9/README.md` — short usage guide.
- `week_9/REPORT.md` — this report.

## Tech Stack
- Language: Python 3
- No external packages required

## How to run
Interactive:

```bash
python3 week_9/main.py
```

Non-interactive example (provides inputs via stdin):

```bash
printf "izzad\n12345678910\nblue screen pc\nlab 101 level 1\n1\n" | python3 week_9/main.py
```

## Example output

When run with the example inputs above the program prints:

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

## Notes
- The code assigns technicians by priority: High → Ahmad, Medium → Siti, Low → Ali.
- Input validation is minimal; negative or empty values are accepted as strings. Consider adding validation rules if required.
- The `week_9` module is self-contained and does not modify global state or require external services.

## Next steps (optional)
- Add input validation and retry prompts.
- Persist tickets to a CSV or JSON file.
- Add an option to view all saved tickets.
- Improve display formatting (align columns or use tables).
- Rename `disply.py` in root to `display.py` to keep naming consistent (already created `display.py` in `week_9`).
- Record a short screencast demonstrating the interactive flow and attach it to the README.

## Author / Date
Created automatically by the assistant during this session.
