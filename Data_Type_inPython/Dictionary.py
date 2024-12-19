#Dictionary

'''
Dictionaries are use to store the data in key : values pairs
They are unordered and mutable(changable) and do not allow duplicate keys
'''

dic={
    "key" : "value",
    "age" : 18,
    "name" : "Aniket",
    "adult": True ,
    "nick_name": ["anu","radha","dolly","appu","anna"],
    "DOB":("26/02/2005")
}

print(dic)  #{'key': 'value', 'age': 18, 'name': 'Aniket', 'adult': True, 'nick_name': ['anu', 'radha', 'dolly', 'appu', 'anna'], 'DOB': '26/02/2005'}

print(dic["nick_name"])     #['anu', 'radha', 'dolly', 'appu', 'anna']  we can access the specific data from dict 

''''''
#we can update the dict element by overriding the values 
#here we updated the age from 18 to 19
dic["age"]=19
print(dic) #{'key': 'value', 'age': 19, 'name': 'Aniket', 'adult': True, 'nick_name': ['anu', 'radha', 'dolly', 'appu', 'anna'], 'DOB': '26/02/2005'}

''''''
#we can add the element in dict by following way
dic["address"]="Bhekrainagar pune-28"
print(dic)
#{'key': 'value', 'age': 19, 'name': 'Aniket', 'adult': True, 'nick_name': ['anu', 'radha', 'dolly', 'appu', 'anna'], 'DOB': '26/02/2005', 'address': 'Bhekrainagar pune-28'}