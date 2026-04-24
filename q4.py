is_match = False
strings: list[str] = []
while True:
    text: str = input("Enter a string: ")
    if text == "quit":
        break
    else:
        strings.append(text)
if len(strings) == 0:
    print("No strings entered")
else:
    strings = set(strings)
    for i in strings:
        if is_match:
            break
        for j in strings:
            if i == j[::-1]:
                is_match = True
                print("Reversed match found")
                break

if not is_match:
    print("No reversed match found")
