#!/usr/bin/env python3

def get_value(line):
    '''
    This function returns only the
    fist and last number after filtering
    the line from all characters
    
    example:
    line = one5six913lbrcc
    return -> 53
    '''
    value = []
    for i in line:
        if(i.isdigit()):
            value.append(i)
    return f"{value[0]}{value[-1]}"

def sumit(file):
    '''
    This function reads a file and
    filter numbers from each line by
    @get_value and sum all returned
    values into one result
    '''
    with open(file, "r") as f:
        numbers = []
        for i in f:
            numbers.append(get_value(i))
    total = 0
    for num in numbers:
        total += int(num)
    return (total)


# print the value 
print(sumit("input.txt"))