#!/usr/bin/env python3

with open("input.txt", "r") as f:
    for i in f:
        total = []
        for j in i:
            if(j.isdigit()):
                total.append(j)
        print("".join(total))
