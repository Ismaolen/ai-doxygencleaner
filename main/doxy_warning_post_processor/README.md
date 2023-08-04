# README.md

---

# doxy_warning_post_processor

This folder contains code for post-processing Doxygen warnings. It includes the following files:

- `README.md`: This file provides an overview of the project's structure, files, and functionalities.
- `doxy_warning_post_processor.py`: The main Python script for post-processing Doxygen warnings.

## `doxy_warning_post_processor.py`

This Python script includes a class named `WarningPostProcessor` that is used to detect and process 
warnings after fixes have been applied to the codebase. Here's a brief overview of this class:

### Class: `WarningPostProcessor`

The `WarningPostProcessor` class doesn't have any class-level attributes. It consists of the following methods:

#### 1. `apply_fix()`

This method applies fixes to the header files and saves changes.

It works by:

- Loading pre-warning details from a JSON file (`preprocessed_warnings_data.json`).
- Loading post-fix file content from a JSON file (`postprocessed_warnings_data.json`).
- Writing the post-fix content back to the header files.

#### 2. `detect_warning()`

This method detects and updates warning details post-fix.

It performs the following steps:

- Loading pre-warning details from a JSON file (`preprocessed_warnings_data.json`).
- Running the `DoxyWarningDetector` to detect warnings after fixes have been applied.
- Updating the warning lists with the post-fix warnings.
- Adding updated warning details to a JSON file (`postprocessed_warnings_data.json`).

This method doesn't take any parameters and doesn't return any value.

### Key Functions Used In This Script

- `load_pre_fix_data_from_json()`: Loads pre-fix warning details from a JSON file.
- `load_data_from_json()`: Loads post-fix file content from a JSON file.
- `FileHandler().write_file()`: Writes post-fix content back to the header files.
- `DoxyWarningDetector().run_doxygen()`: Detects warnings after fixes have been applied.
- `add_data_to_json()`: Adds updated warning details to a JSON file.
- `print_project_details()`: Prints out project details post-fix. 

For additional details, including the individual method's specific parameters and returns, refer to the inline comments and method docstrings within [`doxy_warning_post_processor.py`](./doxy_warning_post_processor.py).

**Note:** Remember to set up any necessary configuration and dependencies before running the script.