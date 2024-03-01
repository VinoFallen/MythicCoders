import tkinter as tk
import login_check as lc


def login_func(root):
    # Function to open the login window
    root.withdraw()
    login_window = tk.Toplevel(root)
    login_window.title("Login")

    # Set font styles
    title_font = ("Helvetica", 20, "bold")
    label_font = ("Helvetica", 12)
    entry_font = ("Helvetica", 10)

    # Set colors
    bg_color = "#1f2833"  # Dark blue
    text_color = "#66FCF1"  # Light blue

    # Set background color
    login_window.configure(bg=bg_color)

    # CipherSafe Label
    cipher_safe_label = tk.Label(login_window, text="CipherSafe", font=title_font, fg=text_color, bg=bg_color)
    cipher_safe_label.pack(pady=10)

    # Login Label
    login_label = tk.Label(login_window, text="Login", font=title_font, fg=text_color, bg=bg_color)
    login_label.pack(pady=10)

    # Username Label and Entry
    global username_entry
    username_label = tk.Label(login_window, text="Username:", font=label_font, fg=text_color, bg=bg_color)
    username_label.pack(pady=5)
    username_entry = tk.Entry(login_window, font=entry_font)
    username_entry.pack(pady=5)

    # Password Label and Entry
    global password_entry
    password_label = tk.Label(login_window, text="Password:", font=label_font, fg=text_color, bg=bg_color)
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_window, show="*", font=entry_font)
    password_entry.pack(pady=5)

    # MySQL Password Label and Entry
    global mysql_password_entry
    mysql_password_label = tk.Label(login_window, text="MySQL Password:", font=label_font, fg=text_color, bg=bg_color)
    mysql_password_label.pack(pady=5)
    mysql_password_entry = tk.Entry(login_window, show="*", font=entry_font)
    mysql_password_entry.pack(pady=5)

    # Submit Button
    submit_button = tk.Button(login_window, text="Login", font=label_font, command=login_callback)
    submit_button.pack(pady=10)

    # Resize the window to fit all widgets
    window_width = 500  # Adjust the width as needed
    window_height = 400  # Adjust the height as needed
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    login_window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')


def get_username(username):
    return username


def get_password(password):
    return password


def get_mysql_password(mysql_password):
    return mysql_password


def login_callback():
    username = username_entry.get()
    password = password_entry.get()
    mysql_password = mysql_password_entry.get()
    bluetooth_id = ''
    if lc.verify_credentials(username, password, bluetooth_id, mysql_password):



