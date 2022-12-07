#!/usr/bin/env python
# coding: utf-8

# In[1]:


# MINI PROJECT: A PYTHON PROGRAM THAT GENERATES AN ACRONYMN WORD FROM A GIVEN SCENTENCE.
s=((input("Enter a Scentence: ")).upper()).split()
a=""
for x in range(len(s)):
    a=a+((s[x])[0])
print("ACRONYMN OF ENTERED SCENTENCE IS:",a)


# In[7]:


def acronymn(s):
    s=list(s)
    a=s[0]
    for x in range (len(s)):
        if ((s[x])==" "):
            a=a+(s[x+1])
        elif ((s[x])=="."):
            return(a.upper())
s=input("ENTER A SCENTENCE (ENDING WITH A FULL STOP): ")
print("ACRONYMN OF ENTERED SCENTENCE IS:",(acronymn(s)))


# In[8]:


n=int(input("ENTER THE NUMBER OF WORDS IN THE SCENTENCE: "))
a=[]
t=""
print("ENTER THE WORDS IN SEPERATE LINES: ")
for x in range(n):
    a.append(input())
    t=t+((a[x])[0]).upper()
print("ACRONYMN OF ENTERED SCENTENCE IS:",t)


# In[ ]:




