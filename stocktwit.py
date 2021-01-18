"""
stocktwit.py
"""

import re


class Twit:
	def __init__(self, raw):
		self.raw = raw

		# find all tags
		tags = re.findall(r'\b[$@]\w+', raw)
		self.cashtags = [tag for tag in tags if tag.startswith('$')]
		self.attags = [tag for tag in tags if tag.startswith('@')]

		# preprocess raw text
		self.text = re.sub('\b[$@]\w+', '', raw)

	def calculate_sentiment(self):
		pass

	def get_cashtags(self):
		return self.cashtags

	def get_attags(self):
		return self.attags

	def get_raw(self):
		return self.raw

	def get_text(self):
		return self.text

	

