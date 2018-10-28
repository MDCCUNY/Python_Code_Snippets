# Linux Commands in Python
import os

""" The functions that the OS module provides allows you to interface with the
underlying operating system that Python is running on – be that Windows, Mac or
Linux. """

def linux_commands():

    print("\nLinux Commands\n\n 1) Change Directory (cd)\n 2) List directory contents (ls)\n",
    "3) Print working directory (pwd)\n 4) Make directory (mkdir)\n 5) Remove directory (rm)\n 6) Exit (0)\n")
    
    user_input = input("\nEnter a command: ")

    if(user_input == 'cd'):                 # Change the directory
        path = input("\nEnter a path: ")
        os.chdir(path)
        
    elif(user_input == 'ls'):               # List the files in the directory
        print(os.listdir(os.getcwd()))
        
    elif(user_input == 'pwd'):              # Print your current directory
        print(os.getcwd())
        
    elif(user_input == 'mkdir'):            # Make a new directory
        name = input("\nEnter a name: ")

        if(os.path.exists(name)):           # Check if the directory already exists
            print("\nThis file already exists!")
        else:
            os.mkdir(name)

    elif(user_input == 'rm'):               # Remove a file/directory (be careful!)
        folder = input("\nEnter a folder: ")
        os.rmdir(folder)

    elif(user_input == '0'):
        return 0;
    
    else:
        print("\nError! That isn't an option!");

    linux_commands()

    
if __name__ == "__main__":
    linux_commands();

