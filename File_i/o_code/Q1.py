#create a new file "practice.txt" using python. Adding the following data in it
'''
hii everyone 
we are learning File I/O
using java .
i like programming in java
'''
'''with open ("practice.txt","w")as f:
    f.write("hii everyone\nwe are learning File I/O\nusing java .\ni like programming in java")'''

#---------------------------------------------------------------------------------------------------


#WAF that replace all the occurance of java with python in above file
'''with open ("practice.txt","r")as f:
    data=f.read()

new_data=data.replace("java","Python")

with open ("practice.txt","w")as f:
    f.write(new_data)'''

#---------------------------------------------------------------------------------------------------

#WAF search if the word "learning" exist in above file
'''with open ("practice.txt","r")as f:
    data=f.read()
if "learning" in data:
    print("Yes exist")
else :
    print("Not Exist") '''     #Yes exist

#---------------------------------------------------------------------------------------------------

'''word="hii"
with open ("practice.txt","r")as f:
    data=f.read()
    if(data.find(word)!=-1):
        print("Found")
    else:
        print("Not Found")   '''   #Found

#---------------------------------------------------------------------------------------------------

#WAP to find in which line of the file dose the word"learning" occurs first 
'''def fun():
    word="programming"
    line_no=1
    data=True
    with open ("practice.txt","r")as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1
          
fun()'''

#---------------------------------------------------------------------------------------------------

#From a file containing number seperated by comma ,print the count of even number 

'''with open ("practice.txt","r")as f:
    data=f.read()
    print(data)
n=""
count=0
for i in range(len(data)):
    if(data[i]==","):
        i=int(n)
        if(i%2!=0):
            count+=1
        n=""
    else:
        n+=data[i]
print(count)'''

#---------------------------------------------------------------------------------------------------


# WAP to copy from one file and paset it inot another
with open ("practice.txt","r")as f,open ("copy.txt","w")as r:
    for l in f:
        r.write(l)
   
