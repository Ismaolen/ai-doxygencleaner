import json


def save_data_to_json(file_path, data_dict):
    """
    Save data to a JSON file.

    Parameters
    ----------
    file_path : str
        The path to the JSON file.

    data_dict : dict
        A dictionary where the key is the name of the data and the value is the list or string to be saved.
    """
    # Save the dictionary in a JSON file
    with open(file_path, "w") as f:
        json.dump(data_dict, f)


def load_data_from_json(file_path):
    """
    Load data from a JSON file and return it.

    Parameters
    ----------
    file_path : str
        The path to the JSON file.

    Returns
    -------
    dict
        A dictionary containing the data loaded from the JSON file.
    """
    # Load the dictionary from the JSON file
    with open(file_path, "r") as f:
        data = json.load(f)

    return data


def add_data_to_json(file_path, new_data):
    """
    Add new data to an existing JSON file.

    Parameters
    ----------
    file_path : str
        The path to the JSON file.

    new_data : dict
        A dictionary containing the new data to be added to the JSON file.
    """
    # Load the existing data
    with open(file_path, "r") as f:
        data = json.load(f)

    # Update the data with the new_data
    data.update(new_data)

    # Write the data back to the file
    with open(file_path, "w") as f:
        json.dump(data, f)


def load_pre_fix_data_from_json():
    """
    Load preprocessed warning data from a JSON file.

    The file contains details of the project folder path, header file names, file contents,
    warning numbers, warning contents, and line numbers of the warnings.

    Returns
    -------
    tuple
        A tuple containing all the loaded data from the JSON file.
    """

    # Load data from the preprocessed warnings data JSON file
    data = load_data_from_json("transport_data/preprocessed_warnings_data.json")

    # Extract specific information from the loaded data
    project_folder_pre_fix_path = data["project_folder_pre_fix_path"]
    header_file_name_pre_fix_list = data["header_file_name_pre_fix_list"]
    file_content_pre_fix_list = data["file_content_pre_fix_list"]
    warning_num_pre_fix_list = data["warning_num_pre_fix_list"]
    warning_content_pre_fix_llist = data["warning_content_pre_fix_llist"]
    warning_line_number_pre_fix_llist = data["warning_line_number_pre_fix_llist"]

    # Return the extracted information as a tuple
    return (project_folder_pre_fix_path, header_file_name_pre_fix_list, file_content_pre_fix_list,
            warning_num_pre_fix_list, warning_content_pre_fix_llist, warning_line_number_pre_fix_llist)


def load_post_fix_data_from_json():
    """
    Load postprocessed warning data from a JSON file.

    The file contains details of the project folder path, header file names, file contents,
    warning numbers, warning contents, and line numbers of the warnings.

    Returns
    -------
    tuple
        A tuple containing all the loaded data from the JSON file.
    """

    # Load data from the postprocessed warnings data JSON file
    data = load_data_from_json("transport_data/postprocessed_warnings_data.json")

    # Extract specific information from the loaded data
    project_folder_post_fix_path = data["project_folder_post_fix_path"]
    header_file_name_post_fix_list = data["header_file_name_post_fix_list"]
    file_content_post_fix_list = data["file_content_post_fix_list"]
    warning_num_post_fix_list = data["warning_num_post_fix_list"]
    warning_content_post_fix_llist = data["warning_content_post_fix_llist"]
    warning_line_number_post_fix_llist = data["warning_line_number_post_fix_llist"]

    # Return the extracted information as a tuple
    return (project_folder_post_fix_path, header_file_name_post_fix_list, file_content_post_fix_list,
            warning_num_post_fix_list, warning_content_post_fix_llist, warning_line_number_post_fix_llist)
