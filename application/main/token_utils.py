from flask import current_app

from konlpy.tag import Okt
from pandas import read_excel


sentences = None
stop_words = None


def noun_frequency_count():
    okt = Okt()

    global sentences
    if sentences is None:
        sentences = get_sentence()

    # 불용어 출처 : https://github.com/stopwords-iso/stopwords-ko
    global stop_words
    if stop_words is None:
        with open(current_app.config['STATIC_PATH'] + '/res/stopwords-ko.txt', 'r') as fp:
            stop_words = fp.read()
        stop_words = stop_words.split('\n')
    word_dic = {}
    for sentence in sentences:
        data = okt.pos(sentence[0], norm=True, stem=True)
        for taeso, pumsa in data:
            if pumsa == 'Noun':
                if not (taeso in word_dic) & (taeso not in stop_words):
                    word_dic[taeso] = 0
                word_dic[taeso] += 1

    return sorted(word_dic.items(), key=lambda kv: kv[1], reverse=True)


def word_frequency_count():
    from nltk.tokenize import word_tokenize

    global sentences
    if sentences is None:
        sentences = get_sentence()

    sentence = " ".join([" ".join(sentence) for sentence in sentences])
    word_tokens = word_tokenize(sentence)

    global stop_words
    if stop_words is None:
        with open(current_app.config['STATIC_PATH'] + '/res/stopwords-ko.txt', 'r') as fp:
            stop_words = fp.read()
        stop_words = stop_words.split('\n')

    word_dic = {}
    for w in word_tokens:
        if w not in stop_words:
            if not (w in word_dic):
                word_dic[w] = 0
            word_dic[w] += 1

    sentences = None
    stop_words = None

    return sorted(word_dic.items(), key=lambda kv: kv[1], reverse=True)


def get_sentence():
    from application.main.model import Problems
    from application import db

    df = read_excel(current_app.config['STATIC_PATH'] + '/res/attach_01.xlsx', names=Problems.problems_model_columns)
    df.to_sql('problem_table', db.engine.connect(), index=False, if_exists='replace')

    return Problems.query.with_entities(Problems.problem_sentence).all()
