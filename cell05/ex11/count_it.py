#!/usr/bin/env python3
import sys

def main():
    args = sys.argv[1:]
    
    if len(args) == 0:
        print("none")
    else:
        print(f"parameters: {len(args)}")
        # Using a for loop as requested
        for arg in args:
            print(f"{arg}: {len(arg)}")
main()
