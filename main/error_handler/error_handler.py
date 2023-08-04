import inspect
import sys


class ErrorHandler:
    """
    A class used to handle common errors that may occur during program execution

    ...

    Static methods
    --------------
    handle_subprocess_error(e, custom_message):
        Handles subprocess errors by displaying the error message in a custom format and terminating the program
    handle_file_not_found_error(e, custom_message):
        Handles file not found errors by displaying the error message in a custom format and terminating the program
    execute_sql(cursor, sql, values=None):
    """

    @staticmethod
    def handle_subprocess_error(e, custom_message):
        """
        Handles subprocess errors by displaying the error message in a custom format and terminating the program

        Parameters
        ----------
        e : Exception
            The exception raised
        custom_message : str
            The custom message to be displayed before the exception message
        """
        print("\033[91m" + custom_message + "\033[0m")  # Red text
        print("\033[93m" + str(e) + "\033[0m")  # Yellow text
        sys.exit(1)

    @staticmethod
    def handle_file_not_found_error(e, custom_message):
        """
        Handles file not found errors by displaying the error message in a custom format and terminating the program

        Parameters
        ----------
        e : Exception
            The exception raised
        custom_message : str
            The custom message to be displayed before the exception message
        """
        print("\033[91m" + custom_message + "\033[0m")  # Red text
        print("\033[93m" + str(e) + "\033[0m")  # Yellow text
        sys.exit(1)

    @staticmethod
    def execute_sql(cursor, sql, values=None):
        """
        Executes a SQL command.

        Parameters
        ----------
        cursor : Database Cursor
            The cursor object from a database connection which is used to execute the SQL query.
        sql : str
            The SQL command to be executed.
        values : tuple, optional
            The values to be inserted into the SQL command (default is None).

        Raises
        ------
        Exception
            If there is an error while executing the SQL command.
        """
        try:
            if values is not None:
                cursor.execute(sql, values)
            else:
                cursor.execute(sql)
            # self.db.commit()
        except Exception as e:
            current_frame = inspect.currentframe()
            calling_frame = inspect.getouterframes(current_frame, 2)
            caller_name = calling_frame[1][3]  # get the name of the calling function
            line_number = calling_frame[1][2]  # get the line number of the calling function
            file_name = calling_frame[1][1]
            ErrorHandler.handle_subprocess_error(e, f"Error while executing the command:\n"
                                                    f"Error occurred:\n"
                                                    f"\t\t\t\tIn Function: {caller_name}\n"
                                                    f"\t\t\t\tAt Line: {line_number}\n"
                                                    f"\t\t\t\tIn File: {file_name}\n"
                                                    f"Error message:")
