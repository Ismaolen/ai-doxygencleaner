from datetime import datetime

from DoxygenWarningFixer.doxygen_warning_fixer import DoxygenWarningFixer
from db_operations.db_insertion_handler import DBInsertionHandler
from doxy_warning_post_processor.doxy_warning_post_processor import WarningPostProcessor
from print_data.print_data import print_project_details
from transport_data.transport_data import save_data_to_json, \
    load_data_from_json, load_pre_fix_data_from_json, \
    load_post_fix_data_from_json

from config.config_paths import *
from config.config_variables import *

from utils.utils import perform_diff_on_files, generate_html_diff, rename_and_move


class AIDoxygenCleaner(WarningPostProcessor, DBInsertionHandler, DoxygenWarningFixer):
    """
    This class is responsible for managing the Doxygen warnings, it consists of several methods
    for configuring Doxygen, detecting warnings, fixing them, saving the fixed warnings and
    printing warning details to a file.

    ...

    Methods
    -------
    doxygen_configuration():
        Configures Doxygen.

    detect_warnings_pre_fix():
        Detects warnings before fixing.

    insert_warnings_to_db():
        Inserts detected warnings into the database.

    fix_doxygen_warning():
        Fixes detected Doxygen warnings.

    apply_fix():
        Applies the fix to the Doxygen warnings.

    detect_warnings_post_fix():
        Detects any remaining warnings after applying the fix.

    print_pre_post_fix_data_to_file():
        Prints warning details to a file before and after the fix.

    generate_html_diff_page():
        Generates an HTML diff page to show differences before and after the fix.
    update_warnings_details_post_fix_in_db():
        Update warning details in the database after applying fixes.
    """

    def __init__(self):
        """
        Initialize the AIDoxygenCleaner object.
        """
        WarningPostProcessor.__init__(self)
        DBInsertionHandler.__init__(self)
        DoxygenWarningFixer.__init__(self)
        pass

    def doxygen_configuration(self):
        """
        Configures Doxygen.

        This method is responsible for configuring Doxygen.
        It removes any existing Doxyfile in the directory and creates a new one.
        The new Doxyfile is then configured using provided parameters.

        The entire process is printed in the console for visibility.
        """
        # Start of Phase 1 - Doxygen Configuration
        print("\n\033[1;96m==============================\033[0m"
              "\033[1;94m PHASE NUMBER 1 \033[0m"
              "\033[1;96m===============================\033[0m")
        print(
            "\n\n\033[1;35m====================\033[0m"
            "\033[1;32m BEGINNING OF DOXYFILE CONFIGURATION \033[0m"
            "\033[1;35m====================\033[0m\n\n")

        # Remove any existing Doxyfile in the directory
        self.remove_doxyfile_if_exists(DOXYFILE_DIRECTORY_PATH)

        # Create a new Doxyfile in the directory
        self.create_doxyfile(DOXYFILE_DIRECTORY_PATH)

        # Configure the newly created Doxyfile using the given parameters
        self.configure_doxyfile(DOXYFILE_PATH, dox_config_parameters)

        # End of Doxyfile Configuration
        print(
            "\n\n\033[1;35m=======================\033[0m"
            "\033[1;32m END OF DOXYFILE CONFIGURATION \033[0m"
            "\033[1;35m=======================\033[0m\n\n")

    def detect_warnings_pre_fix(self):
        """
        This method is responsible for detecting Doxygen warnings before any fixes are applied.
        It stores the warning data and saves it in a JSON file for further processing.

        The entire process is printed in the console for visibility.
        """

        # Start of Phase 2 - Doxygen Warning Detection (Pre Fix)
        print("\n\033[1;96m================================\033[0m"
              "\033[1;94m PHASE NUMBER 2 \033[0m"
              "\033[1;96m=================================\033[0m")
        print("\n\n\033[1;35m================\033[0m"
              "\033[1;32m BEGINNING OF DOXYGEN-WARNING DETECTION (PRE FIX) \033[0m"
              "\033[1;35m===============\033[0m\n\n")

        # Create an instance of the DoxyWarningDetector class
        # detect_warning = DoxyWarningDetector()

        # Execute the Doxygen command and retrieve the warnings
        project_folder_pre_fix_path, header_file_name_pre_fix_list, file_content_pre_fix_list, \
            warning_num_pre_fix_list, \
            warning_content_pre_fix_llist, warning_line_number_pre_fix_llist = self.run_doxygen()

        # Print the data for visibility
        print_project_details(project_folder_pre_fix_path, header_file_name_pre_fix_list,
                              warning_num_pre_fix_list, warning_content_pre_fix_llist,
                              warning_line_number_pre_fix_llist, 'Pre')

        # Store the data in a dictionary for later use
        data = {
            "project_folder_pre_fix_path": project_folder_pre_fix_path,
            "header_file_name_pre_fix_list": header_file_name_pre_fix_list,
            "file_content_pre_fix_list": file_content_pre_fix_list,
            "warning_num_pre_fix_list": warning_num_pre_fix_list,
            "warning_content_pre_fix_llist": warning_content_pre_fix_llist,
            "warning_line_number_pre_fix_llist": warning_line_number_pre_fix_llist,
        }

        # Convert warnings-data-pre-fix into a dictionary and save the dictionary in a JSON file
        save_data_to_json("transport_data/preprocessed_warnings_data.json", data)

        # End of Doxygen Warning Detection (Pre Fix)
        print("\n\n\033[1;35m===================\033[0m"
              "\033[1;32m END OF DOXYGEN-WARNING DETECTION (PRE FIX) \033[0m"
              "\033[1;35m==================\033[0m\n\n")

    def insert_warnings_to_db(self):
        """
        Inserts detected warnings into the database.

        Prints the phase and step of the process.
        Insert details of the warnings into the database.
        """
        print("\n\033[1;96m================================\033[0m"
              "\033[1;94m PHASE NUMBER 3 \033[0m"
              "\033[1;96m=================================\033[0m")
        print("\n\n\033[1;35m=============\033[0m"
              "\033[1;32m BEGINNING OF WARNING INSERTION INTO DATABASE (PRE FIX) \033[0m"
              "\033[1;35m============\033[0m\n\n")

        # Load the dictionary from the JSON file
        data = load_data_from_json("transport_data/preprocessed_warnings_data.json")
        # Extract data from the dictionary
        project_folder_pre_fix_path = data["project_folder_pre_fix_path"]
        header_file_name_pre_fix_list = data["header_file_name_pre_fix_list"]
        file_content_pre_fix_list = data["file_content_pre_fix_list"]
        warning_num_pre_fix_list = data["warning_num_pre_fix_list"]
        warning_content_pre_fix_llist = data["warning_content_pre_fix_llist"]
        warning_line_number_pre_fix_llist = data["warning_line_number_pre_fix_llist"]

        # data_base_handler = DBInsertionHandler()
        self.insert_warnings_details \
            (project_folder_pre_fix_path, header_file_name_pre_fix_list, file_content_pre_fix_list,
             warning_num_pre_fix_list, warning_content_pre_fix_llist, warning_line_number_pre_fix_llist)
        print("\n\033[1;35m-------------------------------------------------------------------------------\033[0m\n")
        print(f"\033[1;92m{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -"
              f" Doxygen warnings successfully inserted into the database.\033[0m")
        print("\033[1;35m===============================================================================\033[0m\n")
        print("\n\n\033[1;35m================\033[0m"
              "\033[1;32m END OF WARNING INSERTION INTO DATABASE (PRE FIX) \033[0m"
              "\033[1;35m===============\033[0m\n\n")

    def fix_doxygen_warning(self):
        """
        Fixes detected Doxygen warnings.

        Prints the phase and step of the process.
        Runs the fixer to fix the warnings.
        """
        print("\n\033[1;96m================================\033[0m"
              "\033[1;94m PHASE NUMBER 4 \033[0m"
              "\033[1;96m==============================\033[0m")
        print("\n\n\033[1;35m=======================\033[0m"
              "\033[1;32m BEGINNING OF DOXYGEN-WARNING FIXING \033[0m"
              "\033[1;35m==================\033[0m\n\n")
        # fixer = DoxygenWarningFixer()
        self.run()
        print("\n\n\033[1;35m==========================\033[0m"
              "\033[1;32m END OF DOXYGEN-WARNING FIXING \033[0m"
              "\033[1;35m=====================\033[0m\n\n")

    def _apply_fix(self):
        """
        Applies the fix to the Doxygen warnings.

        Prints the phase and step of the process.
        Applies the suggested responses from the AI language model to the header files.
        """
        print("\n\033[1;96m================================\033[0m"
              "\033[1;94m PHASE NUMBER 5 \033[0m"
              "\033[1;96m==============================\033[0m")
        print("\n\n\033[1;35m===============\033[0m"
              "\033[1;32m BEGINNING OF DOXYGEN-WARNING FIX APPLICATION \033[0m"
              "\033[1;35m============\033[0m\n\n")
        # WarningPostProcessor()
        self.apply_fix()
        print("\n\033[1;35m-------------------------------------------------------------------------------\033[0m\n")
        print(f"\033[1;92m{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -"
              f"Successfully updated the header files in the doxygen_projects folder with the suggested responses "
              f"from the AI language model.\033[0m")
        print("\033[1;35m===============================================================================\033[0m\n")
        print("\n\n\033[1;35m=================\033[0m"
              "\033[1;32m END OF DOXYGEN-WARNING FIX APPLICATION \033[0m"
              "\033[1;35m================\033[0m\n\n")

    def detect_warnings_post_fix(self):
        """
        Detects Doxygen warnings after applying the fix.

        Prints the phase and step of the process.
        Runs the warning post processor to detect any remaining warnings.
        """

        print("\n\033[1;96m================================\033[0m"
              "\033[1;94m PHASE NUMBER 6 \033[0m"
              "\033[1;96m==============================\033[0m")
        print("\n\n\033[1;35m===============\033[0m"
              "\033[1;32m BEGINNING OF DOXYGEN-WARNING DETECTION (POST FIX) \033[0m"
              "\033[1;35m============\033[0m\n\n")
        # WarningPostProcessor()
        self.detect_warning()
        print("\n\n\033[1;35m=================\033[0m"
              "\033[1;32m END OF DOXYGEN-WARNING DETECTION (POST FIX) \033[0m"
              "\033[1;35m================\033[0m\n\n")

    def print_pre_post_fix_data_to_file(self):
        """
        Prints warning details to a file before and after the fix.

        Prints the phase and step of the process.
        Loads warning details from JSON files and redirects the print to output files.
        """
        print("\n\033[1;96m================================\033[0m"
              "\033[1;94m PHASE NUMBER 7 \033[0m"
              "\033[1;96m=================================\033[0m")
        print("\n\n\033[1;35m=================\033[0m"
              "\033[1;32m BEGINNING OF PRINTING WARNING DETAILS TO FILE \033[0m"
              "\033[1;35m=================\033[0m\n\n")
        # Open the file
        # Load warning details from preprocessed_warnings_data.json

        # file_handler = FileHandler()

        (project_folder_pre_fix_path, header_file_name_pre_fix_list, file_content_pre_fix_list,
         warning_num_pre_fix_list, warning_content_pre_fix_llist,
         warning_line_number_pre_fix_llist) = load_pre_fix_data_from_json()

        pre_or_post_fix = 'Pre'
        output_file_pre_fix = 'data/different_between_pre_and_post/output_pre_fix.cpp'
        self.redirect_print_to_file(project_folder_pre_fix_path, header_file_name_pre_fix_list,
                                    warning_num_pre_fix_list, warning_content_pre_fix_llist,
                                    warning_line_number_pre_fix_llist, file_content_pre_fix_list,
                                    pre_or_post_fix,
                                    output_file_pre_fix)

        # Open the file
        # Load warning details from postprocessed_warnings_data.json
        (project_folder_post_fix_path, header_file_name_post_fix_list, file_content_post_fix_list,
         warning_num_post_fix_list, warning_content_post_fix_llist,
         warning_line_number_post_fix_llist) = load_post_fix_data_from_json()

        pre_or_post_fix = 'Post'
        output_file_post_fix = 'data/different_between_pre_and_post/output_post_fix.cpp'
        self.redirect_print_to_file(project_folder_post_fix_path, header_file_name_post_fix_list,
                                    warning_num_post_fix_list, warning_content_post_fix_llist,
                                    warning_line_number_post_fix_llist, file_content_post_fix_list,
                                    pre_or_post_fix,
                                    output_file_post_fix)

        print("\n\n\033[1;35m===================\033[0m"
              "\033[1;32m END OF PRINTING WARNING DETAILS TO FILE \033[0m"
              "\033[1;35m=====================\033[0m\n\n")

    def generate_html_diff_page(self):
        """
        Prints warning details to a file before and after the fix.

        Prints the phase and step of the process.
        Loads warning details from JSON files and redirects the print to output files.
        """
        print("\n\033[1;96m================================\033[0m"
              "\033[1;94m PHASE NUMBER 8 \033[0m"
              "\033[1;96m=================================\033[0m")
        print("\n\n\033[1;35m=================\033[0m"
              "\033[1;32m BEGINNING OF CREATING THE PRE AND POST FIX DIFF HTML PAGE \033[0m"
              "\033[1;35m=================\033[0m\n\n")
        perform_diff_on_files()
        generate_html_diff()
        rename_and_move('data/different_between_pre_and_post/', '../../implementation_doxygen/Tests/Test_diff_files')
        print("\n\033[1;35m-------------------------------------------------------------------------------\033[0m\n")
        print(f"\033[1;92m{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -"
              f" Successfully created an HTML page at the filepath \nmain/data/different_between_pre_and_post/diff.html "
              f"to display the differences \nbetween doxygen-warning-details before and after fixes applied by the AI "
              f"language model.\033[0m")
        print("\033[1;35m===============================================================================\033[0m\n")
        print("\n\n\033[1;35m===================\033[0m"
              "\033[1;32m END OF CREATING THE PRE AND POST FIX DIFF HTML PAGE \033[0m"
              "\033[1;35m=====================\033[0m\n\n")

    def update_warnings_details_post_fix_in_db(self):
        """
        Update warning details in the database after applying fixes.

        This method handles loading of the post fix data from JSON files, retrieving the pipeline ID and
        then updating the warning details in the database with the help of the DBInsertionHandler instance.

        Prints:
        -------
        Various status messages with timestamps indicating the start and end of the database update operation.
        """
        # Printing the phase number and start of the operation
        print("\n\033[1;96m================================\033[0m"
              "\033[1;94m PHASE NUMBER 9 \033[0m"
              "\033[1;96m=================================\033[0m")
        print("\n\n\033[1;35m=========\033[0m"
              "\033[1;32m BEGINNING OF UPDATING WARNING DETAILS IN DATABASE (POST FIX) \033[0m"
              "\033[1;35m==========\033[0m\n\n")
        # Load post-fix warning details from postprocessed_warnings_data.json
        _, header_file_name_post_fix_list, file_content_post_fix_list, _, \
            warning_content_post_fix_llist, warning_line_number_post_fix_llist \
            = load_post_fix_data_from_json()

        # Load pipeline id from pipeline_id.json
        data = load_data_from_json("transport_data/pipeline_id.json")
        pipeline_id = data["pipeline_id"]

        # Create an instance of the DBInsertionHandler
        data_base_handler = DBInsertionHandler()

        # Update the database with the post-fix warning details
        data_base_handler.update_post_fix_warning_details(pipeline_id, header_file_name_post_fix_list,
                                                          file_content_post_fix_list,
                                                          warning_line_number_post_fix_llist,
                                                          warning_content_post_fix_llist)

        # Printing a divider and a success message with timestamp
        print("\n\033[1;35m-------------------------------------------------------------------------------\033[0m\n")
        print(f"\033[1;92m{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -"
              f" Doxygen-warnings successfully updated in the database.\033[0m")
        print("\033[1;35m===============================================================================\033[0m\n")

        # Printing the end of the operation
        print("\n\n\033[1;35m==========\033[0m"
              "\033[1;32m END OF UPDATING WARNING DETAILS IN DATABASE (POST FIX) \033[0m"
              "\033[1;35m=============\033[0m\n\n")
