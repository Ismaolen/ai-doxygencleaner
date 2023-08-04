import os
import config.config_variables
from ai_language_model.models.gpt_3_5_turbo import GPT3_5TurboModel
from transport_data.transport_data import load_data_from_json, save_data_to_json
import time
import threading
from pygments import highlight
from pygments.lexers import CppLexer
from pygments.formatters import TerminalFormatter
from dotenv import load_dotenv


class DoxygenWarningFixer(GPT3_5TurboModel):
    """
    DoxygenWarningFixer class for fixing Doxygen warnings.

    Methods
    -------
    run(args):
        Run the warning fixer based on the provided arguments.
    wait():
        Print waiting time every second.
    print_query(self, pos):
        Print the query that is sent to the OpenAI server and its corresponding response.
    _concat_warnings_details(self, header_file_name_pre_fix_list, file_content_pre_fix_list, warning_content_pre_fix_llist, warning_line_number_pre_fix_llist):
        Concatenate warning details to generate the prompt_input_str_list.
    _fix_warnings(self, prompt_input_str_list, prompt_instruction):
        Use the GPT model to fix the warnings and return the post-fix file content list.
    """

    def __init__(self, prompt_instruction="default_instruction", prompt_input_str="default_instruction",
                 api_key="default_instruction"):
        """
        Initialize the DoxygenWarningFixer object.

        Attributes
        ----------
        gpt : None
            To be defined GPT model instance.
        colored_prompt_input_str_list : list
            List to hold colored prompt strings for output.
        """
        super().__init__(prompt_instruction, prompt_input_str, api_key)
        self.colored_prompt_input_str_list = []

    def wait(self):
        """
        Print waiting time every second.

        Continuously prints elapsed waiting time every second as long as the thread is running.
        """
        wait_time = 0
        while getattr(threading.current_thread(), "do_run", True):
            time.sleep(1)
            wait_time += 1
            print(f'\033[1;34mWaiting for the response... Elapsed time: {wait_time} seconds...\033[0m')

    def print_query(self, pos):
        """
        Print the query that is sent to the OpenAI server and its corresponding response.

        Parameters
        ----------
        pos : int
            The position of the query in the sequence.
        """

        query_num = pos + 1

        # Print a separator to distinguish between queries
        print('\n\n')
        print(f"\033[1;35m====================== QUERY NUMBER: {query_num} =======================\033[0m\n")

        # More explicit message for sending the query
        print(f'\033[1;4;94mQuery content:\033[0m')
        print(f'\033[1;93m{self.prompt_instruction}\033[0m\n')
        print(f'{self.colored_prompt_input_str_list[pos]}\n')
        print(f'\033[1;36mSending query number {query_num} to OpenAI server:\033[0m')

        # Start the waiting thread
        wait_thread = threading.Thread(target=self.wait)
        wait_thread.start()

        self._send_query()

        # When the task is done, stop the waiting thread
        wait_thread.do_run = False
        wait_thread.join()

        # More explicit message for the received pre-validation response
        print(f'\n\n\n\033[1;93mPre-validation response for query number {query_num} received:\033[0m')
        print(f'\n{highlight(self._get_response_content(), CppLexer(), TerminalFormatter())}')

        self.validate_response_content()

        # More explicit message for the post-validation response
        print(f'\n\n\n\033[1;92mPost-validation response for query number {query_num} received:\033[0m\n')
        print(f'{highlight(self._get_response_content(), CppLexer(), TerminalFormatter())}\n')

    def _concat_warnings_details(self, header_file_name_pre_fix_list, file_content_pre_fix_list,
                                 warning_content_pre_fix_llist, warning_line_number_pre_fix_llist):
        """
        Concatenate warning details to generate the prompt_input_str_list.

        Parameters
        ----------
        header_file_name_pre_fix_list : list
            List of header file names before the fix.
        file_content_pre_fix_list : list
            List of file contents before the fix.
        warning_content_pre_fix_llist : list
            List of warning contents before the fix.
        warning_line_number_pre_fix_llist : list
            List of warning line numbers before the fix.

        Returns
        -------
        list
            List of warning details to be fixed.
        """
        # Initialization of the list to store concatenated warning details
        prompt_input_str_list = []
        for warning_line_number_list, warning_content_list, file_name, file_content_pre_fix, in zip(
                warning_line_number_pre_fix_llist,
                warning_content_pre_fix_llist,
                header_file_name_pre_fix_list,
                file_content_pre_fix_list):
            # Construct the warning detail string for each warning
            prompt_input_str = "Doxygen-Warnings:\n"
            # using ANSI escape sequences for coloring
            colored_prompt_input_str = f"\033[1;94mDoxygen-Warnings:\033[0m\n\n"
            for warning_content, warning_line_number, in zip(warning_content_list, warning_line_number_list):
                prompt_input_str += f'Line number:{warning_line_number} : {warning_content}\n'
                colored_prompt_input_str += f'\033[1;95mLine number:{warning_line_number}\033[0m : ' \
                                            f'\033[4;33m{warning_content}\033[0m\n'
            # Adding file name and content to the warning detail
            prompt_input_str += f'\nFile name: {file_name}\n\nFile content:\n{file_content_pre_fix}'
            colored_prompt_input_str += f'\n\033[1;91mFile name: \033[0m' \
                                        f'\033[4;32m{file_name}\033[0m\n\n' \
                                        f'\033[1;93mFile content:\033[0m\n\n' \
                                        f'{highlight(file_content_pre_fix, CppLexer(), TerminalFormatter())}\n'
            # Append the warning detail to the list
            prompt_input_str_list.append(prompt_input_str)
            self.colored_prompt_input_str_list.append(colored_prompt_input_str)  # add colored string to new list
        return prompt_input_str_list

    def _fix_warnings(self, prompt_input_str_list, prompt_instruction):
        """
        Use the GPT model to fix the warnings and return the post-fix file content list.

        Parameters
        ----------
        prompt_input_str_list : list
            List of concatenated warning details.
        prompt_instruction : str
            Instruction for the GPT model.

        Returns
        -------
        list
            List of file content after the fix.
        """

        # Initialize list to store fixed file content
        file_content_post_fix_list = []
        for pos, prompt_input_str in enumerate(prompt_input_str_list):
            # Initialize GPT model with provided API key
            self.set_prompt_instruction(prompt_instruction)
            self.set_prompt_input_str(prompt_input_str)
            self.create_prompt_content()
            self._set_api_key(os.getenv('OPEN_AI_API_KEY'))
            self.print_query(pos)

            # Get fixed content from the GPT model
            file_content_post_fix = self._get_response_content()
            # Append fixed content to the list
            file_content_post_fix_list.append(file_content_post_fix)
        return file_content_post_fix_list

    def run(self):
        """
        Run the warning fixer based on the provided arguments.

        This method loads the warning details from preprocessed_warnings_data.json, sends them to the GPT model,
        gets the fixed content, and saves the fixed content to postprocessed_warnings_data.json.
        """

        # Load the warning details from preprocessed_warnings_data.json
        data = load_data_from_json("transport_data/preprocessed_warnings_data.json")
        header_file_name_pre_fix_list = data["header_file_name_pre_fix_list"]
        file_content_pre_fix_list = data["file_content_pre_fix_list"]
        warning_content_pre_fix_llist = data["warning_content_pre_fix_llist"]
        warning_line_number_pre_fix_llist = data["warning_line_number_pre_fix_llist"]

        # Concatenate the warning details
        prompt_input_str_list = self._concat_warnings_details(header_file_name_pre_fix_list,
                                                              file_content_pre_fix_list,
                                                              warning_content_pre_fix_llist,
                                                              warning_line_number_pre_fix_llist)

        # Load the OpenAI key
        load_dotenv("config/api_key.env")

        # Use the GPT model to fix the warnings
        file_content_post_fix_list = self._fix_warnings(prompt_input_str_list,
                                                        config.config_variables.prompt_instruction)

        # Add the post-fix file content list to postprocessed_warnings_data.json
        data = {"file_content_post_fix_list": file_content_post_fix_list}
        save_data_to_json("transport_data/postprocessed_warnings_data.json", data)
