import tkinter as tk


def sign_up_func(root):
    # Function to open the sign-up window
    root.withdraw()
    sign_up_window = tk.Toplevel(root)
    sign_up_window.title("Sign Up")

    # Set font styles
    title_font = ("Helvetica", 20, "bold")
    label_font = ("Helvetica", 12)
    entry_font = ("Helvetica", 10)

    # Set colors
    bg_color = "#1f2833"  # Dark blue (cyber security theme)
    text_color = "#66FCF1"  # Light blue

    # Set background color
    sign_up_window.configure(bg=bg_color)

    # CipherSafe Label
    cipher_safe_label = tk.Label(sign_up_window, text="CipherSafe", font=title_font, fg=text_color, bg=bg_color)
    cipher_safe_label.pack(pady=10)

    # Sign Up Label
    sign_up_label = tk.Label(sign_up_window, text="Sign Up", font=title_font, fg=text_color, bg=bg_color)
    sign_up_label.pack(pady=10)

    # Username Label and Entry
    username_label = tk.Label(sign_up_window, text="Username:", font=label_font, fg=text_color, bg=bg_color)
    username_label.pack(pady=5)
    username_entry = tk.Entry(sign_up_window, font=entry_font)
    username_entry.pack(pady=5)

    # Password Label and Entry
    password_label = tk.Label(sign_up_window, text="Password:", font=label_font, fg=text_color, bg=bg_color)
    password_label.pack(pady=5)
    password_entry = tk.Entry(sign_up_window, show="*", font=entry_font)
    password_entry.pack(pady=5)

    # MySQL Password Label and Entry
    mysql_password_label = tk.Label(sign_up_window, text="MySQL Password:", font=label_font, fg=text_color, bg=bg_color)
    mysql_password_label.pack(pady=5)
    mysql_password_entry = tk.Entry(sign_up_window, show="*", font=entry_font)
    mysql_password_entry.pack(pady=5)

    # Submit Button
    submit_button = tk.Button(sign_up_window, text="Submit", font=label_font, command=lambda: get_sign_up_details(username_entry.get(), password_entry.get(), mysql_password_entry.get()))
    submit_button.pack(pady=10)

    # Resize the window to fit all widgets
    window_width = 500  # Adjust the width as needed
    window_height = 400  # Adjust the height as needed
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    sign_up_window.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

def get_sign_up_details(username, password, mysql_password):
    # Function to get sign-up details
    print("Username:", username)
    print("Password:", password)
    print("MySQL Password:", mysql_password)