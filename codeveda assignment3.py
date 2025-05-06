# Function to count words in a file
def count_words_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Split the content into words
            words = content.split()

            # Return the number of words
            return len(words)
    except FileNotFoundError:
        return "❌ The file was not found. Please check the file name or path."

# Ask user for the filename
filename = input("Enter the full path or file name (e.g., 'basic.txt'): ")

# Get word count
word_count = count_words_in_file(filename)

# Print result or error message
if isinstance(word_count, str):
    print(word_count)
else:
    print(f"✅ The file contains {word_count} words.")

