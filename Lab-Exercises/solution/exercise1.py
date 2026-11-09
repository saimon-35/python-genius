# 1. Capture inputs

name = input("Enter your name: ")
age = int(input("Enter your age: "))
developer = input("Are you a developer? (yes/no): ").lower()


# 2. Evaluate conditional logic

if age < 18:
    tier = "Tier 3: Guest"

elif age >= 18 and developer == "yes":
    tier = "Tier 1: Admin Infrastructure Access"

else:
    tier = "Tier 2: Standard Executive Access"


# 3. Print final profile card

print("\n------ Profile Card ------")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Developer: {developer}")
print(f"Clearance Tier: {tier}")