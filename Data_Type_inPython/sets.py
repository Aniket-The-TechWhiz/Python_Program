#set
'''
set is a collection of unordered data
Each element of the set must be unique & immutable
'''

col={1,2,3,4,"Aniket"}
print(col)      #{1, 2, 3, 4, 'Aniket'}
print(type(col))        #<class 'set'>

#Methods
'''
set.add(value)      #to add element
set.remove(value)       #to remove element
set.clear()     #to clear all set
set.pop()       #remove the random value
'''

col.add("hii")
print(col)      #{'Aniket', 1, 2, 3, 4, 'hii'}

col.remove("hii")
print(col)      #{1, 2, 3, 4, 'Aniket'}

col.pop()
print(col)      #{2, 3, 'Aniket', 4}

col.clear()
print(col)      #set()

#Another Method
'''
set1.union(set2)        #combaine both value and return new 
set2.intersection(set2)     #combine common value and return new 
'''

set1={1,2,3,4}
set2={3,0,7,4,9}

print(set1.union(set2))     #{0, 1, 2, 3, 4, 7, 9}

print(set1.intersection(set2))      #{3, 4}