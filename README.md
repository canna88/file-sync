# file-sync

This is a Python script that synchronizes files between two directories. The script performs the following operations:

- Deletes files from the destination directory that are not present in the source directory
- Copies new files from the source directory to the destination directory
- Updates existing files in the destination directory with newer versions from the source directory

Events are logged to a CSV file, including the time, event type (deleted, copied, updated), and file name. The script uses the pandas library to create a dataframe for logging, which could be slower than using the logging library.

The synchronization interval can be customized and is set in seconds.

## Requirements

- Python 3.5 or higher
- Pandas library
- A text editor like Notepad or a software like Visual Studio Code

## Usage

To use this tool, follow these steps:

1. Clone the repository to your local machine
2. Modify the `start.bat` file (you can use a text editor like Notepad or a software like Visual Studio Code) with:
    - python.exe path
    - file_sync.py path
    - For example:
         @echo off
         "C:\Users\Admin\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\Admin\Documents\file_syc_directory\file_sync.py"
         pause
     
3. Run the `start.bat` file to start the synchronization process
    - you will ask to write: source_path, destination_path, log_path and synchronization's interval in seconds
    - you can write the paths without the quotation marks
    - For example:
        C:\Users\Admin\Documents\file_syc_directory\Source_dir\
        C:\Users\Admin\Documents\file_syc_directory\Destination_dir\
        C:\Users\Admin\Documents\file_syc_directory\Log_dir\
        4

## Features

1. Automatically detects changes in source and destination directories
2. Logs events to a CSV file for easy auditing with 3 columns:
    - date and time
    - events: there are 3 types of events:
        - copied: file is in the source directory, but It was not before the synchronization process
        - updated: file is in the source directory, but It was before the synchronization process
        - deleted: file is not in the source directory, but It was before the synchronization process
    - file name
3. errors detector:
    - there is a "An error occurred during synchronization:" message in case is not loop is not working anymore
    - in case there are no files inside source directory, the event will be logged as well

4. Customizable synchronization interval (in seconds)


## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
