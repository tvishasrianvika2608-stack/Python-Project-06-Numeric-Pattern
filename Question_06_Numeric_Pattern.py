
size = int(input("Enter diamond size (1 to 9): "))

if size < 1 or size > 9:
    print("Invalid size! Enter a number between 1 and 9.")

else:
    print("\n----- HOLLOW NUMBER DIAMOND -----")

    for i in range(1, size + 1):
        spaces = " " * (size - i)

        if i == 1:
            pattern = str(i)
        else:
            pattern = str(i) + " " * (2 * i - 3) + str(i)

        print(spaces + pattern)

    for i in range(size - 1, 0, -1):
        spaces = " " * (size - i)

        if i == 1:
            pattern = str(i)
        else:
            pattern = str(i) + " " * (2 * i - 3) + str(i)

        print(spaces + pattern)

    print("---------------------------------")
