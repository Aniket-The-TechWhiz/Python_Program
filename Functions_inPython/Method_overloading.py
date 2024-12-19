def add(a = None, b = None, c = None):
      x=0
      if a !=None and b != None and c != None:
         x = a+b+c
      elif a !=None and b != None and c == None:
         x = a+b
      else:
          x=a
      return x

print(add(2,3))
print(add(3,4,5))
print(add(3))

'''
output:-
5
12
3
'''