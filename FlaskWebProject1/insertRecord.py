import configparser
import sys
import pyodbc as odbc

class insertIntoProduct:

    def insertRecordFunc(self,name, number, price, date,available):
        self.name= name
        self.number= number
        self.price=price
        self.date=date
        self.available=available

        records = [[name, number, price, date,available]]
        

        DRIVER = 'SQL Server'
        SERVER_NAME = '127.0.0.1, 1434'
        DATABASE_NAME = 'Logistic'

        conn_string = f"""
            Driver={{{DRIVER}}};
            Server={SERVER_NAME};
            Database={DATABASE_NAME};
            Trust_Connection=yes;
        """
        

        try:
            conn = odbc.connect(conn_string)
            
        except Exception as e:
            print(e)
            print('task is terminated')
            sys.exit()
        else:
            cursor = conn.cursor()

        
        insert_statement = """
            INSERT INTO Product
            VALUES (?, ?, ?, ?,?)
        """

        try:
            
            for record in records:
                print(record)
                
                cursor.execute(insert_statement, *record)        
        except Exception as e:
            cursor.rollback()
            print(e.value)
            print('transaction rolled back')
        else:
            print('records inserted successfully')
            cursor.commit()
            cursor.close()
            #driver = administrator.administratordetails()
            #driver.initialAdminInput()




