customer={
    "name":"john smith",
    "age":30,
    "is_verified":True
}
print(customer["name"])
print(customer["birthdate"])  #gives a key error
print(customer.get("birthdate")   #this gives none instead of the error message
customer["name"]="ann"
print(customer["name"])