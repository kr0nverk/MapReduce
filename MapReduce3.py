import time
import re
from collections import Counter

start_time = time.time()

def clean_word(word):
    return re.sub(r'[^\w\s]', '', word).lower()

def word_not_in_stopwords(word):
    return word not in ENGLISH_STOP_WORDS and word and word.isalpha()

def find_top_words(data):
    cnt = Counter()
    for text in data:
        tokens_in_text = text.split()
        tokens_in_text = map(clean_word, tokens_in_text)
        tokens_in_text = filter(word_not_in_stopwords, tokens_in_text)
        cnt.update(tokens_in_text)
    return cnt.most_common(100)


if __name__ == '__main__':
    strings = "City Councilwoman Wanda Cochran suggested a review of the budget to see how it can be reduced to pay for increasing salaries and benefits for city employees, who have received pay raises every year"
    list_of_strings = strings.split()
    data = list_of_strings * 100000
    ENGLISH_STOP_WORDS = ['city', 'to']

    print(find_top_words(data))
    print("--- %s seconds ---" % (time.time() - start_time))
    print("--- %s seconds ---" % time.process_time())
