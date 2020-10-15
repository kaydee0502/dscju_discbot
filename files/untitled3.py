#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:22:14 2020

@author: kaydee
"""
import os

bw = []
with open('explit.txt','r') as file:
    bw.extend(list(map(lambda x: x[:-1].lower(),file.readlines())))
    
with open('explith.txt','r') as file:
    bw.extend(list(map(lambda x: x[:-1].lower(),file.readlines())))
    
print(bw)
    
    