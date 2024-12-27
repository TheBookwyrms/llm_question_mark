import os
from tqdm import *
import re
import numpy as np


def frequency_makers():
    end_sent_freq = {}
    beg_sent_freq = {}

    for each_file in (os.listdir("to_open")):
        with open(f'to_open/{each_file}', "r", errors='ignore') as file:
            text = file.read()

            t = [t if t.upper() in ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M", ".", " "] else "." if t.upper() in ["!", "?"] else "" for t in text]
            text = "".join(t)

            b = [text[i] for i in range(len(text)) if text[i] != "\n"]
            c = "".join(b)
            phrases = c.split(".")
            phrases = [phrase for phrase in phrases if phrase != ""]
            for phrase in (phrases):
                words = phrase.split(" ")
                words = [w for w in words if w != '']
                for index, word in (enumerate(words)):
                    if index == 0:
                        try:
                            beg_sent_freq[word] += 1
                        except:
                            beg_sent_freq[word] = 1
                    try:
                        c = words[index+1]
                    except:
                        try:
                            end_sent_freq[word] += 1
                        except:
                            end_sent_freq[word] = 1




    all_text = ""

    for each_file in (os.listdir("to_open")):
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

    for i in tqdm(zip(unique_words[unique_combinations], counts)):
        current = str(i[0][0])
        next = str(i[0][1])
        times = int(i[1])
        try:
            next_word[current].append((next, times))
        except:
            next_word[current] = [(next, times)]


    #print(next_word)


    # next_word = {}
    # possibilities = list(set(next_words))




    # for key in tqdm(next_words):
    #     tuples_lst = []
    #     for word in (possibilities):
    #         a_count = next_words[key].count(word)
    #         if a_count != 0:
    #             tuples_lst.append((word, a_count))
    #     next_word[key] = tuples_lst










    # # NOTE > slightly slower version ?
    # import concurrent.futures

    # def analyse_next_words(key):
    #     tuples_lst = []
    #     #tuples_lst = [(word, count) for word in possibilities if count != 0]
    #     for word in (possibilities):
    #         a_count = next_words[key].count(word)
    #         if a_count != 0:
    #             tuples_lst.append((word, a_count))
    #     next_word[key] = tuples_lst
    #     return next_word

    # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     future_to_map = {executor.submit(analyse_next_words, key): key for key in tqdm(next_words)}
    #     for future in tqdm(concurrent.futures.as_completed(future_to_map)):
    #         pass # progress bar for counting futures




    #print(next_word)
    
    return end_sent_freq, beg_sent_freq, next_word