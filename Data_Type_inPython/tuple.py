#tuple 
'''
tuple are built in Data Type 
tuple is immutable means can not change

'''

tup=(1,2,3,4,"aniket",1,1)
print(tup)                          #(1, 2, 3, 4, 'aniket', 1, 1)
print(type(tup))                    #<class 'tuple'>

print(tup.count(1))                 #3   count the number of values present in tuple
print(tup.index("aniket"))          #4   show the index of value or Element
print(tup[0])                       #Accessing the tuple element by providing index