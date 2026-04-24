
ranks: list[int] = []
while True:
    try:
        rank: int = int(input("please enter a rank"))
    except ValueError:
        print("rank must be a number")
        continue
    if rank == -999:
        if len(ranks) >= 10:
            break
        else:
            print("not done yet, need at least 10 ranks")
            continue
    elif rank > 5 or rank < 1:
        print("rank must be between 1 and 5")
        continue
    else:
        ranks.append(rank)
        continue
print(f"Number of valid grades: {len(ranks)} ")
print(f"Average rank: {sum(ranks) / len(ranks)}")
print(f"Highest rank: {max(ranks)}")