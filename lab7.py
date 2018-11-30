"""
CS 2302
Mark Williams
Lab 7
Diego Aguirre/Manoj Saha
Last Modified: 11-29-18
Purpose: Implements the edit distance algorithm.
"""

from lab7utils import edit_distance

def main():
  print(edit_distance("miners", "money"))
  print(edit_distance("m", "money"))
  print(edit_distance("", "money"))
  print(edit_distance("serendipity", "money"))
  print(edit_distance("", ""))

main()
