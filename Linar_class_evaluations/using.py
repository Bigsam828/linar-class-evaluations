switch_off_computer=input("do you want to switch off your computer")
def switch_off_computer():    
    if switch_off_computer== 'yes':
        print("click the start button on your keyboard or at the bottom left of your desktop")
        print("click the power button, at the bottom left of the page")
        print("click the shutdown option")
        print("click ok") 

    elif switch_off_computer=="of course":
        print("hold \"ctrl\", \"alt\", \"delete\" " )
        print("click power button")
        print("click the shutdown button")
        print("click ok")

    elif switch_off_computer=="yes quickly":
        print("hold \"alt\" \"F4\" ")
        print("press enter")

    elif switch_off_computer=="no":
        print("ok")

    else:
        switch_off_computer_2= input("do you intend to switch off your computer")

        if switch_off_computer_2.strip()=="yes":
            print(" ok ")
            switch_off_computer()
        
x = input("inptu x")
y = input('input y')
def addititon():
    sum=x+y
    