import sys

from print_data.print_data import print_project_details_without_color


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
    find_line_numbers(filename: str, searched_text: str) -> int:
        Finds the line numbers of all the occurrences of a specific text in a file.

    redirect_print_to_file(self, project_folder_path, header_file_name_list,
                               warning_num_list, warning_content_llist,
                               warning_line_number_llist, file_content_list, pre_or_post,
                               output_file):
        Redirects the output of the `print_project_details_without_color` function to a specified file.

    """

    def read_file(self, filename: str):
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

    def write_file(self, filename: str, lines):
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

    def has_single_line(self, list: list):
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

    def find_line_numbers(self, filename: str, searched_text: str):
        """
        Finds the line numbers of all the occurrences of a specific text in a file.

        Parameters
        ----------
        filename : str
            The name of the file to be searched.
        searched_text : str
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
                if searched_text in line:
                    line_numbers.append(num)
        if self.has_single_line(line_numbers):
            return line_numbers[0]

    def redirect_print_to_file(self, project_folder_path, header_file_name_list: list,
                               warning_num_list: list, warning_content_llist: list,
                               warning_line_number_llist: list, file_content_list: list, pre_or_post,
                               output_file):
        """
        Redirects the output of the `print_project_details_without_color` function to a specified file.

        This function modifies the standard output (stdout) to a specified file,
        calls a function to print data without color, and then restores stdout to its original state.

        Parameters
        ----------
        project_folder_path : str
            The path of the project folder.
        header_file_name_list : list
            List of header file names.
        warning_num_list : list
            List of warning numbers.
        warning_content_llist : list
            List of warning content.
        warning_line_number_llist : list
            List of warning line numbers.
        file_content_list : list
            List of file content.
        pre_or_post : str
            String indicating whether it's pre or post data.
        output_file : str
            Path to the output file where print statements are to be redirected.

        """
        with open(output_file, 'w') as f:  # Open the output file in write mode
            original_stdout = sys.stdout  # Save the original stdout
            sys.stdout = f  # Redirect the stdout to the file

            # Call the function to print data without color
            print_project_details_without_color(project_folder_path, header_file_name_list,
                                                warning_num_list, warning_content_llist,
                                                warning_line_number_llist, pre_or_post, file_content_list)

            sys.stdout = original_stdout  # Restore the original stdout
