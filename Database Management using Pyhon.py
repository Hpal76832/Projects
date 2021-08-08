import mysql.connector
import sys

class monitor():

    lis=[]

    def __init__(self,):
        self.con = mysql.connector.connect(host='localhost', user='root', passwd='Hpal76832@', database="NEW")
        self.my_cursor = self.con.cursor()

    def result(self):
        result = self.my_cursor.fetchall()
        for i in result:
            self.lis.append(i)

    def content(self):
        tb=input('Table Name ')
        self.my_cursor.execute(f'SELECT * FROM {tb} ')
        self.result()
        return print(self.lis)

    def show(self):
        self.my_cursor.execute('SHOW TABLES')
        self.result()
        return print(self.lis)

    def describ(self):
        tb=input('Table Name ')
        self.my_cursor.execute(f'DESCRIBE {tb}')
        self.result()
        for i in self.lis:
            print(i[0],end=' ')
        print('\n')
        return None

    def create(self):
        tb=input('Table Name ')
        self.my_cursor.execute(f'''
                                    CREATE TABLE {tb}(id int)
                                    ''')
        return print("Succesfully Created")

    def add_col(self):
        tb=input('Table Name ')
        col=input('Column Name ')
        self.my_cursor.execute(f'''
                                    ALTER TABLE {tb}
                                    ADD {col}
                                    ''')
        return print('Added Succesfully')



    def add_row(self):
        tb=input('Table Name ')
        col=input('Column Name ')
        self.my_cursor.execute(f'''INSERT INTO {tb} VALUES({col})''')
        self.con.commit()
        return print('Added Succesfully')

    def delete(self):
        user=input('row OR column ')
        if user=='row':
            tb = input('Table Name ')
            con = input('Condition ')
            self.my_cursor.execute(f'''DELETE FROM {tb} WHERE({con})''')
            self.con.commit()
            return print('Deleted Succesfully')

        elif user=='column':
            tb = input('Table Name ')
            col = input('Column_Name  ')
            self.my_cursor.execute(f'''ALTER FROM {tb} DROP COLUMN {col})''')
            self.con.commit()
            return print('Deleted Succesfully')

    def drop(self):
        tb = input('Table Name ')
        con = input('Condition ')
        self.my_cursor.execute(f'''DELETE FROM {tb} WHERE({con})''')
        self.con.commit()
        return print('Deleted Succesfully')


moni=monitor()
