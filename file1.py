import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your_password",
    database = "wiley_practice"
)

cursor = connection.cursor()
create_table_query = """create table if not exists 
table1 (column1 int primary key auto_increment, column2 varchar(255), column3 int)"""

cursor.execute(create_table_query)
print("Table created successfully")

insert_query = "insert into table1 (column2, column3) values (%s,%s)"

values = [("Value 1", 10), ("Value 2", 20), ("Value 3", 30)]

for value in values: 
    cursor.execute(insert_query, value)
connection.commit()

select_query = "select * from table1"

cursor.execute(select_query)
rows = cursor.fetchall()

for row in rows:
    print(row)

# more values
values = [("Value 4", 40), ("Value 5", 50), ("Value 6", 60)]
for value in values: 
    cursor.execute(insert_query, value)
connection.commit()
rows = cursor.fetchall()

for row in rows:
    print(row)

connection.commit() ; cursor.close() ; connection.close()