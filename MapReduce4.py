import time
import re
from collections import Counter
from functools import reduce
from multiprocessing import Pool

start_time = time.time()

strings = "City Councilwoman Wanda Cochran suggested a review of the budget to see how it can be reduced to pay for increasing salaries and benefits for city employees, who have received pay raises every year"
list_of_strings = strings.split()
data = list_of_strings * 100000
ENGLISH_STOP_WORDS = ['city', 'to']

def clean_word(word):
    return re.sub(r'[^\w\s]', '', word).lower()

def word_not_in_stopwords(word):
    return word not in ENGLISH_STOP_WORDS and word and word.isalpha()

def mapper(text):
    tokens_in_text = text.split()
    tokens_in_text = map(clean_word, tokens_in_text)
    tokens_in_text = filter(word_not_in_stopwords, tokens_in_text)
    return Counter(tokens_in_text)

def reducer(cnt1, cnt2):
    cnt1.update(cnt2)
    return cnt1

def chunk_mapper(chunk):
    mapped = map(mapper, chunk)
    reduced = reduce(reducer, mapped)
    return reduced

def chunkify(data,number_of_chunks):
    return [data[i::number_of_chunks] for i in range(number_of_chunks)]


if __name__ == '__main__':
    data_chunks = chunkify(data, number_of_chunks=16)
    # step 1:
    mapped = Pool(16).map(chunk_mapper, data_chunks)
    # step 2:
    reduced = reduce(reducer, mapped)
    print(reduced.most_common(100))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s seconds ---" % time.process_time())
