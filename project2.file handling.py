import os
#crate file function.
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"file {filename}: created successfully!")
    except FileExistsError:
        print(f"file {filename} is already exist.")
    except Exception as E:
        print("An error occured")
#view all function.
def view_all_function():
    files=os.listdir()
    if not files:
        print("file not found!")
    else:
        print("file is found!")
        for file in files:
            print(file)
#delete file function
def delete_function(filename):
    try:
        os.remove(filename)
        print(f"file {filename} is successfully deleted.")
    except FileNotFoundError:
        print(f"file {filename} is presented.")

    except Exception as e:
        print("error occoured")

#read file
def read_file(filename):
    try:
        with open(filename,'r') as f:
            content= f.read()
            print(f"the file {filename} content is {content}")
    except FileNotFoundError:
        print(f"file {filename} is not founded! ")

    except Exception as e:
        print("An error occored")

#edit file
def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content=input("enter the data =")
            f.wite(content +"\n")
            print(f"content added to {filename} successfully")

    except FileNotFoundError:
        print(f"file {filename} dosent exist")
    except Exception as e:
        print("An error occored!")


def main():
    while True:
        print("\n File management opreations.")
        print("1.Create file")
        print("2.view all file")
        print("3.Delete file")
        print("4.Read file")
        print("5.Edit file")
        print("6.Exit")

        choice =int(input("Enter your choice ="))
        if choice == 1:
            filename = input("Create file name =")
            create_file(filename)
        elif choice ==2:
            view_all_function()

        elif choice == 3:
            filename=input("write the file name if you delete =")
            delete_function(filename)
        elif choice == 4:
            filename=input("Enter file name =")
            read_file(filename)
        elif choice == 5:
            filename =input("file name to you edit =")
            edit_file(filename)

        elif choice == 6:
            print("you are exit in file.")
            break
        else:
            print("invalid choice please choese the (1-6) range value.")
if __name__ == "__main__":
    main()