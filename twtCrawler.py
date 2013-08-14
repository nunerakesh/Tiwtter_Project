import twitter

TwitterAccountPool = [line.strip() for line in open('TwitterAccountList', 'r')]

AccountToken = 0

def NextAccount():
	global AccountToken
	lines = AccCount()
	AccountToken = (AccountToken + 1) % (lines + 1)

def AccCount():
	count = 0
	thefile = open('TwitterAccountList', 'rb')
	while 1:
		buffer = thefile.read(65536)
		if not buffer:break
		count += buffer.count('\n')
	return count

while True:
	try:
		writingFile = open('D:/Data/CrawledTwt.txt','w')

		api = twitter.Api(
		    consumer_key=TwitterAccountPool[AccountToken].split('\t')[0],
		    consumer_secret=TwitterAccountPool[AccountToken].split('\t')[1],
		    access_token_key=TwitterAccountPool[AccountToken].split('\t')[2],
		    access_token_secret=TwitterAccountPool[AccountToken].split('\t')[3]
		)

		temp = api.GetSearch(term='wtop', geocode=(38.907231,-77.036483,'20mi'))
		for tmp in temp:
		    #writingFile.write(str(tmp) + '\n')
			print tmp
	except Exception, e:
		Errotype = e[0][0]['code']
		if Errotype is 88:
			print 'Switch Account!'
			NextAccount()