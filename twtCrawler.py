import twitter
import time

TwitterAccountPool = [line.strip() for line in open('TwitterAccountList', 'r')]
KeyWordsList = open('Keywords', 'r').read().split('\t')

AccountToken = 0
KeywordToken = 0

def NextAccount(AccNum):
	api = twitter.Api(
	    consumer_key=TwitterAccountPool[AccNum].split('\t')[0],
	    consumer_secret=TwitterAccountPool[AccNum].split('\t')[1],
	    access_token_key=TwitterAccountPool[AccNum].split('\t')[2],
	    access_token_secret=TwitterAccountPool[AccNum].split('\t')[3]
	)
	return api

def AccCount():
	count = 0
	thefile = open('TwitterAccountList', 'rb')
	while 1:
		buffer = thefile.read(65536)
		if not buffer:break
		count += buffer.count('\n')
	return count + 1

def TwitterCrawling():
	while True:
		try:
			TwitterApiInstance = NextAccount(AccountToken)

			while True:
				temp = TwitterApiInstance.GetSearch(term=KeyWordsList[KeywordToken], geocode=(38.907231,-77.036483,'20mi'))
				KeywordToken = (KeywordToken + 1) % len(KeyWordsList)
				# time.sleep(0.5)
				for tmp in temp:
					# writingFile.write(str(tmp) + '\n')
					print tmp

		except Exception, e:
			Errotype = e.message[0]['code']
			if Errotype is 88:
				AccountToken = (AccountToken + 1) % AccCount()
				print 'Switch Account!'
			else:
				print e

if  __name__ == '__main__':
	TwitterCrawling()