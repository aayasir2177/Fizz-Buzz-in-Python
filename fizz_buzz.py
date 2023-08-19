def fizz_buzz(input):
    if(int(input) % 3 == 0):
       return "Fizz"
       
    elif(int(input) % 5 == 0):
       return "Buzz"
      
    else:
       return input
        



print(fizz_buzz(7))
