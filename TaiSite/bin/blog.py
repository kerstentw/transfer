global ARTICLES_PER_PAGE
ARTICLES_PER_PAGE = 2


"""
	1. Instantiate Blog class
	2. Check current Page
	3. Assemble Functions
	4. Send View to app
	
	The instantiation needs number to know what page to go for.
"""

class Blog(object):
	"""
	1. Instantiate Blog
	2. Check current Page
	3. Assemble Functions
	4. Send View to app
	
	This is parent class for Blog:
	
	This collects the data from a tuple of dictionaries
	
	Arranges it into pages of a set number of articles
	
	and IF there are more than the set number of pages
	 
	Create an index of blogs based on the date of blogs 
	
	The Blog Dictionary:
	
	blogdic = {
	"Title":"The Blog Title",
	"Author": "The Author of the Blog",
	"Date" : "The date of the blog-- mm/dd/yy",
	"Content" : "The actual Post"
	}
	
	Needs to be placed in a tuple for pagination.
	
	Assemble and return a full page from outside class.  THIS IS THE ONLY PART THAT THE
	APP TOUCHES.
	
	This needs to be inserted into a class that looks like this:
	
	urls = ("/blogs/(.*)", "Blogs")
	
	"""
	
	def __init__(self, tuple_of_entries = None, current_page = 0):
		self.tuple_of_entries = tuple_of_entries
		self.fullpagelist = []
		self.pagemap = []
		self.current_page = int(current_page)


	def __createDictionaryTuple(self):
		
		"""
		Unpack dictionary tuples then 
		Repack them into a tuple
		of strings.  This is what the mapper reads.
		1
		"""
		
		workinglist = []
		
		for entry in self.tuple_of_entries:
			post = """
			<div class = "blogentries">
			<h1>{Title}</h1>
			<h2>{Author}</h2>
			<h3>{Date}</h3>
			<p>{Content}</p>
			</div>
			""".format(
			Title = entry["Title"],
			Author = entry["Author"],
			Date = entry["Date"],
			Content = entry["Content"]
			)
			
			workinglist.append(post)
	
		self.tuple_of_entries = workinglist



	def __createPageTuples(self):
		"""Create a URL map of links to guide around posts
		DO NOT USE CURRENT PAGE FOR REFERENCE
		2
		"""
		
		upperIndex = ARTICLES_PER_PAGE
		initial_list = range(100)
		initialIndex = 0
		counter = 0
		final_list = []

		while counter <= (len(self.tuple_of_entries)/ARTICLES_PER_PAGE):
			final_list.append(self.tuple_of_entries[initialIndex:upperIndex])
			initialIndex += ARTICLES_PER_PAGE
			upperIndex += ARTICLES_PER_PAGE
			counter += 1
	
		self.tuple_of_entries = tuple(final_list)	
	

	def __createPageMap(self):
			"""Create a URL map of links to guide around posts
			DO NOT USE CURRENT PAGE FOR REFERENCE
			3
			"""
	
			num_of_links = (len(self.tuple_of_entries)/ARTICLES_PER_PAGE) + 1
			
			counter = 0 
			
			map_link = '<a href = "/blog/{map_num}" class = "numberlinks">{map_num}</a>'

			while counter <= num_of_links:
				self.pagemap.append(map_link.format(map_num = counter))
				counter += 1
			
			self.pagemap = "".join(self.pagemap)

	def assembleAll(self):
		"""
		Runs all the functions and places them into a list
		"""
		self.__createDictionaryTuple()
		self.__createPageTuples()
		self.__createPageMap()
	
		final_page = self.pagemap + "".join(self.tuple_of_entries[self.current_page]) + self.pagemap
		
		return final_page
	
	def navigatePages(self,current_page = 0):
		"""
		Set up what the pagination does
		This will take an argument from the browser navigation bar.
		
		Deprecated.  Gets handled when the class is instantiated.
		"""
		self.current_page = current_page
		
		

	def returnFullPage(self):
		if self.tuple_of_entries is None:
			return "There are no Blogs"
		
		else:	
			return self.assembleAll()

#def GetPage():
#	myBlog = Blog()
#	full_blog_page = myBlog.returnFullPage()
#	return full_blog_page

### Instantiate Blog with pagination number...then run returnFullPage
