import time
from tqdm import *
from frequency_makers import *
from guide_llm_freqs import *
from writer import *
import os


def print_time_from(start):
    end = time.time()
    print(end-start)

def main():
    start = time.time()
    next_word = frequency_makers()
    end = time.time()
    print_time_from(start)
    full = []
    for i in range(5):
        paragraph = write_paragraph(10, next_word)
        paragraph = " ".join(paragraph)
        full.append(paragraph)
        full.append("\n")
        full.append("\n")
        name = f"{paragraph[:10]}"
        #with open(f"to_open/{name}.txt", "w+") as n:
        #    n.write(paragraph)

    full = " ".join(full)
    
    print(full)
    print_time_from(start)



main()