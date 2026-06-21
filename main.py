# Simple Recommendation System

items = {
    "Interstellar": ["sci-fi", "space", "drama"],
    "Avengers": ["action", "superhero"],
    "Titanic": ["romance", "drama"],
    "Inception": ["sci-fi", "thriller"],
    "Batman": ["action", "hero"]
}

user_input = input("Enter your interests (comma separated): ")
user_prefs = [x.strip().lower() for x in user_input.split(",")]

def score(prefs, tags):
    return len(set(prefs) & set(tags))

results = []

for item, tags in items.items():
    s = score(user_prefs, tags)
    if s > 0:
        results.append((item, s))

results.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended for you:\n")

if results:
    for r in results:
        print(r[0], "- score:", r[1])
else:
    print("No recommendations found")