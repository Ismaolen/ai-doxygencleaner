# README.md

---

This README provides a brief introduction to the various Python files present 
in the doxygen_management folder. These files contain important classes and 
methods that perform various functions like detecting warnings in Doxygen 
documentation generation, configuring Doxyfiles, and handling file operations.


# doxygen_management

This folder contains scripts for handling and managing Doxygen documentation generation. 
It consists of the following files:

- `README.md`: This file provides an overview of the folder's structure and its functionalities.
- `__init__.py`: A Python initialization script.
- `doxy_warning_detector.py`: The main Python script to detect warnings during 
Doxygen documentation generation.
- `doxyfile_configurator.py`: The Python script to configure the Doxyfile 
used for Doxygen documentation generation.
- `file_handler.py`: The Python script for handling file operations.


## doxy_warning_detector.py

This Python file contains the `DoxyWarningDetector` class, which serves the 
purpose of detecting warnings in Doxygen documentation generation.

### Class: `DoxyWarningDetector`
The `DoxyWarningDetector` class has the following attributes and Key Methods:

- Attributes:
  - `warnings_list` : A list to hold the detected warnings (initialized as an empty list).
  - `doxyfile_configurator` : An object of the class `DoxyfileConfigurator` to configure the Doxyfile.
  - `file_handler` : An object of the class `FileHandler` to handle file operations.

- Key Methods:

  - `check_project_directory()`: Checks if there is only one subfolder in the project 
  directory and returns its name. In case of multiple subfolders, the program exits with an error message.

  - `get_all_header_files(project_folder_path: str)`: Retrieves all the header 
  files in the specified project folder path. If no header files are found, the program 
  exits with an error message.

  - `run_doxygen_for_file(header_file_name: str, lines: list, input_line: str, 
  project_folder_path: str, line_num: int)`: Prepares the Doxyfile with given parameters 
  and runs Doxygen for the specified header file. The result of the Doxygen run is returned.

  - `extract_warnings(result: subprocess.CompletedProcess, header_file_name: str)`: 
  Extracts warnings from the result of a Doxygen run. Returns lists of warning contents, 
  warning line numbers and total number of warnings.

  - `run_doxygen()`: Executes the complete process to run Doxygen for all header 
  files and extract warnings. The process includes preparing the Doxyfile, running Doxygen, 
  and extracting warnings. A tuple containing the results of the process is returned.

## How to Use

To use these classes, you should import the necessary Python files and create 
objects of the classes, as shown below:

```python
from doxygen_management.doxy_warning_detector import DoxyWarningDetector

# Create an object of DoxyWarningDetector
detector = DoxyWarningDetector()

# Use the methods of the object
detector.check_project_directory()
detector.get_all_header_files(project_folder_path)
```
You can replace `project_folder_path` with the path of your project directory.

For any queries or further explanation regarding the classes and their methods, 
please refer to the respective Python files as they contain detailed docstrings 
for each class and method.



# file_handler.py

The `FileHandler` class is responsible for managing file operations. 
It provides various functions to read, write, and find specific lines of text in files. 
Moreover, it offers the capability to redirect the output of certain functions into a file.

### Class: `FileHandler`

The `FileHandler` class consists of the following methods:

## Methods

- `read_file(filename: str) -> list:` This method reads a file and returns its
   contents as a list of lines.

- `write_file(filename: str, lines: list)`: This method writes a list of lines into a file.

- `has_single_line(list: list) -> bool:` This method checks if a list has only a single line. 
   If yes, it returns True, else the program exits with an error message.

- `find_line_numbers(filename: str, searchText: str) -> int:` This method finds the line numbers 
   of all occurrences of a specific text in a file. It returns the line number 
   of the first occurrence of the search text if there is only one occurrence, 
   else the program exits with an error message.

- `redirect_print_to_file(self, project_folder_path, header_file_name_list, 
   warning_num_list, warning_content_llist, warning_line_number_llist, file_content_list, 
   pre_or_post, output_file)`: This method redirects the output of the 
   `print_project_details_without_color` function to a specified file. 
   It modifies the standard output (stdout) to a specified file, calls a 
   function to print data without color, and then restores stdout to its original state.

## Example

```python
from doxygen_management.file_handler import FileHandler
file_handler = FileHandler()

# Read a file
lines = file_handler.read_file('example.txt')

# Write a list of lines into a file
file_handler.write_file('output.txt', lines)

# Check if a list has only a single line
single_line = file_handler.has_single_line(lines)

# Find the line numbers of a certain text in a file
line_number = file_handler.find_line_numbers('example.txt', 'searched_text')

# Redirect the output of a function into a file
file_handler.redirect_print_to_file(project_folder_path, header_file_name_list, warning_num_list, warning_content_llist
```

# doxyfile_configurator.py

The `DoxyfileConfigurator` class is used to configure a Doxyfile. It includes methods 
to create and modify a Doxyfile, add spaces to configuration parameters, 
and check for single subfolders in a directory. The class also includes 
an instance of the `FileHandler` class, used to manipulate files.

### Class: `DoxyfileConfigurator`

The `DoxyfileConfigurator` class has the following attributes and Methods:
## Attributes

- `file_handler : FileHandler:` An instance of the `FileHandler` class used to manipulate files.

## Methods

- `__init__(self):` This method initializes an instance of the `DoxyfileConfigurator` class.

- `remove_doxyfile_if_exists(self, directory_path):` This method removes a 
Doxyfile at the given directory path.

- `create_doxyfile(self, directory_path):` This method creates a Doxyfile at the given directory path.

- `add_spaces_to_string(self, config_parameters):` This method adds specific 
spaces to configuration parameters.

- `get_single_subfolder(self, directory):` This method checks if there is only 
one subfolder in a given directory.

- `get_header_files(self, directory):` This method returns a list of .h and .hpp 
files in the given directory.

- `configure_doxyfile(self, filename, config_parameters):` This method configures the 
Doxyfile with the given parameters.

## Example

```python
doxyfile_configurator = DoxyfileConfigurator()

# Remove a Doxyfile at a directory path
doxyfile_configurator.remove_doxyfile_if_exists('/path/to/directory')

# Create a Doxyfile at a directory path
doxyfile_configurator.create_doxyfile('/path/to/directory')

# Add spaces to configuration parameters
formatted_parameters = doxyfile_configurator.add_spaces_to_string([('EXAMPLE_PARAM', 3)])

# Check if there is only one subfolder in a directory
single_subfolder, subfolder_name = doxyfile_configurator.get_single_subfolder('/path/to/directory')

# Get .h and .hpp files in a directory
header_files_present, header_files = doxyfile_configurator.get_header_files('/path/to/directory')

# Configure the Doxyfile with given parameters
doxyfile_configurator.configure_doxyfile('Doxyfile', formatted_parameters)
```

**Note:** You will need to replace `/path/to/directory` and `Doxyfile` with your 
actual directory paths and filenames. The second value in tuples passed to 
`add_spaces_to_string` should represent the number of spaces you want to add to the 
corresponding parameter.\
**Note:** Remember to set up any necessary configuration and dependencies before running the scripts.
