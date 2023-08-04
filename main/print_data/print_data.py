from datetime import datetime
from pygments import highlight
from pygments.lexers import CppLexer
from pygments.formatters import TerminalFormatter


def print_project_details(project_folder_post_fix_path: list, header_file_name_post_fix_list: list,
                          warning_num_post_fix_list: list, warning_content_post_fix_llist: list,
                          warning_line_number_post_fix_llist: list,
                          pre_or_post, file_content_post_fix_list=None):
    """
    Print details of the project, including file contents, Doxygen warnings, and lines where the warnings occurred.

    Parameters
    ----------
    project_folder_post_fix_path : str
        The path to the project folder.
    header_file_name_post_fix_list : list
        List of the names of the header files.
    warning_num_post_fix_list : list
        List of the numbers of the Doxygen warnings detected.
    warning_content_post_fix_llist : list
        List of the content of the Doxygen warnings detected.
    warning_line_number_post_fix_llist : list
        List of the line numbers where the Doxygen warnings were detected.
    pre_or_post : str
        Indicate if the details are before the fix ('pre') or after the fix ('post').
    file_content_post_fix_list : list, optional
        List of the contents of the files, by default None.

    Returns
    -------
    None
    """

    # Print header for the project details
    print("\n\033[1;35m==================== PROJECT DETAILS ====================\033[0m")
    print(
        f"\n\033[1;96mProject Folder ({pre_or_post}-Fix) Path:\033[0m \033[4;33m{project_folder_post_fix_path}\033[0m\n")
    print("\033[1;35m=========================================================\033[0m\n")

    # Loop over each header file in the project
    for i, header_name in enumerate(header_file_name_post_fix_list):
        print(f"\033[1;91m>> FILE:\033[0m "
              f"\033[4;32m{header_name}\033[0m\n")

        # If file contents are provided, print them
        if file_content_post_fix_list is not None:

            print(f"\033[1;91m>> FILE CONTENT ({pre_or_post}-Fix):\033[0m\n")
            for index, line in enumerate(file_content_post_fix_list[i].splitlines(), start=1):
                print(f"\033[1;94m{index:4}\033[0m: {highlight(line, CppLexer(), TerminalFormatter())}", end='')

        # Print the number of Doxygen warnings detected in the file
        num_warnings = warning_num_post_fix_list[i]
        print(
            f"\n\n\033[1;93m>> Number of Doxygen Warnings Detected ({pre_or_post}-Fix):\033[0m \033[4;31m{num_warnings if num_warnings is not None else 0}\033[0m\n")

        # If there are warnings, print their contents and lines where they occurred
        if warning_content_post_fix_llist[i] is not None and num_warnings > 0:
            print(f"\033[1;94m>> Warning Contents ({pre_or_post}-Fix):\033[0m")
            for j, content in enumerate(warning_content_post_fix_llist[i]):
                print(f"\n\033[1;95m\t>>> Warning {j + 1}:\033[0m \033[4;33m{content}\033[0m")
                if warning_line_number_post_fix_llist[i] is not None:
                    print(
                        f"\033[1;95m\t>>> On Line:\033[0m \033[4;33m{warning_line_number_post_fix_llist[i][j]}\033[0m")

        else:
            # If no warnings were detected, print a success message
            print("\033[1;92mNo Doxygen Warnings Detected After Fixing.\n"
                  "All Doxygen Warnings In This File Were Resolved Through The GPT Model.\033[0m")
        print("\n\033[1;35m---------------------------------------------------------\033[0m\n")
        print(f"\033[1;92m{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - File analysis completed.\033[0m")
        print("\033[1;35m=========================================================\033[0m\n")


def print_project_details_without_color(project_folder_post_fix_path, header_file_name_post_fix_list,
                                        warning_num_post_fix_list, warning_content_post_fix_llist,
                                        warning_line_number_post_fix_llist,
                                        pre_or_post, file_content_post_fix_list=None):
    """
    Print details of the project, including file contents, Doxygen warnings, and lines where the warnings occurred.

    Parameters
    ----------
    project_folder_post_fix_path : str
        The path to the project folder.
    header_file_name_post_fix_list : list
        List of the names of the header files.
    warning_num_post_fix_list : list
        List of the numbers of the Doxygen warnings detected.
    warning_content_post_fix_llist : list
        List of the content of the Doxygen warnings detected.
    warning_line_number_post_fix_llist : list
        List of the line numbers where the Doxygen warnings were detected.
    pre_or_post : str
        Indicate if the details are before the fix ('pre') or after the fix ('post').
    file_content_post_fix_list : list, optional
        List of the contents of the files, by default None.

    Returns
    -------
    None
    """
    print("\n==================== PROJECT DETAILS ====================")
    print(
        f'\n< Project Folder ({pre_or_post}-Fix) Path: {project_folder_post_fix_path}\n')
    print("=========================================================\n")

    for i, header_name in enumerate(header_file_name_post_fix_list):
        print(f">> FILE: "
              f"{header_name}")

        if file_content_post_fix_list is not None:
            print(f">> FILE CONTENT ({pre_or_post}-Fix):\n")
            for index, line in enumerate(file_content_post_fix_list[i].splitlines(), start=1):
                print(f"{line}")

        print("\n---------------------------------------------------------\n")
        num_warnings = warning_num_post_fix_list[i]
        print(
            f"\n\n>> Number of Doxygen Warnings Detected ({pre_or_post}-Fix): {num_warnings if num_warnings is not None else 0}\n")

        if warning_content_post_fix_llist[i] is not None and num_warnings > 0:
            print(f">> Warning Contents ({pre_or_post}-Fix):")
            for j, content in enumerate(warning_content_post_fix_llist[i]):
                print(f"\n\t>>> Warning {j + 1}: {content}")
                if warning_line_number_post_fix_llist[i] is not None:
                    print(
                        f"\t>>> On Line: {warning_line_number_post_fix_llist[i][j]}")
        else:
            print("No Doxygen Warnings Detected After Fixing.\n"
                  "All Doxygen Warnings In This File Were Resolved Through The GPT Model.")
        print("\n---------------------------------------------------------\n")
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - File analysis completed.")
        print("=========================================================\n")
