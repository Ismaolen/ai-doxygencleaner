import subprocess

import os
import re


def perform_diff_on_files():
    """
    Compare two files and output the difference to a text file.
    """

    # Define the path to the files
    PATH = 'data/different_between_pre_and_post'

    # Define the command to perform the diff and output to a text file
    cmd = f"diff -u {PATH}/output_pre_fix.cpp {PATH}/output_post_fix.cpp > {PATH}/diff.txt"

    # Execute the command
    subprocess.run(cmd, shell=True)


def generate_html_diff():
    """
    Generate an HTML file from a diff text file.
    """

    # Define the path to the files
    PATH = 'data/different_between_pre_and_post'

    # Define the command to convert the diff text file to HTML
    cmd = f"diff2html -s side -f html -i file -F {PATH}/diff.html --hc -- {PATH}/diff.txt"

    # Execute the command
    subprocess.run(cmd, shell=True)


def compaine_warn_details(warning_content_llist, warning_line_number_llist, file_content_list,
                          header_file_name_list):
    """
    Compile warning details into a list of prompts.

    Parameters
    ----------
    warning_content_llist : list
        List of warning content.
    warning_line_number_llist : list
        List of warning line numbers.
    file_content_list : list
        List of file content.
    header_file_name_list : list
        List of header file names.

    Returns
    -------
    list
        List of prompts created from warnings and file content.
    """

    # Initialize an empty list for the prompts
    prompt_list = []

    # Iterate through each list
    for warning_content_list, warning_line_number_list, file_content, file_name in zip(warning_content_llist,
                                                                                       warning_line_number_llist,
                                                                                       file_content_list,
                                                                                       header_file_name_list):

        # Initialize an empty string for the query
        query = ""

        # Add warning details to the query
        for warning_content, warning_line_number, in zip(warning_content_list, warning_line_number_list):
            query += f'line number:{warning_line_number} : {warning_content}\n'

        # Add file content to the query
        query += file_content

        # Append the query to the list of prompts
        prompt_list.append(query)

    # Return the list of prompts
    return prompt_list


def rename_and_move(source_path: str, target_dir: str) -> None:
    """
    Move and rename a specific file from source to target directory.

    This function takes a file named `diff.html` from the specified source path
    and moves it to the target directory. In the target directory, the file is
    renamed following the pattern `test_diff_{n}.html`, where `{n}` is determined
    by existing files in the target directory.

    Parameters
    ----------
    source_path : str
        The path to the directory containing the `diff.html` file.
    target_dir : str
        The directory where the file will be moved and renamed.

    Raises
    ------
    FileNotFoundError
        If the `diff.html` file is not found in the source path.

    Examples
    --------
    >>> rename_and_move('/path/to/source', '/path/to/target')

    """
    # Define path to the source file
    source_file_path = os.path.join(source_path, 'diff.html')

    # Check if source file exists
    if not os.path.exists(source_file_path):
        raise FileNotFoundError(f"File {source_file_path} not found.")

    # List all files in the target directory
    existing_files = os.listdir(target_dir)

    # Determine the highest existing number for test_diff_*.html files
    highest_number = 0
    for filename in existing_files:
        match = re.match(r'test_diff_(\d+).html', filename)
        if match:
            number = int(match.group(1))
            highest_number = max(highest_number, number)

    # Determine new file number
    new_number = highest_number + 1
    target_file_path = os.path.join(target_dir, f'test_diff_{new_number}.html')

    # Copy and rename the file
    with open(source_file_path, 'r', encoding='utf-8') as source_file, open(target_file_path, 'w',
                                                                            encoding='utf-8') as target_file:
        target_file.write(source_file.read())


