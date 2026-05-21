print("Welcome to Smart Voting & Student Management System")

print("="*40)
num_voters = int(input("\nHow many voters will vote?: "))
votes = []

for i in range(num_voters):

    while True:
        candidate = input(f"\nEnter candidate name for voter {i+1} (A/B/C): ").upper()

        if candidate in ["A", "B", "C"]:
            votes.append(candidate)
            break
        else:
            print("\n❌ Invalid input! Please enter only A, B, or C.")

print("="*40)
print("Voter List: ")
print(f"\n✅ {votes}")

vote_count = {}

for candidate in votes:
    vote_count[candidate] = vote_count.get(candidate, 0) + 1

print(f"\n📃 Vote Results: {vote_count}")


highest_votes = max(vote_count.values())

winners = []

for candidate, count in vote_count.items():
    if count == highest_votes:
        winners.append(candidate)

if len(winners) == 1:
    print("\n✌✌ Winner is Candidate", winners[0])
else:
    print("\n✔ It's a tie between Candidates:", ", ".join(winners))

print("="*40)

while True:
    search_name = input("\nEnter candidate name to search (A/B/C): ").upper()

    if search_name in vote_count:
        print(search_name, "received", vote_count[search_name], "votes.")
        break
    else:
        print("\n🔻 Candidate not found! Please try again.")





