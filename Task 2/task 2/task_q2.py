
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]


add_more = input("Kya aap movies add karna chahte hain? (yes/no): ").lower()
if add_more == "yes":
    num = int(input("Kitni movies add karna chahte hain? "))
    for i in range(num):
        name = input(f"Movie {i+1} ka naam: ")
        budget = int(input(f"{name} ka budget: "))
        movies.append((name, budget))


total_budget = sum(budget for name, budget in movies)
average_budget = total_budget / len(movies)
print(f"\nAverage budget of all movies: ${average_budget:,.2f}\n")


count_above_avg = 0
print("Movies with budget above average:\n")
for name, budget in movies:
    if budget > average_budget:
        difference = budget - average_budget
        print(f"{name}: ${budget:,} (Above average by ${difference:,.2f})")
        count_above_avg += 1

print(f"\nTotal number of movies above average budget: {count_above_avg}")
