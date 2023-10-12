#A mini calculator to find the tax and leftover of a given amount(salary)
print("welcome to Samuel's Mini Pivate Tax calulator")                                                 #welcoming the user to the mini calculator

#explaining the function of the calculator to the user
print("This calculator can help you whenever you intend to find the tax and leftover of a given amount(salary)")         
print("To get the tax and leftover of a given amount, simply follow the steps below")


#collecitng the two values from the user
salary=input("please input your salary")

#converting the values from string to float datatype
x=float(salary)


#using an operator to find the tax 
a=10/100
tax=a*x

#using an operator to find the leftover
leftover=x-tax
#print out the sum of the two values
print("Your tax is =",tax,"and your leftover is=",leftover)