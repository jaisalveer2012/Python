my_dict = {"name" : "John", "age" : 43 , "city" : "UK" , "name" : "Rohit"}
# print(my_dict)    #Due to duplicate key as "name", Rohit will override John

# my_dict1 = [{"name" : "John", "age" : 43 , "city" : "UK" , "name" : "Rohit"}, {"name" : "John", "age" : 43}]
# print(type(my_dict1)) # list with dict

del my_dict["name"]
print(my_dict)