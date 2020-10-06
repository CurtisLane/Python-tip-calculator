

def check_split():
    splitBool = input("Would you like to split the check? \n").lower()
    if splitBool == "no" or splitBool == "n":
        print(1)
        return 1
    elif splitBool == "yes" or splitBool == "y":
        splitNum = input("\nHow many ways would you like to split the check?\n")
        print(splitNum)
        return(splitNum)
    else:
        print("Please type \"yes\" or \"no\" and hit enter.\n")
        check_split()

check_split()

def tipCalc(splitNum):
    taxBool = input("Sales tax if not included on check: \n")