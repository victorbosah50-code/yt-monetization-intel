from scoring import calculate_score

title = input("Enter your video title: ")
length = int(input("Enter video length in minutes: "))

score = calculate_score(title, length)

print("\nMonetization Score:", score)

if score >= 70:
    print("✅ Strong monetization potential")
elif score >= 50:
    print("⚠️ Average — consider improving title or length")
else:
    print("❌ Low — revise before posting")
