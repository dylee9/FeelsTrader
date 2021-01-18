"""
stocktwitAPI.py
"""

import requests
import json
import datetime

# static variables
USER_ID = "4421399"
USERNAME = "runningmanruns"
SCOPE = "read"
ACCESS_TOKEN = "5f9331e676684789acdbb888934a2fc502555f65"
SAVEPATH = "data/test_data_%s.json" % str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))

# access stocktwits API via trending data request
raw_data = requests.get("https://api.stocktwits.com/api/2/streams/trending.json?access_token=" + ACCESS_TOKEN)
raw_data_json = raw_data.json()
message_data = raw_data_json['messages']

# preprocess raw data
processed_data = dict()
for message in message_data:
	# print(message)
	print("message_id: ", message['id'])
	print("message_body: ", message['body'])
	print("created_at: ", message['created_at'])
	print("user_follower_count: ", message['user']['followers'])
	print("symbols :", [symb['symbol'] for symb in message['symbols']])
	print("sentiment :", message['entities']['sentiment'] if message['entities'] else None)
	print("\n")

	processed_message = {
		'body': message['body'],
		'datetime': message['created_at'],
		'user_follower_count': message['user']['followers'],
		'symbols': [symb['symbol'] for symb in message['symbols']],
		'sentiment': message['entities']['sentiment'] if message['entities'] else None
	}
	processed_data[message['id']] = processed_message

# save preprocessed trending data as json
with open(SAVEPATH, 'w') as fp:
    json.dump(processed_data, fp)







