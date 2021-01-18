"""
test_sentiment_prediction.py
"""
from keras.models import model_from_json
from keras.preprocessing import sequence
from keras.datasets import imdb

import json
import pandas as pd
import re
import nlp

# static variables
DATAPATH = "data/test_data.json"
MODELPATH = "models/imdb_sentiment_model.json"
MODELWEIGHTPATH = "models/imdb_sentiment_model.h5"
PREDICTIONOUTPATH = "data/test_sentiment_prediction.csv"

# read json data
with open(DATAPATH, 'r') as fp:
    rawdata = json.load(fp)

# pre-process data for sentiment prediction
messages = [message['body'] for message in rawdata.values()]

data = []
raw_messages = []
for message in messages:
	# substitute out cashtags and urls
	tag_removed = re.sub('\$(\w+)', '', message)
	url_removed = re.sub(r'https?:\/\/.*[\r\n]*', '', tag_removed, flags=re.MULTILINE)

	# further NLP text cleaning and IMDB coding
	preprocessed = nlp.clean(url_removed)

	if preprocessed:
		# add to dataset
		data.append(preprocessed)
		raw_messages.append(message)

# static modeling variables
max_words = 500

# create test data for model input
# X_test = pd.DataFrame(data=data, columns=['text'])
X_test = sequence.pad_sequences(data, maxlen=max_words)

# load model
json_file = open(MODELPATH, 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(MODELWEIGHTPATH)
 
# create predictions
y_pred = loaded_model.predict(X_test, verbose=0)

# save predictions
word2id = imdb.get_word_index()
id2word = {i: word for word, i in word2id.items()}
output_data = []
for i in range(len(X_test)):
	print("X: ", raw_messages[i])
	print("y: ", y_pred[i][0])
	output_data.append((y_pred[i][0], raw_messages[i]))

output_df = pd.DataFrame(data=output_data, columns=['sentiment', 'raw_message'])
output_df.to_csv(PREDICTIONOUTPATH, index=False)
