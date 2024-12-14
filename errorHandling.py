def main():
    # Ask the user for a filename
    filename = input("Enter the filename: ")

    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read. Please check permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
