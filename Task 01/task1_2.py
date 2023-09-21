#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    c=[]
    counting={}
    for i in s:
        count=0
        
        if i in counting.keys():
            continue
        else:
            for j in s:
                if i==j:
                    count+=1
                counting[i]=count
            c.append(count)
    c.sort()
    vals=c[-3:]
    vals.reverse()
    sorted_keys=sorted(counting.keys())
    counting2={}
    for k in sorted_keys:
        counting2[k]=counting[k]
   
    for v in vals:
        count=1
        for key,value in counting2.items():
            if v==value and count<3:
                print(f"{key} {v}")
                counting2.pop(key)
                count+=1
                break
                