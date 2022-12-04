import configparser
import sys
import pyodbc as odbc
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

class updateProduct:
    
    def dmlUpdateOperationsFunc(self):


        inputProduct = int(input("""\n\n\n 
        Press 1 If you want to update product details for Name for a given Product id , 
        Press 2 If you want to update product details for Product number for a given Product id , 
        Press 3 If you want to update product details for listPrice for a given Product id, 
        Press 4 If you want to update product details for availability for a given Product id, 
        \n\n """))
        
        

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
            Please provide Product id that need to be updated """)
            name_input = input("""\n\n 
            Please provide name that need to be updated """)
            update_statement = " update product set name ="+"'"+name_input+"'"+"where productid="+productIdInput
            #print(update_statement)

        elif(inputProduct ==2):
            productIdInput = input("""\n\n 
            Please provide Product id that need to be updated """)
            name_input = input("""\n\n 
            Please provide product number that need to be updated """)
            update_statement = " update product set productNumber ="+"'"+name_input+"'"+"where productid="+productIdInput
            #print(update_statement)

        elif(inputProduct==3):
            productIdInput = input("""\n\n 
            Please provide Product id that need to be updated """)
            name_input = input("""\n\n 
            Please provide price that need to be updated """)
            update_statement = " update product set listprice ="+"'"+name_input+"'"+"where productid="+productIdInput
            #print(update_statement)

        elif(inputProduct==4):
            productIdInput = input("""\n\n 
            Please provide Product id that need to be updated """)
            name_input = input("""\n\n 
            Please provide availability that need to be updated """)
            update_statement = " update product set available ="+"'"+name_input+"'"+"where productid="+productIdInput
            #print(update_statement)



        else:

            pass
            
        

        try:
            #data = pd.read_sql(update_statement, conn)
            cursor.execute(update_statement)

        
     
        except Exception as e:

            cursor.rollback()
            print(e.value)
            print('transaction rolled back')
        
        else:
            print()
            print("Record updated")
            cursor.commit()
            cursor.close()
            m = int(input("""\n\n Press 1 if you want to try other options in this module else press 2 to come out of this module """))
            return m
        


            
if __name__ == '__main__':
    driver = updateProduct()
    driver.dmlUpdateOperationsFunc()
   






