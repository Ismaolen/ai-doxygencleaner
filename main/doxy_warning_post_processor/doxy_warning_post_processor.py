from doxygen_management.doxy_warning_detector import DoxyWarningDetector
from print_data.print_data import print_project_details
from transport_data.transport_data import load_data_from_json, add_data_to_json, load_pre_fix_data_from_json


class WarningPostProcessor(DoxyWarningDetector):
    """
    The WarningPostProcessor class handles detection and processing of warnings after fixes have been applied.

    Methods
    -------
    apply_fix():
        Applies fixes to the header files and saves changes.
    detect_warning():
        Detects and updates warning details post-fix.
    """

    def __init__(self):
        DoxyWarningDetector.__init__(self)
        """
        Constructs all the necessary attributes for the WarningPostProcessor object.
        """
        pass

    def apply_fix(self):
        """
        Applies fixes to the header files and saves changes.

        This method loads pre-warning details, loads post-fix file content, and writes the post-fix file
        content back to the header files.
        """
        # Load warning details from preprocessed_warnings_data.json
        (project_folder_pre_fix_path, header_file_name_pre_fix_list, _, _, _, _) = load_pre_fix_data_from_json()

        # Load post-fix file content list
        data = load_data_from_json("transport_data/postprocessed_warnings_data.json")
        file_content_post_fix_list = data["file_content_post_fix_list"]

        # Write file_content_post_fix_list to header files
        for file_content_post_fix, header_file_name_pre_fix in zip(file_content_post_fix_list,
                                                                   header_file_name_pre_fix_list):
            file_path = project_folder_pre_fix_path + "/" + header_file_name_pre_fix
            self.write_file(file_path, file_content_post_fix)

    def detect_warning(self):
        """
        Detects and updates warning details post-fix.

        This method loads pre-warning details, detects warnings after fixes, updates warning lists,
        and finally adds the updated warning details to the postprocessed_warnings_data.json file.

        Returns
        -------
        None
        """
        # Load warning details from preprocessed_warnings_data.json
        (project_folder_pre_fix_path, header_file_name_pre_fix_list, file_content_pre_fix_list,
         warning_num_pre_fix_list, warning_content_pre_fix_llist,
         warning_line_number_pre_fix_llist) = load_pre_fix_data_from_json()

        # Detect warnings after fixes have been applied
        # detect_warning = DoxyWarningDetector()
        project_folder_post_fix_path, header_file_name_post_fix_list, \
            _, warning_num_post_fix_list, \
            warning_content_post_fix_llist, warning_line_number_post_fix_llist = \
            self.run_doxygen()

        # Update the warning lists with the post-fix warnings
        # Step 1: Generate a dictionary where the keys are the names from the post-fix list
        # and the values are their corresponding index positions.
        header_file_name_post_fix_dict = {name: idx for idx, name in enumerate(header_file_name_post_fix_list)}
        # Step 2: Loop over the pre-fix list.
        for pos_pre, name in enumerate(header_file_name_pre_fix_list):
            # Step 3: Try to find the value of 'name' in the dictionary.
            pos_post = header_file_name_post_fix_dict.get(name)
            # Step 4: If 'pos_post' is not None (i.e., the name was found in the dictionary),
            # update the values in the pre-fix lists with the corresponding values from the post-fix lists.
            if pos_post is not None:
                warning_num_pre_fix_list[pos_pre] = warning_num_post_fix_list[pos_post]
                warning_content_pre_fix_llist[pos_pre] = warning_content_post_fix_llist[pos_post]
                warning_line_number_pre_fix_llist[pos_pre] = warning_line_number_post_fix_llist[pos_post]
            # If 'pos_post' is None (i.e., the name was not found in the dictionary),
            # set the values in the pre-fix lists to None.
            else:
                warning_num_pre_fix_list[pos_pre] = None
                warning_content_pre_fix_llist[pos_pre] = None
                warning_line_number_pre_fix_llist[pos_pre] = None

        # Add updated warning details to postprocessed_warnings_data.json file
        data = {
            "project_folder_post_fix_path": project_folder_pre_fix_path,
            "header_file_name_post_fix_list": header_file_name_pre_fix_list,
            "warning_num_post_fix_list": warning_num_pre_fix_list,
            "warning_content_post_fix_llist": warning_content_pre_fix_llist,
            "warning_line_number_post_fix_llist": warning_line_number_pre_fix_llist,
        }
        add_data_to_json("transport_data/postprocessed_warnings_data.json", data)
        print_project_details(project_folder_pre_fix_path, header_file_name_pre_fix_list,
                              warning_num_pre_fix_list, warning_content_pre_fix_llist,
                              warning_line_number_pre_fix_llist,
                              'Post')
