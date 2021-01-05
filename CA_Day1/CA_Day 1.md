# Objective 1 - Describe the functional components of a CPU

### **Definitions to cover**
* CPU word
* how RAM works
* how different parts of the CPU communicate
* what CPU instruction is
* what CPU register is
* what the CPU clock represents
* what the system bus is and what size it is
* how the CPU provides concurrency

**CPU Word**
The natural size of a piece of data with which the CPU can interact. Usually written down in the bit "size" of the CPU, i.e., "This is a 64-bit CPU." The CPU can quickly perform math and other operations on data of its word size. It can also work with other data size, though it may not be as speedy about it.

**Random Access Memory (RAM)**
Your computer needs a place to keep track of variables to run your code. RAM is where these variables are stored.
- like a bookshelf with billions and billions of shelves.
- each number of a shelf is called an address.

**CPU instruction**
A byte or sequence of bytes in RA that the computer know how to interpret and perform actions based on.
i.e. `ADD`, `SUB`, `CMP`, `JMP`

**CPU Register**
The CPU has a small, fixed number of special storage locations built-in. Usually there are 16 or 32 of these, and they have set names, such as `R0`, `R1`, `R2`, and so on.

**CPU clock**
The number of timer per second the CPU does some processing.

**System bus**
A collecion of wires on the motherboard between the CPU, memory, and peripherals.
- The memory bus connects the CPU to RAM
- The I/O bus connects the CPU to peripherals
- The control bus allows the CPU to precisely say what it wants to do on the bus, e,g., read or write a word or byte.

**Concurrency and Parallelism**
The CPU can do multiple things at once through a variety of mechanisms, including having multiple cores, or other features such as pipelining or hyperthreading.

### **Challenge**

* How long does it take the number of transistors on a CPU to double? What is the common name for this rule of thumb?
* Why are registers necessary? Why not just use RAM?
* Why is cache useful?
* What is a CPU word?
* What is the system bus and how wide is it?
* Describe the pins that are on a CPU chip
* What is a CPU instruction?

# Overview 2 - Convert between and understand decimal, binary, and hexidecimal

## **Overview**

All major programming languages allow the user a method for converting between different number bases. Some number bases are more convenient to use and easier to understand than others in specific circumstances.

Being able to use binary, decimal, and hex effectively in an important skill that can speed development, and help programmers understand existing code and systems that use those number bases.

We'll see how number bases work, how to count in them, and how to convert between bases.

## **Follow Along**
### **On Numbers**

It's important to understand that when you have 12 apples on the table, it's still the same number of apples regardless of whether or not you say there are "12 apples" (decimal), or "C apples" (hexadecimal), or "1100 apples" (binary).

The count of the number of items doesn't change just because we refer to it in a numbering system of a different base.

In fact, the only place the numbering system matters is when we write down the number someplace (e.g. print it on the screen or write it in source code, etc.). And remember that when you do write it down, the count of what the number refers to remains the same regardless of the base you choose to write it down in.

Re-read the last paragraph for good measure and keep it in mind in the following review.

### **On Bases**

The base of a numbering system refers to how many digits the numbering system has. Decimal numbers like we're used to have 10 digits: 0 through 9. Decimal numbers are base-10.

Similarly, binary numbers have two digits: 0 and 1. Binary is base-2.

And hexadecimal had 16 digits: 0-9 then A-F. It's base-16.

Rarely you might come across octal; it's base-8. (In Unix when you issue a command like chmod 755 or chmod 644, those numbers are octal.)

These different bases have different ways of being represented in JavaScript:

```sh
// All of these represent the number of apples on the table:
let numA = 12;     // decimal
let numB = 0xC;    // hexadecimal, leading 0x
let numC = 0b1100; // binary, leading 0b

numA === numB === numC; // TRUE!

```

### **On Binary**

In decimal, we have 10 digits, 0-9. Multi-digit numbers have the 1's place, the 10's place, and the 100's place, etc.

E.g. 123 has 1 in the 100's place, 2 in the 10's place, and 3 in the 1's place.

In binary, we only have two digits, 0-1. Multi-digit numbers have the 1's place, the 2's place, the 4's place, the 8's place, the 16's place, etc.

It's convenient, as a developer, to have this sequence of powers of two memorized at least up to 1024:

```sh
1 2 4 8 16 32 64 128 256 512 1024
2048 4096 8192 16384 32768 65536
```

These are all powers of 2. 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, etc.

