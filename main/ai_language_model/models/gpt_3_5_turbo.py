import re

from ai_language_model.ai_language_model import AILanguageModel
import openai
import tiktoken


class GPT3_5TurboModel(AILanguageModel):
    """
    This class extends the AILanguageModel class and is specifically designed to
    handle interaction with the GPT-3.5 Turbo model provided by OpenAI. It enables
    communication with the model, formatting and validation of the responses, and
    also contains utility functions for token counting and line removal.
    ...

    Attributes
    ----------
    __api_key : str
        The OpenAI API key used to authenticate requests to the API.

    Methods
    ----------
    _create_response(prompt_content):
        Creates a response from the GPT-3.5 Turbo model using the given prompt content.
    validate_response_content():
        Validates the content of the model's response and performs necessary modifications.
    set_response_content():
        Sets the processed content of the model's response.
    get_num_tokens_from_response(string: str, encoding_name: str) -> int:
        Counts the number of tokens in a given string.
    remove_back_quote():
        Removes backquote encapsulated strings from the model's response.
    remove_cpp_directives():
        Removes C++ directive lines from the model's response.
    remove_unwanted_line():
        Removes unwanted lines from the model's response.
    _set_api_key(self, api_key):

    set_prompt_input_str(self, prompt_input_str):

    set_prompt_instruction(self, prompt_instruction):

    """

    def __init__(self, prompt_instruction, prompt_input_str, api_key):
        """
        Constructs all the necessary attributes for the GPT3_5TurboModel object.

        Parameters
        ----------
        prompt_instruction : str
            The instruction to guide the language model's response.
        prompt_input_str : str
            The initial string input for the language model.
        api_key : str
            The OpenAI API key to be used for making API requests.
        """
        super().__init__(prompt_instruction, prompt_input_str)
        self.__api_key = api_key

    def _set_api_key(self, api_key):
        # Setting the OpenAI API key for requests
        self.__api_key = api_key
        openai.api_key = self.__api_key

    def set_prompt_input_str(self, prompt_input_str):
        self.prompt_input_str = prompt_input_str

    def set_prompt_instruction(self, prompt_instruction):
        self.prompt_instruction = prompt_instruction

    def _create_response(self, prompt_content):
        """
        Calls the OpenAI API and generates a response using the GPT-3.5 Turbo model.

        Parameters
        ----------
        prompt_content : str
            Content of the language model prompt.

        References
        ----------
        1. OpenAI. (no date). API Documentation: Making Requests. OpenAI Platform. Available at:
            https://platform.openai.com/docs/api-reference/making-requests. Accessed on July 8, 2023.

        """
        # Create a message that consists of the role (user) and content
        # (input string = prompt_instruction + prompt_input_str )
        # Configure the model parameters such as temperature, top_p, frequency_penalty,
        # and presence_penalty The response from the model is stored in self.response
        self._response = openai.ChatCompletion.create(
            # model="gpt-3.5-turbo-0613",
            model="gpt-3.5-turbo-0613",
            messages=[
                {"role": "user", "content": prompt_content}
            ],
            temperature=0.2,
            top_p=0.9,
            frequency_penalty=0.5,
            presence_penalty=0.5
        )

    def validate_response_content(self):
        """
        Validates the content of the model's response and performs necessary modifications like removing backquotes and
        unwanted lines, and C++ directives.
        """
        # Performing validation and modification operations on the response content
        self.remove_back_quote()
        self.remove_unwanted_line()
        # self.remove_cpp_directives()

    def set_response_content(self):
        """
        Sets the content of the model's response by extracting the relevant portion
        from the model's response.

        """
        # The 'content' key from the 'message' dictionary of the first choice from the 'choices' list
        # in the response is extracted and set as the response_content
        self.response_content = self._response['choices'][0]['message']['content']

    def get_num_tokens_from_response(self, string: str, encoding_name: str) -> int:
        """
        Counts the number of tokens in a given string using OpenAI's tiktoken library.

        Parameters
        ----------
        string : str
            The string from which tokens are to be counted.
        encoding_name : str
            The name of the encoding method to be used for token counting.

        Returns
        -------
        int
            The number of tokens in the input string.

        openai-cookbook/examples
        References
        ----------
        1. OpenAI Cookbook. (no date). How to count tokens with tiktoken. GitHub. Available at:
            https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
            Accessed on July 8, 2023.
        2. OpenAI. (no date). tiktoken. GitHub. Available at:
            https://github.com/openai/tiktoken/blob/main/tiktoken/model.py Accessed on July 8, 2023.
        3. OpenAI. (no date). Tokenizer. OpenAI Platform. Ac Available at:
            https://platform.openai.com/tokenizer Accessed on July 8, 2023.
        """

        encoding = tiktoken.encoding_for_model(encoding_name)
        num_tokens = len(encoding.encode(string))
        return num_tokens

    def remove_back_quote(self):
        """
        Removes lines containing backquote encapsulated strings from the model's response.
        """
        # Split the response content into separate lines
        lines = self.response_content.split("\n")

        # Remove any line that contains the '```cpp' or '```' string
        lines = [line for line in lines if "```cpp" not in line and "```" not in line]

        # Join the remaining lines back into a single string and set it as the response content
        self.response_content = "\n".join(lines)

    def remove_cpp_directives(self):
        """
        Removes C++ directive lines from the model's response.
        """
        # List of C++ directives to be removed
        cpp_directives = ['#ifndef', '#define', '#endif']

        # Split the response content into separate lines
        lines = self.response_content.split("\n")

        # Remove any line that starts with a C++ directive
        cleaned_lines = [line for line in lines if
                         not any(line.strip().startswith(directive) for directive in cpp_directives)]

        # Join the remaining lines back into a single string and set it as the response content
        self.response_content = "\n".join(cleaned_lines)

    def remove_unwanted_line(self):
        """
        Removes unwanted lines from the model's response using regex in multiline mode for better efficiency.
        Further details and examples can be found in /utils/runtime_measurement.py.
        """

        # Define a list of phrases that, if they appear at the start of a line, mean the line should be removed.
        # This centralizes the unwanted phrases, making it easier to manage and update them in the future.
        unwanted_start_phrases = [
            'Please', 'I have added', 'Explanation:', '\. Added', '\. Fixed', '\. Documented',
            '- Added', '- Fixed', '- Documented', '- Line', '- Provided', 'Note:',
            '- Used', 'Doxygen-Warnings:', 'Line number:', 'File name:', 'File content:', "Let's fix",
            'The added', "Sure, I'll", "This revised", "Here's the", "The provided", 'I hope', 'Here is'
        ]

        # Construct a regex pattern to match lines that start with any of the unwanted phrases.
        # The '^' asserts position at the start of a line, and '\s*' matches any whitespace at the beginning of a line.
        # The '.*\n' matches the rest of the line including the newline character.
        # Using '|'.join(...) creates a pattern that matches any one of the phrases in the list.
        pattern = r"^\s*(" + "|".join(unwanted_start_phrases) + r").*\n?"

        # Compile the regex pattern for faster execution and enable multiline mode.
        # The multiline mode makes '^' and '$' match the start/end of each line (not just start/end of the string).
        regex = re.compile(pattern, re.MULTILINE)

        # Use the compiled regex to remove all lines that start with any of the unwanted phrases.
        # The sub() method replaces lines matching the unwanted phrases with an empty string, removing them.
        # Finally, strip() removes any extraneous whitespace from the updated content.
        self.response_content = regex.sub("", self.response_content).strip()
