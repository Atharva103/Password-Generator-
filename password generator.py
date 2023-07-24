#_______________________________________________________________________________
#Name: Atharva Lokhande
#Purpose: Task
#Task: 3
#Author: atharva
#created: 21-07-23
#_______________________________________________________________________________

import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x250")

        self.password_length = tk.StringVar()

        self.label_instruction = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
        self.label_instruction.pack(pady=10)

        self.entry_password_length = tk.Entry(root, textvariable=self.password_length, font=("Arial", 12), width=10)
        self.entry_password_length.pack()

        self.entry_password_length.bind("<FocusIn>", self.clear_default_value)  # Bind the event to clear the default value

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 12), bg="blue", fg="white")
        self.generate_button.pack(pady=10)

        self.password_display = tk.Label(root, text="", font=("Arial", 14))
        self.password_display.pack(pady=10)

        self.accept_button = tk.Button(root, text="Accept", command=self.accept_password, font=("Arial", 12), bg="green", fg="white", state=tk.DISABLED)
        self.accept_button.pack()

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_password, font=("Arial", 12), bg="red", fg="white")
        self.reset_button.pack(pady=10)

    def generate_password(self):
        try:
            length = int(self.password_length.get())
            if length <= 0:
                raise ValueError("Password length must be a positive integer.")

            password_characters = string.ascii_letters + string.digits + string.punctuation
            generated_password = ''.join(random.choice(password_characters) for _ in range(length))
            self.password_display.config(text=generated_password)
            self.accept_button.config(state=tk.NORMAL)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def accept_password(self):
        password = self.password_display.cget("text")
        messagebox.showinfo("Accepted", f"Password accepted: {password}")

    def reset_password(self):
        self.password_length.set("8")
        self.password_display.config(text="")
        self.accept_button.config(state=tk.DISABLED)

    def clear_default_value(self, event):
        # Clear the default value when the entry box receives focus
        if self.password_length.get() == "8":
            self.entry_password_length.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()
