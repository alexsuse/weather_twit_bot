#!/usr/bin/python
import twitter
import credentials as cr
from numpy.random import permutation

api = twitter.Api(consumer_key=cr.consumer_key, consumer_secret=cr.consumer_secret, access_token_key=cr.token_key, access_token_secret=cr.token_secret)

search_terms = ["crappy weather","shitty weather","fuck this weather","wtf weather","hate this weather"]

statuses = []

for s in search_terms:
	statuses = statuses + api.GetSearch(s)

perm = permutation(len(s))

for i in xrange(20):
	try:
		api.PostRetweet(statuses[perm[i]].id)
		print 'retweeting this!'
	except twitter.TwitterError:
		print 'must have retweeted this already!'

