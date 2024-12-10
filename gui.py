from tkinter import Tk, Label, Entry, Button, messagebox
from typing import Callable, List


class CalculatorGUI:
    """GUI Calculator Application"""

    def __init__(self, root: Tk, on_calculate: Callable[[str, List[float]], float]):
        """
        Initializes the GUI elements for the calculator.

        Args:
            root (Tk): The root Tkinter window.
            on_calculate (Callable[[str, List[float]], float]): Callback for performing calculations.
        """
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x300")
        self.root.config(bg="lightblue")
        self.on_calculate = on_calculate

        # UI Elements
        Label(root, text="Enter Values (comma-separated):", bg="lightblue").pack(pady=10)
        self.entry_values = Entry(root, width=30)
        self.entry_values.pack(pady=5)

        Label(root, text="Select Operation:", bg="lightblue").pack(pady=10)

        Button(root, text="Add", command=lambda: self.handle_calculate("add")).pack(pady=5)
        Button(root, text="Subtract", command=lambda: self.handle_calculate("subtract")).pack(pady=5)
        Button(root, text="Multiply", command=lambda: self.handle_calculate("multiply")).pack(pady=5)
        Button(root, text="Divide", command=lambda: self.handle_calculate("divide")).pack(pady=5)

        self.result_label = Label(root, text="", bg="lightblue", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def handle_calculate(self, operation: str) -> None:
        """
        Handles the calculation button click.

        Args:
            operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
        """
        try:
            # Parse input
            raw_values = self.entry_values.get()
            if not raw_values:
                raise ValueError("No values provided.")
            values = [float(x.strip()) for x in raw_values.split(",")]

            # Perform calculation
            result = self.on_calculate(operation, values)

            # Display result
            self.result_label.config(text=f"Result: {result:.2f}")

        except ValueError as ve:
            messagebox.showerror("Error", f"Invalid Input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
