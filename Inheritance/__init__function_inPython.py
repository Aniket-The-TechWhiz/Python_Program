#__init_function
#constructors
'''
All classes have the functions called __init__(),which is allways executedwhen the class is initiated
'''
#self Parameter
'''
slef parameter is the refrence to the current instance of the class, and is used  to access variable 
that belogs to the class
'''

class car:
    #__init_function
    def __init__ (self): #Defualt counstructor
        print("i am aniket")

    #__init_function
    def __init__ (self,name): #parameterized counstructor
        self.name=name

#created obj
obj=car("Aniket")
print(obj.name)

  