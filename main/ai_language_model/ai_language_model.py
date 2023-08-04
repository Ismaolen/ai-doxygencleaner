from abc import ABC, abstractmethod


class AILanguageModel(ABC):
    """
    AILanguageModel is an abstract class that serves as a base for AI Language Models.
    This class outlines the fundamental methods and attributes derived AI language models should possess.

    ...

    Attributes
    ----------
    prompt_content : str
        The content of the prompt sent to the AI model.
    _response : any
        The raw response returned from the AI model.
    response_content : str
        The extracted content from the AI model response.
    prompt_instruction : str
        The instructions that guide the AI model's response.
    prompt_input_str : str
        The input string that the AI model will respond to.

    Methods
    -------
    _send_query():
        Sends a query to the AI model, including creating the prompt, creating the response,
        and setting and validating the response content.
    _get_response_content() -> str:
        Returns the content of the response from the AI model.
    _get_prompt_content() -> str:
        Returns the content of the prompt that was sent to the AI model.
    create_prompt_content():
        Creates the content of the prompt by concatenating the instruction and the input string.
    _create_response(prompt_content):
        Abstract method for creating a response, to be implemented by a specific AI model class.
    set_response_content():
        Abstract method for setting the response content, to be implemented by a specific AI model class.
    get_num_tokens_from_response(string: str, encoding_name: str) -> int:
        Abstract method for getting the number of tokens from a response,
        to be implemented by a specific AI model class.
    validate_response_content():
        Abstract method for validating the response content, to be implemented by a specific AI model class.
    """

    def __init__(self, prompt_instruction, prompt_input_str):
        """
        Initializes an AILanguageModel with given prompt instructions and input string.

        Parameters
        ----------
        prompt_instruction : str
            Instruction to guide the language model's response.
        prompt_input_str : str
            Initial input for the language model.
        """
        self.prompt_content = None
        self._response = None
        self.response_content = None
        self.prompt_instruction = prompt_instruction
        self.prompt_input_str = prompt_input_str

    def _send_query(self):
        """
        Sends a query to the AI model, including creating the response,
        and setting and validating the response content.
        """
        self._create_response(self.prompt_content)
        self.set_response_content()

    def _get_response_content(self) -> str:
        """
        Gets the processed content of the language model's response.

        Returns
        -------
        str
            Processed content of the language model's response.
        """
        return self.response_content

    def _get_prompt_content(self) -> str:
        """
        Gets the content of the language model prompt.

        Returns
        -------
        str
            the content of the prompt that was sent to the AI model.
        """
        return self.prompt_content

    def create_prompt_content(self):
        """
        Creates the content of the prompt by concatenating the instruction and the input string.
        """
        self.prompt_content = self.prompt_instruction + "\n" + self.prompt_input_str

    @abstractmethod
    def _create_response(self, prompt_content):
        """
        Creates a response from the language model. This is an abstract method that must be implemented in a subclass.

        Parameters
        ----------
        prompt_content : str
            Content of the language model prompt.
        """
        pass

    @abstractmethod
    def set_response_content(self):
        """
        Sets the processed content of the language model's response. This is an abstract method that must be
        implemented in a subclass.
        """
        pass

    def get_num_tokens_from_response(self, string: str, encoding_name: str) -> int:
        """
        Gets the number of tokens in the response. This is an abstract method that must be implemented in a subclass.

        Parameters
        ----------
        string : str
            String from which to count tokens.
        encoding_name : str
            Name of the encoding method to use.

        Returns
        -------
        int
            Number of tokens in the string.
        """
        pass

    def validate_response_content(self):
        """
        Method for validating the response content, to be implemented by a specific AI model class.
        """
        pass
