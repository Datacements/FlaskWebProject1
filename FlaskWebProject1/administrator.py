import insertRecord
import fetchRecords
import updateRecords
import deleteRecords

class administratordetails:

    def initialAdminInput(self):


        admin_entry = int(input("""\n\n\
        Press 1 if you want to add a product , 
        Press 2 if you want to fetch the product details,
        Press 3 if you want to update  a product, 
        Press 4 if you want to delete a product \n\n"""))


        if(admin_entry ==1):


            details = "Please add the details of the product to the added"
            
            print(details)
            
            insertProduct()
         

        elif(admin_entry ==2):

            details = "We are going to fetch the records based on the input provided"
            
            print(details)
            
            fetchRecordsfunc()
            

        elif(admin_entry==3):

            details = "We are going to update the products based on the product id"
            
            print(details)
            
            updateRecordsfunc()

        
        elif(admin_entry==4):

            details = "We are going to delete the products based on the product id"
            
            print(details)
            
            deleteRecordsfunc()
            

        else:
            pass


            

def insertProduct():


    name = input("\n enter the name of the product ")
    number =  int(input("\n enter the number of the product "))
    price = int(input("\n enter the price of the product "))
    date = input("\n enter the date of the product ")
    available = input("\n enter the availability of the product ")
    fun1 = insertRecord.insertIntoProduct()
    fun1.insertRecordFunc(name, number, price, date,available)



def fetchRecordsfunc():

    nwcus = fetchRecords.fetchFromProduct()
    m = nwcus.dmlOperationsFunc()
    while(True):
        if(m==1):
           m = nwcus.dmlOperationsFunc()
        else:
            break


def updateRecordsfunc():

    nwcus = updateRecords.updateProduct()
    m = nwcus.dmlUpdateOperationsFunc()
    while(True):
        if(m==1):
           m = nwcus.dmlUpdateOperationsFunc()
        else:
            break

def deleteRecordsfunc():

    nwcus = deleteRecords.deleteProduct()
    m = nwcus.dmldeleteOperationsFunc()
    while(True):
        if(m==1):
           m = nwcus.dmldeleteOperationsFunc()
        else:
            break


#if __name__ == '__main__':
    #driver = administratordetails()
    #driver.initialAdminInput()
    #insertProduct()


