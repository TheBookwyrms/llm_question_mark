import os
from tqdm import *
import re
import numpy as np


def frequency_makers():
    all_sentences = ""

    for each_file in (os.listdir("to_open")):
        with open(f"to_open/{each_file}", "r", errors="ignore") as file:
            text = file.read()

            m = r"[^a-zA-Z]+"
            dots = re.sub(r"[..]+", " .", text)
            dots = re.sub(r"[\n]+", " ", text)
            line_break = re.sub(r"[.]+", " .", dots)
            letters = re.sub(r"[^a-zA-Z.]+", " ", line_break)
            spacing = re.sub(r"\s+", " ", letters).strip()

            all_sentences += f"{spacing} "


    # tokenize
    all_words = all_sentences.lower().split(" ")
    unique_words, tokens = np.unique(all_words, return_inverse=True)


    # get every possible sequential two-word combinations
    combinations = np.repeat(tokens, 2)[1:-1].reshape((-1, 2))
    unique_combinations, counts = np.unique(combinations, axis=0, return_counts=True)

    next_word = {}

    for i in (zip(unique_words[unique_combinations], counts)):
        current = str(i[0][0])
        next = str(i[0][1])
        times = int(i[1])
        try:
            next_word[current].append((next, times))
        except:
            next_word[current] = [(next, times)]
    
    return next_word

frequency_makers()