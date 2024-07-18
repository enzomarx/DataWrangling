import os
import shutil
import pyautogui
import time

# Define the folders
source_folder = r'C:\Brother'
destination_folder = r'C:\DCTF'

# Function to perform automation and file operations
def perform_operations():
    try:
        # Perform automation actions with pyautogui
        pyautogui.click(x=50, y=41)
        pyautogui.click(x=122, y=201)
        pyautogui.click(x=1072, y=739)
        pyautogui.click(x=953, y=733)
        pyautogui.click(x=895, y=697)
        
        time.sleep(2)  # Add a short delay to ensure actions are completed
        
        # List all .rfb files in source folder
        files = os.listdir(source_folder)
        
        # Create destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)
        
        # Copy .rfb files to destination folder
        for file_name in files:
            if file_name.endswith('.rfb'):
                source_file_path = os.path.join(source_folder, file_name)
                destination_file_path = os.path.join(destination_folder, file_name)
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Copied: {file_name}")
        
        # Delete .rfb files from source folder
        for file_name in files:
            if file_name.endswith('.rfb'):
                file_path = os.path.join(source_folder, file_name)
                os.remove(file_path)
                print(f"Deleted: {file_name}")
        
        print("Operations completed successfully.")
    
    except Exception as e:
        print(f"Error performing operations: {e}")

# Execute the operations
perform_operations()
