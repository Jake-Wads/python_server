def triangle_number(n):
    return int((n * (n + 1)) / 2)

triangle_numbers = [triangle_number(n) for n in range(1, 31)]

import pandas as pd

letters = 'abcdefghijklmnopqrstuvwxyz'

def alphabetical_value(ch):
    if ch.lower() not in letters:
        return 0
    return letters.index(ch.lower()) + 1

words = open('/usr/share/dict/words').read().strip().split('\n')

df = pd.DataFrame(dict(word=words))
df['alpha_value'] = df.word.apply(lambda word: sum([alphabetical_value(ch) for ch in word]))
df.alpha_value.max()
df.alpha_value.isin(triangle_numbers).sum()