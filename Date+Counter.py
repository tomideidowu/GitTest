
# coding: utf-8

# In[ ]:


def calCumulativeSum(numbers):
    result_list = []
    i = 0
    while(i<=len(numbers)-1):
        result_list.append((sum(numbers[j] for j in range(0,i+1))))
        i+=1
    return result_list


# In[ ]:


calCumulativeSum([1,2,3,4,5])


# In[1]:


from datetime import date
d = date(2019, 9, 9)
e=date(2019,12,16)
Datee_count=e-d
print ('The Date count is:', Datee_count)


# In[2]:


#convert hours to mins
hours = int(input("Please enter hours:"))
mins = int(input("Please enter mins:"))
minute = hours * 60
minutes=mins+minute
print(minutes, " Minutes")

