# #220

# Problem
Let D0 be the two-letter string "Fa". For n≥1, derive Dn from Dn-1 by the string-rewriting rules:

"a" → "aRbFR"

"b" → "LFaLb"

Thus, D0 = "Fa", D1 = "FaRbFR", D2 = "FaRbFRRLFaLbFR", and so on.

These strings can be interpreted as instructions to a computer graphics program, with "F" meaning "draw forward one unit", "L" meaning "turn left 90 degrees", "R" meaning "turn right 90 degrees", and "a" and "b" being ignored. The initial position of the computer cursor is (0,0), pointing up towards (0,1).

What is the position of the cursor after  "F"-steps in ?

# Input Format

First line of each test file contains a single integer  that is the number of queries per test file.  blocks of  lines follow, the first of which contains a single integer  and the second contains a single integer . Note, that while  is given in decimal,  is given in hexadecimal.

# Constraints

# Output Format

Print exactly two lines per each query. In the first line print the x-coordinate of the cursor and in the second line print the y-coordinate of the cursor. As  from input, these numbers should also be in hexadecimal.
