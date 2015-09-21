#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/531

def count_char(char, string):
    return len(string.split(char)) - 1

first_line  = input()
# first_line  = 'takahashikunlovesyukicoder'
string      = first_line

length_list = []
length_list.append(count_char(char='t', string=string))
length_list.append(count_char(char='r', string=string))
length_list.append(int(count_char(char='e', string=string) / 2))

print(min(length_list))

# print(length_list)
