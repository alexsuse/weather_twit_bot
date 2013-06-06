#!/usr/bin/python
import twitter
import credentials as cr

api = twitter.Api(consumer_key=cr.consumer_key, consumer_secret=cr.consumer_secret, access_token_key=cr.token_key, access_token_secret=cr.token_secret)

search_terms = ["crappy weather","shitty weather","fuck this weather","wtf weather","hate this weather"]

statuses = []

for s in search_terms:
	statuses = statuses + api.GetSearch(s)

for i in statuses:
	try:
		api.PostRetweet(i.id)
		print 'retweeting this!'
#		api.CreateFriendship(i.user.id)
	except twitter.TwitterError:
		print 'must have retweeted this already!'

