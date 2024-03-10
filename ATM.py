atm_data = {
    'Pin': '9999','admin_pin':'1111','1001':10000,'1002' : 10000,'1003': 10000,'1004': 10000,'1005': 10000,'total':200000,
}

balance = 1000

print("*********************************Welcome to the ATM*******************************")
while True:
    print("\nMenu:\n1.User Mode\n2.Admin Mode\n3.Exit")
    choose=int(input("Enter your choice:"))

    check=0
    checkk=0
    if choose==1:
            for y in range(0,3):
                Passcode=str(input("Enter your pin:"))
                if Passcode== atm_data['Pin']:
                    break
                else:
                    print("Wrong pin enetered\n")
                    check+=1
            print("\n")
            
            while True:

                if check>=3:
                        print("Wrong pin entered 3 times")
                        break
                else:
                        account_no = str(input("Enter your account number : "))
                        count10=0
                        if(account_no =='1001' or account_no =='1002' or account_no =='1003' or account_no =='1004' or account_no =='1005'):
                            while True:
                                print("\nMenu:")
                                print("1. Check Balance")
                                print("2. Deposit")                          
                                print("3. Withdraw")
                                print("4. Change password")
                                print("5. Exit")

                                choice = input("Please select an option (1/2/3/4/5): ")

                                if check>=3:
                                    print("Used wrong pin 3 times.")
                                    break

                                
                                
                                elif choice == '4':
                                    pin = str(input("Enter your current pin: "))
                                    if pin == atm_data['Pin']:
                                        x = input("Enter your new password: ")
                                        atm_data['Pin'] = x
                                        print("Password changed successfully.")
                                    else:
                                        print("Incorrect password.")
                                        count10+=1
                                    
                                elif choice == '1':
                                    print("\n\nYour balance is ",atm_data[account_no]," Rupees\n\n")
                                    
                                elif choice == '2':
                                    pin = str(input("Enter your 4 digit security pin : "))
                                    if(pin == atm_data['Pin'] ):
                                        deposit_amount = float(input("Enter the amount to deposit: "))
                                        atm_data[account_no] += deposit_amount
                                        print("\n\n",deposit_amount," has been deposited. Your new balance is ",atm_data[account_no]," Rupees\n\n")
                                        atm_data['total']+=deposit_amount

                                    else:
                                        print("Wrong pin")
                                        count10+=1
                                    
                                elif choice == '3':
                                    pin = str(input("Enter your 4 digit security pin : "))
                                    if(pin == atm_data['Pin'] ):
                                        withdraw_amount = float(input("Enter the amount to withdraw: "))
                                        if withdraw_amount <= balance:
                                            balance -= withdraw_amount

                                            sum = 0
                                            while(True):
                                                if sum >= withdraw_amount:
                                                    break
                                                else:
                                                    currency = int(input("Please choose the currency note : 2000\n500\n100\n"))
                                                    print("Enter the count of",currency,"Rupee notes :")
                                                    count = int(input())
                                                    sum += currency*count
                                                    print(count,currency,"rupee notes")
                                            print("\n\n",withdraw_amount," has been withdrawn. Your new balance is ",balance," Rupees\n\n")

                                        else:
                                            print("Insufficient funds")
                                    else:
                                        print("Wrong pin")
                                        count10+=1
                                        
                                elif choice == '5':
                                    print("\n\nThank you for using this ATM.\n\n")
                                    break
                                
                                else:
                                    print("\n\nInvalid choice. Please select a valid option.\n\n")
                        
                            else:
                                print("Wrong Pin or Account number entered")

                break
                
    elif choose==2:
        for k in range(0,3):
                Passcode=str(input("Enter your pin:"))
                if Passcode== atm_data['admin_pin']:
                    break
                else:
                    print("Wrong pin enetered\n")
                    checkk+=1
        while True:
            if checkk<3:

                    print("\nAdmin Mode")
                    print("\nMenu:")
                    print("1. Check Balance")
                    print("2. Deposit Cash")                          
                    print("3. View database")
                    print("4. Change password")
                    print("5. Exit")
                    choicee = input("Please select an option (1/2/3/4/5): ")
                    
                    if choicee=='1':
                            print("\nTotal Cash present in the ATM Machine:",atm_data['total'],"\n")              

                    elif choicee == '2':

                            deposit_amountt = float(input("Enter the amount to deposit: "))
                            atm_data['total'] += deposit_amountt
                            print("\n\n",deposit_amountt," has been deposited. The new balance of the machine is ",atm_data['total']," Rupees\n\n")
                            atm_data['total']+=deposit_amountt
        
                    elif choicee == '3':
                            print ("\n 1001 :",atm_data['1001'],"\n","1002 :",atm_data['1002'],"\n","1003 :",atm_data['1003'],"\n","1004 :",atm_data['1004'],"\n","1005 :",atm_data['1005'],"\n")
                    
                    elif choicee == '4':
                            pinn = str(input("Enter your current pin: "))
                            if pinn == atm_data['admin_pin']:
                                xx = input("Enter your new password: ")
                                atm_data['admin_pin'] = xx
                                print("Password changed successfully.")
                            else:
                                print("Incorrect password.")
                    elif choicee == '5':
                        break
                    else:
                        print("\nWrong Choice")
                        break
            else:
                    print("Wrong pin entered 3 times")
