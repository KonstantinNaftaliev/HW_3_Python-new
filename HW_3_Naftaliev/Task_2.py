# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """Носил прозвище Безумный (тур. Deli) ввиду психического заболевания. 
Мустафа I был единственным султаном в истории Османской империи, который дважды восходил на трон и дважды был с него свергнут."""
print(top_10_words(text))