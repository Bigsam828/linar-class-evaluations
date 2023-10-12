#A mini calculator to perform multiplication with two values

print("welcome to Samuel's Mini calulator")                                                 #welcoming the user to the mini calculator

#explaining the function of the calculator to the user
print("This calculator can help you whenever you intend to multiply two numbers")         
print("To get the  of product two numbers, simply follow the steps below")

#collecitng the two values from the user
first_value=input("please input your first number")
second_value=input("please input your second number")

#converting the values from string to float datatype
x=float(first_value)
y=float(second_value)

#using an operator to sum up the two values
product=x*y

#print out the product of the two values
print("Your answer is =",product)