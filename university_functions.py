class UniversityFunctions:
    @staticmethod
    def pay_with_qr_code(user, finances):
        print("Scanning QR code...")
        amount = float(input("Enter amount to pay: "))
        if user.get_id() in finances.accounts:
            if finances.accounts[user.get_id()]['money'] >= amount:
                print(f"Payment of {amount} made successfully with QR code.")
                finances.accounts[user.get_id()]['money'] -= amount
            else:
                print("Insufficient funds.")
        else:
            print("You need to open an account to make a payment.")

    def access_virtual_library(user):
        print("Accessing virtual library...")

    def manage_services_and_loans(user, inventory):
        if user.get_role() == "admin":
            print("Managing services and loans...")

            print("List of available services:")
            inventory.display_inventory()

        else:
            print("You do not have permission to perform this action.")

    def manage_financial_transactions(user, finances):
        if user.get_role() == "admin":
            print("Managing financial transactions...")

            print("Financial transactions history:")
            for student_id, account_info in finances.accounts.items():
                print(f"Student ID: {student_id}")
                print("Transactions:")
                for idx, transaction in enumerate(account_info.get('transactions', []), start=1):
                    print(f"{idx}. Type: {transaction['type']}, Amount: {transaction['amount']}")

        else:
            print("You do not have permission to perform this action.")

    def integrate_payment_methods(user):
        if user.get_role() == "admin":
            print("Integrating payment methods...")

            print("Current payment methods:")
            new_method = input("Enter the new payment method: ")
            print("Payment methods integrated successfully.")

        else:
            print("You do not have permission to perform this action.")

    def manage_inventory(user, inventory):
        if user.get_role() == "admin":
            print("Managing inventory...")
            print("Inventory status:")
            inventory.display_inventory()
            new_product = input("Enter the new product to add: ")
            quantity = int(input("Enter quantity: "))
            inventory.update_inventory(new_product, quantity)

            print("Inventory managed successfully.")

        else:
            print("You do not have permission to perform this action.")

    def make_cashless_payment(user, finances):
        if user.get_id() in finances.accounts:
            amount = float(input("Enter amount to pay: "))
            if finances.accounts[user.get_id()]['money'] >= amount:
                finances.accounts[user.get_id()]['money'] -= amount
                return f"Payment of ${amount} made successfully."
            else:
                return "Insufficient funds."
        else:
            return "You need to open an account to make a payment."

    def rent_high_tech_computer(user, finances, inventory):
        if user.get_role() == 'student':
            if user.get_id() in finances.accounts:
                if inventory.resources.get("computers", 0) > 0:
                    rental_cost = 10
                    if finances.accounts[user.get_id()]['money'] >= rental_cost:
                        finances.accounts[user.get_id()]['money'] -= rental_cost
                        inventory.resources[
                            "computers"] -= 1  # Actualizamos la cantidad de computadoras en el inventario
                        return "High-tech computer rented successfully."
                    else:
                        return "Insufficient funds to rent a high-tech computer."
                else:
                    return "Sorry, no high-tech computers available for rent."
            else:
                return "You need to open an account to rent a high-tech computer."
        else:
            return "Only students can rent high-tech computers."

    def reserve_bicycle(user, finances, inventory):
        if user.get_role() == 'student':
            if user.get_id() in finances.accounts:
                if inventory.resources.get("bicycles",
                                           0) > 0:  # Verificamos la disponibilidad de bicicletas en el inventario
                    rental_cost = 5  # Costo de alquiler
                    if finances.accounts[user.get_id()]['money'] >= rental_cost:
                        finances.accounts[user.get_id()]['money'] -= rental_cost
                        inventory.resources["bicycles"] -= 1  # Actualizamos la cantidad de bicicletas en el inventario
                        return "Bicycle reserved successfully."
                    else:
                        return "Insufficient funds to reserve a bicycle."
                else:
                    return "Sorry, no bicycles available for reservation."
            else:
                return "You need to open an account to reserve a bicycle."
        else:
            return "Only students can reserve bicycles."


