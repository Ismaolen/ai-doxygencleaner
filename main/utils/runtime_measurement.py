import re
import timeit


def remove_unwanted_line(str):
    """
    Removes unwanted lines from the model's response.
    """
    # Split the response content into separate lines
    lines = str.split("\n")

    # Remove any line that contains the words 'Please', 'I have added', or 'Explanation:'
    lines = [line for line in lines if
             'Please' not in line.strip() and 'I have added' not in line.strip() and 'Explanation:' not in line.strip()
             and '. Added' not in line.strip() and '. Fixed' not in line.strip() and '. Documented' not in line.strip()
             and '- Added' not in line.strip() and '- Fixed' not in line.strip() and '- Documented' not in line.strip()
             and '- Line' not in line.strip() and '- Provided' not in line.strip() and 'Note:' not in line.strip()
             and '- Used' not in line.strip() and 'Doxygen-Warnings:' not in line.strip() and 'Line number:' not in line.strip()]
    # Join the remaining lines back into a single string and set it as the response content
    return "\n".join(lines)


# Pre-compile the regex pattern outside the function for reuse
unwanted_start_phrases = [
    'Please', 'I have added', 'Explanation:', '\. Added', '\. Fixed', '\. Documented',
    '- Added', '- Fixed', '- Documented', '- Line', '- Provided', 'Note:',
    '- Used', 'Doxygen-Warnings:', 'Line number:'
]
pattern = r"^\s*(" + "|".join(unwanted_start_phrases) + r").*\n?"
compiled_regex = re.compile(pattern, re.MULTILINE)


# Re-defining the regex-based function
def remove_unwanted_lines_more_efficient(text: str) -> str:
    return compiled_regex.sub("", text).strip()


# Re-defining the dictionary-based function
def remove_unwanted_lines_with_dict(text: str) -> str:
    unwanted_start_phrases = {
        'Please', 'I have added', 'Explanation:', '. Added', '. Fixed', '. Documented',
        '- Added', '- Fixed', '- Documented', '- Line', '- Provided', 'Note:',
        '- Used', 'Doxygen-Warnings:', 'Line number:'
    }
    lines = [line for line in text.splitlines() if
             not any(line.strip().startswith(phrase) for phrase in unwanted_start_phrases)]
    return "\n".join(lines)


def measure_runtimes_for_different_lines(text_template: str):
    """
    Measure the runtime of the three functions for texts with varying number of lines.

    Parameters:
    - text_template (str): The template text to be repeated.

    Returns:
    - dict: A dictionary with line counts as keys and runtimes as values.
    """
    line_counts = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 1000000, 10000000]
    runtimes = {}

    for count in line_counts:
        test_text = text_template * (count // 9)  # Divide by 10 because text_template has 10 lines

        # Measure for remove_unwanted_line
        start_time = timeit.default_timer()
        remove_unwanted_line(test_text)
        remove_unwanted_line_time = timeit.default_timer() - start_time

        # Measure for remove_unwanted_lines_more_efficient
        start_time = timeit.default_timer()
        remove_unwanted_lines_more_efficient(test_text)
        regex_time = timeit.default_timer() - start_time

        # Measure for remove_unwanted_lines_with_dict
        start_time = timeit.default_timer()
        remove_unwanted_lines_with_dict(test_text)
        dict_time = timeit.default_timer() - start_time

        runtimes[count] = {
            "remove_unwanted_line": remove_unwanted_line_time,
            "regex_method": regex_time,
            "dict_method": dict_time
        }
        print(f"For {count} lines:\n"
              f"remove_unwanted_line took {remove_unwanted_line_time:.5f} seconds.\n"
              f"regex_method took {regex_time:.5f} seconds.\n"
              f"dict_method took {dict_time:.5f} seconds.\n"
              "---------------------------------------------")

    return runtimes


# Re-defining the test text
test_text_consecutive = """
#import <node.h>
/**
Line number:52 : warning: return type of member Notifications::Init is not documented

 */
/**
Doxygen-Warnings:
Line number:52 : warning: return type of member Notifications::Init is not documented
Line number:71 : warning: return type of member Notifications::Init is not documented
"""

runtimes = measure_runtimes_for_different_lines(test_text_consecutive)

"""
For 10 lines:
remove_unwanted_line took 0.00001 seconds.
regex_method took 0.00000 seconds.
dict_method took 0.00002 seconds.
---------------------------------------------
For 50 lines:
remove_unwanted_line took 0.00003 seconds.
regex_method took 0.00001 seconds.
dict_method took 0.00006 seconds.
---------------------------------------------
For 100 lines:
remove_unwanted_line took 0.00004 seconds.
regex_method took 0.00001 seconds.
dict_method took 0.00012 seconds.
---------------------------------------------
For 500 lines:
remove_unwanted_line took 0.00021 seconds.
regex_method took 0.00006 seconds.
dict_method took 0.00063 seconds.
---------------------------------------------
For 1000 lines:
remove_unwanted_line took 0.00039 seconds.
regex_method took 0.00010 seconds.
dict_method took 0.00124 seconds.
---------------------------------------------
For 5000 lines:
remove_unwanted_line took 0.00193 seconds.
regex_method took 0.00050 seconds.
dict_method took 0.00588 seconds.
---------------------------------------------
For 10000 lines:
remove_unwanted_line took 0.00380 seconds.
regex_method took 0.00108 seconds.
dict_method took 0.01218 seconds.
---------------------------------------------
For 50000 lines:
remove_unwanted_line took 0.01958 seconds.
regex_method took 0.00561 seconds.
dict_method took 0.06098 seconds.
---------------------------------------------
For 100000 lines:
remove_unwanted_line took 0.04078 seconds.
regex_method took 0.01022 seconds.
dict_method took 0.12191 seconds.
---------------------------------------------
For 1000000 lines:
remove_unwanted_line took 0.40735 seconds.
regex_method took 0.10590 seconds.
dict_method took 1.25409 seconds.
---------------------------------------------
For 10000000 lines:
remove_unwanted_line took 4.08598 seconds.
regex_method took 1.07782 seconds.
dict_method took 12.47559 seconds.
---------------------------------------------
"""