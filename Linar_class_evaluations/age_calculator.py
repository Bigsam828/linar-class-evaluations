'''I'm writing this script to create an age calculator,
that will collect the user's birth yearand the name and
calculate the age by finding the difference between the
two years.'''

#I'm welcoming the user to my Age calculator
print('welcome to my age calculator')

print('to calculate age, please follow the steps below')

#Creating a user defined function too help me calculate perform thhe age calculation
def Age():
    '''Age(name, year of birth, current year) 

    This function calculates user age by collecting three 
    parameters, namely: the name of the user, year of birth,
    and the current year. The function then calculates the 
    age of the user and  prints out the name of the user and
    the age range using the info stated below
    0-5 : infant
    6-12 : kid
    13-19 : teenager
    20-35 : young adult
    35-infinity : adult'''
    #collecting the user's name
    name=(input('please input your name'))

    #collecting the user's birth year. Note: byear is an abbreviation for  birth year
    byear=int(input('please input your birth year'))

    #collecting the present year. Note: byear is an abbreviation for present year`      `
    pyear=int(input('please input the present year'))
    
    #calculating the Age
    Age=pyear-byear

    #setting conditions to determine the age bracket of the user, using the age ranges stated in the function docstring
    if Age>=0 and Age<=5:
        print(f'hey{name},you are {Age}, and you are an infant')
    
    elif Age>=6 and Age<=12:
        print(f'hey {name},you are {Age}, and you are a kid' )

    elif Age>=13 and Age<=19:
        print(f'hey {name},you are {Age}, and you are a teenager' )

    elif Age>=20 and Age<=35:
        print(f'hey {name},you are {Age}, and you are a young adult' )

    elif Age>=35:
        print(f'hey {name},you are {Age}, and you are an adult' )

    else:
        print(f'dear{name}, please enter your correct age')

#calling the age function
Age()




#Creating another user defined function too help me calculate perform the age calculation
def Age(name, byear, pyear):
    '''Age(name, year of birth, current year) 

    This function calculates user age by collecting three 
    parameters, namely: the name of the user, year of birth,njnkioj
    and the current year. The function then calculates the 
    age of the user and  prints out the name of the user and
    the age range using the info stated below
    0-5 : infant
    6-12 : kid
    13-19 : teenager
    20-35 : young adult
    35-infinity : adult'''

    
    #calculating the Age
    Age=pyear-byear

    #setting conditions to determine the age bracket of the user, using the age ranges stated in the function docstring
    if Age>=0 and Age<=5:
        print(f'hey{name},you are {Age}, and you are an infant')
    
    elif Age>=6 and Age<=12:
        print(f'hey {name},you are {Age}, and you are a kid' )

    elif Age>=13 and Age<=19:
        print(f'hey {name},you are {Age}, and you are a teenager' )

    elif Age>=20 and Age<=35:
        print(f'hey {name},you are {Age}, and you are a young adult' )

    elif Age>=35:
        print(f'hey {name},you are {Age}, and you are an adult' )

    else:
        print(f'dear{name}, please enter your correct age')

Age( (input('please input your name')),int(input('please input your birth year')),int(input('please input the present year')))

List=[23,23,34,54,45]
w,x,y,z=List
print(w,x,y,z)