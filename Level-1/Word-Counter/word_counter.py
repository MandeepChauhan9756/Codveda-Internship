# Function to count the word
def count_word(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        words = content.split()
        # print(words)
        print("\n file: ", filename)
        print("Total words: ", len(words))
            
    except FileNotFoundError:
        print("File not found. Try Again")
    except Exception as e:
        print("Error: ", e)
        
file_name = input("Enter file name: ")

# Checking here that file is .txt or not
if not file_name.endswith(".txt"):
    print("Please enter a .txt file only")
    exit()
    
# Calling funtion
count_word(file_name)
