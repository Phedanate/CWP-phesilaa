#!/usr/bin/env python3
import sys

def main():
    """docstring"""
    text = sys.argv[1:]

    match text:
        case []:
            print("none")
        case _:
            for arg in text:
                match arg:
                    case word if word.endswith("ism"):
                        continue
                    case word:
                        print(f"{word}ism")
main()
