import os
import subprocess

from doxygen_management.file_handler import FileHandler
from config.config_paths import *
from error_handler.error_handler import ErrorHandler


class DoxyfileConfigurator(FileHandler):
    """
    A class used to configure a Doxyfile.

    ...

    Methods
    -------
    create_doxyfile(directory_path, cmd):
        Tries to create a Doxyfile at the given directory path, using the provided command
    add_spaces_to_string(config_parameters):
        Adds specific spaces to configuration parameters
    get_single_subfolder(directory):
        Checks if there is only one subfolder in a given directory
    configure_doxyfile(filename, config_parameters):
        Configures the Doxyfile with the given parameters
    """

    def __init__(self):
        """Initializes an instance of the DoxyfileConfigurator class."""
        FileHandler.__init__(self)
        self.error_handler = ErrorHandler()

    def remove_doxyfile_if_exists(self, directory_path):
        """
        Method to remove a Doxyfile at the given directory path.

        Parameters
        ----------
        directory_path : str
            The path of the directory where the Doxyfile will be removed

        Raises
        ------
        subprocess.CalledProcessError
            If there is an error while executing the command
        FileNotFoundError
            If the directory path does not exist
        """
        cmd = "rm -f Doxyfile"  # Command to remove Doxyfile
        # Execute command to remove Doxyfile using subprocess.run method
        try:
            subprocess.run(cmd, shell=True, check=True, cwd=directory_path, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            self.error_handler.handle_subprocess_error(e, "Error while executing the command: ")

    def create_doxyfile(self, directory_path):
        """
        Method to create a Doxyfile at the given directory path, using the provided command.

        Parameters
        ----------
        directory_path : str
            The path of the directory where the Doxyfile will be created

        Raises
        ------
        subprocess.CalledProcessError
            If there is an error while executing the command
        FileNotFoundError
            If the directory path does not exist
        """
        cmd = "doxygen -g"  # Command to generate a new Doxyfile
        # Execute command to create a new Doxyfile using subprocess.run method
        try:
            subprocess.run(cmd, shell=True, check=True, cwd=directory_path, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            print("\033[94m" + "\n>> Doxyfile was successfully created.\n" + "\033[0m")  # Green text
        except subprocess.CalledProcessError as e:
            self.error_handler.handle_subprocess_error(e, "Error while executing the command: ")
        except FileNotFoundError as e:
            self.error_handler.handle_file_not_found_error(e, "Error while creating the Doxyfile: ")

    def add_spaces_to_string(self, config_parameters):
        """
        Method to adds specific spaces to configuration parameters.

        Parameters
        ----------
        config_parameters : list
            A list of configuration parameters to which spaces are added

        Returns
        -------
        list
            A list of configuration parameters with added spaces
        """
        # Formatting each parameter by adding specific number of spaces
        string_with_spaces = [param[0].format(" " * param[1]) for param in config_parameters]
        return string_with_spaces

    def get_single_subfolder(self, directory):
        """
        Checks if there is only one subfolder in a given directory.

        Parameters
        ----------
        directory : str
            The directory to check for subfolders

        Returns
        -------
        bool
            A boolean value indicating the presence of a single subfolder
        str
            The name of the subfolder (if any)
        """
        # List comprehension to get all the subdirectories in the directory
        folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

        # If there is only one folder, return True and the folder name
        if len(folders) == 1:
            return True, folders[0]
        else:  # If there is more than one folder, return False and None
            return False, None

    def get_header_files(self, directory):
        """
        Returns a list of .h and .hpp files in the given directory.

        Parameters
        ----------
        directory : str
            The directory to search

        Returns
        -------
        list
            A list of .h and .hpp file paths
        """
        # List comprehension to get all the files in the directory
        files = os.listdir(directory)
        # Filter out only .h and .hpp files
        header_files = [file for file in files if os.path.splitext(file)[1] in ['.h', '.hpp']]
        if len(header_files) > 0:  # If there are header files, return True and the list of files
            return True, header_files
        else:  # If there are no header files, return False and None
            return False, None

    def configure_doxyfile(self, filename, config_parameters):
        """
        Configures the Doxyfile with the given parameters.

        Parameters
        ----------
        filename : str
            The name of the file to be configured
        config_parameters : list
            A list of configuration parameters

        It modifies the lines in the Doxyfile according to the provided configuration parameters.
        """
        # Add spaces to the configuration parameters
        config_parameters = self.add_spaces_to_string(config_parameters)
        # Read all the lines in the Doxyfile
        lines = list(self.read_file(filename))
        print(f"\033[1;94m>> Modifying "
              f"\033[1;4;91mDoxyfile\033[0m"
              f"\033[1;94m with the specified parameters from the configuration file.\033[0m\n")
        for i in config_parameters:  # Loop through each configuration parameter
            line_num = self.find_line_numbers(DOXYFILE_PATH, i)
            if "LATEX" not in i:  # If the parameter is not related to LATEX
                lines[line_num - 1] = i + " YES" + "\n"  # Set the parameter to YES
            if "LATEX" in i:  # If the parameter is related to LATEX
                lines[line_num - 1] = i + " NO" + "\n"  # Set the parameter to NO
            # Print the modified line number and the new value
            print(f'\033[1;33m\t>>> Modified Line at Position: \033[0m'
                  f'\033[4;33m{line_num}\033[0m, '
                  f'\033[1;32mNew Value: {lines[line_num - 1].strip()}\033[0m')
        # Write the modified lines back to the Doxyfile
        self.write_file(filename, lines)
