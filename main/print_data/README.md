# README.md

---

# print_data
The `print_data` folder is a module part of the `ai_doxygen_cleaner` project. 
It contains the `print_data.py` script which is used to print details about 
projects, including file contents, Doxygen warnings, 
and lines where the warnings occurred.

## Folder Structure

```plaintext
print_data
├── README.md
├── __init__.py
└── print_data.py
```

## Function Overview

`print_data.py` contains two main functions:

1. `print_project_details()`
2. `print_project_details_without_color()`

### print_project_details()

This function is responsible for printing a colorful, detailed 
summary of a project, including file contents, Doxygen warnings, 
and lines where the warnings occurred. It requires parameters like 
project folder path, header file names, warning numbers, warning 
contents, and line numbers. Optionally, it can take file contents as well.

### print_project_details_without_color()

Similar to `print_project_details()`, but this function prints 
the details without color codes.

## Example Usage

Here's how you can use these functions in your Python script:

```python
from print_data import print_project_details, print_project_details_without_color

# assuming these lists are populated with relevant data
project_folder_post_fix_path = "/path/to/project"
header_file_name_post_fix_list = ["header1.h", "header2.h"]
warning_num_post_fix_list = [5, 0]
warning_content_post_fix_llist = [["warning 1", "warning 2"], None]
warning_line_number_post_fix_llist = [[1, 2], None]
file_content_post_fix_list = ["file content 1", "file content 2"]

# Using print_project_details()
print_project_details(
    project_folder_post_fix_path,
    header_file_name_post_fix_list,
    warning_num_post_fix_list,
    warning_content_post_fix_llist,
    warning_line_number_post_fix_llist,
    "post",
    file_content_post_fix_list
)

# Using print_project_details_without_color()
print_project_details_without_color(
    project_folder_post_fix_path,
    header_file_name_post_fix_list,
    warning_num_post_fix_list,
    warning_content_post_fix_llist,
    warning_line_number_post_fix_llist,
    "post",
    file_content_post_fix_list
)
```

In the above examples, we are printing the details of a 
hypothetical project. The results will include details 
like file contents, Doxygen warnings, and lines where 
the warnings occurred, both with and without color coding.