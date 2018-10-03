number = 1
while number <= 105:
    if number % 3 == 0 and number % 5 ==0 and number % 7 == 0:
        print("fizzbuzzbang")
    elif number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")    
    elif number % 3 == 0:
        print("fizz") 
    elif number % 5 == 0:
        print("buzz")
    elif number % 7 == 0:
        print("bang")    
    else:
        print(number)
    number +=1
