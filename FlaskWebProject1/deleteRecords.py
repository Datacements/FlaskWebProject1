
import configparser
import sys
import pyodbc as odbc
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

class deleteProduct:
    
    def dmldeleteOperationsFunc(self):

        
        
        

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

        
        productIdInput = input("""\n\n Please provide Product id that need to be deleted """)
        delete_statement = "delete from product where productid="+productIdInput
            
        

        try:
            #data = pd.read_sql(update_statement, conn)
            cursor.execute(delete_statement)

        
     
        except Exception as e:

            cursor.rollback()
            print(e.value)
            print('transaction rolled back')
        
        else:
            print()
            print("Record deleted")
            cursor.commit()
            cursor.close()
            m = int(input("""\n\n Press 1 if you want to try other options in this module else press 2 to come out of this module """))
            return m
        


            
if __name__ == '__main__':
    driver = deleteProduct()
    driver.dmldeleteOperationsFunc()
   






