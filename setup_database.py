import mysql.connector

def create_table():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="imam",
            password="Aceh2033",
            database="project_uas"
        )
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS knowledge
                     (id INT AUTO_INCREMENT PRIMARY KEY,
                     text TEXT,
                     processed_text TEXT,
                     category TEXT)''')
        conn.commit()
        conn.close()
        print("Table created successfully!")
    except mysql.connector.Error as error:
        print("Error creating table:", error)
