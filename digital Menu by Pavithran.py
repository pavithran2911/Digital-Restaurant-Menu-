import tkinter as tk
from tkinter import ttk

class RestaurantMenuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Restaurant Menu")
        self.root.geometry("800x600")

        self.menu_items = [
            {"name": "Pizza Margherita", "category": "Pizza", "price": 12.99},
            {"name": "Chicken Alfredo", "category": "Pasta", "price": 14.99},
            {"name": "Classic Burger", "category": "Burger", "price": 9.99},
            {"name": "Caesar Salad", "category": "Salad", "price": 8.99},
            # Add more menu items as needed
        ]

        self.create_menu()

    def create_menu(self):
        # Create a Treeview widget to display the menu
        self.tree = ttk.Treeview(self.root, columns=("Name", "Category", "Price"), show="headings", height=20)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Price", text="Price")

        # Insert menu items into the Treeview
        for item in self.menu_items:
            self.tree.insert("", "end", values=(item["name"], item["category"], f"${item['price']:.2f}"))

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Place Treeview and scrollbar in the window
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

def main():
    root = tk.Tk()
    app = RestaurantMenuApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
