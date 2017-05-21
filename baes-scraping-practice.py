## Reddit Webscraping practice

import praw
import requests
from PIL import Image
from io import BytesIO


## API calls require this information to allow access

CLIENT_ID = 'HLzCVKPFAA-8uw'
CLIENT_SECRET = 'O3Yf2e3hQJ1VQmaNRN3-zH02oFs'
USER_AGENT = 'Scraper 1.0 by /u/OrangeJulian12'
USERNAME = ''
PASSWORD = ''
SCORE = 10000
HIT_COUNT = 1000

## This defines a connection to reddit, which can be used as a variable to access different subsections of reddit.

reddit = praw.Reddit(client_id = CLIENT_ID,
	client_secret = CLIENT_SECRET,
	user_agent = USER_AGENT)

print(reddit.read_only) ## Proves access works. If account credentials are added, can be read-write
reddit.read_only = True



## Parses the subreddit into submissions, which have the following variables.
## Not necessarily efficient, but I've included a way to convert the image into a format
## that can be read by Python and opened by an app on your computer.


## This generator function controls the parse to only extract HIT_COUNT number of entries,
## and out of those entries it only returns ones with with a score > SCORE. (Number of upvotes on a post)

gen = (x for x in reddit.subreddit('dankmemes').hot(limit=HIT_COUNT) if x.score > SCORE)


for submission in gen:
	image = Image.open(requests.get(submission.url, stream=True).raw)
	image.show()
	
	print(submission.title, '\n',
	submission.score, '\n',
	submission.id, '\n',
	submission.url, '\n',
	'------------------------------------', '\n')

