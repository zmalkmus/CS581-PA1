import sys
import numpy as np
import argparse
import time
import csv

def gulag_median(arr):
    # Remove the largest and smallest elements from the array until one element remains.
    copy = arr.copy()
    while len(copy) > 1:
        largest = copy[0]
        largest_index = 0 
        for i in range(len(copy)):
            if copy[i] > largest:
                largest = copy[i]
                largest_index = i
        copy.pop(largest_index)

        if len(copy) == 1:
            break
        
        smallest = copy[0]
        smallest_index = 0
        for i in range(len(copy)):
            if copy[i] < smallest:
                smallest = copy[i]
                smallest_index = i
        copy.pop(smallest_index)
    return copy[0]

def median_of_medians(arr, r=5):
    if len(arr) <= r:
        return gulag_median(arr)
    else:
        # Divide arr into subfiles of length r.
        subfiles = []
        for i in range(0, len(arr), r):
            subfile = arr[i:i+r]
            subfiles.append(subfile)
        
        # Calculate the median for each subfile.
        medians = []
        for subfile in subfiles:
            x = median_of_medians(subfile, r)
            medians.append(x)

        return median_of_medians(medians, r)

def quick_sort(arr, r=5):
    if len(arr) <= 1:
        return arr

    pivot = median_of_medians(arr, r)
    
    # Partition the array into three parts: 
    # 1. elements less than the pivot
    # 2. elements equal to the pivot
    # 3. and elements greater than the pivot.

    less = []
    equal = []
    greater = []
    for x in arr:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    
    return quick_sort(less) + equal + quick_sort(greater)

def test(numbers):
    # Test the choose_pivot function.
    arr = [1, 2, 3, 4, 5]
    assert gulag_median(arr) == 3

    arr = [1, 2, 3, 4, 5, 6]
    assert gulag_median(arr) == 3

    arr = [1, 2, 3, 4, 5, 6, 7]
    assert gulag_median(arr) == 4

    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert gulag_median(arr) == 4

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert gulag_median(arr) == 5

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert gulag_median(arr) == 5

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    assert gulag_median(arr) == 6

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert gulag_median(arr) == 6

    # Test the quick_sort function.
    assert quick_sort(numbers) == sorted(numbers)

    print("All tests passed.")

def main():
    parser = argparse.ArgumentParser(description="CS581: Quicksort algorithm using the median of medians as the pivot by Zack Malkmus.")
    parser.add_argument("input_file", help="Path to the input file containing integers")
    parser.add_argument("--r", type=int, default=5, help="The number of elements in each subfile (default: 5)")
    parser.add_argument("--test", action="store_true", help="Run in test mode")
    parser.add_argument("--save", action="store_true", help="Save the results to a CSV file")
    
    args = parser.parse_args()

    file_path = args.input_file

    # ==============================================
    # Read File
    # ==============================================
    try:
        with open(file_path, "r") as file:
            numbers = []
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    numbers.append(int(stripped_line))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Could not convert data to an integer. {e}")
        sys.exit(1)

    # ==============================================
    # Testing Mode
    # ==============================================
    if args.test:
        test(numbers)
        return

    # ==============================================
    # Run Quicksort and time it
    # ==============================================
    time_start = time.time()
    sorted_numbers = quick_sort(numbers, args.r)
    time_end = time.time()

    runtime = time_end - time_start
    # print(f"Time taken: {runtime:.4f} seconds")

    if not args.save:
        for number in sorted_numbers:
            print(number, end=' ')
        print()

    # ==============================================
    # Append results to CSV file
    # ==============================================
    if args.save:
        csv_file = "results.csv"
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([args.input_file, len(numbers), args.r, f"{runtime:.4f}"])

if __name__ == '__main__':
    main()
