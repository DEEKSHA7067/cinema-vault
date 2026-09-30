from data import food_menu, food_orders, users

def add_food_item():
    fid = input("Food ID: ")
    name = input("Name: ")
    price = float(input("Price: "))
    food_menu[fid] = {"name": name, "price": price}
    print("Added.")

def view_food_menu():
    for f_id, info in food_menu.items():
        print(f"{f_id}: {info['name']} (₹{info['price']})")

def prebook_food(username):
    fid = input("Food ID: ")
    if fid not in food_menu:
        print("Not found.")
        return
    food_orders.append({"food_id": fid, "user": username, "price": food_menu[fid]["price"]})
    users[username]['loyalty'] += 2
    print("Food pre-booked. Loyalty +2.")

def view_my_food_orders(username):
    orders = [o for o in food_orders if o['user']==username]
    for o in orders:
        print(f"{food_menu[o['food_id']]['name']} (₹{o['price']})")

def cancel_food_order(username):
    fid = input("Food ID to cancel: ")
    for o in food_orders:
        if o['user']==username and o['food_id']==fid:
            food_orders.remove(o)
            print("Cancelled.")
            return
    print("No such order.")

