# README.md

## Overview
`main.py` serves as the main execution script for the AIDoxygenCleaner tool. 
This AI-based tool automates several tasks related to the management of 
Doxygen warnings. The following operations are automated:

- Configuring Doxygen
- Detecting warnings
- Inserting warnings into a database
- Fixing warnings using an AI language model
- Applying these fixes
- Re-detecting warnings after fixes have been applied
- Printing warning details to a file
- Generating a diff page in HTML format
- Updating warning data in the database post-fix

## Structure

The file is structured into the importing of necessary modules, creating an 
`ArgumentParser` instance for handling command-line arguments, defining 
optional arguments for the script, and creating an instance of `AIDoxygenCleaner`. 
Following this, the script processes each argument and calls the appropriate 
`AIDoxygenCleaner` method. 

## Command Line Arguments

The script provides several optional command line arguments that control the 
execution of the different functionalities of the tool:

- `-c`, `--configure-doxygen`: Configure Doxygen using predefined 
configuration parameters.
- `-dw`, `--detect-warnings-pre-fix`: Detect Doxygen warnings in the 
specified project.
- `-iwdb`, `--insert-warnings-db`: Insert detected Doxygen warnings into
the database.
- `-fdw`, `--fix-doxygen-warnings`: Attempt to fix detected Doxygen warnings 
using an AI language model.
- `-af`, `--apply-fix`: Apply suggested fixes from the AI language model to 
the original header files.
- `-dwpf`, `--detect-warnings-post-fix`: Re-run Doxygen to detect warnings after the 
fixes have been applied.
- `-pwdtf`, `--print-warning-details-to-file`: Print details of pre and 
post-fix warnings to a file.
- `-gdhp`, `--generate-html-diff-page`: Generate an HTML diff page to visualize 
changes made by the fix application.
- `-uwd`, `--update-warning-data-in-db`: Update the warning data in the 
database after applying fixes.

## Example Usage

The `main.py` script can be executed from the terminal using Python. The optional 
command line arguments can be provided to control the execution of the tool. 
Here are a few examples:

- To run the script with the `configure-doxygen` and `detect-warnings-pre-fix` options:

```
python main.py -c -dw
```

- To run the script with all options:

```
python main.py -c -dw -iwdb -fdw -af -dwpf -pwdtf -gdhp -uwd
```

Please ensure to replace `python` with the correct Python command 
based on your Python installation and system configuration.



