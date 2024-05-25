from utils.jamo import jamo_to_word, word_to_jamo
from utils.mecab import extract_morphs
from tqdm import tqdm
import pandas as pd

df = pd.read_excel('projects.xlsx')
# print(' '.join(df.iloc[0].values.astype(str)))  

def tokenize_by_jamo(text):
    return [word_to_jamo(word) for word in extract_morphs(text)]


tokenized_data = []

# print(' '.join(df.values[0].astype(str)))

for sample in df.values:
    tokenized_sample = tokenize_by_jamo(' '.join(sample.astype(str)))
    # print(tokenized_sample)
    tokenized_data.append(tokenized_sample)

print(tokenized_data[0])


with open('tokenized_data.txt', 'w', encoding='utf-8') as out:
    for line in tqdm(tokenized_data, unit=' line'):
        out.write(' '.join(line) + '\n')
