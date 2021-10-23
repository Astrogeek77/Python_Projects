import psycopg2

conn = psycopg2.connect("dbname = 'storeDB' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
cursor = conn.cursor()

def create_table():   
    cursor.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
       
def insert_data(item, quantity, price):
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))

def view_data():
    cursor.execute('SELECT * FROM store')
    results = cursor.fetchall()
    return results

def update_item(quantity, price, item):
    cursor.execute("UPDATE store SET quantity = %s, price = %s WHERE Item = %s", (quantity, price, item))

def delete_item(item):
    cursor.execute("DELETE FROM store WHERE Item = %s", (item, ))
    
create_table()
delete_item('Mommy Dildo')
insert_data('Papa Dildo', 7, 655.33)
update_item(12, 106.65, 'Papa Dildo')
print(view_data())

conn.commit()
conn.close()