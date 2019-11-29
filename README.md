# wordsearch-solver

Finds words hidden in a two-dimensional grid of characters. A personal exercise in designing algorithms that traverse lists in creative ways.

### Example

```
$ python3 solver.py puzzle.txt wordlist.txt
```

```
 ·  ·  ·  ·  ·  ·  C  ·  E  V  L  O  S  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 D  ·  A  ·  ·  ·  ·  R  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 A  ·  ·  L  ·  ·  ·  ·  Y  ·  ·  ·  P  ·  ·  ·  P  ·  ·  ·  ·  ·  ·
 T  ·  ·  ·  G  ·  ·  ·  ·  P  ·  ·  ·  E  ·  ·  ·  Y  ·  ·  ·  ·  ·
 A  ·  ·  ·  ·  O  ·  ·  ·  ·  T  ·  ·  ·  R  ·  ·  ·  T  ·  ·  ·  ·
 M  ·  ·  ·  ·  ·  R  ·  ·  ·  ·  O  ·  ·  ·  M  ·  ·  ·  H  ·  ·  ·
 I  ·  ·  ·  ·  ·  ·  I  ·  ·  ·  ·  G  ·  ·  ·  U  ·  ·  ·  O  ·  ·
 N  ·  ·  ·  ·  ·  ·  ·  T  ·  ·  ·  ·  R  ·  ·  ·  T  ·  ·  ·  N  ·
 I  ·  ·  ·  ·  ·  ·  ·  ·  H  ·  ·  ·  ·  A  ·  ·  ·  A  ·  ·  ·  ·
 N  ·  ·  ·  ·  ·  ·  ·  ·  ·  M  ·  ·  ·  ·  P  ·  ·  ·  T  ·  ·  ·
 G  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  H  ·  ·  ·  I  ·  ·
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  Y  ·  ·  ·  O  ·
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  N
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·
 ·  ·  ·  ·  ·  ·  E  N  C  R  Y  P  T  I  O  N  ·  ·  ·  ·  ·  ·  ·
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  T  E  C  H  N  O  L  O  G  Y  ·  ·
```

### Notes

The puzzle and wordlist files accept either uppercase or lowercase letters. 
