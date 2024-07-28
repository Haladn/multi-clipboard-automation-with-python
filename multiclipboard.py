import json.tool
import sys # to manipulate python runtime environment (command line) arguments
import clipboard  # for copy and paste clipboard data
import json
import os

SAVED_DATA = "clipboard.json"

# define a function to create a json file
def save_data(filepath,data):
    with open(filepath,"w") as f:  # "w" to overwrite the file if exist or write a new one 
        json.dump(data,f)

def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}
    
def delete_data(filepath):
    try:
        with open(filepath,"w") as f:
            json.dump({},f)
        print("The data deleted.")
        
    except:
        print('The file does not exist.')


# check that we have 2 command line arguments
if len(sys.argv) == 2:

    data = load_data(SAVED_DATA)
    # get second argument (first one is our file name argument "multiclipboard.py")
    command = sys.argv[1]
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data saved!")
    elif command == "load":
        key = input("enter a key: ")
        if key in data:
            clipboard.copy(data[key]) # copy the data to the clipboard
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")   
    elif command == "list":
        print(data)
    elif command == "delete":
        key = input("Enter y/n to continue: ").lower()
        if key == "y":
            delete_data(SAVED_DATA)
            print("Clipboards deleted successfully")
        else:
            print("deletion is cancelled.")
    else:
        print("Unknown command")

else:
    print("Please pass exactly one command.")

    
