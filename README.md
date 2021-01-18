# FeelsTrader

A trading algorithm and website based off of public market sentiment. The project stems from the idea of predicting stock market sentiment via deep learning neural networks based off of social media platforms such as Twitter, StockTwits, Reddit, etc. A model trained on sentiment-labeled tweets/messages will be able to predict sentiments of tweets/messages posted in the future, allowing for the information to make trading decisions. These predictive results will also be visually displayed on the Django web application for users to make their own trading decisions as well.

## Requirements
- Python 3.7.4
- cryptography

### Python Modules
- Keras==2.4.3
- tensorflow==2.4.0
- h5py==2.10.0
- nltk==3.5
- requests==2.25.1
- regex==2020.11.13
- pandas==1.2.0
- PyMySQL==0.10.01

## Sources
### Basic 
- https://www.tensorflow.org/tutorials/text/text_classification_rnn
- https://towardsdatascience.com/a-beginners-guide-on-sentiment-analysis-with-rnn-9e100627c02e
- https://analyticsindiamag.com/how-to-implement-lstm-rnn-network-for-sentiment-analysis/
- https://d2l.ai/chapter_natural-language-processing-applications/sentiment-analysis-rnn.html
- https://www.kaggle.com/drscarlat/imdb-sentiment-analysis-keras-and-tensorflow/comments

### Natural Language Processing
- https://machinelearningmastery.com/clean-text-machine-learning-python/

### Sentiment Analysis wtih CNN
- https://humboldt-wi.github.io/blog/research/information_systems_1718/05sentimentanalysis/

## Setting up DB for Dev Environment
- Create a dedicated MySQL User. (Step 3) https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04
	- DO NOT USE auth_socket.
	- GRANT ALL ON database_name.* TO user@xx.xxx.xx.xx IDENTIFIED BY 'your_password';
	- Update databaseconfig.py with your user details. 
	- Restart server and you should be goo to go. 

## In Progress
- Verify model predictions are working. (Jason)
- Research hosting services. (Suresh)
    - Lowest Cost
    - Easiest to integrate Django
- Start hosting subcriptiong and setup remote DB (Suresh)
- Find a project management tool. (Suresh)

## Backlog
- Implement data aggregration 
- Research multiple ticker parsing methods
- Acquire dataset for training model

## Completed
- Implement stocktwits API
- 10 minute one-time scan twit scraper 
- Create RNN sentiment analysis model
- Connect MySQL database 
- Create DB schema
- Implement object relational model

