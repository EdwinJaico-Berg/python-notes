import sys


# https://realpython.com/python-bitwise-operators/#bitwise-and

"""
Bitwise &
Imagining a binary representation of a number, bitwise & returns
the intersection of the operator's argument.

i.e. 1001001
        &
     0011001
    =0001001

From this we see that for each index we are multiplying the 
top by the bottom.

(a & b)_i = a_i x b_i
"""
print("Bitwise AND (&)")
print(6 & 4) # 110 & 100 = 100

"""
Bitwise | (OR)
Union of the operators arguments.

i.e. 1001001
        |
     0011001
    =1011001

(a | b)_i = a_i + b_i - (a_i x b_i)
"""
print("Bitwise OR (|)")
print(156 | 52) # 10011100 | 00110100 = 10111100 (188)

"""
Bitwise XOR (^)

Every bit pair must have opposing bit values to have a one

i.e. 10011100
        ^
     00110100
    =10101000
"""
print("Bitwise XOR (^)")
print(156 ^ 52) 

"""
Bitwise NOT (~)

Inverts the bit value

i.e. ~10011100
      01100011
"""
print("Bitwise NOT (~)")
print(~156) 

"""
Bitwise Shift (>> <<)

Shifts the bits by x either to the right or to the left.

i.e. 10011100>>3 = 10011
     10011100<<2 = 1001110000

Mathematically
a << n = a x 2^n
a >> 2 = a // 2^n 
"""
print("Bitwise Shift (>> <<)")
print(156 >> 2, 156 << 2, sep='\n')

"""
Masks for Bitwise Shift 

As we saw from the examples above, a bitwise shift is able to increase
size of the resulting bit pattern. In most practical cases however, you 
would want to constrain the length of a bit pattern to be a multiple of
8 (the standard byte length). 
    To do this, you can use a mask which we can implement by using &
"""
print("Masked bit-shift")
print((39 << 3) & 255)


"""
Bitwise Shift for Negative Numbers

As Python does not work with unsigned integers, when we shift negative 
numbers we are using their 2's complement value. This is calculated by 
finding the NOT + 1 of a binary pattern.

This way we always have a unambiguous 0 (other ways of defining sign such
as one's compliment have an ambiguous 0 as it could be either negative or 
positive).
"""

print(sys.int_info)

"""
Converting int to Binary

Can call bin(), or you can format a string. 
You can also get hexadecimal and octal values by using hex() and oct()
"""
print("Converting int to bin")
print(f"{42:b}",f"{42:032b}", sep="\n")
print(bin(42))
age = 0b101010
print(age)

"""
Big Vs Little Endian

Most data types are not made up of single bytes. An integer, for example,
is made of 4 bytes. How do we then read the binary pattern that represents
an integer? We can either store the pattern in Big or Little Endian order.

The binary pattern for the integer 1969 is 00000000000000000000011110110001.
If we were to use Big Endian order then the Byte Order would be the 
following:
00000000-00000000-00000111-10110001, where the individual blocks are stored
in contiguous blocks in memory.

Alternatively, we can use little endian order, in which case the pattern
would be as follows:
10110001-00000111-00000000-00000000

There is no inherently better way of storing information, and depends on
the computer architecture.
"""

print("Big and Little Endian Problems")
raw_bytes = (1969).to_bytes(length=4, byteorder="big")
print(int.from_bytes(raw_bytes, byteorder="little"))
print(int.from_bytes(raw_bytes, byteorder="big"))

print("Native Endianess")
print(sys.byteorder)

"""
Bitmask

Bitmasks, as we have seen, act as stencils, which leave behind the 
binary patterns that we are interested in.

We can therefore create functions that are able to give the bit for a
specific index using the AND (&) operator.
"""

print("Getting bits")


def get_bit(value: int, bit_index: int) -> int:
    return value & (1 << bit_index)


get_bit(0b10000000, bit_index=5)
get_bit(0b10100000, bit_index=5)


def get_normalised_bit(value: int, bit_index: int) -> int:
    return (value >> bit_index) & 1


get_normalised_bit(0b10000000, bit_index=5)
get_normalised_bit(0b10100000, bit_index=5)

print("Setting and Unsetting a bit")


def set_bit(value, bit_index):
    return value | (1 << bit_index)


def clear_bit(value, bit_index):
    return value & ~(1 << bit_index)


print("Toggling a bit")


def toggle_bit(value, bit_index):
    return value ^ (1 << bit_index)


"""
Built-In Data Types

Python bitwise operators are defined for the following built-in data types:
    -int
    -bool
    -set and frozenset
    -dict
"""
fruits = {"apple", "banana", "tomato"}
veggies = {"eggplant", "tomato"}

print(fruits | veggies)
print(fruits ^ veggies)
print(fruits - veggies)