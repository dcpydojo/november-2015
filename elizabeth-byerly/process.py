import csv
from functools import reduce
from collections import Counter
import re
import gensim
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

'''
Tweets taken from https://github.com/ndanielsen/trumptrain
'''

punc = re.compile("[^0-9A-z@#]")
lmtzr = WordNetLemmatizer()

trumps = []
with open("trump_tweets.csv",
          newline='', encoding='utf-8') as csvfile:
  trump_reader = csv.reader(csvfile, delimiter='|')
  for row in trump_reader:
    row = [punc.sub("", word).lower() for word in row[2].split()]
    row = [lmtzr.lemmatize(word) for word in row if word not in
           stopwords.words('english')]
    trumps.append(row)

model = gensim.models.Word2Vec(trumps, min_count = 10)

model.most_similar(positive=['republican', 'trump'], negative = ['fiorina'])

model.similarity('trump', 'fiorina')
model.similarity('trump', 'cruz')
model.similarity('trump', 'bush')
