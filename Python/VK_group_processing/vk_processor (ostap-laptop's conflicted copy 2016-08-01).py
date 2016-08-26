# -*- coding: utf-8 -*-
import vk, json, re 
from datetime import datetime, date, timedelta as td
from stop_words import get_stop_words
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, MonthLocator, DateFormatter


# id, date, text, text of comments

# access_token = 'a3073aa3eca4d092cd71d81cae676fb9335f83f8b5247b5c2f95429ea807fc0593a647d6c325c2551acfb'

# access_token_pages = '78a7803482e6309ae6'
# authSession = vk.AuthSession('5316637', 'sergiyana@mail.ru', 'sergiyana112358OO', access_token=access_token_pages)

# authApi = vk.API(authSession)

# when doing that part 1 of OAuth
# It is not necessary to specify redirect_uri param
#
# Thats the format:
# api.groups.getById(group_id='antimaydan')

# return date in unix format
# a = datetime.fromtimestamp(int('1456764309')).strftime(('%Y-%m-%d %H:%M:%S'))

# timestamp is UTC time

# def nextHundredPosts(domain):

# 	global offset
# 	offset = offset + 100
# 	offset_full_wall = api.wall.get(domain=domain, extended=1, count =100, offset=offset)
# 	nextHundredPosts = offset_full_wall['wall']

# postsToGet = api.wall.get(domain='antimaydan', extended=1, count=100, offset=0)['wall']

### offset 18200

# start date 1390694400
# end date 1423612800

# api.wall.get() returns a list of messages listed from the oldest to the newest. The first one is the newest, the last one is the oldest

# with offset the processing starts after the next element after the offset number. So if you specify offset 100, the first 100 elements will be skipped, and the first element to be processed will be 101-th element. In other words, to select element number 135, the offset should be set to 134.

# first_ten = api.wall.get(domain='antimaydan', extended=1, count=10, offset=0)['wall'][1:]
# second_ten = api.wall.get(domain='antimaydan', extended=1, count=10, offset=10)['wall'][1:]
# first_twenty = api.wall.get(domain='antimaydan', extended=1, count=20, offset=0)['wall'][1:]
# alt_first_twenty = first_ten+second_ten

# tenth_element = first_ten[9]

# to work with cyrillics in python I should write cyrillic words as:
# u'test_in_cyrillics'

# def find_find():
# 	global tenth_element
# 	for index in range(100):
# 	   offset = index 
# 	   element = api.wall.get(domain='antimaydan', extended=1, count=1, offset=offset)['wall'][1:][0]
# 	   if tenth_element['id'] == element['id']:
# 	       return offset

# def find_pattern(pattern, posts, limit):
# 		patterns = {}
# 		counter = 0
# 		for index in range (len(posts)-1):
# 			if counter < limit:
# 				a = pattern.findall(posts[index]['text'])
# 				print 'processing post {}'.format(index)
# 				if a:
# 					print 'appending'
# 					patterns['match'append(a)
# 					patterns.append(index)
# 					counter = counter +1
# 			else: return 

# def messagesAsSingleText(dict_posts):
# 	global_text = ""
# 	i = len(dict_posts)-1
# 	for key in dict_posts:
# 		i -= 1
# 		print "processing post {}".format(i)
# 		global_text = global_text + " " + dict_posts[key]['text']
# 	return global_text

# def messagesAsSingleText(list_posts):
# 	global_text = ""
# 	for item in list_posts:
# 		print "processing post {}".format(str(item['id']))
# 		global_text = global_text + " " + item['text']
# 	return global_text

# def find_pattern(re_pattern, list_posts):
# 		patterns = {}
# 		for index in range (len(list_posts)-1):
# 			match = re_pattern.findall(list_posts[index]['text'])
# 			print 'processing post {}'.format(index)
# 			if match:
# 				print 'appending'
# 				date = humanDate(list_posts[index]['date'])
# 				match.append(list_posts[index]['id'])
# 				patterns[date].append(match)
		# return patterns

# for index in range (len(posts)-1):
# 	a = pattern.search(posts[index]['text'])
# 	if a:
# 		patterns.append(a)
# 		print a.group()

# dict_digit = {'digit':'\S*\d+[:.-]*\d*\.?S*'}
# yuliaDict = {'yulia': u'(\s[Юю]л((ь(к\S*|ч\S*))|([яеию]\S*))+\s)'}
# re_yulia = onePatternToRegex(yuliaDict['yulia'])

def humanDate(unix_date):
	'''takes unix date stamp and
	converts it to a readable human
	format 2111-11-11'''
	date = datetime.utcfromtimestamp(int(unix_date)).strftime(('%Y-%m-%d'))
	return date

# process posts
def leave_keys(list_posts, set_keys):
	'''takes a product of list of 
	postsInDates function (list_posts)
	and leaves only those keys specified 
	in set of keys provided set_keys'''
	# for index, other_keys in enumerate(list_posts):
	for index in range(len(list_posts)-1):
		for key in set(list_posts[index]) - set_keys:
		# for key in set(other_keys) - set_keys:
			list_posts[index].pop(key)

def remove_stop_words_digits_brs(list_posts):
	'''removes stop words, digits and <br/>
	from text fields from product of postsInDates 
	function'''
	new_list_posts = list_posts
	s_words = get_stop_words('ru')
	for post in new_list_posts:
		new_list_words = post['text'].split()
		for word in new_list_words:
			noBrWord = word.replace('<br>', " ")
			new_list_words[new_list_words.index(word)] = noBrWord
			noDigitWord = returnIfNumber(noBrWord)
			new_list_words[new_list_words.index(noBrWord)] = noDigitWord
			for stop_word in s_words:
				if noDigitWord.lower() == stop_word.lower():
					new_list_words.remove(noDigitWord)
		post['text'] = " ".join(new_list_words)
	return new_list_posts

def list_posts_to_dict(list_posts):
	'''takes a product of list of 
	postsInDates function (list_posts),
	converts it to dictionary with 
	ID keys'''
	result = {}
	for post in posts:
		result[post['id']] = {'date': post['date'], 'text': post['text']}
	return result

#process text
def removeBrs(text):
	'''takes a product of messagesAsSingleText
	and removes all the <br>'s from it
	returns the text as string'''
	list_words = text.split() 
	global_text = " ".join(map(lambda item:item.replace('<br>', ' '), list_words))
	return global_text

def removeNumbers(text):
	'''takes a product of messagesAsSingleText
	and removes numbers from it
	returns the text as string'''
	list_words = text.split() 
	global_text = " ".join(map(lambda item:returnIfNumber(item), list_words))
	return global_text

def returnIfNotNumber(word):
	'''takes a word and checks if
	its a number. If its a number, returns
	nothing. Otherwise returns the word'''
	string_pattern = '\S*\d+[:.-]*\d*\.?S*'
	compiled_pattern = re.compile(string_pattern, re.I)

	if re.match(compiled_pattern, word):
		return ""
	return word

#get posts
def getPostBy_id (id_, list_posts):
	'''takes a product of list of 
	postsInDates function (list_posts)
	and gets a post with a given id_ 
	from it'''
	for post in posts:
		if post['id'] == id_:
			return post

def getPostsBy_date(date, list_posts):
	'''takes a product of list of 
	postsInDates function (list_posts)
	and date in 2111-11-31 format and 
	returns a list of posts within
	that date'''
	result_posts = []
	for post in posts:
		if humanDate(post['date']) == date:
			result_posts.append(post)
	return result_posts


def print_words(findAll_pattern):
	for i in range(len(dictionary)-1):
		for j in range(len(dictionary[i]['word'])-1):
		  print dictionary[i]['word'][j]

def setOfDates():
	'''takes a the beginning and end dates
	and returns a set of dates in between'''
	result = set()

	d1 = date(2014, 1, 26)
	d2 = date(2015, 2, 11)

	delta = d2 - d1

	for i in range(delta.days + 1):
	    new_date = str(d1 + td(days=i))
	    result.add(new_date)

	return result

#get matches
def getMatchesBy_date(date, result):
	""" returns a dictionary where 
	dates are keys and matches are
	values """
	this_result = {date : list()}
	for date_key1 in result.itervalues(): # {u'2999-12-31': {u'111111': [[u'\u0438\,', u'u0430\']], u'222222': [[u'\u044f', u'\u044f']]}, u'2998-12-31': {u'333333': [[ ... ]]}}
		for date_key2 in date_key1.iterkeys(): # 2014-01-31
			if date_key2 == date:
				for id_ in date_key1[date_key2].itervalues(): # [[u'\u0438\u0438', u'', u'', u'\u0438\u0438']]
					for match_list in id_: # [u'\u0438\u0438', u'', u'', u'\u0438\u0438']
						for single_match in match_list: # type "unicode"
							this_result[date].append(single_match)
	return this_result

def getMatchesIn_dates(result):
	'''takes resulting matches object from get_
	patterns function and returns a dictionary
	matches associated with each date'''
	result1 = dict()
	for date in setOfDates():
		result1.update(getMatchesBy_date(date, result))
	return result1

def getAllMatches(result):
	""" takes resulting matches object from get_
	patterns function and returns
	all of the matches from it as a list of strings"""
	allMatches = []
	for date in result.itervalues():
		for id_ in date.itervalues():
			for match_group in id_.itervalues():
				for match in match_group:
					print match
					allMatches.append(match)
	return allMatches

def getMatchesBy_PostID(id_,result):
	"""checks  """
	matches = []
	counter = 0
	for date in result.itervalues():
		for ids in date.itervalues():
			for id_1 in ids.keys():
				counter += 1
				print type(id_1)
				if int(id_1) == id_:
					matches.append(ids[id_1])
					# for match_group in id_.itervalues():
					# 	for match in match_group:
					# 		print match
					# 		matches.append(match)
	return matches, counter

# a.b.
def postsWithMatches(result):
	""" takes a product of get_patterns
	and returns a set of post ids in which
	any element of the vocabulary occurs
	"""
	posts = set()
	for date in result.itervalues():
		for ids in date.itervalues():
			for id_1 in ids.keys():
				posts.add(id_1)

	print "there is " + str(len(posts)) + " posts with matches, which is " + str(float((len(posts)*100)/len(list_posts))) + "% from total number of posts"
	return posts, len(posts)

#a.a.
def vocabInWholeText(allMatches, string_text):
	""" takes product of getAllMatches function and
	a product of messagesAsSingleText function and
	caluclates which part of the second occupies the first
	returns string
	"""
	list_text = string_text.split()
	result = str(float((len(allMatches)))/len(list_text)*100) + "%"
	return result

def averageTextLengthInPost(list_posts):
	""" calculates length of in words count """
	numberOfPosts = len(list_posts)
	totalPostsLengthInWords = 0
	for post in list_posts:
		totalPostsLengthInWords = totalPostsLengthInWords + len(post['text'].split())
	result = float(totalPostsLengthInWords)/numberOfPosts
	print str(totalPostsLengthInWords) + " " + str(numberOfPosts)
	return result

def averageVocabInPost(list_posts):
	pass

def messagesAsSingleText(list_posts):
	""" takes list of posts from postsInDates 
	function and returns its text
	keys's values merged in a string"""
	global_text = " ".join(map(lambda item:item['text'], list_posts))
	return global_text


def find_word(search_for_word, post):
	'''takes a word and searches for it
	in a specific post
	returns a dictoionary with the following
	structure date: id: word'''
	
	matches = {}
	words = ()

	for word in post['text'].split():
		if word == search_for_word:
			words = words + (word,)

	if len(words) >=1:
		date = humanDate(post['date'])
		match = {post['id']: words}
		matches[date] = match
		print "appending"

	return matches 

def get_words(dict_words, list_posts):
	'''takes a dictionary of words and a product of 
	postsInDates and searches in the latter for each 
	word from the dictionary
	returns a dictionary of the following structure:
	keyword : date : id : word'''
	result = {}
	i = len(list_posts)
	for post in list_posts:
		i-=1
		print "processing post {}".format(i) 
		for key, array in dict_words.iteritems():
			for word in array:
				matches = find_word(word,post)
				if len(matches) != 0:
					date_key = "".join(matches.keys())
					id_key = matches[date_key].keys()[0]
					if not result.has_key(key): # if no pattern key
						result[key] = matches
					elif result[key].has_key(date_key): # if there is date key
						result[key][date_key][id_key] = matches[date_key][id_key]
					else: result[key][date_key] = matches[date_key] # if no date key
	return result

def find_pattern(re_pattern, post):
	'''takes a regex pattern and searches for it
	in a specific post
	returns a dictoionary with the following
	structure date: id: word'''
	matches = {}
	match = re_pattern.findall(post['text'])
	
	if match:
		print "appending"
		final = ()
		for m in match:
			final = final + (m,)
		global match
		match = final
		date = humanDate(post['date'])
		match1 = {post['id']: match}
		if matches.has_key(date):
			matches[date].append(match1)
		else: matches[date] = match1
	return matches

def get_patterns(dict_patterns, list_posts):
	'''takes a dictionary of regex patterns and a product of 
	postsInDates and searches in the latter for each 
	word from the dictionary
	returns a dictionary of the following structure:
	keyword : date : id : word'''
	result = {}
	i = len(list_posts)
	for post in list_posts:
		i-=1
		print "processing post {}".format(i) 
		for key, pattern in dict_patterns.iteritems():
			re_pattern = onePatternToRegex(pattern)
			matches = find_pattern(re_pattern,post)
			if len(matches) != 0:
				date_key = "".join(matches.keys())
				id_key = matches[date_key].keys()[0]
				if not result.has_key(key): # if no pattern key
					result[key] = matches
				elif result[key].has_key(date_key): # if there is date key
					result[key][date_key][id_key] = matches[date_key][id_key]
				else: result[key][date_key] = matches[date_key] # if no date key
	return result


def postsInDates(domain, start_date, end_date, offset=0):

	"""end_date = 1423612800 start_date = 1390694400"""

	offset = getToEndDatePost(domain=domain, end_date=end_date,offset=offset)[0]

	postsToGet = api.wall.get(domain=domain, extended=1, count=100, offset=offset)['wall']

	final_posts = []

	should_restart = True

	while should_restart == True:
		for index in range(1, len(postsToGet)):
			if postsToGet[index]['date'] < start_date:
				print "the earliest post is with date {}, has index {} in offset {}. In sum {} posts are collected".format(postsToGet[index]['date'], index, offset, len(final_posts))
				result = final_posts
				return result
			elif index == len(postsToGet)-1:
				final_posts.append(postsToGet[index])
				global postsToGet 
				offset = offset + 100
				postsToGet = api.wall.get(domain=domain, extended=1, count=100, offset=offset)['wall']
				print "cheking offset {}".format(offset)
				break
			else: final_posts.append(postsToGet[index])


def getToEndDatePost(domain, end_date, offset=0):

	postsToGet = api.wall.get(domain=domain, extended=1, count=100, offset=offset)['wall']

	should_restart = True

	while should_restart == True:
		for index in range(1, len(postsToGet)):
			if postsToGet[index]['date'] < end_date:
				print "element with the start date {} has index {} in offset {}".format(postsToGet[index]['date'], index, offset)
				return offset+index-1, index, postsToGet[index]['date']
			elif index == len(postsToGet)-1:
				global postsToGet
				offset = offset + 100
				postsToGet = api.wall.get(domain=domain, extended=1, count=100, offset=offset)['wall']
				print "checking offset {}".format(offset)
				break
			else: continue

def openJSON(file_name):
	with open (file_name) as file:
		posts = json.load(file)
		return posts

def openPatternsJSON(file_name_dict):
	with open (file_name_dict) as file:
		patterns = json.load(file)
		#patterns = patterns.encode('utf8') # should be done for cyrillic
		for value in patterns.itervalues():
			value = value.replace('\\\\', '\\') # escaping is for regex
		return patterns

# in JSON each backslash should be escaped by putting an extra backslash before

def onePatternToRegex(string_pattern):
	'''takes a regex pattern in string format
	and converts it regex format
	returns regex pattern'''
	final_pattern = string_pattern
	final_pattern = re.compile(string_pattern, re.I)
	return final_pattern

def patternsToRegex(list_patterns):
	'''takes a list of regex patterns in string
	format and produces out of it a list of 
	regex patterns'''
	result_patterns = []
	for pattern in list_patterns:
		re_pattern = re.compile(pattern, re.I)
		result_patterns.append(re_pattern)
	return result_patterns

def savePostsPickle(list_posts, file_name):
	'''save a product of postsInDates by
	pickling'''
	new_file = open (file_name, 'w')
	pickle.dump(posts,new_file)

def saveJSON(whatever, file_name):
	with open(file_name, 'w') as outfile:
		json_str = json.dumps(whatever)
		outfile.write(json_str)

#plotting
def matchesInDatesForPlot(matchesInDates):
	'''takes a product of matchesInDates and
	converts it into a format appropriate for 
	plotting'''
	itms = matchesInDates.items()
	result_lst_tpl = []
	for item in itms:
		date = datetime.strptime(item[0], "%Y-%m-%d")
		value = len(item[1])
		date_count = (date, value)
		result_lst_tpl.append(date_count)
	return sorted(result_lst_tpl, key=lambda item:item[0])

end_date = 1423612800
start_date = 1390694400

session = vk.Session()

api = vk.API(session)

amaydan_wall = api.wall.get(domain='antimaydan', extended=1)

amaydan_wall_wall = amaydan_wall['wall']

final_posts = []


result = openJSON('result.json')

list_posts = openJSON('posts_cleaned_text.json')

matchesInDates = getMatchesIn_dates(result)

result_lst_tpl = matchesInDatesForPlot(matchesInDates)

dates = [d[0] for d in result_lst_tpl]
values = [d[1] for d in result_lst_tpl]
fig, ax = plt.subplots()
ax.plot_date(dates, values, '-')
months = MonthLocator()
days = DayLocator()
monthsFmt = DateFormatter("%b")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthsFmt)
ax.xaxis.set_minor_locator(days)
ax.autoscale_view()

ax.grid(True)
fig.autofmt_xdate()
plt.show()

