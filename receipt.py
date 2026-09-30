from data import bookings, food_orders, users

def generate_receipt(username):
    user_bookings = [b for b in bookings if b['user']==username]
    last = user_bookings[-1] if user_bookings else None
    food = [o for o in food_orders if o['user']==username]
    food_total = sum([o['price'] for o in food])
    b_total = (last['ticket_price'] if last else 0) + (last['glasses_fee'] if last else 0)
    total = b_total + food_total
    print("\n=== RECEIPT ===")
    if last:
        print(f"Movie: {last['movie_title']} ({last['movie_id']})")
        print(f"Showtime: {last['showtime']}, Seat: {last['seat']}")
        print(f"Ticket: ₹{last['ticket_price']} 3D Fee: ₹{last['glasses_fee']}")
    print("Food Ordered:")
    for o in food:
        print(f"{o['food_id']} ₹{o['price']}")
    print(f"Loyalty Points: {users[username]['loyalty']}")
    print(f"TOTAL: ₹{total}\n================\n")
