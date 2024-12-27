import os
import re
import time
import numpy as np

start = time.time()

all_text = ""

for each_file in os.listdir("to_open"):
    with open(f"to_open/{each_file}", "r", errors="ignore") as file:
        text = file.read()

        m = r"[^A-Z]+"
        letters = re.sub(r"[^A-Z]+", " ", text.upper())
        spacing = re.sub(r"\s+", " ", letters).strip()

        all_text += f"{spacing} "


# tokenize
all_words = all_text.upper().split(" ")
unique_words, tokens = np.unique(all_words, return_inverse=True)


# get every possible sequential two-word combinations
combinations = np.repeat(tokens, 2)[1:-1].reshape((-1, 2))
unique_combinations, counts = np.unique(combinations, axis=0, return_counts=True)

next_word = {}

for i in zip(unique_words[unique_combinations], counts):
    current = i[0][0]
    next = i[0][1]
    times = i[1]
    try:
        next_word[current].append((next, times))
    except:
        next_word[current] = [(next, times)]

