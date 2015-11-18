#!/usr/bin/env python3
import csv
import random
import collections

# Assumes the `trump_tweets` from github.com/ndanielsen/trumptrain
# are in the same directory
with open("trump_tweets.csv") as f:
    r = csv.reader(f, delimiter="|")
    tweet_data = list(r)

# note: the 3rd item in each row is the text
tweet_texts = [x[2] for x in tweet_data]

# Pull all the text together into one big corpus, filtering
# out @usernames, URLs, and so on
consolidated_text = " ".join(tweet_texts)
consolidated_text = consolidated_text\
    .replace("\"", " ")\
    .replace(".@", "@")\
    .replace("”", " ")

def is_relevant(word):
    w = word.strip()
    return (not w.startswith("@") and not w.startswith("http")
         and not (w.startswith("&") and w.endswith(";")))

words = [w.strip() for w in consolidated_text.split(" ") if is_relevant(w)]

# Build up a dictionary mapping words to a list of words that have followed
# that word in the corpus
words_with_followers = collections.defaultdict(list)
for i, w in enumerate(words[:-1]):
    words_with_followers[w].append(words[i + 1])

# Now, randomly choose words that have followed each other...
print("And now, some words of wisdom...")
length = random.randint(6, 15)
phrase = [random.choice(words)]
for _ in range(length):
    w = phrase[-1]
    while w not in words_with_followers:
        w = random.choice(words)
    phrase.append(random.choice(words_with_followers[w]))

print("\t", " ".join(phrase))
