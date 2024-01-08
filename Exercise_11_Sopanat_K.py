num_rows = int(input())
for i in range(1, num_rows + 1):
    print(" " * (num_rows - i), end="")
    print("*" * (2 * i - 1), end="")
    print()
