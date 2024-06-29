import getpass
try:
        p=getpass.getpass()
except Exception as error:
        print('ERORR', error)
    else:
            print('entered password is:', p)
print("Getpass tested")
