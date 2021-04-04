
def OddOrEven(number):
    if (number % 2) == 0:
        print(str(number) +" is even")
    else:
        print(str(number)+ " is odd")


# I will call this function to test if it works.
#OddOrEven(-11)
#OddOrEven(0)
#OddOrEven(6)
#OddOrEven(1234567890)

# this function will tell me which numbers are smaller than the number I give 
def lessNum(list, num):
    for number in list:
        if num > number:
            print(number)


# I will call this function to test if it works.
#lessNum([1,2,3,4,5,6,7,8,9,10,44,55,66,77,101],102)



# This function when given a list will return the sum
def number_list (list):
    total = 0 
    for num in list:
     total = total + num 
    return total 

#print(number_list([1,2,3,-6]))

#reture A**B

def expoint(A,B):
    A = A**B
    return A 

#print(expoint(1, 2))
#print(expoint(2,3))
