# README.md

---

# Configuration Module
The configuration module contains all the necessary configurations for the 
application, including API keys, environment variables, paths and other configuration settings.


## Structure
Here is the structure of the module:
config\
├── Doxyfile\
├── README.md\
├── api_key.env\
├── config_paths.py\
├── config_variables.py\
└── db_local_variables.env

## Description of Files
### [`Doxyfile`](./Doxyfile)
The Doxyfile is a configuration [file](./Doxyfile) for Doxygen, a tool utilized for generating documentation 
from commented source code. It defines the settings and preferences for documentation 
generation. Each time the ai-doxygencleaner pipeline is triggered, this file is automatically 
generated and configured based on the [`dox_config_parameters`](./config_variables.py) variable.


### api_key.env
The api_key.env file stores the API keys required by the application.



### [`config_paths.py`](./config_paths.py)
The config_paths.py file is a Python script that includes configurations related to file paths, 
specifically defining the locations of data files, logs, and other resources used by the application.

### [`config_variables.py`](./config_variables.py)
The [`config_variables.py`](./config_variables.py) file is Python script that contains 
various application-wide settings. These settings may include flags to control application behavior, 
constants used throughout the application, and other types of configuration variables. 
The file houses two specific variables:
- `dox_config_parameters`: This variable houses settings that help configure the Doxyfile as needed.
- `prompt_instruction`: This variable contains the prompt instruction sent along with the query to the AI language model. 

### db_local_variables.env
The db_local_variables.env file stores local environment variables related to the database, 
including the database name, user, password, host, and port.

## How to Use
To utilize these configurations, import the appropriate Python files 
([`config_paths.py`](./config_paths.py) or [`config_variables.py`](./config_variables.py)) into your script, 
and access the configuration variables as necessary. 
As for the environment variables, they should be loaded 
into your environment prior to running your script. The Doxyfile is automatically generated and 
configured each time the pipeline starts. 
This file's configuration is dependent on the variable defined in the config_variables.py file. 
This variable can be modified to change the configuration if required.
