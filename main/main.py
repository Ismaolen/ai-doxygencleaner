"""
This script is the main entry point of the Doxygen configuration process.
It creates and configures a Doxyfile according to the given configuration parameters and paths.
"""

from doxygen_config.config_paths import *
from doxygen_config.config_variables import *
from doxygen_management.doxyfile_configurator import DoxyfileConfigurator

if __name__ == '__main__':
    """
    Main execution block that will be executed if the script is run directly.
    It creates an instance of the DoxyfileConfigurator class and uses it to create and configure a Doxyfile.
    """

    # Instantiate the Doxyfile configurator
    configurator = DoxyfileConfigurator()

    # Create the Doxyfile in the specified directory using the provided command
    configurator.create_doxyfile(DOXYFILE_DIRECTORY_PATH, "doxygen -g")

    # Configure the Doxyfile using the provided configuration parameters
    configurator.configure_doxyfile(DOXYFILE_PATH, dox_config_parameters)
