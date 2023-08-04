/*
* File: update_procedures.sql
* Author: Ismail Al Shuaybi
* Created on: 2023-07-01
* Last updated: 2023-07-02
* Description: This script is comprised of stored procedures designed for updating
* records in the database tables used for the analysis of Doxygen warnings. The updates occur after these warnings
* have been addressed and resolved by ChatGPT. These procedures play a key role in maintaining
* data accuracy and consistency throughout the analysis. Furthermore, they provide insights into the number
* of warnings resolved by ChatGPT and present the content of the associated file after the resolution.
* Therefore, they offer a mechanism to evaluate the effectiveness of the fixes implemented by ChatGPT.
*/


/*
* Procedure: UpdateHeaderFileContentPostFix
* Description: This stored procedure updates the field 'Header_file_content_post_fix' in a specific header file
* associated with a given pipeline ID. This procedure is invoked when the Doxygen warnings in a header file
* have been addressed and resolved by ChatGPT, thus reflecting the state of the header file post-resolution.
* Parameters:
* - pipeline_id_input: The ID of the pipeline linked to the header file to be updated.
* - header_file_name_input: The name of the header file where the update will be applied.
* - content_post_fix_input: The revised content of the header file after the warnings have been fixed.
*/
DELIMITER $$

CREATE PROCEDURE UpdateHeaderFileContentPostFix(
    IN pipeline_id_input INT,
    IN header_file_name_input VARCHAR(255),
    IN content_post_fix_input TEXT)
BEGIN
    UPDATE ci_cd_pipeline_table, project_table, header_file_table
    SET header_file_table.Header_file_content_post_fix = content_post_fix_input
    WHERE ci_cd_pipeline_table.Pipeline_ID = project_table.Pipeline_ID
    AND project_table.Project_ID = header_file_table.Project_ID
    AND ci_cd_pipeline_table.Pipeline_ID = pipeline_id_input
    AND header_file_table.Header_file_name = header_file_name_input;
END$$
DELIMITER ;


/*
* Procedure: UpdateFixedStatus
* Description: This stored procedure is tasked with managing the 'Fixed' status of a
* specific Doxygen warning associated with a specified pipeline and header file.
* The procedure is designed to perform the following actions:
* - Checks if a warning exists in the warning_table.
* - If the warning doesn't exist, it adds the warning to the table, assigning it a 'Fixed'
*   status of 0 (indicating it has not been resolved) and the type 'Post-Fix'.
*   This signifies that the warning was identified following a resolution attempt by ChatGPT.
* - If the warning is found, it means the warning wasn't fixed by ChatGPT.
*   Hence, we need to update the 'Fixed' status to 0. Any warning not detected
*   post ChatGPT's resolution attempt is considered fixed and retains 'Fixed' status 1.
* - The procedure also manages the 'Number_of_Warnings' field in the 'header_file_table'
*   by incrementing the count when a new warning is added.
* Parameters:
* - fixed_status_input: The new status of the warning after ChatGPT's resolution attempt.
*   This can be either 0 (not fixed) or 1 (fixed).
* - pipeline_id_input: The ID of the pipeline that the warning is associated with.
* - header_file_name_input: The name of the header file that the warning originates from.
* - warning_content_input: The content or description of the Doxygen warning that needs to be managed.
*/
DELIMITER $$
CREATE PROCEDURE UpdateFixedStatusPostFix(
    IN line_number_post_fix_input INT,
    IN fixed_status_input INT,
    IN pipeline_id_input INT,
    IN header_file_name_input VARCHAR(255),
    IN warning_content_input TEXT)
BEGIN
    DECLARE rowCount INT;

    SELECT COUNT(*)
    INTO rowCount
    FROM ci_cd_pipeline_table, project_table, header_file_table, warning_table
    WHERE ci_cd_pipeline_table.Pipeline_ID = project_table.Pipeline_ID
    AND project_table.Project_ID = header_file_table.Project_ID
    AND header_file_table.Header_file_ID = warning_table.Header_file_ID
    AND ci_cd_pipeline_table.Pipeline_ID = pipeline_id_input
    AND header_file_table.Header_file_name = header_file_name_input
    AND warning_table.Warning_Content = warning_content_input;
    select rowCount;
    # If rowCount is 0, the warning does not exist in the warning table and
    # needs to be added with a 'Post-Fix' status.
    # We also need to increment the Number_of_Warnings by 1.
    IF rowCount = 0 THEN
        Select 'The warning does not exist';
        # Get HeaderFileID of the specified header file, necessary to add
        # the Doxygen warning in the right header file using the InsertIntoWarningTable procedure.
        Select header_file_table.Header_file_ID
        INTO @HeaderFileID
        FROM ci_cd_pipeline_table, project_table, header_file_table, warning_table
        WHERE ci_cd_pipeline_table.Pipeline_ID = project_table.Pipeline_ID
        AND project_table.Project_ID = header_file_table.Project_ID
        AND header_file_table.Header_file_ID = warning_table.Header_file_ID
        AND ci_cd_pipeline_table.Pipeline_ID = pipeline_id_input
        AND header_file_table.Header_file_name = header_file_name_input
        LIMIT 1;
        # Insert the new warning into the warning table.
        CALL InsertIntoWarningTablePostFix(@HeaderFileID, warning_content_input,
            line_number_post_fix_input, 0, 'Post-Fix');
        Select 'The warning has been added to the warning table';
        # As a new warning has been inserted, we need to update the
        # Number_of_Warnings for this header file by incrementing it.
        UPDATE ci_cd_pipeline_table, project_table, header_file_table, warning_table
        SET header_file_table.Number_of_Warnings = header_file_table.Number_of_Warnings + 1
        WHERE ci_cd_pipeline_table.Pipeline_ID = project_table.Pipeline_ID
        AND project_table.Project_ID = header_file_table.Project_ID
        AND header_file_table.Header_file_ID = warning_table.Header_file_ID
        AND ci_cd_pipeline_table.Pipeline_ID = pipeline_id_input
        AND header_file_table.Header_file_name = header_file_name_input;

    ELSE
        # If the warning is found, it means the warning wasn't fixed by ChatGPT.
        # Hence, we need to update the 'Fixed' status to 0. Any warning not detected
        # post ChatGPT's resolution attempt is considered fixed and retains 'Fixed' status 1.
        UPDATE ci_cd_pipeline_table, project_table, header_file_table, warning_table
        SET warning_table.Fixed = fixed_status_input, warning_table.Line_Number_post_fix = line_number_post_fix_input
        WHERE ci_cd_pipeline_table.Pipeline_ID = project_table.Pipeline_ID
        AND project_table.Project_ID = header_file_table.Project_ID
        AND header_file_table.Header_file_ID = warning_table.Header_file_ID
        AND ci_cd_pipeline_table.Pipeline_ID = pipeline_id_input
        AND header_file_table.Header_file_name = header_file_name_input
        AND warning_table.Warning_Content = warning_content_input;
    END IF;

END$$
DELIMITER ;



