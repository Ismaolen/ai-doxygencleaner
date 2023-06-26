import argparse
import openai
import os
import subprocess
import sys

from doxygen_management.file_handler import FileHandler
from doxygen_config.config_paths import *
from error_handler.error_handler import ErrorHandler


class DoxyfileConfigurator(object):
    """
    A class used to configure a Doxyfile.

    ...

    Attributes
    ----------
    file_handler : FileHandler
        an instance of the FileHandler class used to manipulate files

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
        self.file_handler = FileHandler()

    def create_doxyfile(self, directory_path, cmd):
        """
        Tries to create a Doxyfile at the given directory path, using the provided command.

        Parameters
        ----------
        directory_path : str
            The path of the directory where the Doxyfile will be created
        cmd : str
            The command used to create the Doxyfile

        Raises
        ------
        subprocess.CalledProcessError
            If there is an error while executing the command
        FileNotFoundError
            If the directory path does not exist
        """
        try:
            subprocess.run(cmd, shell=True, check=True, cwd=directory_path, stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL)
            print("\033[92m" + "\nDoxyfile was successfully created.\n" + "\033[0m")  # Green text
        except subprocess.CalledProcessError as e:
            ErrorHandler.handle_subprocess_error(e, "Error while executing the command: ")
        except FileNotFoundError as e:
            ErrorHandler.handle_file_not_found_error(e, "Error while creating the Doxyfile: ")

    def add_spaces_to_string(self, config_parameters):
        """
        Adds specific spaces to configuration parameters.

        Parameters
        ----------
        config_parameters : list
            A list of configuration parameters to which spaces are added

        Returns
        -------
        list
            A list of configuration parameters with added spaces
        """
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
        folders = [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]

        if len(folders) == 1:
            return True, folders[0]
        else:
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
        config_parameters = self.add_spaces_to_string(config_parameters)
        lines = self.file_handler.read_file(filename)
        for i in config_parameters:
            line_num = self.file_handler.find_line_numbers(DOXYFILE_PATH, i)
            if "INPUT" and "LATEX" not in i:
                lines[line_num - 1] = i + " YES" + "\n"
            if "LATEX" in i:
                lines[line_num - 1] = i + " NO" + "\n"
            if "INPUT" in i:
                exists_single_folder, folder_name = self.get_single_subfolder(PROJECT_DIRECTORY_PATH)
                if not exists_single_folder:
                    return sys.exit("\033[91m" + "Error: Multiple subfolders detected." + "\033[0m")

                else:
                    lines[line_num - 1] = i + " " + "../" + PROJECT_DIRECTORY_PATH + "/" + folder_name + "\n"
            print(line_num)
            print(lines[line_num - 1])
        self.file_handler.write_file(filename, lines)
