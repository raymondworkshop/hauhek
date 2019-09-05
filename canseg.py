# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

import jieba_fast as jieba

jieba.load_userdict("./data/dict.txt")

#parse argument
parser = reqparse.RequestParser()
parser.add_argument('query')

class Segmentation(Resource):
    def get(self):
        # find the query
        args = parser.parse_args()
        user_query = args['query']
        print("query:", user_query)

        words = jieba.cut(user_query)
        #print('words:', words)

        _output = '/'.join(words)
        print('_output:', _output)

        #JSON object
        output = {'Text': user_query, 'Output': _output}

        return output

api.add_resource(Segmentation, '/')

if __name__ == '__main__':
    """
    sents = ["呢幾日天氣成日變，你要小心保重身體。",
             "呢段時間過得順唔順吖？做嘢好辛苦嘞？",
             "叔叔，唔該你送俾我嘅禮物，我好中意。",
             "我真係冇諗到會搞成噉㗎，原諒我好唔好？",
             "佢真係唔係幾識曹太架"]

    for i in range(len(sents)):
        words = jieba.cut(sents[i])
        print('-'.join(words) + '\n')
    """
    app.run(debug=True)
