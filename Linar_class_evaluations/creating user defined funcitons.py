
print('Welcome to my volume calculator')
x=input('Do you want to calculate volume in inches, in cm or in feet:')

if x=="feet": 
    def volume():
        '''volume(length,breadth,height)
        this function takes three values
        (all three expected to be intergers),
        and prints out the volume by finding
        the product of the three values'''
        length=int(input("Input length in  feet "))
        breadth=int(input("Input breadth in  feet"))
        height=int(input("Input height in  feet"))
        vol=length*breadth*height
        print(f'Volume={vol} feet^3')

elif x=="inches":
    def volume():
        '''volume(length,breadth,height)
        this function takes three values
        (all three expected to be intergers),
        and prints out the volume by finding
        the product of the three values'''
        length=int(input("Input length in inches "))
        breadth=int(input("Input breadth in inches"))
        height=int(input("Input height in inches"))
        vol=length*breadth*height
        print(f'Volume={vol} inch^3')

elif x=="cm":
    def volume():
        '''volume(length,breadth,height)
        this function takes three values
        (all three expected to be intergers),
        and prints out the volume by finding
        the product of the three values'''
        length=int(input("Input length in  cm "))
        breadth=int(input("Input breadth in  cm"))
        height=int(input("Input height in  cm"))
        vol=length*breadth*height
        print(f'Volume={vol} cm^3')

else :
    print('please input the dimension you want to caluclate volume in' )
volume()


print('Welcome to my volume calculator')
x=input('Input preferred dimension(cm/inch/feet):')
if x=='cm'or x=='inch' or x=='feet':
    def volume():
            '''volume (length,breadth,height)
            this function takes three values
            (all three expected to be intergers),
            and prints out the volume by finding
            the product of the three values'''
            length=int(input(f"Input length in {x}"))
            breadth=int(input(f"Input breadth in {x}"))
            height=int(input(f"Input height in {x}"))
            vol=length*breadth*height
            print(f'Volume={vol} {x}^3')

    volume()
else :
    print('please enter a valid dimension')

# The folowing set of code is an even more optimized 
# version of the previous sets of code. (I came up with
# this one in case the user doesn't want to use the dimension
# option. And thus takes 4 parameters at max)


print('Welcome to my volume calculator')
def volume():
    '''volume(length,breadth,height)
    this function takes four values
    (Thr first three expected to be intergers, 
    and the last a string),and prints out
    the volume by findingthe product of the
    three values'''
    length=int(input(f"Input length "))
    breadth=int(input(f"Input breadth "))
    height=int(input(f"Input height in "))
    dimension=(input('input dimension in cm/inch/feet (optional)') )
    vol=length*breadth*height
    if dimension=='cm' or dimension=='inch' or dimension=='feet':
        print(f'Volume={vol} {dimension}^3')

    else:
        print(f'Volume={vol}')   


volume()

