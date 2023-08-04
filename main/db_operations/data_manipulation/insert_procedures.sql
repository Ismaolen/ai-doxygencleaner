/*
* File: insert_procedures.sql
* Author: Ismail Al Shuaybi
* Created on: 2023-07-01
* Last updated: 2023-07-02
* Description: This script contains stored procedures for inserting records into the tables
* created to analyze the Doxygen warnings before they are resolved by ChatGPT. These stored
* procedures simplify the process of adding new data to the database and maintain data consistency.
*/



/*
* Procedure: InsertIntoPipelineTable
* Description: Inserts a new record into the ci_cd_pipeline_table.
* Parameters:
* - pipe_line_id_input: The unique ID of the CI/CD pipeline.
* - branch_name_input: The name of the branch associated with the pipeline.
* - pipe_line_link_input: The URL link to the pipeline.
*/
DELIMITER $$
CREATE PROCEDURE InsertIntoPipelineTable
(
IN pipe_line_id_input INT,
IN branch_name_input VARCHAR(255),
IN pipe_line_link_input TEXT
)
BEGIN
    INSERT INTO ci_cd_pipeline_table (Pipeline_ID, Branch_Name, Pipeline_Link)
    VALUES (pipe_line_id_input, branch_name_input, pipe_line_link_input);
END$$
DELIMITER ;



/*
* Procedure: InsertIntoProjectTable
* Description: Inserts a new record into the project_table.
* Parameters:
* - pipe_line_id_input: The ID of the associated pipeline.
* - project_folder_path_input: The file path of the project folder.
* - last_projekt_id_output: The last inserted project ID.
*/
DELIMITER $$
CREATE PROCEDURE InsertIntoProjectTable
(
IN pipe_line_id_input INT,
IN project_folder_path_input TEXT,
OUT last_projekt_id_output INT
)
BEGIN
    INSERT INTO project_table (Pipeline_ID, Project_folder_path)
    VALUES (pipe_line_id_input, project_folder_path_input);
    SET last_projekt_id_output = LAST_INSERT_ID();
END$$
DELIMITER ;



/*
* Procedure: InsertIntoHeaderFileTable
* Description: Inserts a new record into the header_file_table.
* Parameters:
* - project_id_input: The ID of the associated project.
* - header_file_name_input: The name of the header file.
* - header_file_content_pre_fix_input: The content of the header file before fixes are applied.
* - number_of_warnings_input: The number of detected Doxygen warnings in the header file.
* - header_file_id_output: The last inserted header file ID.
*/
DELIMITER $$
CREATE PROCEDURE InsertIntoHeaderFileTable(
IN project_id_input INT,
IN header_file_name_input VARCHAR(255),
IN header_file_content_pre_fix_input TEXT,
IN number_of_warnings_input INT,
Out header_file_id_output INT
)
BEGIN
    INSERT INTO header_file_table (Project_ID, Header_file_name, Header_file_content_pre_fix, Number_of_Warnings)
    VALUES (project_id_input, header_file_name_input, header_file_content_pre_fix_input, number_of_warnings_input);
    SET header_file_id_output = last_insert_id();
END$$
DELIMITER ;


/*
* Procedure: InsertIntoWarningTable
* Description: Inserts a new record into the warning_table.
* Parameters:
* - LastHeaderFILEID: The ID of the associated header file.
* - WarningContent: The text content of the warning.
* - FixedStatus: The indicator if the warning has been fixed (1) or not (0).
* - warning_type_input: The type of warning: 'Pre-Fix' or 'Post-Fix'.
*/
DELIMITER $$
CREATE PROCEDURE InsertIntoWarningTablePreFix
(
IN last_header_file_id_input INT,
IN warning_content_input TEXT,
IN line_number_pre_fix_input INT,
IN fixed_status_input TINYINT,
IN warning_type_input ENUM('Pre-Fix', 'Post-Fix')
)
BEGIN
    INSERT INTO warning_table (Header_file_ID, Warning_Content, Line_Number_pre_fix, Fixed, Warning_Type)
    VALUES (last_header_file_id_input, warning_content_input, line_number_pre_fix_input,
            fixed_status_input, warning_type_input);
END$$
DELIMITER ;



DELIMITER $$
CREATE PROCEDURE InsertIntoWarningTablePostFix
(
IN last_header_file_id_input INT,
IN warning_content_input TEXT,
IN line_number_post_fix_input INT,
IN fixed_status_input TINYINT,
IN warning_type_input ENUM('Pre-Fix', 'Post-Fix')
)
BEGIN
    INSERT INTO warning_table (Header_file_ID, Warning_Content, Line_Number_post_fix, Fixed, Warning_Type)
    VALUES (last_header_file_id_input, warning_content_input, line_number_post_fix_input,
            fixed_status_input, warning_type_input);
END$$
DELIMITER ;