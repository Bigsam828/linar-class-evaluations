#A mini calculator to find the square root of a number

print("welcome to Samuel's Mini calulator")                                                 #welcoming the user to the mini calculator

#explaining the function of the calculator to the user

print("This calculator can help you whenever you intend to find the square root of a number")   
print("To get the square root of a number, simply follow the steps below")
      

#collecting the two values from the user
first_value=input("please input your number")

#converting the values from string to float datatype
x=float(first_value)


#using an operator to find the squareroot of the number
square_root=x**0.5

#print out of the squareroot of the number
print( "Your answer is =",square_root)