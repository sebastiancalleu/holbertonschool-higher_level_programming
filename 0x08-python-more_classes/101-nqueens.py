#!/usr/bin/python3
"""
Program to find solutions to
n-queens puzzle
"""
import sys

if len(sys.argv != 2):
    print("Usage: nqueens N")
    exit(1)
if not isinstance(sys.argv[1], int):
    print("N must be a number")
    exit(1)
if sys.argv[1] < 4:
    print("N must be at least 4")
    exit(1)
