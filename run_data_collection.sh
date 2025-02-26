#!/usr/bin/env bash
#
# run_data_collection.sh
#
# Description: This script runs the data collection process, executes tests,
#              and appends results to a CSV file in the format: filename,len,r,time
#
# Usage: ./run_data_collection.sh
# Example: ./run_data_collection.sh

# r_values=(3 4 5 7 8 9 11)
r_values=(6 10 25 26)

for r in "${r_values[@]}"; do
    echo "Processing for r_value: $r"
    for input_file in data/*; do
        if [ -f "$input_file" ]; then
            echo "  Processing file: $input_file"
            python3 sort.py --save --r "$r" "$input_file"
        fi
    done
done
