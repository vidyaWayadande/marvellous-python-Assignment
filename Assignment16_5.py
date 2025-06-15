# Open the file in read mode
with open("data.txt", "r") as file:
    print("Lines with more than 5 words:\n")
    for line in file:
        # Split the line into words
        words = line.strip().split()
        
        # Check if the line has more than 5 words
        if len(words) > 5:
            print(line.strip())
