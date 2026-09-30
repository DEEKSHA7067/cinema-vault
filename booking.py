from data import bookings, movies, ticket_prices, users

def book_ticket(username):
    movie_id = input("Movie ID: ")
    if movie_id not in movies:
        print("Movie not found.")
        return
    showtime = input("Showtime: ")
    if showtime not in movies[movie_id]['showtimes']:
        print("Showtime invalid.")
        return
    seat = input("Seat (A1-A5): ")
    need_3d = input("3D glasses needed? (yes/no): ").lower() == "yes"
    price = ticket_prices.get(movie_id, 0)
    glasses_fee = 50 if need_3d else 0
    for b in bookings:
        if b['movie_id'] == movie_id and b['showtime'] == showtime and b['seat'] == seat:
            print("Seat booked.")
            return
    bookings.append({
        "movie_id": movie_id,
        "movie_title": movies[movie_id]['title'],
        "showtime": showtime,
        "seat": seat,
        "user": username,
        "ticket_price": price,
        "3d_glasses": need_3d,
        "glasses_fee": glasses_fee,
        "paid": False
    })
    users[username]['loyalty'] += 10
    print("Ticket booked. Loyalty +10.")

def cancel_ticket(username):
    movie_id = input("Movie ID: ")
    showtime = input("Showtime: ")
    seat = input("Seat: ")
    for b in bookings:
        if b['movie_id']==movie_id and b['showtime']==showtime and b['seat']==seat and b['user']==username:
            bookings.remove(b)
            print("Cancelled.")
            return
    print("Not found.")

def view_booking_history(username):
    user_bookings = [b for b in bookings if b['user']==username]
    for b in user_bookings:
        print(f"{b['movie_title']} {b['showtime']} Seat:{b['seat']} 3D:{'Yes' if b['3d_glasses'] else 'No'} Paid:{b['paid']}")

def pay_for_booking(username):
    unpaid = [b for b in bookings if b['user']==username and not b['paid']]
    if not unpaid:
        print("No unpaid bookings.")
        return
    b = unpaid[-1]
    method = input("Pay method (credit/upi/cash): ")
    b['paid'] = True
    print("Payment successful.")
