#How to take the input in Python
'''
When we use olny the keyword input then it will cosidered as string 
->To take the int value as iput :- int(input())
->To take the float value as iput :- float(input())
'''

'''
output :-

Enter a value : aniket
aniket
<class 'str'>
Enter integer value :23
23
<class 'int'>
Enter float value :2.4
2.4
<class 'float'>
'''

a=input("Enter a value : ")
print (a)
print(type(a))

b=int(input("Enter integer value :"))
print (b)
print(type(b))

c=float(input("Enter float value :"))
print (c)
print(type(c))
