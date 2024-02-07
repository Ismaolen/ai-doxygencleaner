![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![GitHub](https://img.shields.io/badge/GitHub-ai--doxygencleaner-blue)
![Documentation](https://img.shields.io/badge/documentation-100%25-brightgreen)


# AI-DoxygenCleaner:

## Description
AI-DoxygenCleaner is a robust, AI-powered tool that simplifies and streamlines 
the management of Doxygen-generated documentation. This innovative project 
employs a comprehensive, step-by-step process to configure, detect, fix, 
and apply changes to Doxygen warnings, while meticulously documenting these 
changes for future review. The power of machine learning is harnessed to 
analyze, interpret, and resolve Doxygen warnings, providing developers 
with insightful and actionable solutions.

The tool is structured around one main Python file, `ai_doxygen_cleaner.py`, 
which carries out the primary operations. These operations encompass a wide 
range of functionalities from configuring Doxygen, detecting and inserting 
warnings into a database, to applying fixes using an AI language model. 
Following the application of fixes, the tool detects remaining warnings, 
prints detailed warning information to a file, generates a diff page in 
HTML format, and updates warning data in the database post-fix.

This comprehensive approach significantly improves the overall documentation 
quality and maintainability of software projects, reducing the need for 
manual intervention. This README file serves as a guide, detailing the 
structure of the project and the functionality of the classes and 
functions contained within, aiming to provide a clear understanding 
of the purpose and use of each component.



## Directory Structure
Here's the project structure for your understanding:

```text
ai-doxygencleaner
├── Dockerfile
├── README.md
├── documentation
├── logs
├── main
│   ├── DoxygenWarningFixer
│   │   ├── README.md
│   │   └── doxygen_warning_fixer.py
│   ├── README.md
│   ├── __init__.py
│   ├── ai_doxygen_cleaner
│   │   ├── README.md
│   │   └── ai_doxygen_cleaner.py
│   ├── ai_language_model
│   │   ├── README.md
│   │   ├── ai_language_model.py
│   │   └── models
│   │       └── gpt_3_5_turbo.py
│   ├── config
│   │   ├── Doxyfile
│   │   ├── README.md
│   │   ├── api_key.env
│   │   ├── config_paths.py
│   │   ├── config_variables.py
│   │   └── db_local_variables.env
│   ├── data
│   │   └── different_between_pre_and_post
│   │       ├── diff.html
│   │       ├── diff.txt
│   │       ├── output_post_fix.cpp
│   │       └── output_pre_fix.cpp
│   ├── db_operations
│   │   ├── README.md
│   │   ├── data_manipulation
│   │   │   ├── README.md
│   │   │   ├── insert_procedures.sql
│   │   │   └── update_procedures.sql
│   │   ├── db_insertion_handler.py
│   │   ├── main.sql
│   │   └── setup
│   │       ├── README.md
│   │       ├── create_table.sql
│   │       └── drop_tables_procedures.sql
│   ├── doxy_warning_post_processor
│   │   ├── README.md
│   │   └── doxy_warning_post_processor.py
│   ├── doxygen_management
│   │   ├── README.md
│   │   ├── doxy_warning_detector.py
│   │   ├── doxyfile_configurator.py
│   │   └── file_handler.py
│   ├── error_handler
│   │   ├── README.md
│   │   └── error_handler.py
│   ├── main.py
│   ├── print_data
│   │   ├── README.md
│   │   └── print_data.py
│   ├── transport_data
│   │   ├── README.md
│   │   ├── pipeline_id.json
│   │   ├── postprocessed_warnings_data.json
│   │   ├── preprocessed_warnings_data.json
│   │   └── transport_data.py
│   └── utils
│       ├── README.md
│       └── utils.py
└── update_docker_image.sh

19 directories, 49 files
```

## ai_doxygen_cleaner.py Overview

This file is the heart of the AI-DoxygenCleaner. It contains the AI-DoxygenCleaner 
class that performs all the operations related to the management of Doxygen-generated documentation. 

The class consists of the following key methods:
1. **configure_doxygen_files:** This method starts the process by configuring the 
Doxygen files. It creates and configures a Doxyfile using a DoxyfileConfigurator 
object.

2. **detect_warnings_pre_fix:** This method is responsible for detecting Doxygen warnings 
before any fixes are applied. It uses a DoxyWarningDetector object to carry out the 
detection process. The warnings and associated details are saved to a json file for later use.

3. **insert_warnings_to_db:** This method inserts the details of the detected warnings 
into a database. The data for this process is loaded from the previously created json file.

4. **fix_doxygen_warning:** This method applies fixes to the Doxygen warnings 
using a DoxygenWarningFixer object.

5. **apply_fix:** This method applies the suggested fixes to the header files 
in the doxygen_projects folder. 

6. **detect_warnings_post_fix:** This method detects Doxygen warnings after 
the fixes have been applied using a WarningPostProcessor object.

7. **print_pre_post_fix_data_to_file:** This method writes the warning 
details before and after the fix to a file, to give a clear comparison of changes made.

8. **generate_html_diff_page:** This method generates an HTML page displaying 
the differences between the Doxygen warning details before and after the fixes have been applied.

9. **update_warnings_details_post_fix_in_db:** This method updates the 
warning details in the database after the fixes have been applied.

### Note
Each of the methods follows a similar pattern of operations: initializing a 
specific object related to the task at hand, executing the task, and then printing a 
confirmation message to the console indicating the successful completion of the task.





## Getting Started
To utilize this tool, import the `AIDoxygenCleaner` class from the 
`ai_doxygen_cleaner.py` file. You can then create an instance of the class and 
call the desired methods on this instance.

```python
from ai_doxygen_cleaner import AIDoxygenCleaner

# Create instance
cleaner = AIDoxygenCleaner()

# Call desired methods
cleaner.configure_doxygen_files()
cleaner.detect_warnings_pre_fix()
# ... and so on ...
```

Each method is meant to be called in sequence, as each one builds upon 
the actions of the previous method.

Please refer to the method documentation in the `ai_doxygen_cleaner.py` 
file for more detailed information about each function, its parameters, and what it does.

For a deeper understanding of the project and how to use it, please refer to the full documentation.





### Key Directories and Files:

- **main**: This directory is the heart of the project where all the core functionality 
lies. It contains several subdirectories, each dedicated to a specific aspect of 
the Doxygen warning management.
  - **DoxygenWarningFixer**: This module is responsible for fixing the Doxygen warnings.
  - **ai_doxygen_cleaner**: This module handles the overall management of Doxygen warnings.
  - **ai_language_model**: This is where the AI model for language processing resides.
  - **config**: Contains configuration files for the application.
  - **data**: Stores data related to pre and post warning fix.
  - **db_operations**: Contains files related to database operations.
  - **doxygen_management**: This module is dedicated to managing 
  Doxygen configurations and warnings.
  - **error_handler**: Handles errors throughout the application.
  - **print_data**: This module helps in printing warning details to a file.
  - **transport_data**: Used for storing and transporting data across the pipeline.
  - **utils**: Contains utility functions used across the application.
- **main.py**: The main script for executing the Doxygen Warning Manager tool.
- **Dockerfile**: Contains Docker instructions to build the application's image.
- **update_docker_image.sh**: A shell script to update the Docker image of the application.
- **docs**: Contains all the documentation related files.
- **logs**: Logs produced by the application will be stored here.




## How to Run

To run the main.py script, navigate to the 'main' directory 
and execute the following command in the terminal:

```bash
python3 main.py --configure-doxygen --detect-warnings-pre-fix --insert-warnings-db \
--fix-doxygen-warnings --apply-fix --detect-warnings-post-fix \
--print-warning-details-to-file --generate-html-diff-page --update-warning-data-in-db
```

Each option corresponds to a specific operation:

- `-c, --configure-doxygen`: Configure Doxygen using predefined configuration parameters.
- `-dw, --detect-warnings-pre-fix`: Detect Doxygen warnings in the specified project.
- `-iwdb, --insert-warnings-db`: Insert detected Doxygen warnings into the database.
- `-fdw, --fix-doxygen-warnings`: Attempt to fix detected Doxygen warnings using an AI language model.
- `-af, --apply-fix`: Apply suggested fixes from the AI language model to the original header files.
- `-dwpf, --detect-warnings-post-fix`: Re-run Doxygen to detect warnings after the fixes have been applied.
- `-pwdtf, --print-warning-details-to-file`: Print details of pre and post-fix warnings to a file.
- `-gdhp, --generate-html-diff-page`: Generate an HTML diff page to visualize changes made by the fix application.
- `-uwd, --update-warning-data-in-db`: Update the warning data in the database after applying fixes.

Please select the options that best meet your needs.

**Note**: 
The options `-iwdb, --insert-warnings-db` and `-uwd, --update-warning-data-in-db` 
aren't essential to run the AI Doxygen Cleaner tool. They exist solely for 
storing the resulting data in a database and managing it for the purposes 
of academic research. Consequently, installing MySQL isn't a requirement 
and isn't necessary for the operation of the tool. However, it's important 
to observe the specified order of the arguments to ensure 
the correct functioning of the tool.

## Documentation

The project's documentation employs the `Numpydoc` style, 
a flexible and detailed documentation standard that enjoys 
broad use within the Python community. Every directory 
contains a `README` file that elucidates the functions, 
classes, and overall purpose of its contents. This 
project's comprehensive documentation is designed to 
guide you through each facet of the application, 
ensuring you comprehend the role and usage of each 
individual function and class.



In addition to this, the [documentation](./documentation) folder 
contains both  LaTeX and HTML versions of the  `ai_doxygencleaner` Python code's documentation.
- **View the most recent LaTeX documentation**: 
<u>**<a href="https://gitlab.com/ismsh/ai-doxygencleaner/-/jobs/4810045439/artifacts/file/public/latex/ai-doxygencleaner.pdf" target="_blank"> click here</a>**</u>
- **View the most recent HTML documentation**: 
<u>**<a href="https://ismsh.gitlab.io/-/ai-doxygencleaner/-/jobs/4810045439/artifacts/public/html/index.html" target="_blank"> click here</a>**</u>

These resources, created from Numpydoc strings, 
can further assist your understanding of the code. 
This documentation was generated using the `Sphinx tool`
and contains no warnings, thereby ensuring 
its accuracy and reliability. 

## Dockerization and Image Updating

AI-DoxygenCleaner is dockerized and can be run within a Docker container. A `Dockerfile` 
is provided in the project directory for creating a Docker image. This Docker 
image is based on the latest version of Alpine Linux and includes all necessary 
dependencies such as Python3, Doxygen, pip, and other dependencies. It also 
installs Python and Node.js packages that are necessary for running AI-DoxygenCleaner.

You can build and push the Docker image to your registry as follows:

1. Ensure Docker is installed and properly configured on your system.

2. Navigate to the project directory containing the Dockerfile.

3. Run the `update_docker_image.sh` script to build and update the Docker image:

    ```bash
    ./update_docker_image.sh
    ```

The script performs the following steps:

- It builds a new Docker image with the tag `doxycleaner`.
- It tags the new image with the tag 
`registry.gitlab.com/ismsh/ai-doxygencleaner/doxycleaner:latest`.
- It logs in to your Docker registry (you will be prompted to 
enter your login credentials).
- It pushes the new Docker image to your Docker registry.

Make sure you have the appropriate permissions to push images 
to the specified Docker registry. You can customize the 
script to suit your specific requirements and environment 
by modifying the Docker registry path and other parameters.







## Pipeline Configuration

The pipeline configuration can be found in the `.gitlab-ci.yml` file. 
This file includes instructions for different pipeline stages 
such as `build_fix`, `apply_fix`, `test_fix` and `pages`. 
All these stages help automate the Doxygen warning 
management process in CI/CD pipeline.


#### The tool requires:

- **Python 3.8** or later version to be installed in your system. 

- **Doxygen** should be installed and configured appropriately in your 
* system to run the Doxygen warning detection part of the pipeline. \
#### Optional:
- **GitLab** or any other CI/CD platform where you can run your CI/CD pipelines.
- **Docker** if you wish to run the application as a Docker container. 
- **MySQL** Database Server to store Doxygen warning related information.


## Platform Compatibility

The AI Doxygen Cleaner tool is built to be platform-independent. 
Its compatibility extends to any operating system capable of 
supporting Python, Doxygen, and Node.js (required for installing diff2html). 
This makes it highly versatile, covering Windows, Linux, and macOS environments.

If your project is hosted on GitLab and follows a CI/CD pipeline, 
the AI Doxygen Cleaner tool offers additional convenience. To use it 
in this context, ensure Docker is installed in your environment. 
You can then run the `update_docker_image.sh` script, which 
updates the Docker image. Once these steps are done, every 
time you commit changes to your GitLab repository, the tool's 
operations will be automatically triggered via the provided `.gitlab-ci.yml` file.

Remember that appropriate permissions and settings should be 
in place on GitLab to allow for this automatic execution. 
The `.gitlab-ci.yml` and Docker settings can be customized 
to fit your project's specific requirements.


## Troubleshooting

If you run into any issues during the setup or operation of the tool, 
I recommend consulting the `ISSUES` tab in the project repository. 
Here, you can explore solutions to previous issues and pose new questions. 
If the issue persists, don't hesitate to open a new issue detailing 
the problem you're encountering. I will strive to resolve it as promptly as possible.

To facilitate easier navigation, issues are categorized with labels, 
simplifying the process of finding solutions for specific problems. 
This troubleshooting section is continuously updated to encompass 
solutions to all potential issues. If you're unable to find a 
solution to your problem, please feel free to reach out directly. I'm here to assist.

## Contacts

Should you require additional assistance, or if you wish to share 
feedback, propose new ideas, or discuss potential collaborations, 
don't hesitate to contact me via the `ISSUES` tab in the project 
repository. Your contributions can significantly impact the continuous 
improvement of this project, and they are always appreciated.



