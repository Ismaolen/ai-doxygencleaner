# DoxygenWarningFixer

The `DoxygenWarningFixer` folder is part of the larger `ai_doxygen_cleaner` project. It contains a script 
`doxygen_warning_fixer.py` that hosts the `DoxygenWarningFixer` class, which is designed to detect and 
fix Doxygen warnings in your code documentation.

This folder structure is as follows:

```plaintext
DoxygenWarningFixer
├── README.md
├── __init__.py
└── doxygen_warning_fixer.py
```

The `doxygen_warning_fixer.py` file contains the logic for the Doxygen warning fixer.

## DoxygenWarningFixer Class

The `DoxygenWarningFixer` class is the main class responsible for detecting and fixing Doxygen warnings 
in the code documentation. It uses the GPT-3.5-turbo model from OpenAI for fixing the warnings. 
The class has the following methods:

### `__init__()`

This method is used to initialize the `DoxygenWarningFixer` object. It defines the GPT model 
instance (`self.gpt`) and initializes a list to hold colored prompt strings 
for output (`self.colored_prompt_input_str_list`).

### `wait()`

This method is used to print the elapsed waiting time every second as long as the thread is running. 
This is useful when you are waiting for a response from the OpenAI server.

### `print_query(pos)`

This method prints the query that is sent to the OpenAI server and its corresponding response. 
It takes one argument `pos` which represents the position of the query in the sequence.

### `_concat_warnings_details(...)`

This method concatenates warning details to generate the prompt_input_str_list. 
It accepts the following parameters:

- `header_file_name_pre_fix_list`: List of header file names before the fix.
- `file_content_pre_fix_list`: List of file contents before the fix.
- `warning_content_pre_fix_llist`: List of warning contents before the fix.
- `warning_line_number_pre_fix_llist`: List of warning line numbers before the fix.

It returns a list of warning details to be fixed.

### `_fix_warnings(prompt_input_str_list, prompt_instruction)`

This method uses the GPT model to fix the warnings and return the post-fix 
file content list. It takes two arguments:

- `prompt_input_str_list`: List of concatenated warning details.
- `prompt_instruction`: Instruction for the GPT model.

It returns a list of fixed file content.

### `run()`

This is the main method that orchestrates the warning fixing process. It loads the 
warning details from `preprocessed_warnings_data.json`, sends them to the GPT model, 
gets the fixed content, and saves the fixed content to `postprocessed_warnings_data.json`.

Remember, before you run the warning fixer, you need to set your 
OpenAI API key in the `config/api_key.env` file.

## Usage

To use the `DoxygenWarningFixer`, you simply need to create an instance of the class 
and call the `run()` method. Before you do this, make sure your OpenAI API key is set 
and the warning details are properly loaded in `preprocessed_warnings_data.json`. 
The warning details include the file names, file contents, warning contents, and warning line numbers.

```python
doxygen_fixer = DoxygenWarningFixer()
doxygen_fixer.run()
```

After running the warning fixer, you can find the fixed content in `postprocessed_warnings_data.json`.