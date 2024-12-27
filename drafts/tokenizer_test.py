import numpy as np


input_text = "The quick brown fox jmups over the lazy dog"

# tokenize
all_words = input_text.upper().split(" ")
unique_words, tokens = np.unique(all_words, return_inverse=True)


# get every possible sequential two-word combinations
combinations = np.repeat(tokens, 2)[1:-1].reshape((-1, 2))
unique_combinations, counts = np.unique(combinations, axis=0, return_counts=True)

...
