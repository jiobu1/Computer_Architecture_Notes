Bitwise Operations

First, Boolean


A   B          A and B
_______________________
F   F            F

F   T            F

T   F            F

T   T            T

```
If A and B:
    print("hi")
```

A   B          A or B
----------------------
F   F            F

F   T            T

T   F            T

T   T            T


A              NOT A
--------------------
T               F
F               T


Then, bitwise:
A   B          A & B (bitwise AND)
--------------------------------
0   0            0

0   1            0

1   0            0

1   1            1


A   B          A | B (bitwise OR)
--------------------------------
0   0            0

0   1            1

1   0            1

1   1            1



A               ~A (bitwise NOT)
--------------------------------
1                0
0                1

Examples:
  1100
& 0110
------
  0100

  101101100110101
& 000001111111000        "AND masking", stencil
-----------------
  000000011010000

Bitwise AND can mask out parts of a number, or clear individual bits of a number to 0

255.255.255.0  Subnet  mask
111111111.111111111.111111111.000000000

Bit shifting
------------
10101011
01010101
00101010
00010101
00001010
00000101
00000010
00000001
00000000

Analogy in Base 10 of extracting numbers
----------------------------------------
  vv
1234567
0123456        shift 3 right(AKA//1000)
0012345
0001234
     ^^

0000034   mas out 34

Now in Binary
-------------
0101001010110

0101001010110 Shift right by 6
 010100101011
  01010010101
   0101001010
    010100101
     01010010
      0101001
         ^^^^

  0101001
& 0001111
---------
  0001001

if n is a power of 2:
    x % n
    is the same as
    x & (n-1)
