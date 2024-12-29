import time
from tqdm import *
from frequency_makers import *
from writer import *

def main():
    start = time.time()
    next_word = frequency_makers()
    paragraph = write_paragraph(10, next_word)
    paragraph = " ".join(paragraph)
    end = time.time()

    print(paragraph)
    print(end-start)




main()