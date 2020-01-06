
# coding: utf-8

# In[1]:


numbers=[5,2,5,2,2]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output +='x'
    print (output)


# In[2]:


numbers=[2,2,2,2,5]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output +='x'
    print (output)


# In[6]:


##largest number
list1=[1,2,3,4,5,6,7,8,9,0]
max=list1[0]
for item in list1:
    if item>max:
        max=item
print (max)

