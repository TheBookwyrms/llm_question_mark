import numpy as np
from collections import OrderedDict
from tqdm import *
import time

def write_paragraph(x_sentences, next_word):
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

        rs = ''
        for index, word in enumerate(phrase):
            if word == ".":
                rs += "."
            else:
                if index == 0:
                    w_l = [w for w in word]
                    w_l[0] = w_l[0].upper()
                    word = "".join(w_l)
                else:
                    if word == "i":
                        word = "I"
                    word = " "+word
                rs += word
        paragraph.append(rs)

    return paragraph
