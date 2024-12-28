import time
from tqdm import *
from frequency_makers import *
from writer import *

def main():
    start = time.time()
    end_sent_freq, beg_sent_freq, next_word = frequency_makers()
    #print(end_sent_freq)
    #print(beg_sent_freq)
    #print(next_word["."])
    
    #print(beg_sent_freq)
    #print(end_sent_freq)
    #for item in next_words.items():
    #    print(item)
    paragraph = write_paragraph(10, end_sent_freq, beg_sent_freq, next_word)
    paragraph = " ".join(paragraph)
    end = time.time()

    print(paragraph)
    print(end-start)




main()