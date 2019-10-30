from flask import current_app

import os.path

from pandas import read_excel
from gensim.models import word2vec


def isNaN(num):
    return num != num


def create_movie_model():
    df = read_excel(current_app.config['STATIC_PATH'] + '/res/attach_03.xls')
    df = df.drop_duplicates(['has출연자', 'has연출감독'], keep="first")

    result = []
    for data in df.values:
        if not isNaN(data[1]):
            result.append(' '.join(data[1].split(',')))

    output = ' '.join(result)
    with open('mayfarm_w2v.txt', 'w', encoding='utf-8') as fp:
        fp.write(output)

    w2v_data = word2vec.LineSentence('mayfarm_w2v.txt')
    # sg
    # 0 : CBOW, 1 : skip-gram
    model = word2vec.Word2Vec(w2v_data, size=300, window=10, hs=1, min_count=3, sg=1)
    model.save('mayfarm_w2v.model')

    print('모델 생성완료')


def get_w2v(query):
    if not os.path.exists('mayfarm_w2v.model'):
        create_movie_model()

    model = word2vec.Word2Vec.load('mayfarm_w2v.model')

    return model.most_similar(positive=[query], topn=15)
