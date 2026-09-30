import users, movies, booking, seats, food, receipt

def manager_menu():
    while True:
        print("\nManager Menu")
        print("1. Add Movie")
        print("2. Delete Movie")
        print("3. View Movies")
        print("4. Add Food Item")
        print("5. View Food Menu")
        print("6. Logout")
        c = input("> ")
        if c == "1":
            movies.add_movie()
        elif c == "2":
            movies.delete_movie()
        elif c == "3":
            movies.view_movies()
        elif c == "4":
            food.add_food_item()
        elif c == "5":
            food.view_food_menu()
        elif c == "6":
            break
        else:
            print("Invalid choice. Try again.")

def customer_menu(username):
    while True:
        print("\nCustomer Menu")
        print("1. View Movies")
        print("2. View Showtimes")
        print("3. Book Ticket")
        print("4. Cancel Ticket")
        print("5. View Booking History")
        print("6. Pay for Booking")
        print("7. View Available Seats")
        print("8. View Food Menu")
        print("9. Pre-book Food")
        print("10. View My Food Orders")
        print("11. Cancel Food Order")
        print("12. Add/See Movie Reviews")
        print("13. Generate Receipt")
        print("14. Logout")
        ch = input("> ")
        if ch == "1":
            movies.view_movies()
        elif ch == "2":
            movies.view_showtimes()
        elif ch == "3":
            booking.book_ticket(username)
        elif ch == "4":
            booking.cancel_ticket(username)
        elif ch == "5":
            booking.view_booking_history(username)
        elif ch == "6":
            booking.pay_for_booking(username)
        elif ch == "7":
            seats.view_available_seats()
        elif ch == "8":
            food.view_food_menu()
        elif ch == "9":
            food.prebook_food(username)
        elif ch == "10":
            food.view_my_food_orders(username)
        elif ch == "11":
            food.cancel_food_order(username)
        elif ch == "12":
            sub = input("1:Add 2:View > ")
            if sub == "1":
                movies.add_review(username)
            else:
                movies.view_reviews()
        elif ch == "13":
            receipt.generate_receipt(username)
        elif ch == "14":
            break
        else:
            print("Invalid choice. Try again.")

def main():
    while True:
        print("\n******_____WELCOME TO CinemaVault_____******")
        print("1. Manager")
        print("2. Customer")
        print("3. Register")
        print("4. Exit")
        mode = input("> ")
        if mode == "1":
            pwd = input("Enter Manager password: ")
            if pwd == "0030":
                manager_menu()
            else:
                print("Incorrect Manager password!")
        elif mode == "2":
            username = users.login()
            if username:
                customer_menu(username)
        elif mode == "3":
            users.register()
        elif mode == "4":
            break

if __name__ == "__main__":
    main()

