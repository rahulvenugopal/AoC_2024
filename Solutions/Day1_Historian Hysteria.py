# -*- coding: utf-8 -*-
"""
Created on Sat May 10 21:14:56 2025

Day 1

@author: Rahul Venugopal
"""
# Load data which is in text format
file = open('input','r')
data = file.readlines()

# Create two lists
first = []
second = []

for line in data:
    first.append(int(line.split('\n')[0].split('   ')[0]))
    second.append(int(line.split('\n')[0].split('   ')[1]))

# Convert to int and Sort the lists
first = sorted(first)
second = sorted(second)

diff = []
for one, two in zip(first,second):
    diff.append(abs(one- two))

sum(diff)

#%% Part 2

occurences = []
for entry in first:
    occurences.append(second.count(entry) * entry)

sum(occurences)
