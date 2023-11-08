import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import tensorflow as tf
import random
import pickle
import json

# set up stemmer
stemmer = LancasterStemmer()

# config config model
data = pickle.load( open( "./chat/models/training_data", "rb" ) )
words = data['words']
classes = data['classes']
train_x = data['train_x']
train_y = data['train_y']

# mở file json
try:
    with open('./chat/data/data.json') as json_data:
        intents = json.load(json_data)
except:
    print("Hệ thống đang bị lỗi, vui lòng thử lại sau!")
    exit()

# config config model
net = tflearn.input_data(shape=[None, len(train_x[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net, tensorboard_dir='tflearn_logs')

# load model
try:
    model.load('./chat/models/model.tflearn')
except:
    print("Hệ thống đang bị lỗi, vui lòng thử lại sau!")
    exit()

def clean_up_sentence(sentence):
    try:
        sentence_words = nltk.word_tokenize(sentence)

        sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words
    except:
        return None
    
# bag of words
def bow(sentence, words, show_details=False):
    try:
        sentence_words = clean_up_sentence(sentence)
        bag = [0]*len(words)
        for s in sentence_words:
            for i,w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print ("found in bag: %s" % w)
        return(np.array(bag))
    except:
        return None

def classify(sentence):
    try:
        ERROR_THRESHOLD = 0.25
        results = model.predict([bow(sentence, words)])[0]
        results = [[i,r] for i,r in enumerate(results) if r>ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append((classes[r[0]], r[1]))
        return return_list
    except:
        return None

def chatResponse(sentence):
    try:
        results = classify(sentence)
        if results:
            while results:
                for i in intents['intents']:
                    if i['tag'] == results[0][0]:
                        if not 'context_filter' in i:
                            return random.choice(i['responses'])
                results.pop(0)
    except:
        return "Hệ thống đang bị lỗi, vui lòng thử lại sau!"