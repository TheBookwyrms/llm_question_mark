import numpy as np
from collections import OrderedDict
from tqdm import *

def write_paragraph(x_sentences, end_sent_freq, beg_sent_freq, next_word):
    total_starters = 0
    for key in beg_sent_freq:
        total_starters += beg_sent_freq[key]

    start_probs = OrderedDict([(None, 0)])
    for key in beg_sent_freq:
        lst = [d for d in zip(start_probs.keys(), start_probs.values())]
        start_probs[key] = lst[-1][1] + beg_sent_freq[key]

    end_probs = OrderedDict([(None, 0)])
    for key in end_sent_freq:
        lst = [d for d in zip(end_probs.keys(), end_probs.values())]
        end_probs[key] = lst[-1][1] + end_sent_freq[key]
    

    try:
        paragraph = []
        for i in range (x_sentences):
            phrase = []
            starter = np.random.randint(1, total_starters)
            d = -1
            #print(starter)
            while starter != d:
                for kv in (zip(start_probs.keys(), start_probs.values())):
                    if kv[1] == starter:
                        word = kv[0]
                        starter = d
                if starter != d:
                    starter += 1
                
            phrase.append(word)

            last_word = False

            while last_word == False:
                try:
                    possibilities = next_word[phrase[-1]]

                    num_can = 0
                    for i in possibilities:
                        num_can += i[1]
                    
                    word_probs = OrderedDict([(None, 0)])
                    for key in tqdm(next_word):
                        lst = [d for d in zip(word_probs.keys(), word_probs.values())]
                        for tuple in next_word[key]:
                            word_probs[key] = lst[-1][1] + tuple[1]

                    word_num = np.random.randint(1, num_can)

                    d = -1
                    #print(word_num)
                    while word_num != d:
                        for kv in (zip(word_probs.keys(), word_probs.values())):
                            if kv[1] == word_num:
                                word = kv[0]
                                word_num = d
                        if word_num != d:
                            word_num += 1
                    
                    phrase.append(word)

                except:
                    last_word = True
            
            phrase = " ".join(phrase)
            paragraph.append(phrase)
    except:
        paragraph = None


    return paragraph
