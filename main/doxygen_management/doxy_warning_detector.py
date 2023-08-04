import subprocess
import sys

from config.config_paths import DOXYFILE_PATH, PROJECT_DIRECTORY_PATH, DOXYFILE_DIRECTORY_PATH
from doxygen_management.doxyfile_configurator import DoxyfileConfigurator
from doxygen_management.file_handler import FileHandler


class DoxyWarningDetector(DoxyfileConfigurator):
    """
    A class used to detect warnings in Doxygen documentation generation.

    ...

    Attributes
    ----------
    warnings_list : list
        a list to hold the detected warnings (initialized as an empty list)

    Methods
    -------
    check_project_directory():
        Checks the project directory for the existence of a single subfolder.

    get_all_header_files(project_folder_path: str):
        Gets all the header files in the given project folder path.

    run_doxygen_for_file(header_file_name: str, lines: list, input_line: str, project_folder_path: str, line_num: int):
        Runs Doxygen for the given header file.

    extract_warnings(result: subprocess.CompletedProcess):
        Extracts warnings from the result of a Doxygen run.

    run_doxygen():
        Executes the complete process to run Doxygen for all header files and extract warnings.
    """

    def __init__(self):
        """Initializes DoxyWarningDetector with a DoxyfileConfigurator and a FileHandler."""
        self.warnings_list = []
        DoxyfileConfigurator.__init__(self)

    def check_project_directory(self):
        """
        Checks if there is only one subfolder in the project directory.
        If there are multiple subfolders, the program exits with an error message.
        Returns the name of the single subfolder if it exists.

        Returns
        -------
        str
            the name of the single subfolder
        """
        # Check if there is only one subfolder in the project directory
        exists_single_folder, folder_name = self.get_single_subfolder(PROJECT_DIRECTORY_PATH)
        if not exists_single_folder:
            # Exit the program if multiple subfolders are detected
            return sys.exit("\033[91m" + "Error: Multiple subfolders detected." + "\033[0m")
        else:
            # Return the name of the single subfolder
            return folder_name

    def get_all_header_files(self, project_folder_path):
        """
        Gets all the header files in the project directory.
        If there are no header files, the program exits with an error message.
        Returns the list of header files if they exist.

        Parameters
        ----------
        project_folder_path: str
            The path to the project directory

        Returns
        -------
        list
            A list of all header files in the project directory.
        """
        # Get all the header files in the project directory
        exists_header_files, header_files = self.get_header_files(project_folder_path)
        if not exists_header_files:
            # Exit the program if no header files are found
            Error_Massage = "Error: No header files found ending with .h or .hpp"
            return sys.exit("\033[91m" + Error_Massage + "\033[0m")
        else:
            # Return the list of header files
            return header_files

    def run_doxygen_for_file(self, header_file_name, lines: list, input_line, project_folder_path, line_num):
        """
        Prepares the Doxyfile with the given parameters and runs Doxygen for the header file.
        Returns the result of the Doxygen run.

        Parameters
        ----------
        header_file_name: str
            The name of the header file
        lines: list
            A list of lines in the Doxyfile
        input_line: str
            The line to add to the Doxyfile
        project_folder_path: str
            The path to the project directory
        line_num: int
            The line number in the Doxyfile to modify

        Returns
        -------
        subprocess.CompletedProcess
            The result of the Doxygen run
        """
        # Prepare the input line for doxygen
        lines[line_num - 1] = input_line + " " + "../" + project_folder_path + "/" + header_file_name + "\n"
        # Write the modified lines to the Doxyfile
        self.write_file(DOXYFILE_PATH, lines)
        # Prepare the command to run doxygen
        cmd = "doxygen Doxyfile 2>&1 | grep warning"
        # Run the doxygen command and capture the output
        result = subprocess.run(cmd, shell=True, check=False, cwd=DOXYFILE_DIRECTORY_PATH, capture_output=True,
                                text=True)
        # Return the result of running doxygen
        return result

    def extract_warnings(self, result):
        """
        Extracts warnings from the result of a Doxygen run.
        Returns the extracted warnings.

        Parameters
        ----------
        result: subprocess.CompletedProcess
            The result of the Doxygen run

        Returns
        -------
        list, list, int
            Lists of warning contents, warning line numbers and total number of warnings.
        """
        # Split the output by newlines to get individual lines
        lines = result.stdout.split('\n')

        # Initialize an empty list to store the warnings
        warnings = []
        warnings_line_number = []

        # Loop over each line
        for line in lines:
            # Check if the line is not just whitespace
            if line.strip():
                # Split the line at colons and rejoin from the second element, then add to the list
                warnings.append(":".join(line.split(":")[2:]).strip())
                warnings_line_number.append(line.split(":")[1])
        return warnings, warnings_line_number, len(warnings)

    def run_doxygen(self):
        """
        Executes the complete process to run Doxygen for all header files and extract warnings.
        The process includes preparing the Doxyfile, running Doxygen, and extracting warnings.
        Returns a list of results containing the header file name, project folder path, file content, and warnings.

        Returns
        -------
        tuple
            The result of running doxygen and extracting warnings. It includes the project folder path,
            list of header file names, list of file contents, list of warning counts,
            list of warning contents, and list of warning line numbers.
        """
        # Prepare the input line for the Doxyfile
        input_line = "INPUT{}=".format(" " * 18)
        # Find the line number for the input line in the Doxyfile
        line_num = self.find_line_numbers(DOXYFILE_PATH, input_line)
        # Read the contents of the Doxyfile
        lines = self.read_file(DOXYFILE_PATH)
        # Check the project directory and get the folder name
        folder_name = self.check_project_directory()
        # Prepare the path to the project folder
        project_folder_path = PROJECT_DIRECTORY_PATH + "/" + folder_name
        # Get the list of all header files in the project directory
        header_files = self.get_all_header_files(project_folder_path)
        header_file_name_list = []
        file_content_list = []
        warning_num_list = []
        warning_content_llist = []
        warning_line_number_llist = []
        for header_file_name in header_files:
            # Run doxygen for each header file
            result = self.run_doxygen_for_file(header_file_name, lines, input_line, project_folder_path, line_num)
            # If there is no output, skip the rest of the loop for this iteration
            if not result.stdout.strip():
                continue

            # Extract warnings from the doxygen output
            warnings, warnings_line_number, warnings_num = self.extract_warnings(result)
            # Read the contents of the header file
            with open(project_folder_path + "/" + header_file_name, 'r') as file:
                file_content = file.read()
            header_file_name_list.append(header_file_name)
            file_content_list.append(file_content)
            warning_num_list.append(warnings_num)
            warning_content_llist.append(warnings)
            warning_line_number_llist.append(warnings_line_number)

        # Return the list of results
        return project_folder_path, header_file_name_list, file_content_list, warning_num_list, \
            warning_content_llist, warning_line_number_llist
