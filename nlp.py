"""
nlp.py
"""
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from keras.datasets import imdb


def clean(text):
	'''
	Uses NLP algorithms to clean raw text and returns an array
	of most commonly used words

	Input:
		text: raw text as string
	Output:
		ret: array of words converted to most commmonly used indices (from imdb database)
	'''

	# split string into tokens
	tokens = word_tokenize(text)

	# remove stop words & punctuation
	stop_words = stopwords.words('english')
	words = [word for word in tokens if word.isalpha() and word not in stop_words]

	# convert into stem words
	# porter = PorterStemmer()
	# stemmed = [porter.stem(word) for word in words]

	# convert into imdb frequency dictionary indices
	vocabulary_size = 5000
	word2id = imdb.get_word_index()
	imdb_coded = [word2id.get(word, 0) for word in words]
	imdb_coded_sized = [code for code in imdb_coded if code < vocabulary_size]

	return imdb_coded_sized



# if __name__ == "__main__":
# 	raw = "Tesla is now the leader in self-driving technology for electric vehicles, but there is no guarantee that it will continue.  Because Tesla wanted to reduce manufacturing costs, it defeated XPEV in the price war and abandoned the use of laser radar.  This is a wrong choice. Tesla will not be able to upgrade the L5 level of autonomous driving technology in the future."

# 	print(clean(raw))