import tkinter
from tkinter import messagebox

class Product:
    def __init__(self, main):
        self.main = main
        main.title("Product Cart")
        self.main_frame = tkinter.Frame(main)
        self.main_frame.pack()

        self.add_cart = []
        self.product_list = {
            "0101": {"name": "Coke Mismo", "price": 15.00},
            "0102": {"name": "Pringles (107g)", "price": 85.00},
            "0103": {"name": "Century Tuna 155", "price": 38.00},
            "0104": {"name": "Milo (300g)", "price": 100.00},
            "0105": {"name": "Nescafe (185g)", "price": 160.00},
            "0106": {"name": "Pancit Canton (80g)", "price": 16.00},
            "0107": {"name": "Stick-O (368g)", "price": 95.00},
            "0108": {"name": "C2 (500 mL)", "price": 32.50},
        }

    def user_cart(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        cart_label = tkinter.Label(self.main_frame, text="[YOUR CART]")
        cart_label.pack(anchor='w')

        cart_head = tkinter.Frame(self.main_frame)
        cart_head.pack(anchor='w')

        code_head = tkinter.Label(cart_head, text="CODE", width=6)
        code_head.grid(row=0, column=0)

        name_head = tkinter.Label(cart_head, text="PRODUCT NAME", width=20)
        name_head.grid(row=0, column=1)

        price_head = tkinter.Label(cart_head, text="PRICE", width=10)
        price_head.grid(row=0, column=2)

        qty_head = tkinter.Label(cart_head, text="QTY", width=10)
        qty_head.grid(row=0, column=3)

        sub_head = tkinter.Label(cart_head, text="SUBTOTAL", width=8)
        sub_head.grid(row=0, column=4)

        cart_separator = "----------------------------------------------------------------------------------"
        cart_separator_label = tkinter.Label(self.main_frame, text=cart_separator)
        cart_separator_label.pack(anchor='w')

        if len(self.add_cart) == 0:
            empty_label = tkinter.Label(self.main_frame, text="\n--> NO PRODUCTS ENTERED YET!\n\n")
            empty_label.pack(anchor='w')
        else:
            for items in self.add_cart:
                code, name, price, qty, subtotal = items
                cart_item_head = tkinter.Frame(self.main_frame)
                cart_item_head.pack(anchor='w')

                code_item = tkinter.Label(cart_item_head, text=code, width=6)
                code_item.grid(row=0, column=0)

                name_item = tkinter.Label(cart_item_head, text=name, width=20)
                name_item.grid(row=0, column=1)

                price_item = tkinter.Label(cart_item_head, text=format(price, '.2f'), width=10)
                price_item.grid(row=0, column=2)

                qty_item = tkinter.Label(cart_item_head, text=qty, width=10)
                qty_item.grid(row=0, column=3)

                sub_item = tkinter.Label(cart_item_head, text=format(subtotal, '.2f'), width=8)
                sub_item.grid(row=0, column=4)

        option_label = tkinter.Label(self.main_frame, text="\n[OPTIONS]")
        option_label.pack(anchor='w')

        enter_btn = tkinter.Button(self.main_frame, text="Enter Product", command=self.enter_product)
        enter_btn.pack(anchor='w')

        checkout_btn = tkinter.Button(self.main_frame, text="Checkout", command=self.checkout)
        checkout_btn.pack(anchor='w')

        exit_btn = tkinter.Button(self.main_frame, text="Exit")
        exit_btn.pack(anchor='w')

    def enter_product(self):
        new_window = tkinter.Toplevel(self.main)
        new_window.title("Enter Product Window")

        enter_product_label = tkinter.Label(new_window, text="[ENTER PRODUCT]")
        enter_product_label.grid(row=0, column=0)

        code_label = tkinter.Label(new_window, text="Enter Code:")
        code_label.grid(row=1, column=0)
        code_entry = tkinter.Entry(new_window)
        code_entry.grid(row=1, column=1)

        qty_label = tkinter.Label(new_window, text="Enter Qty:")
        qty_label.grid(row=2, column=0)
        qty_entry = tkinter.Entry(new_window)
        qty_entry.grid(row=2, column=1)

        enter_btn = tkinter.Button(new_window, text="Enter Product", command=lambda: self.input_process(new_window, code_entry.get(), qty_entry.get()))
        enter_btn.grid(row=3, column=1, sticky=tkinter.W)

    def input_process(self, new_window, code, qty):
        new_window.destroy()

        if code in self.product_list:
            if qty.isdigit() == True:
                item_product = self.product_list[code]
                product_name = item_product["name"]
                product_price = item_product["price"]
                product_qty = int(qty)
                found = False

                for added_products in self.add_cart:
                    if added_products[0] == code:
                        added_products[3] = int(added_products[3]) + product_qty
                        added_products[4] = float(added_products[3]) * int(added_products[2])
                        found = True
                        break
                    
                if not found:
                    product_subtotal = product_price * product_qty
                    item_lst = [code, product_name, product_price, product_qty, product_subtotal]
                    self.add_cart.append(item_lst)
                self.user_cart()
            else:
                messagebox.showerror("Invalid Entry", "Invalid Entry, Try Again")
                self.enter_product()
        else:
            messagebox.showerror("Invalid Entry", "Invalid Entry, Try Again")
            self.enter_product()

    def checkout(self):
        checkout_window = tkinter.Toplevel()
        checkout_window.title("Checkout Window")

        checkout_frame = tkinter.Frame(checkout_window)
        checkout_frame.pack()

        checkout_label = tkinter.Label(checkout_frame, text="[CHECKOUT]")
        checkout_label.pack(anchor='w')

        checkout_head = tkinter.Frame(checkout_frame)
        checkout_head.pack(anchor='w')

        checkout_name = tkinter.Label(checkout_head, text="PRODUCT NAME", width=20)
        checkout_name.grid(row=0, column=0)

        checkout_price = tkinter.Label(checkout_head, text="PRICE", width=10)
        checkout_price.grid(row=0, column=1)

        checkout_qty = tkinter.Label(checkout_head, text="QTY", width=10)
        checkout_qty.grid(row=0, column=2)

        checkout_sub = tkinter.Label(checkout_head, text="SUBTOTAL", width=8)
        checkout_sub.grid(row=0, column=3)

        checkout_separator = "------------------------------------------------------------------------"
        checkout_separator_label = tkinter.Label(checkout_frame, text=checkout_separator)
        checkout_separator_label.pack(anchor='w')

        initial_total = 0

        for items in self.add_cart:
            code, name, price, qty, subtotal = items
            checkout_item_head = tkinter.Frame(checkout_frame)
            checkout_item_head.pack(anchor='w')

            checkout_name = tkinter.Label(checkout_item_head, text=name, width=20)
            checkout_name.grid(row=0, column=0)

            checkout_price = tkinter.Label(checkout_item_head, text=price, width=10)
            checkout_price.grid(row=0, column=1)

            checkout_qty = tkinter.Label(checkout_item_head, text=qty, width=10)
            checkout_qty.grid(row=0, column=2)

            checkout_sub = tkinter.Label(checkout_item_head, text=subtotal, width=8)
            checkout_sub.grid(row=0, column=3)

            initial_total += subtotal

        checkout_separator = "------------------------------------------------------------------------"
        checkout_separator_label = tkinter.Label(checkout_frame, text=checkout_separator)
        checkout_separator_label.pack(anchor='w')

        subtotal_frame = tkinter.Frame(checkout_frame)
        subtotal_frame.pack(anchor='w')

        subtotal_label = tkinter.Label(subtotal_frame, text="Subtotal:", width=20)
        subtotal_label.grid(row=0, column=0)

        subtotal_value = tkinter.Label(subtotal_frame, text=initial_total, width=28)
        subtotal_value.grid(row=0, column=1)

master_window = tkinter.Tk()
GUI = Product(master_window)
GUI.user_cart()
master_window.mainloop()