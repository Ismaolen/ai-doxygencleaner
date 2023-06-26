import sys


class ErrorHandler(object):
    """
    A class used to handle common errors that may occur during program execution

    ...

    Static methods
    -------
    handle_subprocess_error(e, custom_message):
        Handles subprocess errors by displaying the error message in a custom format and terminating the program
    handle_file_not_found_error(e, custom_message):
        Handles file not found errors by displaying the error message in a custom format and terminating the program
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
