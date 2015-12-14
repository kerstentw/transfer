 #!/usr/bin/python
 # -*- coding: <'utf-8'> -*-

testpost = (
"/static/testimage.jpg",
'<a href = "https://github.com/kerstentw/wordartgame"> WordBit </a>',
"15 October 2015",
"""
Wordart is an implementation of an idea by New York artist 
<a href = "http://www.thanelund.com">Thane Lund</a>.
Executed with Python and Pygame, it is a faux 'word game' wherein
a player presses a button and changes the position, content, and color 
of a word on the screen.  this was my first attempt at non character 
stream inputs and screen 
outputs.  The application has been written to be run on a raspberry pi.  
It has been built to take custom input so it can be attached to an 
Arduino board or game controller for display.
  In the repository is both a naive functional prototype and 
  a slightly nicer OOP implementation.  
"""
)

testpost4 = (
"/static/testimage.jpg",
'<a href = "https://github.com/kerstentw/documentalist">\
Documentalist (WIP) </a>',
"5 June 2015",
"""
 Documentalist is a work-in-progress application for analyzing written
 texts.  It will implement a binary tree to figure out what casing and 
 tense a sentence is using by analyzing grammatical structures created
 from a corpus of pre-analyzed works.  It also goes over the texts and 
 gets word counts, most common words, etc.  This is an attempt at
 applying algorithms to tasks involving large bodies of data.
"""
)

testpost2 = (
"/static/testimage.jpg",
"<a href = 'http://www.koreanalex.com'>Korean Alex </a>",
"4 April 2015",
"""
 Link: <a href = "http://www.koreanalex.com">URL</a><br>

Korean Alex is a media personality in Seoul, Korea who writes and acts
in youtube videos, broadcast shows, and various podcasts around South 
Korea.  I built his site as a hub site and portfolio piece to his
specifications, mounting various paging tools I built for web.py apps
into the site.  I also act as the webmaster for the site.  From this
I worked for the first time from the facebook, youtube, and twitter
application programming interfaces (API). 
<br/>
<br/>
It is deployed on a Digital Ocean server with an Ubuntu interface.
I built this by hand with a web.py application on an Apache2 server
in order to build experience using terminal applications such as Vim
greatest amount of control while also learning the basics. 

"""
)


testpost3 = (
"/static/testimage.jpg",
"<a href = 'http://170.107.230.52/gameproposals'>Game Proposals (WIP) </a>",
"1 March 2014",
"""
Game Proposals is my first website I built for supporting an internet
community.  It features a php3 forum, blog feature, and other pages
built on a Postgres SQL backend.  I am currently in the process of 
rewriting the site as a full voting application similar to reddit, 
built on a Ruby on Rails backend.

It is deployed on a Digital Ocean server with an Ubuntu interface.
"""
)




###########################################################################

post_tuple = (testpost, testpost4, testpost2, testpost3)
