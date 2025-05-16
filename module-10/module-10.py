import mysql.connector


config = {
    'host': 'localhost', 
    'user': 'root', #This part is just full of inputs that you need to put in manually. Like, yk where you replace the things with your info. In this code...
    'password': 'Pandasarecool2@',
    'database': 'Bacchus_Winery'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()

    for (table_name,) in tables:
        print(f"\n--- Table: {table_name} ---")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if rows:
            col_names = [desc[0] for desc in cursor.description]
            print(" | ".join(col_names))
            print("-" * 50)

            for row in rows:
                print(" | ".join(str(cell) for cell in row))
        else:
            print("Nothing in this table")

    cursor.close()
    conn.close()

except mysql.connector.Error as err:
    print("Database error:", err)