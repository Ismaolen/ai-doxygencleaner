"""
This module defines the configuration parameters for Doxygen.

The `dox_config_parameters` variable is a list of tuples. Each tuple contains two elements:
    1. The Doxygen configuration parameter as a string, followed by '{}' and '='.
    2. The number of spaces to insert between the parameter and the '=' sign.

In the actual Doxygen configuration file, each parameter is followed by either 'YES' or 'NO'.
"""

dox_config_parameters = [
    ["GENERATE_LATEX{}=", 9],
    ["GENERATE_HTML{}=", 10],
    ["WARNINGS{}=", 15],
    ["WARN_IF_UNDOCUMENTED{}=", 3],
    ["WARN_IF_DOC_ERROR{}=", 6],
    ["WARN_NO_PARAMDOC{}=", 7]
]

prompt_instruction = '''
1- Fix the following Doxygen-warnings.
2- Ensure that the revised comments are intelligible, detailed, comprehensive, meaningful and adhere to the Doxygen format.
3- Do not change the code, just add comments that resolve the Doxygen warnings, and then send me the complete code with the generated comments.
4- Do not add any new code to this code.
5- You are not allowed to add any code such as #ifndef or anything similar.
6- You are not allowed to change the code.
7- You are not allowed to add additional text like note other.
8- Provide the code without adding back-quotes at the beginning and end, so that I can copy it directly.
9- Do not forget to add Doxygen comments for the compound of the provided class.
10- Do not forget to add the return type '@return None' in Doxygen comments for void member functions.
'''
