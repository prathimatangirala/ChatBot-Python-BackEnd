import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json
import pickle
from tensorflow.python.framework import ops

class CsuModel:
   

    def chatBotAPI(self, inp):
        print("Start talking with the bot (type quit to stop)!")
        f = open('intents.json')
        data = json.loads(f.read())
        with open("data.pickle", "rb") as f:
          words, labels, training, output = pickle.load(f)
        ops.reset_default_graph()
        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
        net = tflearn.regression(net)
        model = tflearn.DNN(net)  
        model.load("model.tflearn")
        results = model.predict([self.bag_of_words(inp, words)])
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        for tg in data["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses']
        return random.choice(responses)

    def bag_of_words(self, s, words):
       bag = [0 for _ in range(len(words))]
       s_words = nltk.word_tokenize(s)
       s_words = [stemmer.stem(word.lower()) for word in s_words]
       for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
       return numpy.array(bag)
