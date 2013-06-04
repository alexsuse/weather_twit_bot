import twitter
import credentials as cr

api = twitter.Api(consumer_key=cr.consumer_key, consumer_secret=cr.consumer_secret, access_token_key=cr.token_key, access_token_secret=cr.token_secret)

statuses = api.GetSearch("crappy weather")

for i in statuses:
	try:
		api.PostRetweet(i.id)
		print 'retweeting this!'
		api.CreatFriendship(i.user.id)
	except twitter.TwitterError:
		print 'must have retweeted this already!'

