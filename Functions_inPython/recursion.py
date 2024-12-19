#Recursion 
'''
When function call its self repeatedly
it works like stack
'''

#Example 
#recursive fuction
def show(n):
    if (n==0):
        return 0    #returns the control
    print(n)
    show(n-1)
    
#call Function 
show(2)
'''
output :-
2
1
'''
#base cae
'''
if (n==0):
        return 
''' 

'''def show(n):
    if (n==0):                               
        return     #returns the control
    print(n)
    show(n-1)
    print("End")   #this print function will not print until the above block of code will not stop after the completion of above block the this statement will print
#call Function 

show(2)'''

'''
output :-
2
1
End    #by returning the control the block of function till show(n-1) is already fished their work so they print the following statement print("end)
End
'''

#WAF to print factorial number using recursive fuction

'''def fact (n):
    
    if(n==0 or n==1):
        return 1
    return fact(n-1)*n

#call fucntion
print(fact(4))  '''    #24
