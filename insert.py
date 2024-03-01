import mysql.connector


def insert_into_users_table(username, website_name, user_name, encrypted_password, part_of_password, host,
                            user, password):
    """
    Insert values into the 'users' table within the given database.
    """
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(host=host, user=user, password=password, database=username)
        cursor = conn.cursor()

        # Encode password as bytes
        encrypted_password_bytes = encrypted_password.encode('utf-8')

        # Insert values into users table
        sql = "INSERT INTO users (website_name, username, encrypted_password, part_of_password) VALUES (%s, %s, %s, %s)"
        val = (website_name, user_name, encrypted_password_bytes, part_of_password)
        cursor.execute(sql, val)
        conn.commit()

        print("Values inserted into 'users' table successfully.")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        # Close the database connection
        if conn.is_connected():
            cursor.close()
            conn.close()
