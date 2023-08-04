"""
Main execution script for the Doxygen Warning Manager tool.

The AI Doxygen Cleaner is a tool that automates several tasks related to Doxygen warning management. This includes
configuring Doxygen, detecting warnings, inserting warnings into a database, fixing warnings using an AI language
model, applying these fixes, detecting warnings after fixes have been applied, printing warning details to a file,
generating a diff page in HTML format, and updating warning data in the database post-fix.
"""

import argparse
from ai_doxygen_cleaner.ai_doxygen_cleaner import AIDoxygenCleaner

if __name__ == '__main__':
    # Create an ArgumentParser object to handle command line arguments
    parser = argparse.ArgumentParser(
        description="A script for configuring Doxygen, detecting and managing warnings.")

    # Define the optional arguments for the script
    parser.add_argument("-c", "--configure-doxygen", required=False, action="store_true",
                        help="Configure Doxygen using predefined configuration parameters.")
    parser.add_argument("-dw", "--detect-warnings-pre-fix", required=False, action="store_true",
                        help="Detect Doxygen warnings in the specified project.")
    parser.add_argument("-iwdb", "--insert-warnings-db", required=False, action="store_true",
                        help="Insert detected Doxygen warnings into the database.")
    parser.add_argument("-fdw", "--fix-doxygen-warnings", required=False, action="store_true",
                        help="Attempt to fix detected Doxygen warnings using an AI language model.")
    parser.add_argument("-af", "--apply-fix", required=False, action="store_true",
                        help="Apply suggested fixes from the AI language model to the original header files.")
    parser.add_argument("-dwpf", "--detect-warnings-post-fix", required=False, action="store_true",
                        help="Re-run Doxygen to detect warnings after the fixes have been applied.")
    parser.add_argument("-pwdtf", "--print-warning-details-to-file", required=False, action="store_true",
                        help="Print details of pre and post-fix warnings to a file.")
    parser.add_argument("-gdhp", "--generate-html-diff-page", required=False, action="store_true",
                        help="Generate an HTML diff page to visualize changes made by the fix application.")
    parser.add_argument("-uwd", "--update-warning-data-in-db", required=False, action="store_true",
                        help="Update the warning data in the database after applying fixes.")

    # Parse the arguments
    args = parser.parse_args()

    # Create a AIDoxygenCleaner instance
    doxygen_warning_manager = AIDoxygenCleaner()

    # Process each argument and call the appropriate AIDoxygenCleaner method
    if args.configure_doxygen:  # Configure Doxygen
        doxygen_warning_manager.doxygen_configuration()

    # Detect warnings before fixes
    if args.detect_warnings_pre_fix:
        doxygen_warning_manager.detect_warnings_pre_fix()

    # Insert warnings into database
    if args.insert_warnings_db:
        doxygen_warning_manager.insert_warnings_to_db()

    # Fix detected warnings
    if args.fix_doxygen_warnings:
        doxygen_warning_manager.fix_doxygen_warning()

    # Apply suggested fixes
    if args.apply_fix:
        doxygen_warning_manager._apply_fix()

    # Detect warnings after fixes
    if args.detect_warnings_post_fix:
        doxygen_warning_manager.detect_warnings_post_fix()

    # Print warning details to file
    if args.print_warning_details_to_file:
        doxygen_warning_manager.print_pre_post_fix_data_to_file()

    # Generate HTML diff page
    if args.generate_html_diff_page:
        doxygen_warning_manager.generate_html_diff_page()

    # Update warning data in database
    if args.update_warning_data_in_db:
        doxygen_warning_manager.update_warnings_details_post_fix_in_db()
