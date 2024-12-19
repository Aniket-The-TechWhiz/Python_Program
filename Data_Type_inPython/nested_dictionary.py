nest_dic= {
    "Name":"Aniket",
    "Course" :"Diploma",
    "Subject" :{
        #nested_dict
        "Python" : 145,
        "MAD" : 140,
        "NIS ":146,
        "MAN":140,
        "ETI":145,
    }
}

print(nest_dic)     #{'Name': 'Aniket', 'Course': 'Diploma', 'Subject': {'Python': 145, 'MAD': 140, 'NIS ': 146, 'MAN': 140, 'ETI': 145}}

print(nest_dic["Subject"])      #{'Python': 145, 'MAD': 140, 'NIS ': 146, 'MAN': 140, 'ETI': 145}

print(nest_dic["Subject"]["Python"])        #145

#Methods
'''
dic.keys()  #return all keys

dic.values()    #return all values

dic.items()     #return all the (keyes : values)

dic.get("key")    #return the key according to value

dic.update(newDict)     #insert the sepecific item to the dic

dic.clear()     #to clear all element from the dic

dic.pop(key)        #remove the value
'''

print(nest_dic.keys())      #dict_keys(['Name', 'Course', 'Subject'])

print(nest_dic.values())        #dict_values(['Aniket', 'Diploma', {'Python': 145, 'MAD': 140, 'NIS ': 146, 'MAN': 140, 'ETI': 145}])

print(nest_dic.items())     #dict_items([('Name', 'Aniket'), ('Course', 'Diploma'), ('Subject', {'Python': 145, 'MAD': 140, 'NIS ': 146, 'MAN': 140, 'ETI': 145})])

print(nest_dic.get("Name"))     #Aniket

nest_dic.update({"Course": "Art","Address":"Bhekrainagar"})
print(nest_dic)     #{'Name': 'Aniket', 'Course': 'Art', 'Subject': {'Python': 145, 'MAD': 140, 'NIS ': 146, 'MAN': 140, 'ETI': 145}, 'Address': 'Bhekrainagar'}

nest_dic.pop("Name")
print(nest_dic)     #{'Course': 'Art', 'Subject': {'Python': 145, 'MAD': 140, 'NIS ': 146, 'MAN': 140, 'ETI': 145}, 'Address': 'Bhekrainagar'}

nest_dic.popitem()  #{'Course': 'Art', 'Subject': {'Python': 145, 'MAD': 140, 'NIS ': 146, 'MAN': 140, 'ETI': 145}}
print(nest_dic)

nest_dic.clear()
print(nest_dic)     #{}