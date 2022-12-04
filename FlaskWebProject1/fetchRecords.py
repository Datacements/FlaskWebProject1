import configparser
import sys
import pyodbc as odbc
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

class fetchFromProduct:
    
    def dmlOperationsFunc(self):


        inputProduct = int(input("""\n\n\n 
        Press 1 If you want to get product details using Product id , 
        Press 2 If you want to get all records from products table , 
        Press 3 If you want to get product details using Name, 
        Press 4 If you want to get product details using Product number, 
        Press 5 If you want to get product details under this price,
        Press 6 If you want to get product details using date from which this product is available,
        Press 7 List products which are available 
        Press 8 List products which are not available  
        Press 9 if you want to come out of administrator \n\n"""))
        
        

        DRIVER = 'SQL Server'
        SERVER_NAME = '127.0.0.1, 1434'
        DATABASE_NAME = 'Logistic'

        conn_string = f"""
            Driver={{{DRIVER}}};
            Server={SERVER_NAME};
            Database={DATABASE_NAME};
            Trust_Connection=yes;"""
        
        

        try:
            conn = odbc.connect(conn_string)
            
        except Exception as e:
            print(e)
            print('task is terminated')
            sys.exit()
        else:
            cursor = conn.cursor()

        if(inputProduct ==1):
            productIdInput = input("""\n\n 
            Please provide Product id for which you are looking for  """)
            select_statement = " select * from Product where productid="+productIdInput
            #print(select_statement)

        elif(inputProduct ==2):
            print("""\n\n We are going to get all products from product table \n\n""")
            select_statement = " select * from Product order by productid"
            #print(select_statement)

        elif(inputProduct==3):
            productIdInput = input("""\n\n 
            Please provide Product name for which you are looking for  """)
            select_statement = " select * from Product where name=" +"'"+productIdInput+"'"
            #print(select_statement)

        elif(inputProduct==4):
            productIdInput = input("""\n\n 
            Please provide Product number for which you are looking for  """)
            select_statement = " select * from Product where productnumber=" +"'"+productIdInput+"'"

        elif(inputProduct==5):
            productIdInput = input("""\n\n 
            Please provide List Price for product you are looking for  """)
            select_statement = " select * from Product where listprice<="+productIdInput +"order by listprice"

        elif(inputProduct==6):
            productIdInput = input("""\n\n 
            We are going to get all products from product table which are available from date """)
            select_statement = " select * from Product where modifieddate=" +"'"+productIdInput+"'"
            #print(select_statement)

        elif(inputProduct==7):
            print("""\n\n 
            We are going to get all products from product table which are available  """)
            select_statement = " select * from Product where available='yes'"
        
        elif(inputProduct==8):
            print("""\n\n 
            We are going to get all products from product table which are not available  """)
            select_statement = " select * from Product where available='no'"


        else:

            pass
            
        

        try:
            data = pd.read_sql(select_statement, conn)

        
     
        except Exception as e:

            cursor.rollback()
            print(e.value)
            print('transaction rolled back')
        
        else:
            print()
            print(data)
            cursor.commit()
            cursor.close()
            m = int(input("""\n\n Press 1 if you want to try other options in this module else press 2 to come out of this module """))
            return m
        
            
            

            #driver = administrator.administratordetails()
            #driver.initialAdminInput()






            
#if __name__ == '__main__':
    #driver = fetchFromProduct()
    #dmlOperationsFunc()
   





