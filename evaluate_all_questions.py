import csv
import os

import config
from _3_run_llm_llama_cpp import ask_question
from common.file_utils import createFolderIfNotExists
from evaluations.evaluations import persist_evaluation


def evaluate_all_questions(channel_handle: str):
    questions_file_path = f"{config.evaluations_dir_path}/{channel_handle}/questions.csv"
    createFolderIfNotExists(questions_file_path)
    if not os.path.exists(questions_file_path):
        print("In order to evaluate all questions, you need to provide a questions.csv file in the evaluations "
              "directory. This will be done automatically when you start asking questions while you have evaluations "
              "enabled. To enable it, set evaluations_enabled = True in config. Check evaluations/readme.md for more.")
        print("You can also create the file manually and add questions to it.")
        exit(1)

    with open(questions_file_path) as questions_file:
        questions = csv.DictReader(questions_file)
        for question in questions:
            print(question["query"])
            rag_response = ask_question(question["query"], enable_vector_search=True, k=config.k)
            persist_evaluation(rag_response, k = config.k)


evaluate_all_questions("BenFelixCSI") # todo this channel is hardcoded now, implement other channels
