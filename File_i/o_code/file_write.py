#write operation 

f =open ("aniket.txt","w")      #by using the w - write mode the data will be override
data=f.write("how are you!")    #how are you! is override with the avilable data from file
f.close() 

f =open ("aniket.txt","a")      #by using the a - append mode the data will be add or append at the last line of data in file
data=f.write("\n I  am fine")
f.close()
'''
how are you!
 I  am fine
'''