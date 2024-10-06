import os
import json
import openai
from helper_functions import llm

# Load the JSON file
filepath = './data/feedback_mockdata.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_feedback = json.loads(json_string)
    print()


def identify_category(user_message):
    delimiter = "####"

    system_message = f"""
    You are tasked with categorizing customer feedback  for a library\
    The feebcack will be enclosed in
    the pair of {delimiter}.

    Decide if the feedback is relevant to any predefined categories
    in the Python dictionary below, which each key is a predefined category
    and the value is a list of sample feedback. Study the below dictionary:

    {dict_of_feedback}

    You may assign multiple categories to a single piece if appropriate. For each category assigned, identify and extract relevant keywords or phrases from the original text\
    that justify the categorization. Try to find and assign the best match that is closest to the predefined categories.
    Ouput should be in this json format: Key is the Category and the value is the relevant keywords or phrases
    
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    feedback_category = llm.get_completion_by_messages(messages)
    return feedback_category


def process_feedback_class(user_input):
    delimiter = "```"
    return identify_category(user_input)
   