
ypb = []
ynum = []
num = []
print("Welcome to Lottery numbers checker!")
rng = input("How many sets of numbers do you need to check for this draw? ")

# this function inputs the winning numbers


def winnty():
    for i in range(5):
        dig = input("Enter the winning numbers one number at a time: ")
        if dig.isdigit():
            num.append(dig)
        else:
            print("Try again, your numbers were not numbers")
            winnty()
    return num


num = winnty()
# this function inputs the winning powerball number


def pbnty():

    pbn = input("Enter the winning powerball number: ")
    if pbn.isdigit():
        ball = pbn
        return ball
    else:
        print("try again, your number wasn't a number")
        pbnty()


pb = pbnty()
# this code establishes the powerplay option (if selected)
multi = input("Enter the multiplier. If you didn't get the powerplay option, enter 1: ")
# this code displays the winning numbers and powerball for accuracy
print("The winning numbers are: ")
for el in num:
    print(el)
print("The winning powerball is: ", pb)
# this code will create an array of the player's numbers


def numnty():
    global ynum
    ynum = []
    for i in range(5):
        dig = input("Enter your numbers one at a time: ")
        if dig.isdigit():
            ynum.append(dig)
        else:
            print("Your number isn't a number, try again")
            numnty()


def yp():
    global ypb
    ypb = 0
    ypbn = input("Enter your powerball: ")
    if ypbn.isdigit():
        ypb = ypbn
    else:
        print("your number isn't a number, try again")
        yp()



def yours():
    for i in range(int(rng)):
        numnty()
        yp()
        winchk()
# this code checks to see if the numbers match and displays the winnings


def winchk():
    print("Your numbers Are: ", ynum," and for your powerball: ", ypb)
    print("The winning numbers are: ",num ,"with ", pb, " as the powerball.")
    counter = 0
    pbm = False
    for n in ynum:
        if n in num:
            counter += 1
    print("You matched ", counter, " numbers")
    if pb == ypb:
        pbm = True
    if counter == 5 and pbm == True:
        print("You won the Jackpot!")
    elif counter == 5 and pbm == False:
        print("You won  ")
        print(1000000 * int(multi))
    elif counter == 4 and pbm == True:
        print("you won")
        print(50000 * int(multi))
    elif counter == 4 and pbm == False:
        print("you won")
        print(100 * int(multi))
    elif counter == 3 and pbm == True:
        print("you won")
        print(100 * int(multi))
    elif counter == 3 and pbm == False:
        print("you won")
        print(7 * int(multi))
    elif counter == 2 and pbm == True:
        print("you won")
        print(7 * int(multi))
    elif counter == 1 and pbm == True:
        print("you won")
        print(4 * int(multi))
    elif counter == 0 and pbm == True:
        print("you won")
        print(int(multi) * 4)
    else:
        print("Not a winner this time.")
yours()

