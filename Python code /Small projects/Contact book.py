def contacts_book(name):

    if name == "Abel":
        return "310 - 720 - 1920"
    elif name == "Aaron":
        return "310 - 972 - 0 - 678"
    elif name == "Lily":
        return  "1 - 424 - 335 - 9848"
    elif name == "Ambar":
        return "310 - 972 - 9375"
    elif name == "Maria":
        return "310 - 720 - 2412"
    elif name == "Isaac":
        return "1 - 424 - 397 - 9689"
    else:
        print("invalid name")
    
print("What phone number would you like to know")
theName = input("enter either - Able, Aaron, Lily, Ambar, Maria, Isaac: ")
print(contacts_book(theName))

    
    
   
    