from os import system
from IPv4Calculator import IPv4Calculator

if __name__ == "__main__":
    #loop for the main code
    while True:
        #clear the terminal
        system("cls")

        #get the user inputs
        ip = input("Enter an IP address (like '000.000.000.000'): ")
        cidr = int(input("Enter an CIDR from 0 to 32: "))

        #do the calculations of the CIDR
        calc = IPv4Calculator(ip=ip, cidr=cidr)
        calc.calculate()

        #print the exit of the calculation
        print("\n\n" + str(calc) + "\n\n")

        #see if the user wants to do it again
        choice = input("Enter Y [yes] to execute again or just Enter to exit: ")

        #check the user choice
        if choice == 'y' or choice.upper() == 'Y' or choice == 'yes' or choice.upper == 'YES':
            continue
        else:
            print("Exiting...")
            break