
 # Used for performing operating system related operations like listing files, deleting files, etc.
import os
# Used for high-level file operations like moving files, copying files, etc.
import shutil 
# Used to create GUI windows and widgets
import tkinter as tk   
# Used to create various GUI dialogs like file dialog, message box, etc.
from tkinter import filedialog, messagebox, simpledialog
# Module for working with JSON data   
import json
# for working with time-related functions
import time
# for working with file paths
from pathlib import Path

#create class of app
class FileUtilityApp:
    def __init__(self):
        # main window of app with tk
        self.window = tk.Tk()
        self.window.title("File Editor")
        self.window.geometry("600x710")

        # Create a top frame for the welcome label and description
        top_frame = tk.Frame(self.window)
        top_frame.pack(side=tk.TOP, padx=20, pady=20)

        # Add a welcome heading
        welcome_label = tk.Label(
            top_frame, text="Welcome to File Editor",
            font=("Helvetica", 24, "bold")
        )
        welcome_label.pack()

        # multi line string app description
        app_description = (
            "This application allows you to perform various file and folder operations.\n\n"
            "Features include:\n"
            "- Searching files in a directory\n"
            "- Moving files between directories\n"
            "- Deleting files\n"
            "- Creating new folders\n"
            "- Viewing recent changes\n"
            "- Saving recent changes to a file\n"
            "- Viewing file properties\n"
        )
        description_label = tk.Label(
            top_frame, text=app_description, justify=tk.LEFT, font=("Helvetica", 8, "bold")
        )
        description_label.pack(pady=5)

        # Create the search button
        search_button = tk.Button(
            self.window, text="Search Files", command=self.search_files,
            fg="#fff", bg="#4CAF50", activebackground="#3E8E41", bd=0,
            padx=10, pady=5, font=("Helvetica", 14, "bold"),
            borderwidth=2, relief="solid", highlightthickness=1, highlightcolor="#000"
        )
        search_button.pack(padx=10, pady=5, anchor="w")

        # Create the move button
        move_button = tk.Button(
            self.window, text="Move Files", command=self.move_files,
            fg="#fff", bg="#2196F3", activebackground="#0E88B1", bd=0,
            padx=16, pady=5, font=("Helvetica", 14, "bold"),
            borderwidth=2, relief="solid", highlightthickness=1, highlightcolor="#000"
        )
        move_button.pack(padx=10, pady=5, anchor="w")

        # Create the delete button
        delete_button = tk.Button(
            self.window, text="Delete Files", command=self.delete_files,
            fg="#fff", bg="#F44336", activebackground="#A92C25", bd=0,
            padx=16, pady=5, font=("Helvetica", 14, "bold"),
            borderwidth=2, relief="solid", highlightthickness=1, highlightcolor="#000"
        )
        delete_button.pack(padx=10, pady=5, anchor="w")

        # Create the create folder button
        create_folder_button = tk.Button(
            self.window, text="Create Folder", command=self.create_folder,
            fg="#fff", bg="#FFC107", activebackground="#E09600", bd=0,
            padx=16, pady=5, font=("Helvetica", 14, "bold"),
            borderwidth=2, relief="solid", highlightthickness=1, highlightcolor="#000"
        )
        create_folder_button.pack(padx=10, pady=5, anchor="w")

        # Create the recent changes button
        recent_changes_button = tk.Button(
            self.window, text="Recent Changes", command=self.show_recent_changes,
            fg="#fff", bg="#607D8B", activebackground="#455A64", bd=0,
            padx=16, pady=5, font=("Helvetica", 14, "bold"),
            borderwidth=2, relief="solid", highlightthickness=1, highlightcolor="#000"
        )
        recent_changes_button.pack(padx=10, pady=5, anchor="w")

        # Create the save recent changes button
        save_changes_button = tk.Button(
            self.window, text="Save Recent Changes", command=self.save_recent_changes,
            fg="#fff", bg="#9C27B0", activebackground="#6A1B9A", bd=0,
            padx=16, pady=5, font=("Helvetica", 14, "bold"),
            borderwidth=2, relief="solid", highlightthickness=1, highlightcolor="#000"
        )
        save_changes_button.pack(padx=10, pady=5, anchor="w")


        # create an empty list for self class, used to store recent changes
        self.recent_changes = []

        # Create the view file properties button
        view_file_properties_button = tk.Button(
            self.window, text="View File Properties", command=self.view_file_properties,
            fg="#fff", bg="#009688", activebackground="#00695C", bd=0,
            padx=16, pady=8, font=("Helvetica", 14, "bold"),
            borderwidth=2, relief="solid", highlightthickness=1, highlightcolor="#000"
        )
        view_file_properties_button.pack(padx=10, pady=5, anchor="w")

    def search_files(self):
        # Show a file dialog box to choose the directory to search in
        directory = filedialog.askdirectory(title="Select Directory to Search In")
        if directory:
            # Show a message box with the list of files found in the directory
            files = os.listdir(directory)
            message = f"Files found in {directory}:\n\n{files}"
            messagebox.showinfo("Search Results", message)

    def move_files(self):
        # Show a file dialog box to choose the file to move
        source_file = filedialog.askopenfilename(title="Select File to Move")
        if source_file:
            # Show a file dialog box to choose the destination directory
            destination_dir = filedialog.askdirectory(
                title="Select Destination Directory"
            )
            if destination_dir:
                # Move the file to the destination directory
                destination_file = os.path.join(
                    destination_dir, os.path.basename(source_file)
                )
                shutil.move(source_file, destination_file)
                # Add the time and file name to the recent changes list
                modification_time = os.path.getmtime(destination_file)
                self.recent_changes.append(f"{destination_file} ({modification_time})")
                # Show a message box to confirm that the move was successful
                messagebox.showinfo(
                    "Move Successful", f"{source_file} moved to {destination_file}"
                )

    def delete_files(self):
        # Show a file dialog box to choose the file to delete
        file_to_delete = filedialog.askopenfilename(title="Select File to Delete")
        if file_to_delete:
            # Show a message box to confirm that the user really wants to delete the file
            if messagebox.askyesno(
                "Confirm Delete", f"Are you sure you want to delete {file_to_delete}?"
            ):
                # Delete the file
                os.remove(file_to_delete)
                # Add the time and file name to the recent changes list
                modification_time = os.path.getmtime(file_to_delete)
                self.recent_changes.append(f"{file_to_delete} ({modification_time})")
                # Show a message box to confirm that the delete was successful
                messagebox.showinfo("Delete Successful", f"{file_to_delete} deleted")

    # function to create a new folder
    def create_folder(self):
        # Show a file dialog box to choose the directory to create the folder in
        directory = filedialog.askdirectory(
            title="Select Directory to Create Folder In"
        )
        if directory:
            # Show an entry dialog box to get the name of the new folder
            folder_name = simpledialog.askstring(
                "Create Folder", "Enter the name of the new folder:"
            )
            if folder_name:
                # Create the new folder
                new_folder = os.path.join(directory, folder_name)
                os.mkdir(new_folder)
                # Add the time and folder name to the recent changes list
                modification_time = os.path.getmtime(new_folder)
                self.recent_changes.append(f"{new_folder} ({modification_time})")
                # Show a message box to confirm that the folder was created
                messagebox.showinfo("Folder Created", f"Folder {new_folder} created")

    # function to display recent changes
    def show_recent_changes(self):
        # Show a message box with the list of recent changes
        message = "Recent changes:\n\n" + "\n".join(self.recent_changes)
        messagebox.showinfo("Recent Changes", message)

    # save the recent changes
    def save_recent_changes(self):
        # Show a file dialog box to choose the file to save to
        file_to_save = filedialog.asksaveasfilename(
            title="Save Recent Changes As",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if file_to_save:
            # Write the recent changes list to the file
            with open(file_to_save, "w") as f:
                f.write("\n".join(self.recent_changes))
            # Show a message box to confirm that the save was successful
            messagebox.showinfo("Save Successful", f"Recent changes saved to {file_to_save}")


    def view_file_properties(self):
        # Show a file dialog box to choose the file
        file_to_view = filedialog.askopenfilename(title="Select File to View Properties")
        if file_to_view:
            # Get the file properties using the get_file_properties function
            file_properties = self.get_file_properties(file_to_view)
            
            # Create a mini frame (Toplevel) to display the file properties as a separate window
            mini_frame = tk.Toplevel(self.window)
            mini_frame.title("File Properties")
            mini_frame.geometry("400x300")

            # Add a scrollbar to the mini frame for easier navigation of the content
            scrollbar = tk.Scrollbar(mini_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            # Create a text widget to display the JSON content of the file properties
            text_widget = tk.Text(mini_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
            # Insert the file properties (formatted as JSON with indents) into the text widget
            text_widget.insert(tk.END, json.dumps(file_properties, indent=2))
            # Add the text widget to the mini frame and fill it to the available space
            text_widget.pack(expand=True, fill=tk.BOTH)
            
            # Configure the scrollbar to control the text widget's vertical scrolling
            scrollbar.config(command=text_widget.yview)

    def get_file_properties(self, file_path):
        # Use the pathlib.Path object to represent the file path
        file = Path(file_path)
        # Get the file's stat object, which contains information about the file
        file_stat = file.stat()
        
        # Create a dictionary of the file properties using the stat object and pathlib.Path attributes
        properties = {
            "name": file.name,  # File name
            "path": str(file),  # Full file path as a string
            "size": file_stat.st_size,  # File size in bytes
            "created": time.ctime(file_stat.st_ctime),  # Creation time as a string
            "modified": time.ctime(file_stat.st_mtime),  # Modification time as a string
            "accessed": time.ctime(file_stat.st_atime),  # Access time as a string
        }
        
        # Return the dictionary containing the file properties
        return properties

    # run the tkinter window
    def run(self):
        self.window.mainloop()

# create a FileUtilityApp object and run the application
if __name__ == "__main__":
    app = FileUtilityApp()
    app.run()
