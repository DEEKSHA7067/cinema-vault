from data import movies, bookings

def view_available_seats():
    movie_id = input("Movie ID: ")
    showtime = input("Showtime: ")
    if movie_id not in movies or showtime not in movies[movie_id]['showtimes']:
        print("Invalid selection.")
        return
    all_seats = [f"A{i}" for i in range(1,6)]
    booked = [b['seat'] for b in bookings if b['movie_id'] == movie_id and b['showtime'] == showtime]
    print("Seat Map:")
    for s in all_seats:
        print(f"{s} [{'Booked' if s in booked else 'Available'}]")
