# Imports
import re
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords


# Functions to clean up the text
def clean_up(s):
    """
    Cleans up numbers, URLs, and special characters from a string.

    Args:
        s: The string to be cleaned up.

    Returns:
        A string that has been cleaned up.
    """
    return re.sub(r'  *', ' ', re.sub(r'[^a-z]', ' ',
                                      re.sub(r'www\.\S*', ' ',
                                             re.sub(r'http[s]?://\S*', ' ',
                                                    s.lower())))).strip()


def tokenize(s):
    """
    Tokenize a string.

    Args:
        s: String to be tokenized.

    Returns:
        A list of words as the result of tokenization.
    """
    return nltk.word_tokenize(s)


def stem_and_lemmatize(l):
    """
    Perform stemming and lemmatization on a list of words.

    Args:
        l: A list of strings.

    Returns:
        A list of strings after being stemmed and lemmatized.
    """
    ps = PorterStemmer()
    wnl = WordNetLemmatizer()

    stemmed_list = [ps.stem(w) for w in l]
    lemmed_on_stemmed_list = [wnl.lemmatize(w) for w in stemmed_list]

    return lemmed_on_stemmed_list


def remove_stopwords(lst, lang='english'):
    """
    Remove English (default) stopwords from a list of strings.

    Args:
        lst: A list of strings.
        lang = Language of the stopwords.

    Returns:
        A list of strings after stop words are removed.
    """
    stop_words = stopwords.words(lang)
    return [word for word in lst if word not in stop_words]


# Example of using all those NLP funcs in a Pandas' Series
'''
ds_sample['text_processed'] = \
ds_sample['text'].apply(lambda x: remove_stopwords(stem_and_lemmatize(tokenize(
clean_up(x)))))
'''


# Building the features


def find_features(document, bow):
    text = document.lower()
    features = dict()
    for w, c in bow:
        features[w] = w in text
    return features


def make_matrix(series_text, series_target, bow):
    return [(find_features(s, bow), t)
            for s, t in zip(series_text.values, series_target.values)]
