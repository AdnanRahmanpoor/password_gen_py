import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator") # title of the app
        self.root.geometry("400x600") # size of app window

        # checkboxes
        self.use_lowercase = tk.BooleanVar(value=True) # lowercase
        self.use_uppercase = tk.BooleanVar(value=True) # uppercase
        self.use_numbers = tk.BooleanVar(value=True) # numbers
        self.use_symbols = tk.BooleanVar(value=True) # symbols
        self.password_length = tk.IntVar(value=12) # password length
        self.password_var = tk.StringVar() # password

        self.create_widgets()

    def create_widgets(self):
        # main app frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # character options (views for the created checkboxes)
        ttk.Label(main_frame, text="Password Options", font=("Helvetica", 12, 'bold')).grid(row=0, column=0, pady=10, sticky=tk.W)

        ttk.Checkbutton(main_frame, text="Lowercase Letters (a-z)", variable=self.use_lowercase).grid(row=1, column=0,sticky=tk.W)
        ttk.Checkbutton(main_frame, text="Uppercase Letters (A-Z)", variable=self.use_uppercase).grid(row=2, column=0,sticky=tk.W)
        ttk.Checkbutton(main_frame, text="Numbers (0-9)", variable=self.use_numbers).grid(row=3, column=0,sticky=tk.W)
        ttk.Checkbutton(main_frame, text="Symbols (!@#$%^&*)", variable=self.use_symbols).grid(row=4, column=0,sticky=tk.W)

        # Password length
        ttk.Label(main_frame, text="Password Length:").grid(row=5, column=0, pady=(20, 5), sticky=tk.W)
        length_frame = ttk.Frame(main_frame)
        length_frame.grid(row=6, column=0, sticky=tk.W)

        ttk.Scale(length_frame, from_=4, to=50, orient=tk.HORIZONTAL, variable=self.password_length, length=200, command=lambda s:self.password_length.set('%d' % float(s))).pack(side=tk.LEFT)
        ttk.Label(length_frame, textvariable=self.password_length).pack(side=tk.LEFT, padx=10)

        # Password generate Button
        ttk.Button(main_frame, text="Generate Password", command=self.generate_password).grid(row=7, column=0, pady=20)

        # Display password
        ttk.Label(main_frame, text="Generated Password:").grid(row=8, column=0, pady=(10,5), sticky=tk.W)
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, width=40)
        password_entry.grid(row=9, column=0, pady=(0,10))

        # Password Copy Button
        ttk.Button(main_frame, text="Copy To Clipboard", command=self.copy_to_clipboard).grid(row=10, column=0)

        # Password Strength Indicator
        ttk.Label(main_frame, text="Password Strength").grid(row=11, column=0, pady=(20,5), sticky=tk.W)
        self.strength_var = tk.StringVar()
        tk.Label(main_frame, textvariable=self.strength_var, font=('Helvetica', 13,'bold')).grid(row=12, column=0, sticky=tk.W)

        # Tips
        ttk.Label(main_frame, text="Tips:", font=('Helvetica', 10, 'bold')).grid(row=13, column=0, pady=(20,5), sticky=tk.W)
        
        tips_text = """
            • Use at least 12 characters for strong passwords
            • Mix different character types
            • Avoid common words and patterns
            • Use unique passwords for each account
        """

        ttk.Label(main_frame, text=tips_text, justify=tk.LEFT).grid(row=14, column=0, sticky=tk.W)

    def generate_password(self):
        # Validate that atleast one of options is selected
        if not any([self.use_lowercase.get(), self.use_uppercase.get(), self.use_numbers.get(), self.use_symbols.get()]):
            self.password_var.set("Please select at least one character type")
            return
        
        # Create characters based on selections
        chars = ''
        if self.use_lowercase.get():
            chars += string.ascii_lowercase
        if self.use_uppercase.get():
            chars += string.ascii_uppercase
        if self.use_numbers.get():
            chars += string.digits
        if self.use_symbols.get():
            chars += string.punctuation

        # Generate password
        length = self.password_length.get()
        password = ''.join(random.choice(chars) for _ in range(length))
        self.password_var.set(password)

        # update password strength indicator
        self.update_password_strength(password)

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password and password != "Please select at least one character type:":
            pyperclip.copy(password) 

    def update_password_strength(self, password):
        strength = 0 
        criteria = [
            (len(password) >= 12, "Length >= 12"),
            (any(c.islower() for c in password), "Lowercase"),
            (any(c.isupper() for c in password), "Uppercase"),
            (any(c.isdigit() for c in password), "Numbers"),
            (any(c in string.punctuation for c in password), "Symbols"),
        ]

        met_criteria = [desc for met, desc in criteria if met]
        strength = len(met_criteria)

        if strength <= 2:
            strength_text = 'Weak'
        elif strength <= 3:
            strength_text = 'Moderate'
        elif strength <= 4:
            strength_text = 'Strong'
        else:
            strength_text = 'Very Strong'

        self.strength_var.set(f"{strength_text}")

def main():
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()