Computers find it convenient to represent numbers in base 2 for a variety of reasons. One is that it's easy to represent as a voltage on a wire: `0` volts is a `0` and 5 volts (or whatever) is a `1`. Another is that you can do boolean logic with `0` being `FALSE` and `1` being `TRUE`.

    There are 10 kinds of people in the world: those who understand binary and those who don't.

### **Convert Binary to Decimal**
**In JavaScript**

```sh
// Binary constants:

let myBinary = 0b101; // 101 binary is 5 decimal

// Converting a binary string to a Number

let myValue1 = Number('0b101');

// or

let myValue2 = parseInt('101', 2); // base 2

// All these print 5:
console.log(myBinary); // 5
console.log(myValue1); // 5
console.log(myValue2); // 5
```

**By hand**

```sh
+------ 8's place
|+----- 4's place
||+---- 2's place
|||+--- 1's place
||||
1010
```

The above example has one 8, zero 4s, one 2, and zero 1s. That is, it has one 8
and one 2. One 8 and one 2 is 10, `8+2=10`, so:

`1010` binary == `10` decimal.

### **Convert Decimal to Binary**

**In Javascript**

```sh
// Decimal constants (just like normal)

const val = 123;

// Converting a decimal to a binary string

const binVal = val.toString(2); // convert to base 2 number string

console.log(`${val} decimal is ${binVal} in binary`);
```


Note that the result is a string. This makes sense because you already
had the number in val as a Number type; the only other way to
represent it is as a string.

**By Hand**

This one's a little trickier, since you have to work the binary-to-decimal
conversion backwards.

Example: convert 123 decimal into binary. You have to come up with sum of the
powers of two that add up to it.

Start with the highest power of two that's lower than the number: 64. We
know we have zero 128s in the number, because it's only 123. But there
must be a 64 in there.

So let's put a 1 in the 64s place:

```sh 1xxxxxx     All the x's are unknown```

Now we compute `123-64` because we've taken the 64 out of there.
`123-64=59`. So let's go to the next power of two down: 32.

59 has a 32 in it, so that must be a 1 in the 32's place, as well:

``` sh 11xxxxx     All the x's are unknown```

Then we compute `59-32=27` and go down to the next power of two: 16. There's one
16 in 27, so that's a 1 in the 16s place:

```sh 111xxxx     All the x's are unknown``

Then we compute `27-16=11` and do the next power of two: 8. There's 1 8 in 11,
so that's 1, too:

```sh 1111xxx     All the x's are unknown```

Then we compute 11-8=3 and do the next power of two: 4. There are zero 4s in 1. so that's a 0 for a change:

```sh 11110xx     All the x's are unknown```

We're still at 3 decimal, but we drop to the next power of two: 2. There is one
2 in 3, so that's a 1:

```sh 111101x     All the x's are unknown```

And we compute 3-2=1, and drop to the last power of two: 1. There is
one 1 in 1, so that's a 1:

```sh 1111011 binary is 123 decimal```

### **Hexadecimal**

Hex is a base-16 numbering system. It has 6 more digits than decimal
(which is base 10). These 6 digits, which come after 9, are A, B, C, D,
E, and F.

Counting to decimal 16 in hexadecimal goes like this:

```sh 0 1 2 3 4 5 6 7 8 9 A B C D E F 10```

You might have already seen hexadecimal numbers in CSS colors, such as
`#ccff00`.

### **Converting Binary to Hex**

Fortunately, since 16 and 2 are powers of two, there are an even number
of binary bits per hex digit: 4 bits per hex digit.

So if we have a 1-byte number, like `01101100`, we split it in segments
of 4 bits and convert each of those to a hex digit. It might be more
convenient to convert do decimal first for numbers over 9 decimal.

```sh 00111100```

split into sequences of 4 bits.

```sh 0011 1100```

convert to hex (or decimal then hex, if more convenient):

```sh 0011 1100
 3    C      (C hex == 12 decimal == 1100 binary)
```

So `0b00111100` is equivalent to `0x3c`. (Hex constants are written with
a leading `0x` in JS, C, and many other languages.)

Converting hex to binary is the same in reverse. 4 bits per hex digit.
Challenge

    Count to `0x20` in hex
    What is `0x2F` in binary?
    Convert `0b11011` to decimal
    What is `0b11100111` in hex?
    What is `27` in binary?
    Write a program that outputs a value in binary. Hint: >> and &

Additional Resources

Ars Technica: Gangnam Style overflows INT_MAX, forces YouTube to go 64-bit
# https://arstechnica.com/information-technology/2014/12/gangnam-style-overflows-int_max-forces-youtube-to-go-64-bit/