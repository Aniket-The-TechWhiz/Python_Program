# list

'''
List is built in data type in python.
List are mutable in python
It can store the element of different type, i.e list=[integer, string, float, etc] 
''' 
l=[1,12.3,33,44,1]

print(type(l)) #type of data

print(len(l)) #Lenght of list

print(l[0])# accesing the data by using index

l[0]="Aniket"
print(l) #updating the list 

print(l[1:3]) #List slicing

# List methods

'''
append, sort, sort(reverse=true), reverse, insert(index,element), remove(element), pop(idx), count(value), copy
'''

l.append(34)
print(l)

l.reverse()
print(l)

l.insert(0,"HII")
print(l)

l.remove("HII")
print(l)

l.pop(2)
print(l)

print(l.count(33))
