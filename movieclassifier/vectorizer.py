from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle

cur_dir = os.path.dirname(os.path.abspath(__file__))
stop = pickle.load(open(os.path.join(cur_dir, 'pkl_objects','stopwords.pkl'), 'rb'))

def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',
    text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) \
            + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

vect = HashingVectorizer(decode_error='ignore', n_features=2**21,preprocessor=None, tokenizer=tokenizer)



#Checking if serialization works perfectly 

# clf=pickle.load(open(os.path.join(cur_dir, 'pkl_objects','classifier.pkl'), 'rb'))
# import numpy as np 
# label={0:"negative",1:"positive"}

# sample=["The actor sucks but the movie was too good"]
# X=vect.transform(sample)

# print(clf.predict(X))

# print(clf.predict(X)[0])

# print(clf.predict_proba(X))

# print(label[clf.predict(X)[0]],np.max(clf.predict_proba(X))*100)

# Connecting with sqlite database

# conn = sqlite3.connect('reviews.sqlite')
# c = conn.cursor()

# c.execute("DROP TABLE review_db")

# c.execute('CREATE TABLE review_db'\
#         ' (review TEXT, sentiment INTEGER, date TEXT)')

# example1 = 'I love this movie'
# c.execute("INSERT INTO review_db"\
#         " (review, sentiment, date) VALUES"\
#         " (?, ?, DATETIME('now'))", (example1, 1))

# example2 = 'I disliked this movie'
# c.execute("INSERT INTO review_db"\
#         " (review, sentiment, date) VALUES"\
#         " (?, ?, DATETIME('now'))", (example2, 0))

# Checking connection with db

# conn.commit()
# conn.close()

# conn = sqlite3.connect('reviews.sqlite')
# c = conn.cursor()
# c.execute("SELECT * FROM review_db WHERE date"\
#         " BETWEEN '2018-09-01 00:00:00' AND DATETIME('now')")
# results = c.fetchall()
# conn.close()
# print(results)