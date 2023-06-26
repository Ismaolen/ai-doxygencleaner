import sys


class FileHandler(object):
    """
    A class used to handle file operations.

    ...

    Methods
    -------
    read_file(filename: str) -> list:
        Reads a file and returns its contents as a list of lines.
    write_file(filename: str, lines: list):
        Writes a list of lines into a file.
    has_single_line(list: list) -> bool:
        Checks if a list has only a single line.
    find_line_numbers(filename: str, searchText: str) -> int:
        Finds the line numbers of all the occurrences of a specific text in a file.
    """

    def read_file(self, filename):
        """
        Reads a file and returns its contents as a list of lines.

        Parameters
        ----------
        filename : str
            The name of the file to be read.

        Returns
        -------
        list
            A list of lines from the file.
        """
        lines = [line for line in open(filename, 'r').readlines()]
        return lines

    def write_file(self, filename, lines):
        """
        Writes a list of lines into a file.

        Parameters
        ----------
        filename : str
            The name of the file to write to.
        lines : list
            A list containing the lines to be written to the file.
        """
        with open(filename, 'w') as file:
            file.writelines(lines)

    def has_single_line(self, list):
        """
        Checks if a list has only a single line.

        Parameters
        ----------
        list : list
            The list to check.

        Returns
        -------
        bool
            True if the list has only a single line, else it exits the program.
        """
        if len(list) == 1:
            return True
        else:
            return sys.exit("Error: More than one line detected.")

    def find_line_numbers(self, filename, searchText):
        """
        Finds the line numbers of all the occurrences of a specific text in a file.

        Parameters
        ----------
        filename : str
            The name of the file to be searched.
        searchText : str
            The text to be found.

        Returns
        -------
        int
            The line number of the first occurrence of the search text
            if there is only one occurrence, else it exits the program.
        """
        line_numbers = []
        with open(filename, 'r') as file:
            for num, line in enumerate(file, 1):
                if searchText in line:
                    line_numbers.append(num)
        if self.has_single_line(line_numbers):
            return line_numbers[0]
