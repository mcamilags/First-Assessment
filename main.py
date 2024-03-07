from authentication import Authentication
from user import User
from finances import Finances
from inventory import Inventory
from university_functions import UniversityFunctions


def main_menu():
    print("Welcome to the University Platform for Services and Loans (PUSP)")
    print("1. Register User")
    print("2. Log In")
    print("3. Exit")


def user_menu(user):
    print(f"Welcome, {user.get_name()} ({user.get_id()})")
    if user.get_role() == 'student':
        print("1. Rent High-tech Computer")
        print("2. Reserve Bicycle")
        print("3. Make Cashless Payment")
        print("4. Pay for Food in the Cafeteria and Tools using QR Code")
        print("5. Access Virtual Library of Academic Resources")
    elif user.get_role() == 'admin':
        print("1. Manage Services and Loans")
        print("2. Manage Financial Transactions")
        print("3. Integrate Payment Methods")
        print("4. Manage Inventory")
    print("6. Log Out")


def main():
    authentication = Authentication()
    finances = Finances()
    inventory = Inventory()

    while True:
        main_menu()
        option = input("Select an option: ")

        if option == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            id = input("Enter your ID: ")
            password = input("Enter your password: ")
            role = int(input("Are you a student or an admin? Enter 1 for student, 2 for admin: "))
            if role == 1:
                role = "student"
            elif role == 2:
                role = "admin"
            else:
                print("Invalid role. Please enter 1 for student or 2 for admin.")
                continue
            user = User(name, email, id, password, role)
            print(authentication.register_user(user))
            if role == "student":
                finances.open_account(user)
        elif option == "2":
            id = input("Enter your ID: ")
            password = input("Enter your password: ")
            user = authentication.login(id, password)
            if user:
                while True:
                    user_menu(user)
                    user_option = input("Select an option: ")
                    if user_option == "6":
                        print("Logged out.")
                        break
                    elif user_option == "3" and user.get_role() == "student":
                        amount = float(input("Enter amount to add: "))
                        print(finances.add_funds(user, amount))
                    elif user_option == "4" and user.get_role() == "admin":
                        resource = input("Enter resource to update: ")
                        quantity = int(input("Enter quantity: "))
                        print(inventory.update_inventory(resource, quantity))
                    elif user_option == "1" and user.get_role() == "student":
                        print(UniversityFunctions.rent_high_tech_computer(user, finances, inventory))
                    elif user_option == "2" and user.get_role() == "student":
                        print(UniversityFunctions.reserve_bicycle(user, finances, inventory))
                    elif user_option == "3" and user.get_role() == "student":
                        print(UniversityFunctions.make_cashless_payment(user, finances))
                    elif user_option == "4" and user.get_role() == "student":
                        print(UniversityFunctions.pay_with_qr_code(user, finances))
                    elif user_option == "5" and user.get_role() == "student":
                        UniversityFunctions.access_virtual_library(user)
                    elif user_option == "1" and user.get_role() == "admin":
                        UniversityFunctions.manage_services_and_loans(user, inventory)
                    elif user_option == "2" and user.get_role() == "admin":
                        UniversityFunctions.manage_financial_transactions(user, finances)
                    elif user_option == "3" and user.get_role() == "admin":
                        UniversityFunctions.integrate_payment_methods(user)
                    elif user_option == "4" and user.get_role() == "admin":
                        UniversityFunctions.manage_inventory(user, inventory)
                    else:
                        print("Invalid option. Please select a valid option.")
            else:
                print("Incorrect ID or password.")
        elif option == "3":
            print("Thanks for using PUSP. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    main()
