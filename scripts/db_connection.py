import psycopg2
import pandas as pd

# Connection parameters
conn = psycopg2.connect(
    host="localhost",   # Update with your host
    database="tellcom", # Use your database name
    user="postgres",    # Update with your user
    password="ofge"
)

# Query data
query = "SELECT * FROM xdr_data;"  # Replace with your table name
# df = pd.read_sql(query, conn)

# Close connection
conn.close()

# Display the data
# df.head()
