import twitter
import credentials as cr

api = twitter.Api(consumer_key=cr.consumer_key, consumer_secret=cr.consumer_secret, access_token_key=cr.token_key, access_token_secret=cr.token_secret)

api.PostUpdate('Gotta hate myself this weather! DAMN! #wtfweather')
