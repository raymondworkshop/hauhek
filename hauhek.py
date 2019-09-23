# -*- coding: utf-8 -*-

# curl cann't support unicode -> chinese
""" 
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
"""

#import timeit

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('query', help="python canseg.py query='呢幾日天氣成日變，你要小心保重身體'")
#parser.add_argument('print', help)
args = parser.parse_args()

import jieba_fast as hauhek
#import jieba

hauhek.load_userdict("./data/dict.txt")

"""
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

        _output = '-'.join(words)
        print('_output:', _output)

        #JSON object
        output = {'Text': user_query, 'Output': _output}

        return output

api.add_resource(Segmentation, '/')
"""


def segmentation():
    # find the query
    user_query = args.query
    #print("query:", user_query)

    words = hauhek.cut(user_query)
    #print('words:', words)

    _output = '-'.join(words)
    #print('_output:', _output)

    #JSON object
    output = {'query': user_query, 'output': _output}

    print(_output)

    #return output

#print(timeit.timeit(segmentation, number=1))

if __name__ == '__main__':
   
    """
    sents = ["呢幾日天氣成日變，你要小心保重身體。",
             "叔叔，唔該你送俾我嘅禮物，我好中意。"
             ]

    for i in range(len(sents)):
        words = jieba.cut(sents[i])
        print('-'.join(words) + '\n')
    """
    
    segmentation()
    
    #app.run(debug=True)
