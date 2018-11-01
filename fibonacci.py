#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 14:36:59 2018

@author: yeoyoung
"""


##recursive

def fibo(n):
    if n==0 or n==1:        
        return n
        
    else:    
        return fibo(n-1)+fibo(n-2)
        


fibo(10)



##조건문
ip=int(input())

def fibo(n):
    a=0
    if n==0 or n==1:        
        return n
    else:    
        if a==0:
            a=fibo(n-1)+fibo(n-2)
        else:
             a=a+n-1
           
        return a

fibo(10)
fibo(ip)

##효율성 
ip=int(input())

def fibo(n):
    list=[0,1]
    
    for i in range(2,n+2):
        list.append(list[i-1]+list[i-2])
        
    return list[n]

fibo(10)
fibo(ip)

#--
ip=int(input())

def fibo(n):
    a=0
    if n==0 or n==1:        
        return n
    else:
        if a!=0:
            a=a+n-1
            return a
        else:
            a= fibo(n-1)+fibo(n-2)
            return a
  

fibo(10)
fibo(ip)
