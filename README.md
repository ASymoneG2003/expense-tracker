# Expense Tracker

A command-line expense tracker built in Python. Record what you spend and 
save it to a file so your data is still there next time.

## Features
- Add an expense with an amount, category, and date
- Saves every entry to a CSV file that opens in Excel or Google Sheets
- Simple menu: `A` to add an expense, `Q` to quit

## How to run
1. Install Python 3
2. Download `tracker.py`
3. In a terminal, run: `python3 tracker.py`

## What I used
- Python
- The built-in `csv` module for reading and writing files

## What I learned
- Writing functions that take parameters
- Saving data to a file with `with open(...)`
- Building a menu loop with `while True`

## Planned features
- View all expenses
- Totals by category
- Input validation so bad entries don't crash the program
