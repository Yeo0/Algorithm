#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:27:23 2018

@author: yeoyoung
"""

N=int(input("배열 크기를 입력하세요: " ))
 
inputlist=[]

for i in range(N):
    element=input("배열 원소를 입력해 주세요: ")
    inputlist.append(element)

012345
 19627

inputlist=[1,9,6,2,7]   

#정답

def heap(x,root, heapsize):
    largest=root
    if root*2+1 < heapsize and x[root*2+1]>x[largest]:
        largest=2*root+1
    if root*2+2 < heapsize and x[2*root+2]>x[largest]:
        largest=2*root+2
        
    if largest !=root:
        x[largest], x[root] =x[root], x[largest]
        heap(x,largest,heapsize)

    
def heapsort(x):
    n=len(x)
    for i in range(n//2-1,-1,-1):
        heap(x,i,n)
    for i in range(n-1,0,-1):
        x[0],x[i]= x[i], x[0]
        heap(x,0,i)
    return x

    
print(heapsort(inputlist))


#-10/13
inputlist=[4,1,7,2,3,5,6]
inputlist=[3,1,5,7,2,4,8]







def heap(x, root, heapsize):
    
    
        while(root>root*2+1 and root>root*2+2):
            fpr o 
            if x[root*2+1]>=x[root*2+2]:
                childindex=1
            if x[root*2+1]<x[root*2+2]:
                childindex=2
            
            if x[root]<x[root*2+childindex]:
                temp=x[root]
                x[root]=x[root*2+childindex]
                x[root*2+childindex]=temp
            
            root=root*2+childindex


    return x

print(heap(inputlist,0,len(inputlist)))

def heapsort(x):
    output=[]
    heap(x,0,len(x))
    
    



  

    
    childindex=0
    
    for i in range(len(x)):
        
        temp=x[0]
        x[0]=x[heapsize-1]
        x[heapsize-1]=temp
        
        root=0
        
        while(root*2+1<=heapsize):
            if root <=heapsize:
                break
        
            if x[root*2+1]>x[root*2+2]:
                childindex=0
            else:
                childindex=1
                  
            temp=x[root]
            x[root]=x[root*2+childindex]
            x[root*2+childindex]=temp
            
            root=root*2+childindex
     

        heapsize-=1
        
    return new_arr

print(heap(inputlist))





#--
def heap(x,root):
    
    while x[root]*2+1 <= len(x)  :

        if x[root*2]>x[root*2+1]:
            childindex=0
        else:
            childindex=1
            
        if x[root]>=x[root*2+childindex]:
            return
        
        temp=x[root]
        x[root]=x[root*2+childindex]
        x[root*2+childindex]=temp

        root=2*root+childindex
    

def heapsort(x):
    heapsize=len(x)-1
    for i in range(heapsize,-1):
        x[0],x[i] = x[i], x[0]
        heapsize-=1
        heap(x,0)
    
    return x

heapsort(inputlist)

#ㅇ없이

inputlist=[1,5,3,2,8,4,6]

def heap(x):
    xlen=(len(x))
    heapsize=len(x)
    childindex=0
    new_arr=[]
    
    
    
    for i in range(0,xlen):
        temp=x[0]
        x[0]=x[heapsize-1]
        x[heapsize-1]=temp
        
        new_arr.append(x[heapsize-1])
        x.remove(x[heapsize-1])
        
        root=0
        while(root*2+1<=heapsize):
            if root <=heapsize:
                break
        
            if x[root*2+1]>x[root*2+2]:
                childindex=0
            else:
                childindex=1
                  
            temp=x[root]
            x[root]=x[root*2+childindex]
            x[root*2+childindex]=temp
            
            root=root*2+childindex
     

        heapsize-=1
        
    return new_arr

print(heap(inputlist))




#맞는것같아
inputlist=[1,5,3,2,8,4,6]
def heap(x):
    x.insert(0,0)
    heapsize=len(x)
    childindex=0
    new_arr=[]
    
    for i in range(1,len(x)):
        
        temp=x[1]
        x[1]=x[heapsize-1]
        x[heapsize-1]=temp
        
        new_arr.append(x[heapsize-1])
        
        root=0
        
        while(root*2+1<=heapsize):
            if root <=heapsize:
                break
        
            if x[root*2+1]>x[root*2+2]:
                childindex=0
            else:
                childindex=1
                  
            temp=x[root]
            x[root]=x[root*2+childindex]
            x[root*2+childindex]=temp
            
            root=root*2+childindex
     

        heapsize-=1
        
    return new_arr

print(heap(inputlist))


#--힙
def heap(x):
    x.insert(0,0)
    heapsize=len(x)
    root=0
    childindex=0
    
    
    for i in range(1,heapsize):
        temp=x[1]
        x[1]=x[heapsize-1]
        x[heapsize-1]=temp
        
        while(root*2+1<=heapsize):
            if x[root*2]>x[root*2+1]:
                childindex=1
            else:
                childindex=2
            
            temp=x[root]
            x[root]=x[root*2+childindex]
            x[root*2+childindex]=temp
            root=root*2+childindex
        heapsize-=1
      
        
    return x


def heapsort(x):
    heap(x)

print(heap(inputlist))
-----

inputlist=[1,9,6,2,7]   
sorted(inputlist)[len(inputlist)-1]
0123456
 192530
 
x

def heap(x):
    x.insert(0,0)
    heapsize=len(x)
    lefti= 2*i+1
    righti=2*i+2
    largest=sorted(x)[len(x)-1]
    largest_index=x.index(largest)
    
    for
    
    
    if lefti<heapsize and x[lefti]>largest_index:
        largest_index=lefti
        
    if righti<heapsize and x[righti]>largest_index:
        largest_index=righti
    
    if largest_index
    





#---
inputlist=[1,9,6,2,7,6,10,8]   

def heap(x,root, heapsize):
    largest=root
    if root*2+1 < heapsize and x[root*2+1]>x[largest]:
        largest=2*root+1
    if root*2+2 < heapsize and x[2*root+2]>x[largest]:
        largest=2*root+2
        
    if largest !=root:
        x[largest], x[root] =x[root], x[largest]
        heap(x,largest,heapsize)

    
def heapsort(x):
    n=len(x)
    for i in range(n//2-1,-1,-1):
        heap(x,i,n)
    for i in range(n-1,0,-1):
        x[0],x[i]= x[i], x[0]
        heap(x,0,i)
    return x

    
print(heapsort(inputlist))


