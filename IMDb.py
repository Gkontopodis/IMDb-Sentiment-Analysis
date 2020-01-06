import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Train positive/negative
train_pos=pd.read_csv('/home/c1969865/Downloads/AM_COurseWork/train/imdb_train_pos.txt', delimiter='\n', names=['text'])
train_neg=pd.read_csv('/home/c1969865/Downloads/AM_COurseWork/train/imdb_train_neg.txt', delimiter='\n', names=['text'])
train_pos['label']=1
train_neg['label']=0
train_pos_neg=pd.concat([train_pos,train_neg])
train_shuf=train_pos_neg.sample(frac=1)

# Developement positive/negative
dev_pos=pd.read_csv('/home/c1969865/Downloads/AM_COurseWork/dev/imdb_dev_pos.txt', delimiter='\n', names=['text'])
dev_neg=pd.read_csv('/home/c1969865/Downloads/AM_COurseWork/dev/imdb_dev_neg.txt', delimiter='\n', names=['text'])
dev_pos['label']=1
dev_neg['label']=0
dev_pos_neg=pd.concat([dev_pos,dev_neg])
dev_shuf=dev_pos_neg.sample(frac=1)

# Test positive/negative
test_pos=pd.read_csv('/home/c1969865/Downloads/AM_COurseWork/test/imdb_test_pos.txt', delimiter='\n', names=['text'])
test_neg=pd.read_csv('/home/c1969865/Downloads/AM_COurseWork/test/imdb_test_neg.txt', delimiter='\n', names=['text'])
test_pos['label']=1
test_neg['label']=0
test_pos_neg=pd.concat([test_pos,test_neg])
test_shuf=test_pos_neg.sample(frac=1)

train_x = train_shuf['text']
train_y = train_shuf['label']
dev_x = dev_shuf['text']
dev_y = dev_shuf['label']
test_x = dev_shuf['text']
test_y = dev_shuf['label']

# Text vectorization

tfidf = TfidfVectorizer(min_df=2, max_df=0.5, ngram_range=(1,2), stop_words='english')
tfidf.fit(train_x,dev_x)
tfidf.fit(test_x)

train_x_tfidf = tfidf.transform(train_x)
dev_x_tfidf = tfidf.transform(dev_x)
test_x_tfidf = tfidf.transform(test_x)

# Logistic Regression Model

Model = LogisticRegression()
Model.fit(train_x_tfidf, train_y)

# Development prediction and model scores

Predictions_dev = Model.predict(dev_x_tfidf)
print('Scores for development dataset:\n',classification_report(dev_y,Predictions_dev))

# Test prediction and model scores

Predictions_test = Model.predict(test_x_tfidf)
print('Scores for test dataset:\n',classification_report(test_y,Predictions_test))