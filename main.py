
def main():

    # Store the file path and text from the text document into variables
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    # Remove the white space and get the word count from the text
    num_words = get_num_words(text)
    
    # pull the dictionary from the get_chars_dict function to get the character counts and sorted list from the chars_sorted_list function
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    # Print startup text
    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document")
    print()

    # loop to print organized text showing the character counts for each letter
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue   
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    # Print end text
    print("--- End Report ---")

#Function to add the key: sort_on when sorting the new list
def sort_on(d):
    return d["num"]

# Function to take the characters in the dictionary and turn them into a list
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# Function to turn text into lowercase and count the characters
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


# Function to split string on whitespace
def get_num_words(text):
    words = text.split()
    return len(words)

# Function to open the file and read its contents
def get_book_text(path):
    with open(path) as f:
        return f.read()

# Run the main Function
main()