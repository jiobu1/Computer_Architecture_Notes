# a = 0b1001
# b = 0b0110

# c = a & b # 0b0000
# d = a | b # 0b1111
# e = a ^ b # 0b1111

# print(format(c, '04b')) # print binary padding with up to 4 places
# print(format(d, '04b'))
# print(format(e, '04b'))

# m = a << 2 #0b100100
# n = a >> 2 #0b10 || 2 --> Wall that crushes the number


# # LS8-spec
# #Meanings of the bits in the first byte of each instruction: `AABCDDDD`
# #* `AA` Number of operands for this opcode, 0-2

# INSTRUCTION = 0b10000010 # >> 6 --> 0b10 & 0b11 --> 0b10
# PC = 0
# number_of_times_to_increment_pc = ((INSTRUCTION >> 6) & 0b11) + 1
# PC += number_of_times_to_increment_pc

import sys

try:
    with open("Computer_Architecture_Notes/CA_Day2/print8.ls8") as my_file:
        for line in my_file:
            comment_split = line.split("#")
            maybe_binary_number = comment_split[0]

            try:
                x = int(maybe_binary_number, 2)
                print("{:08b}: {:d}".format(x, x))
            except:
                print(f"failed to cast {maybe_binary_number} to an int")
                continue

except FileNotFoundError:
    print("file not found...")