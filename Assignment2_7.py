n = int(input())

for i in range(n):
    print("  " * i, end=" ")  # Print leading spaces
    for j in range(1, n + 1):
        print(j, end=" ")
print()