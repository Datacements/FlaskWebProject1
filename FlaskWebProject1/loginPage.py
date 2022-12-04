import administrator

class loginPage:

    print("\n\n Welcome to the Happy Logistics application")
    print("\n\nPlease select one of the below options appropriately")

entry = int(input("""\n\n
Press 1 if you are an existing customer , 
Press 2 if you are a new customer, 
Press 3 if you are an existing employee, 
Press 4 if you are an administrator in the Happy Logistics   \n"""))



def initialLoginInput():



    if(entry ==1):


        details = "existing customer"
        print()
        print(details + "  is the option you have selected. ")
        print()
        excus = existingCustomer.existingCustomerdetails()
        excus.exisCustDetails()
     

    elif(entry ==2):

        details = "new customer"
        print()
        print(details + "  is the option you have selected. ")
        print()
        nwcus = newCustomer.newCustomerDetails()
        nwcus.newCustDet()
        

    elif(entry==3):

        details = "employee"
        print()
        print(details + "  is the option you have selected. ")
        print()
        empl = employee.employeedetails()
        empl.emplDetails()
        

    else:


        details = "administrator"
        print()
        print(details + "  is the option you have selected. ")
        print()
        
        admin = administrator.administratordetails()
        admin.initialAdminInput()
        
        



if __name__ == '__main__':
    driver = loginPage()
    initialLoginInput()
    
    
    
    

    



