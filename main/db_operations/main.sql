
CALL InsertIntoPipelineTable(124, 'main', 'http://', @LastID);
SELECT @LastID;
CALL InsertIntoProjectTable(@LastID, '/path/to/project', @LastProjektID);
SELECT @LastProjektID;
CALL InsertIntoHeaderFileTable(@LastProjektID, 'Beispiel.h',
    'Inhalt vor dem fixen', 4, @LastHeaderFileID);
SELECT @LastHeaderFileID;

CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 1', 50,1, 'Pre-Fix');
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 2', 51,1, 'Pre-Fix');
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 3', 52, 1, 'Pre-Fix');
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 4', 53 ,1, 'Pre-Fix');
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 5',  54,1, 'Pre-Fix');



CALL InsertIntoHeaderFileTable(@LastProjektID, 'test.h',
    'Inhalt vor dem fixen', 7, @LastHeaderFileID);
SELECT @LastHeaderFileID;
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 1',  40,1, 'Pre-Fix');
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 2',  41,1, 'Pre-Fix');
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 3',  42,1, 'Pre-Fix');
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 4',  43,1, 'Pre-Fix');
CALL InsertIntoWarningTablePreFix(@LastHeaderFileID, 'Warnung 5',  44,1, 'Pre-Fix');





CALL UpdateHeaderFileContentPostFix(124, 'test.h', 'inhalt nach dem fix');
CALL UpdateFixedStatusPostFix(37, 0, 124, 'test.h', 'Warnung 11');

select ci_cd_pipeline_table.Pipeline_ID,
       header_file_table.Header_file_name,
       Number_of_Warnings, Warning_Content, Fixed, Warning_Type, Line_Number_pre_fix, Line_Number_post_fix,
       Header_file_content_pre_fix, Header_file_content_post_fix
from ci_cd_pipeline_table, project_table, header_file_table, warning_table
where ci_cd_pipeline_table.Pipeline_ID = project_table.Pipeline_ID and ci_cd_pipeline_table.Pipeline_ID = 928792229
 and project_table.Project_ID = header_file_table.Project_ID
 and header_file_table.Header_file_ID = warning_table.Header_file_ID;