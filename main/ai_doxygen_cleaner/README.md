# README.md

---

# AIDoxygenCleaner

The `AIDoxygenCleaner` class handles the various phases of 
warning management, including detection, fixing, and application of fixes.

## Directory Structure
```
ai_doxygen_cleaner
├── README.md
├── __init__.py
└── ai_doxygen_cleaner.py
```

## AIDoxygenCleaner Class

Located in the `AIDoxygenCleaner.py` file, the `AIDoxygenCleaner` 
class consists of the following methods:

### `detect_warnings_pre_fix()`

This method is responsible for detecting Doxygen warnings before any fixes have 
been applied. It uses the `DoxyWarningDetector` to detect warnings and saves 
the warnings to a JSON file.

### `insert_warnings_to_db()`

This method is responsible for loading the pre-fix warnings from a JSON 
file and inserting these warnings into a database.

### `fix_doxygen_warning()`

This method uses the `DoxygenWarningFixer` class to fix the detected Doxygen warnings.

### `apply_fix()`

This method uses the `WarningPostProcessor` to apply the fixes to the warnings.

### `detect_warnings_post_fix()`

This method detects any Doxygen warnings that still exist after the fixes have 
been applied. It uses the `WarningPostProcessor` to detect post-fix warnings.

### `print_pre_post_fix_data_to_file()`

This method prints the details of the warnings before and after the fixes 
were applied to a file. It uses the `FileHandler` for handling the printing operation.

### `generate_html_diff_page()`

This method generates an HTML diff page to display the differences between 
the warnings before and after the fixes have been applied.

### `update_warnings_details_post_fix_in_db()`

This method updates the warnings' details in the database after the fixes 
have been applied.

Each of these methods corresponds to a phase in the handling of Doxygen 
warnings. They are designed to be called in order, progressing through 
the detection, fixing, and application of fixes to Doxygen warnings.

Please note that this class is meant to be used as a part of a larger 
system, and its methods are not intended to be used standalone.
```
# Example of How to Use the AIDoxygenCleaner Functions

You can use the functions provided in the AIDoxygenCleaner class as follows:

```python
from doxygen_warning_manager import AIDoxygenCleaner

# create an instance of the AIDoxygenCleaner
manager = AIDoxygenCleaner()

# perform the Doxygen configuration
manager.doxygen_configuration()

# detect warnings before applying any fixes
manager.detect_warnings_pre_fix()

# insert detected warnings into the database
manager.insert_warnings_to_db()

# fix the detected Doxygen warnings
manager.fix_doxygen_warning()

# apply the fixes
manager.apply_fix()

# detect warnings after the fixes have been applied
manager.detect_warnings_post_fix()

# print pre- and post-fix data to file
manager.print_pre_post_fix_data_to_file()

# generate an HTML page showing differences between the pre- and post-fix data
manager.generate_html_diff_page()

# update the warning details in the database after applying the fixes
manager.update_warnings_details_post_fix_in_db()
```

Make sure to import the `AIDoxygenCleaner` class from the 
`ai_doxygen_cleaner` module as shown above.

Note: Depending on your specific use case, you may need to use these 
functions in a different order or use only a subset of them. 
The example above shows how to use all the functions provided 
in the `AIDoxygenCleaner` class.
























