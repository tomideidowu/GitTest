
# coding: utf-8

# In[ ]:


name=input("What is your name?")

height =float(input("What is your height_m?"))

weight=float(input("What is your weight_kg?"))

       
bmi=(weight/(height*height))
print ("bmi: ", "{0:.2f}".format(bmi))

if bmi<25:
    print (name, "is not overweight")
else :
    print(name, "is overweight")

print("Thank you! Have a great day!")