from data import movies, ticket_prices, reviews, bookings

def add_movie():
    movie_id = input("Movie ID: ")
    if movie_id in movies:
        print("ID exists.")
        return
    name = input("Movie title: ")
    showtimes = input("Showtimes (comma separated): ").split(",")
    showtimes = [s.strip() for s in showtimes]
    price = float(input("Ticket price (₹): "))
    movies[movie_id] = {"title": name, "showtimes": showtimes}
    ticket_prices[movie_id] = price
    reviews[movie_id] = []
    print(f"Movie '{name}' added.")

def view_movies():
    for m_id, info in movies.items():
        avg = "N/A"
        if reviews[m_id]:
            avg = round(sum([r['stars'] for r in reviews[m_id]]) / len(reviews[m_id]), 2)
        print(f"ID:{m_id} Title:{info['title']} AvgRating:{avg}")

def view_showtimes():
    movie_id = input("Movie ID: ")
    if movie_id in movies:
        print(f"Showtimes: {', '.join(movies[movie_id]['showtimes'])}")
    else:
        print("Not found.")

def delete_movie():
    movie_id = input("Movie ID to delete: ")
    if movie_id in movies:
        del movies[movie_id]
        del ticket_prices[movie_id]
        # Also remove bookings for this movie:
        bookings[:] = [b for b in bookings if b['movie_id'] != movie_id]
        print("Movie and related bookings deleted.")
    else:
        print("Movie not found.")

def add_review(username):
    movie_id = input("Movie ID to review: ")
    if movie_id not in movies:
        print("Not found.")
        return
    stars = int(input("Stars (1-5): "))
    text = input("Comment: ")
    reviews[movie_id].append({"user": username, "stars": stars, "text": text})
    print("Review added.")

def view_reviews():
    movie_id = input("Movie ID: ")
    if movie_id in reviews and reviews[movie_id]:
        for r in reviews[movie_id]:
            print(f"{r['user']}: {r['stars']}⭐ - {r['text']}")
    else:
        print("No reviews.")
