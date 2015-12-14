#!/usr/bin/python
# -*- coding: <'utf-8'> -*-

import sqlite3,site

site.addsitedir("/home/tk/pprojects/TaiSite/bin")
import testFiles
 
class FrontPage(object):
	
	def __init__(self):
		self.frontpage = ""
		
	def __buildCodingTemplate(self, (article_image, article_title,
							article_date, article_content)):
		
		template = """
		<div id = "MainTextContainer">
		<p>
		<img class = "codefriend" href = {image} ></img>
		<h2> {title} </h2>
		<h3> {date} </h3>
		<br>
		<div class = "FrontPosts">
		{content}
		</div>
		
		</p>
		</div>
		""".format(
			image = article_image,
			title = article_title,
			date = article_date,
			content = article_content,
			)
	
		return template
	
	def dbAcquirePosts(self):
		pass
		
		
	def __localAcquirePosts(self):
		myposts = testFiles.post_tuple 
		return myposts

	def __assemblePosts(self):

		post_list_for_front = []
		posts = self.__localAcquirePosts()  ##For Testing
		##dbAcquirePosts
		
		for entry in posts:
			list_post = self.__buildCodingTemplate(entry)
			post_list_for_front.append(list_post)
			
		self.frontpage = "".join(post_list_for_front)
		
	def generateFrontPage(self):
		self.__assemblePosts()
		return self.frontpage

