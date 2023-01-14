#!/usr/bin/env python
# coding: utf-8

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# In[1]:


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = []
    for i in arr:
        l.append(i)
    m=max(l)
    a=[]
    while m in l:    
        l.remove(m)
    print(max(l))

