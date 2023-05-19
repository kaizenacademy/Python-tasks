dict1 = {"apple": 50, 5: 76, "grapes": "good"}

#replace grapes value to 75
#get the value of key "5"
# Add a key value "Hello" = "Goodbye"
#Print the sum of values of "apple" and "grapes"


#replace grapes value to 75
dict1["grapes"] = 75
print(dict1)
#get the value of key "5"
print(dict1[5])
# Add a key value "Hello" = "Goodbye"
dict1["Hello"] = "Goodbye"
print(dict1)
#Print the sum of values of "apple" and "grapes"
print(dict1["apple"] + dict1["grapes"])
