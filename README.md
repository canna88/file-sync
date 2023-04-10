# file-sync

This tool provides an automated way to synchronize files between two directories. It can be used to ensure that files are always up-to-date between a local directory and a remote server, for example.

## Getting Started

To use this tool, follow these steps:

1. Clone the repository to your local machine
2. Modify the `start.bat` file with the paths to your source directory, destination directory, and log directory
3. Run the `start.bat` file to start the synchronization process

## Features

- Automatically detects changes in source and destination directories
- Logs events to a CSV file for easy auditing
- Customizable synchronization interval

## Requirements

- Python 3.5 or higher
- Pandas library

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
