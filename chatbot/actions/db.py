import sqlite3

conn = sqlite3.connect('rasa.db')
# conn = sqlite3.connect('rasa.db',timeout=5)
# conn = sqlite3.connect('./rasa.db')
print("The database connect sucefully")


class Repo:

  @staticmethod
  #自动创建表   
  def initDb():
    conn.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Address TEXT UNIQUE NOT NULL,
            Phone TEXT UNIQUE NOT NULL
        );
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS goods (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Price TEXT NOT NULL,
            Shop TEXT NOT NULL
        );
    ''')

    
    conn.commit()
    conn.close
    print("The table created")
  
  @staticmethod
  def initGoods(name, price, shop):
    conn.execute('''
      INSERT INTO goods (Name, Price, Shop) VALUES (?, ?, ?);
    ''', (name, price, shop))
    conn.commit()
    conn.close
  
  @staticmethod
  def insert(name, address, phone):
    conn.execute('''
      INSERT INTO customer (Name, Address, Phone) VALUES (?, ?, ?);
    ''', (name, address, phone))
    conn.commit()
    conn.close


  @staticmethod
  def select():

    cur = conn.cursor()

    cur.execute('''
      SELECT * FROM customer;
    ''')

    rows = cur.fetchall()
    conn.close
    for row in rows:
        print(row)

    return str(rows).strip('[]') if len(rows) > 0 else "No records found"
    
  @staticmethod
  def selectshopping():

    cur = conn.cursor()

    cur.execute('''
      SELECT * FROM shopping;
    ''')

    rows = cur.fetchall()
    conn.close
    for row in rows:
        print(row)
        print("\n")

    return str(rows).strip('[]') if len(rows) > 0 else "No records found"
  
  @staticmethod
  def selectgoods(name):

    cur = conn.cursor()

    cur.execute('SELECT * FROM goods WHERE Name LIKE ?', ('{}%'.format(name),))
    rows = cur.fetchall()
    for row in rows:
        print(row)
        print('\n')
    conn.close
    return str(rows).strip('[]') if len(rows) > 0 else "No records found"
  

  @staticmethod
  def buygoods(name):

    cur = conn.cursor()
    cur.execute('SELECT * FROM goods WHERE Name LIKE ?', ('{}%'.format(name),))
    rows = cur.fetchall()
    for row in rows:
        cur.execute('''
        INSERT INTO shopping (Name, Price, Shop) VALUES (?, ?, ?);
       ''', (row[1], row[2], row[3]))
        conn.commit()
        print(row[1],row[2],row[3])
    conn.close
    return str(rows).strip('[]') if len(rows) > 0 else "Please check out Name"
  
    
  @staticmethod
  def delete(value):

    cur = conn.cursor()
    sql = "DELETE FROM customer WHERE Name LIKE '"+value+"'"
    cur.execute(sql)
    conn.commit()
    conn.close

  @staticmethod
  def deleteshopping(value):

    cur = conn.cursor()
    sql = "DELETE FROM shopping WHERE Name LIKE '"+value+"'"
    rows = cur.fetchall()
    # print(sql,[value])
    cur.execute(sql)
    conn.commit()
    conn.close
    return str(rows).strip('[]') if len(rows) > 0 else "Please check out Name"



  @staticmethod
  def clean():
    cur = conn.cursor()
    rows = cur.fetchall()
    cur.execute('DELETE FROM shopping')

    conn.commit()
    conn.close
    return str(rows).strip('[]') if len(rows) > 0 else "Please check out Name"

  
  @staticmethod
  def count():
    cur = conn.cursor()
    cur.execute('SELECT * FROM shopping')
    rows = cur.fetchall()
    money = 0
    for row in rows:
        money = money + int(row[2])
    return money
    cur.close
  