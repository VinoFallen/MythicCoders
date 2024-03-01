import tkinter as tk
from signupGUI import *
from loginGUI import *

# Create the main window
root = tk.Tk()
root.title("CipherSafe")

# Set window size and position it in the center of the screen
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

# Set font styles
title_font = ("Helvetica", 24, "bold")
button_font = ("Helvetica", 14)

# Set colors
bg_color = "#1f2833"  # Dark blue (cyber security theme)
text_color = "#66FCF1"  # Light blue

# Set background color
root.configure(bg=bg_color)

# Create title label
title_label = tk.Label(root, text="CipherSafe", font=title_font, fg=text_color, bg=bg_color)
title_label.pack(pady=20)

# Create Sign Up button
sign_up_button = tk.Button(root, text="Sign Up", font=button_font, command=lambda: sign_up_func(root))
sign_up_button.pack(pady=10)

# Create Login button
login_button = tk.Button(root, text="Login", font=button_font, command=lambda: login_func(root))
login_button.pack(pady=10)

# Run the application
root.mainloop()
