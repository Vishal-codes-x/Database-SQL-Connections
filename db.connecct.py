# Import mysql.connector to connect Python with MySQL.
# Use mysql.connector.connect() to connect to the MySQL server.
# Create a cursor object to run SQL queries.
# Execute SELECT DATABASE(); and fetch the result to confirm connection.
# Finally, close the cursor and database connection.



import mysql.connector

# Step 1: connecct to MySQL
conn = mysql.connector.connecct(
    host="localhost", # your host
    user="root", # your MYSQL username
    password="your_password", # Your MySQL password
    database="testdb"
)

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Execute SQL Query
cursor.execute("SELECT DATABSE();")

# Step 4: Fetch result
data = cursor.fetchone()
print("connected to Database:", data)

# Step 5: Clone connection
cursor.clone()
conn.close()