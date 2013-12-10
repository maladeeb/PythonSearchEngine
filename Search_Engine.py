def get_next_target(page):
    start_link = page.find('<a href=')
    if (start_link == -1):
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
    while (page):
        url, endpos = get_next_target(page)
        if (url):
            print url
            page = page[endpos:]
        else:
            break 

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""  #if can't open url, then return empty string
    
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

# If keyword not in index, add keyword and url pair to index.
# If keyword in index and url is not paired with keyword, add url to keyword in index.
# If keyword in index and url is paird with keyword, then do nothing.
def add_to_index(index, keyword, url):
	# format of index: [[keyword, [[url,count], [url,count], ...]], ...]
	for entry in index:
		if entry[0] == keyword:
			for url_entry in entry[1]:
				if url == url_entry[0]:
					url_entry[1] = url_entry[1] + 1
					return	
			entry[1].append([url,0]) #add the url and count
			return
	# not found, add new keyword to index
	index.append([keyword, [[url,0]]])

def add_to_index_with_dict(index, keyword, url):
	# format of index: {keyword: [url, url, ...], keyword: [url, url, ...], ...}
	if keyword in index:
		if url not in index[keyword]: 
			index[keyword].append(url)
	else:
		index[keyword] = [url]
	
#def record_user_click(index, keyword, url):
#	urls = lookup(index, keyword)
#	if urls:
#		for entry in urls:
#			if entry[0] == url:
#				entry[1] = entry[1] + 1
				
def lookup(index, keyword):
	for entry in index:
		if entry[0] == keyword:
			return entry[1]
	return []
	
def lookup_with_dict(index, keyword):
	if keyword in index:
		return index[keyword]
	else:
		None
		

def add_page_to_index(index, url, content):
	words = content.split()
	for word in words:
		add_to_index_with_dict(index, word, url)
	return

# Max_depth indicates the depth to crawl the web. 
# Max_depth = 1 means crawl seed and seed's links.
# Max_depth = 2 means crawl seed, seed's links, and seed's links' links.
def crawl_web(seed, max_depth):
	tocrawl = [seed]
	crawled = []
	next_depth = []
	index = {}
	depth = 0
	while tocrawl and depth <= max_depth:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(next_depth, get_all_links(content))
			crawled.append(page)
		if not tocrawl:
			tocrawl, next_depth = next_depth, []
			depth = depth + 1
	return crawled, index

crawled, index = crawl_web('http://www.udacity.com/cs101x/index.html', 1)

print ""
print ""
print "****************************************"
print "**  Search Engine under development.  **"
print "****************************************"
print ""
print "Crawling the site www.udacity.com/cs101x/index.html with a maximum crawling depth of 1 web page, the following web pages were crawled ="
print ""
print crawled
print ""
print ""
print "Indexing the words in the crawled web pages, the following dictionary includes the indexed words = \r\r"
print ""
print index
