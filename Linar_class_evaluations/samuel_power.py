#A mini calculator to raise a number to the power of another

print("welcome to Samuel's Mini calulator")                                                 #welcoming the user to the mini calculator

#explaining the function of the calculator to the user
print("This calculator can help you whenever you intend to riase a number to the power of another")   
print("To index a number, simply follow the steps below")
      
#collecting the two values from the user
first_value=input("please input your base(number to be indexed)")
second_value=input("please input your power(index)")

#converting the values from string to float datatype
x=float(first_value)
y=float(second_value)

#using an operator to sum up the two values
answer=x**y

#print out the product of the two values
print( "Your answer is =",answer)