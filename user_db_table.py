import mysql.connector


def create_user_database(username, host, user, password):
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password)
        cursor = conn.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {username}")
        print(f"Database '{username}' created successfully.")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


def create_users_table(username, host, user, password):
    """
    Create a 'users' table within the given database.
    """
    try:
        conn = mysql.connector.connect(host=host, user=user, password=password, database=username)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                website_name VARCHAR(255),
                username VARCHAR(255),
                encrypted_password BINARY(255),
                part_of_password VARCHAR(255)
            )
        """)

        print("Table 'users' created successfully.")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
