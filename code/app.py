
def OddOrEven(number):
    if (number % 2) == 0:
        print(str(number) +" is even")
    else:
        print( str(number)+ " is odd")


# I will call this function to test if it works.
OddOrEven(-11)
OddOrEven(0)
OddOrEven(6)
OddOrEven(1234567890)





def lessNum(list, num):
    for number in list:
        if num > number:
            print(number)

   
    


    
  
  
  
  
  


   


# I will call this function to test if it works.
lessNum([1,2,3,4,5,6,7,8,9,10,44,55,66,77,101],102)