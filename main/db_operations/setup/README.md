# README.md

---

# Setup Scripts

This directory contains the scripts necessary for setting up the database. 
It includes the following SQL scripts:
## Files

### `create_table.sql`
- Author: Ismail Al Shuaybi  
- Created on: 2023-07-01  
- Last updated: 2023-07-02  

This script creates tables to analyze Doxygen warnings both before and after their 
resolution through ChatGPT. These tables are normalized to the third normal form and include:

1. `ci_cd_pipeline_table`: Stores information about each CI/CD pipeline. This information 
   aids in identifying the pipeline and branch where the Doxygen warning was detected and resolved.

2. `project_table`: Stores information about each project present in the `doxygen_projects` folder. 
Each project is linked to a CI/CD pipeline. This table is particularly useful when dealing 
with multiple projects.

3. `header_file_table`: Stores information about each header file within a project. 
Each header file is associated with a project.

4. `warning_table`: Stores information about each Doxygen warning in a header file. 
Each warning is linked to a header file. Each warning has a `fix-status` that 
indicates if the warning has been successfully resolved (1) or not (0). 
The `warning type` indicates if the warning was detected before (`Pre-Fix`) 
or after (`Post-Fix`) the fixes applied by ChatGPT.

### `drop_tables_procedures.sql`
- Author: Ismail Al Shuaybi  
- Created on: 2023-07-01  
- Last updated: 2023-07-02  

This script removes any existing stored procedures or tables to avoid naming conflicts. 
The script does the following:

1. Drops stored procedures used to insert records into the PipelineTable, 
ProjectTable, HeaderFileTable, and WarningTable, if they exist.

2. Drops stored procedures used to update the `HeaderFileContentPostFix` field 
and the `FixedStatus` field, if they exist.

3. Drops tables used to store data related to CI/CD pipelines, projects, 
header files, warnings if they exist.
