# Open the input file in read mode and output file in write mode
with open("input.txt", "r") as infile, open("cleaned.txt", "w") as outfile:
    for line in infile:
        # Write the line to output only if it's not blank (ignoring whitespace)
        if line.strip():
            outfile.write(line)

print("Blank lines removed and cleaned content saved to cleaned.txt.")
