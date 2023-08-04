# README.md

---

## Directory Structure
```
transport_data
├── README.md
├── __init__.py
├── pipeline_id.json
├── postprocessed_warnings_data.json
├── preprocessed_warnings_data.json
└── transport_data.py
```

## Overview
The `transport_data` directory is part of the `ai_doxygen_cleaner` project. 
The primary role of this module is to handle the saving, loading, and 
updating of data in JSON format. The data is used to manage preprocessed 
and postprocessed warning data from Doxygen.

The `transport_data.py` script contains five primary functions:

- `save_data_to_json()`
- `load_data_from_json()`
- `add_data_to_json()`
- `load_pre_fix_data_from_json()`
- `load_post_fix_data_from_json()`

## `save_data_to_json(file_path: str, data_dict: dict) -> None`
This function takes a file path and a data dictionary as 
inputs and saves the dictionary in a JSON file at the specified file path. 

Example usage:
```python
save_data_to_json("path/to/file.json", {"key": "value"})
```

## `load_data_from_json(file_path: str) -> dict`
This function loads data from a JSON file and returns a 
dictionary. The input is the path to the JSON file.

Example usage:
```python
data = load_data_from_json("path/to/file.json")
```

## `add_data_to_json(file_path: str, new_data: dict) -> None`
This function adds new data to an existing JSON file. 
It takes a file path and a dictionary of new data as inputs.

Example usage:
```python
add_data_to_json("path/to/file.json", {"new_key": "new_value"})
```

## `load_pre_fix_data_from_json() -> tuple`
This function loads preprocessed warning data from the 
`preprocessed_warnings_data.json` file and returns a 
tuple containing the project folder path, header file 
names, file contents, warning numbers, warning contents,
and line numbers of the warnings.

Example usage:
```python
data = load_pre_fix_data_from_json()
```

## `load_post_fix_data_from_json() -> tuple`
This function loads postprocessed warning data from the 
`postprocessed_warnings_data.json` file and returns a 
tuple containing the project folder path, header file 
names, file contents, warning numbers, warning contents, 
and line numbers of the warnings.

Example usage:
```python
data = load_post_fix_data_from_json()
```

## JSON Files
The `transport_data` directory includes three JSON files:

- `pipeline_id.json`: Stores the pipeline ID data.
- `postprocessed_warnings_data.json`: Stores the postprocessed warning data.
- `preprocessed_warnings_data.json`: Stores the preprocessed warning data.

These files are used by the `transport_data.py` script 
to manage data across different stages of the Doxygen cleanup process.

## Summary
The `transport_data` directory is an essential part of the 
`ai_doxygen_cleaner` project, responsible for data 
storage and retrieval before and after processing Doxygen warnings.












