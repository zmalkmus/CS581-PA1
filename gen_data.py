#!/usr/bin/env python3
import random
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a file with random integers, one per line.")
    parser.add_argument("n", type=int, help="Number of integers to generate")
    parser.add_argument("--min", type=int, default=1, help="Minimum integer value (default: 1)")
    parser.add_argument("--max", type=int, default=10**9, help="Maximum integer value (default: 1000000000)")
    parser.add_argument("--outfile", type=str, default="random_integers.txt", help="Output file name (default: random_integers.txt)")
    
    args = parser.parse_args()
    
    with open(args.outfile, "w") as f:
        for _ in range(args.n):
            number = random.randint(args.min, args.max)
            f.write(f"{number}\n")
    
    print(f"Generated {args.n} random integers in '{args.outfile}'.")

if __name__ == "__main__":
    main()
