# README.md

---
# AI Language Model

The `ai_language_model` module contains classes designed for interacting with AI language models. 
These classes support a variety of functionalities such as sending queries to the model, 
creating prompts and responses, and validating the content of the model's responses.

## Structure

The module is structured as follows: \
ai_language_model\
├── ai_language_model.py\
└── models\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; └── gpt_3_5_turbo.py


## `AILanguageModel` class

This file contains the abstract base class `AILanguageModel` which outlines the fundamental methods and attributes that 
a derived AI language model should possess. 

The `AILanguageModel` class, defined in the ai_language_model.py file, is an abstract base class that 
outlines the fundamental methods and attributes that derived AI language models should possess.
More details can be found in the [file](./ai_language_model.py) itself.


### Methods:
1. `_send_query()`: Sends a query to the AI model, creates the response, and sets and validates the response content.
2. `_get_response_content()`: Returns the content of the AI model's response.
3. `_get_prompt_content()`: Returns the content of the prompt sent to the AI model.
4. `create_prompt_content()`: Creates the content of the prompt by concatenating the instruction and the input string.
5. `_create_response(prompt_content)`: An abstract method for creating a response that should be 
implemented by a specific AI model class.
6. `set_response_content()`: An abstract method for setting the response content that should 
be implemented by a specific AI model class.
7. `get_num_tokens_from_response(string, encoding_name)`: An abstract method for getting the 
number of tokens from a response that should be implemented by a specific AI model class.
8. `validate_response_content()`: An abstract method for validating the response content 
that should be implemented by a specific AI model class.




## models/`GPT3_5TurboModel` class
The `GPT3_5TurboModel` class, defined in the `gpt_3_5_turbo.py` file within the `models` folder, extends 
the `AILanguageModel` class. It is specifically designed to handle interactions with OpenAI's GPT-3.5 Turbo model.


This file contains the class `GPT3_5TurboModel` which extends the abstract base class `AILanguageModel` and is 
specifically designed to handle interactions with the OpenAI's GPT-3.5 Turbo model. This class provides 
methods to create a response, set and validate the response content, count tokens in a response, and 
remove certain elements from the response. More details can be found in the [file](./models/gpt_3_5_turbo.py) itself.

### Methods:
`_create_response(prompt_content)`: Creates a response from the GPT-3.5 Turbo model using the given prompt content.
`validate_response_content()`: Validates the content of the model's response and performs necessary modifications.
`set_response_content()`: Sets the processed content of the model's response.
`get_num_tokens_from_response(string, encoding_name)`: Counts the number of tokens in a given string.
`remove_back_quote()`: Removes backquote encapsulated strings from the model's response.
`remove_cpp_directives()`: Removes C++ directive lines from the model's response.
`remove_unwanted_line()`: Removes unwanted lines from the model's response.

This class enables the interaction with the model, the formatting and validation of the 
responses, and also contains utility functions for token counting and line removal.


## How to Use
To use these classes, instantiate the appropriate class (`AILanguageModel` or `GPT3_5TurboModel`), pass the required 
parameters during initialization, and call the desired methods. Note that the `AILanguageModel` class 
is abstract and is intended to be extended by concrete classes (like `GPT3_5TurboModel`) that implement its abstract methods.


To use this code, you will also need to provide your `OpenAI API key` which is used to authenticate requests 
to the OpenAI API. The API key should be passed when creating an instance of the `GPT3_5TurboModel` class.

