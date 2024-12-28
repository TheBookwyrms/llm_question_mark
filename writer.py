import numpy as np
from collections import OrderedDict
from tqdm import *
import time

def write_paragraph(x_sentences, end_sent_freq, beg_sent_freq, next_word):
    # total_starters = 0
    # for key in beg_sent_freq:
    #     total_starters += beg_sent_freq[key]

    # start_probs = OrderedDict([(None, 0)])
    # for key in beg_sent_freq:
    #     lst = [d for d in zip(start_probs.keys(), start_probs.values())]
    #     start_probs[key] = lst[-1][1] + beg_sent_freq[key]

    # end_probs = OrderedDict([(None, 0)])
    # for key in end_sent_freq:
    #     lst = [d for d in zip(end_probs.keys(), end_probs.values())]
    #     end_probs[key] = lst[-1][1] + end_sent_freq[key]
    
    #print(start_probs)

    #try:
    paragraph = []
    for i in range (x_sentences):
        phrase = []

        word_probs = OrderedDict([(None, 0)])
        for key in tqdm(next_word):
            lst = [(None, 0)]
            for tuple in next_word[key]:
                tuple = (tuple[0], tuple[1]+lst[-1][1])
                lst.append(tuple)
            word_probs[key] = lst

        last_word = False

        while last_word == False:
            #try:
            try:
                possibilities = next_word[phrase[-1].lower()]
                prev = phrase[-1]
            except:
                possibilities = next_word["."]
                prev = "."

            try:
                word_num = np.random.randint(1, word_probs[prev][-1][1])
            except:
                word_num = 1

            d = -1
            #print(word_num)
            while word_num != d:
                for kv in word_probs[prev]:
                    if kv[1] == word_num:
                        word = kv[0]
                        word_num = d
                if word_num != d:
                    word_num += 1
            
            phrase.append(word)
            if word == ".":
                last_word = True

            #except:
            #    last_word = True
        
        phrase = " ".join(phrase)
        paragraph.append(phrase)
    #except:
    #    raise ValueError("no clue what's wrong")


    return paragraph
