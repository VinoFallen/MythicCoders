import mysql.connector
import bcrypt

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_pass",
    database="password_manager"
)
cursor = conn.cursor()


# Function to hash password
def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


# Function to sign up a new user
def sign_up(username, password, bluetooth_id):
    try:
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        if user:
            print("Username already exists. Please choose a different username.")
        else:
            hashed_password = hash_password(password)
            cursor.execute('INSERT INTO users (username, password, bluetooth_id) VALUES (%s, %s, %s)', (username, hashed_password, bluetooth_id))
            conn.commit()
            print("Sign up successful. You can now log in.")
    except mysql.connector.Error as err:
        print("Error:", err)


# Function to log in a user
def login(username, password, bluetooth_id):

    # Retrieve the stored hashed password and Bluetooth ID from the database
    cursor.execute('SELECT password, bluetooth_id FROM users WHERE username = %s', (username,))
    stored_data = cursor.fetchone()

    if stored_data:
        stored_password, stored_bluetooth_id = stored_data
        # Convert the stored password to bytes-like object
        stored_password_bytes = stored_password.encode()

        # Check if the password and Bluetooth ID match the stored values
        if bcrypt.checkpw(password.encode(), stored_password_bytes) and bluetooth_id == stored_bluetooth_id:
            print("Login successful. Welcome, {}!".format(username))
        else:
            print("Incorrect password or Bluetooth ID. Please try again.")
    else:
        print("User not found. Please sign up.")

    # Close the database connection
    cursor.close()
    conn.close()


# Test the functionality
sign_up("user2", "password123", "example_bluetooth_id")
login("user2", "password123", "example_bluetooth_id")
