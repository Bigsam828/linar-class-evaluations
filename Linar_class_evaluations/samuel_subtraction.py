#A mini calculator to perform subtraction with two values
print("welcome to Samuel's Mini calulator")                                                 #welcoming the user to the mini calculator

#explaining the function of the calculator to the user
print("This calculator can help you whenever you intend to find the difference between two numbers")         
print("To get the difference between two numbers, simply follow the steps below")


#collecitng the two values from the user
first_value=input("please input your first number")
second_value=input("please input your second number")

#converting the values from string to float datatype
x=float(first_value)
y=float(second_value)

#using an operator to find the difference between the two values
difference=x-y

#print out the sum of the two values
print("Your answer is =",difference)