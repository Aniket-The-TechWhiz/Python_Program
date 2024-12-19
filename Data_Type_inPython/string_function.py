# String function 
# string are immutable in pyhton

'''
output:-
6
True
Aniket
hiii
After replace strg is  aniket
0
1
'''

strg='aniket'
print(len(strg)) #to find lenght of string

b=strg.endswith("et") #return true if the given string is end with declare string 
print(b)

print(strg.capitalize()) # Capitalize first char

print(strg.replace("aniket","hiii")) # replace str into new (old,new)
print("After replace strg is ",strg)

print(strg.find("a")) # find the char from str

print(strg.count("k")) # count of char presented in str