filename = input("Enter the filename to open (e.g., students.csv): ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile content:")
        print(content)

except FileNotFoundError:
    print("Oops! That file doesn't exist yet ")
