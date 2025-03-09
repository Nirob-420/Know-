print("💖 Love Matching Calculator 💖")

# Taking two names as input
name1 = input("Enter the first person's name: ").lower().replace(" ", "")
name2 = input("Enter the second person's name: ").lower().replace(" ", "")

# Combine both names
combined_name = name1 + name2

# Simple algorithm to calculate match percentage
match_score = 0
for char in combined_name:
    match_score += ord(char)  # Convert character to ASCII value and sum

# Convert to a percentage (between 50 to 100 for better results)
love_percentage = 50 + (match_score % 51)

# Display the result
print(f"\n❤️ {name1.capitalize()} & {name2.capitalize()} ❤️")
print(f"Your Love Compatibility: {love_percentage}%")

# Give a fun message based on percentage
if love_percentage > 90:
    print("🔥 Perfect Match! You two are made for each other! 🔥")
elif love_percentage > 75:
    print("💞 Strong Connection! A bright future ahead! 💞")
elif love_percentage > 50:
    print("😊 Good Match! With some effort, this can work well! 😊")
else:
    print("💔 Uh-oh! You might need to work a little harder on this relationship! 💔")
