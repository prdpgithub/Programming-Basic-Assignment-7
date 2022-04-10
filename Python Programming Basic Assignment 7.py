#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 1.	Write a Python Program to find sum of array?

def sum(arr): 
    sum=0
    for i in arr:
        sum = sum + i
          
    return(sum) 
arr=[] 
arr = [12, 3, 4, 15] 
ans = sum(arr) 
print ('Sum of the array is ', ans) 


# In[15]:


# 2.	Write a Python Program to find largest element in an array?

def largest(arr,n):
  
    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max
arr = [10, 324, 45, 90, 9808]
n = len(arr)
Ans = largest(arr,n)
print ("Largest in given array is",Ans)


# In[16]:


# 3.	Write a Python Program for array rotation?


def rotateArray(arr, n, d):
    temp = []
    i = 0
    while (i < d):
        temp.append(arr[i])
        i = i + 1
    i = 0
    while (d < n):
        arr[i] = arr[d]
        i = i + 1
        d = d + 1
    arr[:] = arr[: i] + temp
    return arr
 
 
# Driver function to test above function
arr = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotateArray(arr, len(arr), 2))
 


# In[18]:


# 4.	Write a Python Program to Split the array and add the first part to the end?


def splitArray(arr,n,k):
    for i in range(0,k):
        x=arr[0]
        for j in range (0, n-1):
            arr[j]=arr[j+1]
            arr[n-1]=x
            
arr=[15,20,25,30,35,40]
n= len(arr)
position=2
splitArray(arr,n,position)
for i in range(0,n):
    print(arr[i],end=' ')
    


# In[19]:


# 5.	Write a Python Program to check if given array is Monotonic?


def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
# Driver program
A = [6, 5, 4, 4]
  
# Print required result
print(isMonotonic(A))


# In[ ]:




