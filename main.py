def randomchr():
    import random
    tempvar=random.randint(1, 3)
    if tempvar==1:
        tempchr=random.randint(97, 122)
        return chr(tempchr)
    elif tempvar==2:
        tempchr=random.randint(65, 90)
        return chr(tempchr)
    else:
        tempchr=random.randint(48, 57)
        return chr(tempchr)


passdata = []

def passgen():
    domain=input("Enter Website Domain for which you want password: ")
    pass1= str(randomchr() + randomchr() + randomchr() + randomchr()+ randomchr() + randomchr() + randomchr()+ randomchr() + randomchr() + randomchr()+ randomchr() + randomchr() )
    passdata.append([domain, pass1])   
    print("Password Generated and Saved in Database.")
    runpr()

def encrp_save():
    print("Error - Funtion not found")
    passfile = open("passwords.txt", "w")
    for domain, pass1 in passdata:
        passfile.write(f"{domain}: {pass1}\n")
    passfile.close()
    print("New file with created")
    runpr()

def output_pass():
    print(passdata)
    runpr()

def errorinp():
    print("Input a Valid choice")
    runpr()


def runpr():
    print("---------- Random Password Generator & Database ----------")
    print("Use the following commands to operate through the program:")
    print("1. Press '1' to generate and store a New Password.")
    print("2. Press '2' to output Stored Passwords.")
    print("3. Press '3' to Save Encrypted Password File.")
    print("4. Press '4' to Quit.")
    tempvar=input("Input Your Choice: ")
    if tempvar=="1":
        passgen()
    elif tempvar=="2":
        output_pass()
    elif tempvar=="3":
        encrp_save()
    elif tempvar=="4":
        print("Exiting Program")
    else:
        errorinp()
def readpassfile():
    try:
        passfile = open("passwords.txt", "r")
        for line in passfile:
            domain, password = line.strip().split(": ")
            passdata.append([domain, password])
        passfile.close()
        print("Passwords loaded from 'passwords.txt'")
    except FileNotFoundError:
        print("Password file not found.")


readpassfile()
runpr()      


    
    
