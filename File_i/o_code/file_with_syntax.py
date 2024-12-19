#with 
import os

with open ("aniket.txt","r") as f:
    data=f.read()
    print(data)
'''
how are you!
I  am fine
'''

with open ("aniket.txt","w") as f:
    f.write("appnacollege")  #appnacollege

