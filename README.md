# file-sync


# File Synchronization Tool

This is a Python script that synchronizes files between two directories. The script performs the following operations:

- Deletes files from the destination directory that are not present in the source directory
- Copies new files from the source directory to the destination directory
- Updates existing files in the destination directory with newer versions from the source directory

Events are logged to a CSV file, including the time, event type (deleted, copied, updated), and file name. The script uses the pandas library to create a dataframe for logging, which could be slower than using the logging library.

The synchronization interval can be customized and is set in seconds.

## Usage

To use this tool, follow these steps:

1. Clone the repository to your local machine
2. Modify the `start.bat` file with:
  - Source directory path
  - Destination directory path
  - Log directory path
  - Synchronization interval in seconds
 To modify the start.bat file, you can use a text editor like Notepad or a software like Visual Studio Code
 
 For example:
  start.bat C:\Users\user\source_directory C:\Users\user\destination_directory C:\Users\user\log_directory 60
 This will synchronize the `source_directory` with `destination_directory` every 60 seconds and log events to the `log_directory`.
4. Run the `start.bat` file to start the synchronization process

## Features

- Automatically detects changes in source and destination directories
- Logs events to a CSV file for easy auditing
- Customizable synchronization interval

## Requirements

- Python 3.5 or higher
- Pandas library

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
