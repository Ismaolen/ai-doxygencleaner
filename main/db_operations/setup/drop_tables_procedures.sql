/*
* File: drop_tables_procedures.sql
* Author: Ismail Al Shuaybi
* Created on: 2023-07-01
* Last updated: 2023-07-02
*/

/*
* Description: If they exist, this block drops stored procedures used to insert records
* into the PipelineTable, ProjectTable, HeaderFileTable, and WarningTable.
* This is typically done before creating or recreating these procedures to avoid naming conflicts.
*/
drop procedure if exists InsertIntoPipelineTable;
drop procedure if exists InsertIntoProjectTable;
drop procedure if exists InsertIntoHeaderFileTable;
drop procedure if exists InsertIntoWarningTablePreFix;
drop procedure if exists InsertIntoWarningTablePostFix;
/*
* Description: If they exist, this block drops stored procedures used to update the
* 'HeaderFileContentPostFix' field and the 'FixedStatus' field.
* This is typically done before creating or recreating these procedures to avoid naming conflicts.
*/
drop procedure if exists UpdateHeaderFileContentPostFix;
drop procedure if exists UpdateFixedStatusPostFix;

/*
* Description: If they exist, this statement drops tables used to store data related
* to CI/CD pipelines, jobs, projects, header files, warnings, and warning counts.
* This is typically done before creating or recreating these tables to avoid naming conflicts.
*/
DROP TABLE IF EXISTS ci_cd_pipeline_table, project_table,
    header_file_table, warning_table;
