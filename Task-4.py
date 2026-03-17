print("Welcome to CR election platform!")
print("Nominated candidates information is given below:")

candidates = [
    "1. Raian",
    "2. Mahadi",
    "3. Sanzida",
    "4. Sinthy"
]

for c in candidates:
    print(c)

users = []
votes = []

i = 0
while i < 2:
    user_id = input("Enter your id to vote: ")

    if user_id in users:
        print("You've already voted")
    else:
        print(candidates)
        v = int(input("Give your vote: {1/2/3/4} "))

        if v in [1, 2, 3, 4]:
            votes.append(v)
            users.append(user_id)
            print("Thanks for your valuable vote")
            i = i + 1
        else:
            print("Invalid vote")


input("Press Enter key for the result\n")
print("Raian got", votes.count(1), "vote's\n")
print("Mahadi got", votes.count(2), "vote's\n")
print("Sanzida got", votes.count(3), "vote's\n")
print("Sinthy got", votes.count(4), "vote's")
