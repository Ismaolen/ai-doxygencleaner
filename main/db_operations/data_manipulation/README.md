# README.md

---

# Data Manipulation Scripts

This directory contains SQL scripts used to manipulate data in the database. 
These scripts mainly include stored procedures for inserting and updating 
records in the database tables.

## Files



### `insert_procedures.sql`

- Author: Ismail Al Shuaybi  
- Created on: 2023-07-01  
- Last updated: 2023-07-02  

This script contains stored procedures for inserting records into the 
tables created to analyze the Doxygen warnings before they are resolved 
by ChatGPT. These stored procedures simplify the process of adding new 
data to the database and maintain data consistency.

This script includes four main procedures:

1. **`InsertIntoPipelineTable`:** This procedure inserts a new record into the ci_cd_pipeline_table.

2. **`InsertIntoProjectTable`:** This procedure inserts a new record into the project_table.

3. **`InsertIntoHeaderFileTable`:** This procedure inserts a new record into the header_file_table.

4. **`InsertIntoWarningTable`:** This procedure inserts a new record into the warning_table.


### `update_procedures.sql`

- Author: Ismail Al Shuaybi   
- Created on: 2023-07-01  
- Last updated: 2023-07-02  

This script is comprised of stored procedures designed for updating 
records in the database tables used for the analysis of Doxygen warnings. 
These updates occur after the warnings have been addressed and resolved by ChatGPT. 
These procedures play a key role in maintaining data accuracy and consistency 
throughout the analysis. They also provide insights into the number of warnings 
resolved by ChatGPT and present the content of the associated file after resolution. 
Therefore, they offer a mechanism to evaluate the effectiveness of the fixes implemented by ChatGPT.

This script includes two main procedures:

1. **`UpdateHeaderFileContentPostFix`**: This procedure updates the field 
'Header_file_content_post_fix' in a specific header file associated with 
a given pipeline ID. It reflects the state of the header file post-resolution.

2. **`UpdateFixedStatus`:** This stored procedure is tasked with managing the 'Fixed' status of a 
specific Doxygen warning associated with a specified pipeline and header file. 
The procedure is designed to perform the following actions:
    - Checks if a warning exists in the `warning_table`.
    - If the warning doesn't exist, it adds the warning to the table, assigning it a `Fixed`
      status of 0 (indicating it has not been resolved) and the type `Post-Fix`.
      This signifies that the warning was identified following a resolution attempt by ChatGPT.
    - If the warning is found, it means the warning wasn't fixed by ChatGPT.
      Hence, we need to update the `Fixed` status to 0. Any warning not detected
      post ChatGPT's resolution attempt is considered fixed and retains `Fixed` status 1.
    - The procedure also manages the `Number_of_Warnings` field in the `header_file_table`
      by incrementing the count when a new warning is added.

## Usage

To use these scripts, import them into your preferred SQL client and execute the 
procedures as needed, providing the necessary input parameters.

