#!/usr/bin/env bash
# Run from any directory using: bash /path/to/run.sh
set -e
cd -- "$(dirname -- "$0")"
python3 stock_profit_calculator.py
