import time
from collections import defaultdict
import pandas as pd
from fuzzywuzzy import fuzz
from data_preprocess import extract_tokenize_from_doc

def load_key_words(path):
    df = pd.read_excel(path, header=None)
    df[0] = df[0].apply(str.lower)
    max_l = df[0].map(lambda x: len(x.split(' '))).max()
    return df[0].tolist(), max_l


def count_key_word(keywords, content):
    count_dict = defaultdict()
    for keyword in keywords:
        word_length = len(keyword.split(' '))
        count = 0
        left = 0
        while left < len(content)-word_length:
            word = ' '.join(content[left:left+word_length])
            probability = fuzz.ratio(keyword, word)
            if probability > 90:
                count+=1
                left += 1
            elif probability < 35:
                left += 2
            else:
                left += 1
        if count > 0:
            count_dict[keyword] = count

    return count_dict

if __name__ == '__main__':
    keywords, _ = load_key_words(r'./job_skills.xlsx')
    print(len(keywords))
    content = extract_tokenize_from_doc(r'./ChaoyuDeng_CV_2021.docx')
    start = time.time()
    count_dict = count_key_word(keywords,content)
    print(time.time() - start)
    print(content)
    count = 0
    for k in count_dict:
        print(k, count_dict[k])
        count+=count_dict[k]
    print(count)
