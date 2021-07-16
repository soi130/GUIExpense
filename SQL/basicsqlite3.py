import sqlite3

#create DB
conn = sqlite3.connect('expense.sqlite3')

#create curser
c = conn.cursor()

#create table
c.execute("""CREATE TABLE IF NOT EXISTS expenselist (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                transactionid TEXT,
                datetime TEXT,
                title TEXT,
                expense REAL,
                quantity INTEGER,
                total REAL
            ) """)

def insert_expense(transactionid,datetime,title,expense,quantity,total): #C Create in CRUD
    ID = None
    with conn: 
        c.execute("""INSERT INTO expenselist VALUES (?,?,?,?,?,?,?)""",
        (ID,transactionid,datetime,title,expense,quantity,total))
    conn.commit() #commit (save) data into the DB
    print('Insert Success!')

def show_expense(): #R Read in CRUD
    with conn:
        c.execute("SELECT * FROM expenselist")
        expense = c.fetchall()
        print(expense)
    return expense

def update_expense(transactionid,title,expense,quantity,total): #U Update in CRUD
    with conn:
        c.execute("""UPDATE expenselist SET title = ?, expense = ?, quantity = ?, total=? WHERE transactionid = ?""",
        ([title,expense,quantity,total,transactionid]))
    conn.commit()
    print('Data Updated')

def delete_expense(transationid): #D Delete in CRUD
    with conn:
        c.execute("DELETE FROM expenselist WHERE transactionid=?",([transationid]))
        conn.commit()
        print('Data Deleted')
    


#insert_expense('1234567','วันเสาร์ 2021-06-19','มะละกอ',50,2,100)
#update_expense('548656465454','แอปเปิล',200,2,400)
delete_expense("1234567")
show_expense()

print('sucess')


