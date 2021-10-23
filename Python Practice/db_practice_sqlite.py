import sqlite3

conn = sqlite3.connect('lite.db')
cursor = conn.cursor()

def create_table():   
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    
    
def insert_data(item, quantity, price):
    cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))

def view_data():
    cursor.execute('SELECT * FROM store')
    results = cursor.fetchall()
    return results

def update_item(quantity, price, item):
    cursor.execute("UPDATE store SET quantity = ?, price = ? WHERE Item = ?", (quantity, price, item ))

def delete_item(item):
    cursor.execute("DELETE FROM store WHERE Item = ?", (item, ))
    
create_table()
# delete_item('Mommy Dildo')
# insert_data('Mommy Dildo', 7, 655.33)
update_item(12, 106.65, 'Dipper Condoms')
print(view_data())

conn.commit()
conn.close()