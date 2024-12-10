import tkinter as tk
from tkinter import messagebox
from typing import Optional
import formulas

class PhoneStyleCalculator:
    """Phone-style calculator implemented using Tkinter."""

    def __init__(self, root: tk.Tk):
        """
        Initialize the calculator's GUI elements.

        Args:
            root (tk.Tk): The main Tkinter window.
        """
        self.root = root
        self.root.title("Phone Style Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.config(bg="lightgray")

        self.expression = ""  # Holds the current calculation
        self.create_widgets()

    def create_widgets(self):
        """Create and position widgets for the calculator."""
        # Display Entry
        self.display = tk.Entry(
            self.root, font=("Arial", 24), bg="white", bd=10, relief=tk.RIDGE, justify="right"
        )
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15)

        # Button layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(
                self.root, text=text, font=("Arial", 18), bg="lightblue", fg="black",
                width=5, height=2, command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text: str):
        """
        Handle button clicks.

        Args:
            button_text (str): The label of the button clicked.
        """
        if button_text == "C":
            # Clear the display
            self.expression = ""
            self.display.delete(0, tk.END)
        elif button_text == "=":
            # Perform the calculation
            self.calculate_result()
        else:
            # Add to the expression and update display
            self.expression += button_text
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def calculate_result(self):
        """Evaluate the expression and display the result."""
        try:
            # Split expression into values and operator
            result = eval(self.expression)  # Caution: Ensure proper input sanitization
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, f"{result:.2f}")
            self.expression = str(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Calculation")
            self.expression = ""
            self.display.delete(0, tk.END)


def main():
    """Main function to run the calculator application."""
    root = tk.Tk()
    PhoneStyleCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
