# Step 1: Create the file and write student names with marks
with open("marks.txt", "w") as file:
    file.write("Vidya 82\n")
    file.write("Swara 65\n")
    file.write("Sanika 90\n")
    file.write("Rutuja 74\n")
    file.write("Shweta 78\n")

# Step 2: Read the file and display students who scored more than 75
print("Students who scored more than 75 marks:\n")

with open("marks.txt", "r") as file:
    for line in file:
        name, mark = line.strip().split()
        mark = int(mark)
        if mark > 75:
            print(f"{name} - {mark}")
