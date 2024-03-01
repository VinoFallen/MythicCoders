import mysql.connector
import bcrypt
import loginGUI as lg


def verify_credentials(username, password, bluetooth_id, mysql_password):
    try:
        # Connect to the main database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password=mysql_password,
            database="password_manager"
        )
        cursor = conn.cursor()

        # Retrieve hashed password and Bluetooth ID from the main database
        cursor.execute('SELECT password, bluetooth_id FROM users WHERE username = %s', (username,))
        stored_credentials = cursor.fetchone()

        if stored_credentials:
            stored_password = stored_credentials[0]
            stored_bluetooth_id = stored_credentials[1]

            # Check if the inputted password matches the stored hashed password
            if bcrypt.checkpw(password.encode(), stored_password.encode()) and bluetooth_id == stored_bluetooth_id:
                return True
            else:
                return False
        else:
            print("User not found.")
            return False

    except mysql.connector.Error as err:
        print("Error:", err)
        return False

    finally:
        # Close the database connection
        if conn.is_connected():
            cursor.close()
            conn.close()



