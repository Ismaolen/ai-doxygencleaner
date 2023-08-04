# README.md

---

# Database Operations Module

The Database Operations module contains Python and SQL scripts that handle the insertion, 
manipulation, and setup of data in a MySQL database. The primary purpose is to manage data 
related to Doxygen warnings, from capturing details about pipelines, projects, and header files, to 
inserting and updating warnings in the database.

## Structure

Here is the module's structure:

```
db_operations
├── README.md
├── __init__.py
├── data_manipulation
│   ├── README.md
│   ├── insert_procedures.sql
│   └── update_procedures.sql
├── db_insertion_handler.py
├── main.sql
└── setup
    ├── README.md
    ├── create_table.sql
    └── drop_tables_procedures.sql
```

## Description of Files

### [data_manipulation](./data_manipulation/README.md)

This directory contains SQL scripts used for manipulating data in the database. 
These scripts mainly include stored procedures for inserting and updating records in the database tables. 

- `insert_procedures.sql`: This script contains stored procedures for inserting records into the various tables for 
Doxygen warnings analysis.

- `update_procedures.sql`: This script includes stored procedures designed 
for updating records in the database tables.

[See More](./data_manipulation/README.md)

### [setup](./setup/README.md)

This directory contains the scripts necessary for setting up the database.

- `create_table.sql`: This script creates tables to analyze Doxygen warnings.

- `drop_tables_procedures.sql`: This script removes any existing stored procedures or tables to avoid naming conflicts.

[See More](./setup/README.md)

### [`db_insertion_handler.py`](./db_insertion_handler.py)

The `db_insertion_handler.py` is a Python class designed to manage connections to a MySQL 
database and provide methods for inserting information related to Doxygen warnings, 
such as pipeline, project, and warnings details. 

This script contains the `DBInsertionHandler` class with the following methods:

- `connect_to_database()`: Connects to the MySQL database using environment variables.
- `create_cursor()`: Creates a new cursor to execute database commands.
- `set_pipeline_data()`: Sets pipeline data by getting information from environment variables.
- `update_last_project_id()`: Updates the `last_project_id` member variable with the most recent project ID.
- `update_last_header_file_id()`: Updates the `last_header_file_id` member variable with the most recent header file ID.
- `execute_sql(sql: str, values: tuple, optional)`: Executes a SQL command.
- `insert_into_pipeline_table()`: Inserts pipeline details into the pipeline table.
- `insert_into_project_table(project_folder_path: str)`: Inserts project details into the project table.
- `insert_into_header_file_table(file_name: str, file_content: str, 
number_of_warnings: int)`: Inserts header file details into the header file table.
- `insert_into_warning_table_pre_fix(warning_content: str, line_number_pre_fix: 
int, fixed_status: int = FIXED_STATUS_DEFAULT)`: Inserts warning details into the warning table.
- `insert_warnings_details(project_folder_path: str, file_name_list: list, 
file_content_list: list, number_of_warnings_list: list, warning_content_llist: list, line_number_pre_fix_llist: list)`: 
Wrapper function that inserts pipeline, project, 
header file, and warning details into their respective tables.
- `update_post_fix_warning_details(self, pipeline_id, file_name_list, 
file_content_list, line_number_llist, warnings_content_llist)`: 
Update the database with the details of post-fix warnings.

### `main.sql`

The `main.sql` file is the main SQL script file that integrates and runs 
the SQL procedures defined in the `data_manipulation` and `setup` folders.

## How to Use

To use this module:

1. Ensure that the appropriate environment variables are set in your environment before 
running any scripts, particularly those related to database access.

2. Run the setup scripts first to set up the required tables in your database.

3. Use the Python class `DBInsertionHandler` in your Python scripts to insert or update data in the database.

4. The data manipulation scripts can be imported into your preferred SQL client and executed as needed.

## Contributions

Contributions are welcome. If you find any bugs or issues, or if you want to enhance any functionality, 
feel free to contribute. Remember to follow the standard Python and SQL style guidelines and avoid committing 
sensitive information like API keys or database credentials.

**Note:** Ensure that you have the necessary permissions and clearances before accessing or manipulating any data.
