/*
* File: create_table.sql
* Author: Ismail Al Shuaybi
* Created on: 2023-07-01
* Last updated: 2023-07-02
* Description: This script creates tables to analyze the Doxygen warnings before and after
* their resolution using ChatGPT. These tables are normalized to the third normal form.
*/


/*
* Table: ci_cd_pipeline_table
* Description: Stores information about each CI/CD pipeline. This information aids in identifying
* the pipeline and branch where the Doxygen warning was detected and resolved.
*/
CREATE TABLE ci_cd_pipeline_table (
    Pipeline_ID INT PRIMARY KEY,  -- Unique ID for each pipeline
    Branch_Name VARCHAR(255),     -- Name of the branch associated with the pipeline
    Pipeline_Link TEXT            -- URL link to the pipeline
);

/*
* Table: project_table
* Description: Stores information about each project present in the 'doxygen_projects' folder.
* Each project is linked to a CI/CD pipeline. This table is particularly useful when dealing
* with multiple projects.
*/
CREATE TABLE project_table (
    Project_ID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each project
    Pipeline_ID INT,                             -- ID of the associated pipeline
    Project_folder_path TEXT,                    -- File path of the project folder
    FOREIGN KEY (Pipeline_ID)
    REFERENCES ci_cd_pipeline_table(Pipeline_ID) -- Foreign key reference to ci_cd_pipeline_table
);

/*
* Table: header_file_table
* Description: Stores information about each header file within a project. Each header file
* is associated with a project.
*/
CREATE TABLE header_file_table (
    Header_file_ID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique ID for each header file
    Project_ID INT,                                  -- ID of the associated project
    Header_file_name VARCHAR(255),                   -- Name of the header file
    Header_file_content_pre_fix TEXT,                -- Content of the header file before fixes
    Header_file_content_post_fix TEXT,               -- Content of the header file after fixes
    Number_of_Warnings INT,                          -- Number of detected Doxygen warnings in the header file
    FOREIGN KEY (Project_ID) REFERENCES project_table(Project_ID) -- Foreign key reference to project_table
);

/*
* Table: warning_table
* Description: Stores information about each Doxygen warning in a header file. Each warning is
* linked to a header file. Each warning has a 'fix-status' that indicates if the warning has been
* successfully resolved (1) or not (0). The 'warning type' indicates if the warning was detected
* before ('Pre-Fix') or after ('Post-Fix') the fixes applied by ChatGPT.
*/
CREATE TABLE warning_table (
    Warning_ID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique ID for each warning
    Header_file_ID INT,                              -- ID of the associated header file
    Warning_Content TEXT,                            -- Text content of the warning
    Line_Number_pre_fix INT,
    Line_Number_post_fix INT,
    Fixed TINYINT(1) DEFAULT 1,                      -- Indicator if the warning has been fixed (1) or not (0)
    Warning_Type ENUM('Pre-Fix', 'Post-Fix') NOT NULL DEFAULT 'Pre-Fix',  -- Type of warning: 'Pre-Fix' or 'Post-Fix'
    Warning_Time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,             -- Timestamp of when the warning was generated
    FOREIGN KEY (Header_file_ID)
    REFERENCES header_file_table(Header_file_ID) -- Foreign key reference to header_file_table
);








