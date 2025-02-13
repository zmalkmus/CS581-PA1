import sys
import numpy as np

def median(arr):
    # I chose to use numpy's partition function to find the median of the array.
    # Numpy partition is an O(n) time complexity algorithm that partitions the 
    # array in such a way that the elements on the left are less than the elements on the right.
    # The median is the element at the middle of the array after partitioning.
    partition = np.partition(arr, len(arr) // 2)
    return partition[len(arr) // 2]

def median_of_medians(arr, r=5):
    if len(arr) <= r:
        return median(arr)
    else:
        # Divide arr into subfiles of length r.
        subfiles = []
        for i in range(0, len(arr), r):
            subfile = arr[i:i+r]
            subfiles.append(subfile)
        
        # Calculate the median for each subfile.
        medians = []
        for subfile in subfiles:
            med = median(subfile)
            medians.append(med)
        
        return median_of_medians(medians, r)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = median_of_medians(arr, 5)
    
    # Partition the array into three lists.
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

def main():

    # ==============================================
    # Read File
    # ==============================================

    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

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

    # print("Numbers read from file:", numbers)

    # ==============================================
    # Sort Numbers
    # ==============================================

    sorted_numbers = quick_sort(numbers)
    # print(sorted_numbers)
    for number in sorted_numbers:
        print(number, end=' ')
    print()

if __name__ == '__main__':
    main()