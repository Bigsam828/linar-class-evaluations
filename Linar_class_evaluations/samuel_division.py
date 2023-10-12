#A mini calculator to perform division with two values

print("welcome to Samuel's Mini calulator")                                                 #welcoming the user to the mini calculator

#explaining the function of the calculator to the user
print("To get the quotient of two numbers, simply follow the steps below")
print("This calculator can help you whenever you intend to divide one number by another")         

#collecting the two values from the user
first_value=input("please input your dividend(number to be divided)")
second_value=input("please input your divisor(dividing number)")

#converting the values from string to float datatype
x=float(first_value)
y=float(second_value)

#using an operator to sum up the two values
quotient=x/y

#print out the product of the two values
print( "Your answer is =",quotient)