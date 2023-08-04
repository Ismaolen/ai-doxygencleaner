# ErrorHandler Module

The `error_handler` module is part of the `ai_doxygen_cleaner` package. It contains the 
`ErrorHandler` class which provides methods for handling common errors that may occur 
during program execution. It's a key tool for error handling and debugging in the system.

## Structure

The `error_handler` folder contains the following files:

- `__init__.py`: This is an initialization file for the module.
- `error_handler.py`: This is the main script of the module that contains the `ErrorHandler` class.

## ErrorHandler Class

The `ErrorHandler` class provides static methods to handle common types of errors. 
Specifically, it deals with subprocess errors, file not found errors, and SQL execution errors.

### Static Methods

The class offers the following static methods:

#### handle_subprocess_error(e, custom_message)

This method handles subprocess errors by displaying a custom error message 
and terminating the program.

Parameters:
- `e` (Exception): The exception raised
- `custom_message` (str): The custom message to be displayed before the 
exception message

Example usage:
```python
try:
    # some code that may raise a subprocess error
except Exception as e:
    ErrorHandler.handle_subprocess_error(e, "A subprocess error occurred.")
```

#### handle_file_not_found_error(e, custom_message)

This method handles file not found errors by displaying 
a custom error message and terminating the program.

Parameters:
- `e` (Exception): The exception raised
- `custom_message` (str): The custom message to be 
displayed before the exception message

Example usage:
```python
try:
    # some code that may raise a FileNotFoundError
except Exception as e:
    ErrorHandler.handle_file_not_found_error(e, "A file not found error occurred.")
```

#### execute_sql(cursor, sql, values=None)

This method executes a SQL command. If an error occurs 
during the execution, it calls `handle_subprocess_error` to handle it.

Parameters:
- `cursor` (Cursor): The cursor to execute the SQL command
- `sql` (str): The SQL command to be executed
- `values` (tuple, optional): The values to be inserted 
into the SQL command. Defaults to None.

Example usage:
```python
sql = "SELECT * FROM some_table"
try:
    ErrorHandler.execute_sql(cursor, sql)
except Exception as e:
    ErrorHandler.handle_subprocess_error(e, "An error occurred while executing SQL command.")
```
Note: Error messages are printed in different colors (red for 
custom error messages and yellow for exception messages) 
to enhance readability and assist debugging.

## Conclusion

The `error_handler` module is a helpful tool for managing and 
debugging common errors within the `ai_doxygen_cleaner` package. 
By providing informative error messages and terminating the program 
when necessary, it helps to prevent silent failures and facilitates troubleshooting.