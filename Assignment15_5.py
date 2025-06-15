# Accept filename and search string from user
filename = input("Enter the filename: ")
search_string = input("Enter the string to search: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        frequency = content.count(search_string)
        
    print(f'The string "{search_string}" appears {frequency} times in the file {filename}.')
except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
