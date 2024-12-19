#file
'''
read() method read all data presented in file
'''
'''f=open("aniket.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()'''

'''
readline() method is used to read a single line from file
'''
f=open("aniket.txt","r")
data=f.readline()
print(data)
data1=f.readline()
print(data1)
print(type(data))
f.close()