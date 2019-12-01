# wordsearch-solver

Finds words hidden in a common wordsearch puzzle by scanning a grid of characters in all possible directions, including backwards and diagonally.

### Example

```
$ python3 solver.py puzzle.txt wordlist.txt
```

```
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  I
 ·  ·  ·  ·  C  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  C
 E  ·  ·  ·  A  ·  ·  ·  ·  ·  ·  B  ·  ·  ·  ·  ·  ·  ·  O  ·  ·  E
 S  ·  ·  ·  P  ·  ·  ·  ·  ·  ·  L  ·  ·  ·  ·  ·  ·  ·  N  ·  ·  D
 P  ·  ·  ·  P  ·  ·  ·  ·  ·  ·  O  ·  ·  ·  ·  ·  ·  ·  A  ·  ·  ·
 R  ·  ·  ·  U  ·  ·  ·  ·  ·  ·  N  ·  C  ·  ·  ·  ·  ·  C  ·  ·  ·
 E  ·  ·  ·  C  ·  ·  ·  ·  ·  ·  D  ·  ·  R  ·  B  ·  ·  I  ·  ·  ·
 S  ·  ·  ·  C  ·  ·  ·  ·  ·  ·  E  ·  ·  ·  E  E  ·  ·  R  ·  ·  ·
 S  ·  ·  ·  I  ·  ·  ·  D  ·  ·  ·  ·  ·  ·  ·  A  ·  ·  E  ·  ·  ·
 O  ·  ·  ·  N  ·  ·  ·  ·  R  ·  ·  ·  ·  ·  ·  N  M  ·  M  ·  ·  ·
 ·  ·  ·  ·  O  ·  ·  ·  L  ·  I  ·  ·  ·  ·  ·  S  ·  ·  A  ·  ·  ·
 ·  ·  ·  ·  ·  ·  ·  ·  ·  A  ·  P  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  T  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  T  ·  S  K  I  N  N  Y  ·  ·  ·  ·
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  E  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
```

### Notes

The puzzle and wordlist files accept either uppercase or lowercase letters. 
