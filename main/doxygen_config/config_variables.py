
"""
This module defines the configuration parameters for Doxygen.

The `dox_config_parameters` variable is a list of tuples. Each tuple contains two elements:
    1. The Doxygen configuration parameter as a string, followed by '{}' and '='.
    2. The number of spaces to insert between the parameter and the '=' sign.

In the actual Doxygen configuration file, each parameter is followed by either 'YES' or 'NO'.
"""

dox_config_parameters = [
    ["INPUT{}=", 18],
    ["GENERATE_LATEX{}=", 9],
    ["GENERATE_HTML{}=", 10],
    ["WARNINGS{}=", 15],
    ["WARN_IF_UNDOCUMENTED{}=", 3],
    ["WARN_IF_DOC_ERROR{}=", 6],
    ["WARN_NO_PARAMDOC{}=", 7]
]

