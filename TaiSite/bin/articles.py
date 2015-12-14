###Get this into a Database pronto.  Doing this shit by hand is super retarded



blogdic1 = { ################ NOT ACTIVE
	"Title":"Reinventing the wheel: Building an admin site from scratch.",
	"Author": "Tai Kersten",
	"Date" : "The date of the blog-- mm/dd/yy",
	"Content" : """    One of the first tutorials I did for Python was Zed A. Shaw's

'Learn Python the Hardway' wherein he asserts that banging ones head

against a problem was an excellent way to learn how to program.  In this

tradition, I am setting about tackling an app that has been built

many times in the past for my own edification and to work on my own problem

solving skills.


    During the past month I have been working on building my second website

completely from scratch.  This means that I am not using any boilerplate,

bootstrapping, drag and drop, or pre made graphics.  I am attempting to build the entire site

by myself using text editors for code and gimp/inkblot for graphics.  As of currently, I have a working front end which pulls data from a database managed by postgresql.


I will supply a link and a write up on that as it starts looking less crappy.


    Currently, I need an admin site on the backend that can allow entries into the front

page's newsfeed as well as make entries into a longform 'features'  section

of the website.  It needs to be fully accessible from any area of the internet

while also limiting the users to a core group of administrators.


    I want to build an admin site that  can place and remove

elements of a database which will be displayed by

the front end.  It needs three items of core functionality with the ability

to be fully modular in the case that I want to add functionality or to accommodate

any growth on the front site.


The three core functions are:


1.) A log in front page using sessions and a store of encrypted passwords.

2.) The ability to view the contents of the site database.

3.) The ability to edit/add/delete contents from the database.


So essentially the admin is a wrapper for the back end of the

database.  It will make changes to the site that will be fully

visible to any user.


I will be building it with python.web.py/apache/html and should be extremely

simple to use.  More updates to follow as I bang my head against this one..."""
	}

blogdic2 = {############## NOT ACTIVE
	"Title":"The Blog Title 2",
	"Author": "The Author of the Blog",
	"Date" : "The date of the blog-- mm/dd/yy",
	"Content" : "The actual Post"
	}
	
blogdic3 = {
	"Title":"Web Admin Update and other stuff",
	"Author": "Tai Kersten",
	"Date" : "3/15/2015",
	"Content" : """I have been busy as of late starting some online classes, working on my basics of Korean and programming, while also trying to have friends.  It's a full time job I tell ya.  Anyway, I will be doing a post soon on part 3 of the web admin and on how I am beginning to understand various tools such as github, pip, and vm.

The web admin post may take a bit.  It has gone from being an app for the site I am working on to becoming a full on app that can generate an admin site for any website I build in the future.  I think it's a better tool for me and I will be including the repository for it in the future.

Sorry for the wait.  This will be going up soon.   "
	"""
	}
	
blogdic4 = {
	"Title": "Math is Hard",
	"Author": "The Author of the Blog",
	"Date" : "3/6/2015",
	"Content" : """
		
		To an outsider, math looks a lot like a more boring form of tarot or tea leaves reading.  

I took a class in University by a professor named Warren Esty entitled, "The Language of Mathematics".  It was a class that took a slightly different viewpoint on math wherein we discussed the forms of Mathematics as language acts, treating math as a descriptive act.  We started with basic algebra and then moved into sets and proofs while learning the basics of axioms and trying to get to QED via proofs.  I liked this class as it contained very little arithmetic.

However, when I showed the book to a more "math brained" engineer friend he remarked "This isn't real math," and walked off.  He may have been right, it was a 100 level class for English majors to get their math prereq out of the way.  I did learn a fair bit about math and it was nice to finally find out that it involved more than just filling out times tables which had been my experience with the field up to that point. 

That said, I did receive a 'C' in the class because I didn't do the homework.  However, a very friendly and motivated TA named something something Smiley did teach me a very important lesson about math that may have been erroneous but I am hoping not:

Math is learnable. 

This seems like a strange and obvious thing, however, for a long time I have been told that some people 'just can't do math' which is severely demotivating to a self learner.  Academically, math has never been a strong suit of mine.  I was quite good at it for a while but then fell off, getting flummoxed in the equations of Mr. Swenson's physics class and finally losing my way entirely on the way to calculus.  I may just not be 'math brained'... however, I refuse to believe this  Mainly for one reason...

I am lazy.

I have always been lazy and continue to be so.  Luckily, I have been told this is a good characteristic for a programmer.  This also bodes well for my math education because It means that I didn't learn math well back in school, not because of my lacking of base intelligence, but rather because I never did apply myself in math class with any earnestness.  I didn't learn math for the same reason I didn't learn French after a year of taking it: I didn't study, do the homework, or attend many classes. 

I am currently working under the assumption that I can learn math and then learn to apply it.  I just have to be less lazy.

Here's the plan of attack:

1.) I am planning on taking the GRE whose math section is focused on more logic and 'mathematical thinking' kinds of things over large arithmetic problems or solving through erudite equations.  I hope by preparing for the test I can simply become more comfortable with thinking about math and building problem solving routines under a time crunch.       

2.) Taking online classes and perhaps a terrestrial class here in Seoul (oh yeah I live in Seoul, Korea too.  It's a great city for self study, there are a glut of resources).  I want to take more traditional classes simply to get forced to do things that I dont want to do and to maintain motivation since, let's face it, math isn't fun a lot of the time.  I will focus on discreet mathematics since it is most directly related to thinking about programs and algorithms as well as a pre-calc course since this is where I left off.  I am also hoping to pick up some large erudite equations to jam in my head too.

3.) I am going to spend time writing small applets, after I finish this admin site, that deal more with calculations and analysing numerical data.  This is useful for obvious reasons.  Also, I find that I learn best when I am trying to problem solve and apply new ideas so just jumping in and making mistakes seems like a healthy thing to do.

I will be posting more here about that third one as I begin trying to make applets that aren't total garbage using the various math libraries that python offers.  If I'm wrong about learning math then, well, shit.  Probably will move to an organic farm in NorCal and till manure between bouts of throwing pottery (actually that sounds pretty nice). 
		
		"""
	}
	
blogdic5 = {
"Title":"Reinventing the wheel part 2: First attempt.  I screwed up.",
"Author": "Tai Kersten",
"Date" : "3/2/2015",
"Content" : """
	Welp after a solid two days of plugging code into a python file I have built a rudimentary admin site with the ability to log in and check sessions.  It also can insert information from input boxes and can read from the Postgresql database.  However when I start getting into editing the database, specifically, being able to change previously written posts and/or delete them from the database, I ran into some trouble.  I think I have figured out why and will be writing a large section of the framework  over again and completely overhauling the module that reads from the database.

What follows is a breakdown of what I did, what I did wrong, and then how I will proceed to solve this problem or, in the very least, have more screwups to blog about (and, of course, learn from).

So here we go,

First I created the web.py application and set up sessions.

Here's a bit of the application :


Some notes (These are also comments in the code):

#passbool (created in the initializer in the session instantiation and stored in the instance.) changes if the input from the user matches with the password and user on record.

#adminpage is the primary handler module that contains the functions to edit, delete, and add elements to the site's database.  It also creates the HTML for the admin page itself (this also creates a myriad of problems for me since I didn't keep them modular and I keep passing around data between functions really clumsily.  More on that later)

# The Key is the name and the dictionary entry is the password.  I would rather keep these in an encrypted database... need to figure out how to do that and then have it talk to the application...more learning!

#I generate html blocks in the handler classes for each page then have them get served into the html via a '$:content' variable on the html page.  I do this because it allows for a more dynamic page and cuts down on the number of html files I have in the directory.  I would use forms but the web.py form support is just as unwieldy as this with less fine control of the actual html.  (However, this bites me in the behind later for reasons that will become clear).

#wbc is a terrible variable name and I don't remember why I chose it.  I need to fix this as well as adopt a better naming practice.  WBC is the list of inputs from the html.  I build the submission tuples that the adminpage module places in the database.

#Submit tuple needs to be (integer(1: blog, 2: features), postnumber, title, author, date, body).  This tuple takes the information provided in the input form on the page and organize it based on the labels above.  The integers allow the 'adminpage' module to separate the posts going to a blog and a features section of the site.

#The edit page is at all coded because I'm not sure I need to use it or have that functionality attached to the adminpage module.

# There are 4 pages here:  The login page where the user submits their name and password.  The admin page which basically just takes html blocks from the app and adminpage module for editing the database... once again, not sure if this is the best way to do this.  The passon is a page the links the login and admin pages.  I want this buffer page for testing and may not be there in the final since the admin page has the ability to check passbool.  The logout page just kills the session and kicks the user out of the page. 

The application file:

(You can see me using a lot of default variable names here.  I'm not sure if this is best practice but it works and makes looking things up easier).
<div class = "codebox"><code> 
 import web, site, time

site.addsitedir('/home/user/programming/admin')
import sqlhandler, adminpage

#adminpage is the module that contains the SQL scripts and #functions that edit the database which connects with the #frontpage.


urls = ('/login','LogIn',
        '/admin','Admin',
        '/passon','PassOn',
        '/logout', 'LogOut',
        )

web.config.debug = False


render = web.template.render('/home/tai/programming/admin')

app = web.application (urls, locals())

session = web.session.Session(app, web.session.DiskStore('/home/user/projects/admin/pass_bool'), initializer = {'pass_bool' : False}) #passbool changes if the input from the user matches with the password and user on record.

class LogIn(object):
   
    session.pass_bool = False

    def __init__(self):
       
        self.authenticated = {
            'admin' : 'notreal',
            'admin2' : 'alsonotreal',
            } # The Key is the name and the dictionary entry is the password.  I would rather keep these in an encrypted database... need to figure out how to do that and then have it talk to the application...
       
        self.loginhtml = ' &ltform class = "" action = "/login"  method = "POST"&gt&ltbr/&gt\
                    User: &ltinput type = "text" value = "User" name = "user"&gt &ltbr/&gt\
                    Password: &ltinput type = "password" value = "Password" name = "pwd"&gt&ltbr/&gt\
                    &ltinput type = "submit" value = "LOG IN"&gt &lt/form&gt' #I generate these html blocks then have them get served into the html.  I do this because it allows for a more dynamic page and cuts down on the number of html files I have in the directory.  I would use forms but the web.py form support is just as unwieldy as this with less fine control of the actual html.
               
    def GET(self):
        if session.pass_bool == False:
            content = self.loginhtml
            return render.login(content = content)

        elif session.pass_bool == True:
            return web.seeother('/admin')
           
        else:
            return "Session Error.  Check Cookies settings"
           
    def POST(self):
       
        pass_input = web.input()
       
       
        if session.pass_bool == False and pass_input.user in self.authenticated:
            if pass_input.gpapwd in self.authenticated[pass_input.user]:
                session.pass_bool = True
                raise web.seeother('/passon')
               
            else:
                content = '&ltem style = "color: red"&gt Incorrect password &lt/em&gt' + self.loginhtml # More HTML blocks in the app.
                return render.login(content = content)
               
        elif session.pass_bool == True:
            raise web.seeother('/admin')
           
        else:
            content = '&ltem style = "color: red"&gt Incorrect user or password &lt/em&gt' + self.loginhtml
           
            return render.login(content = content)

           
   
application = app.wsgifunc()
           


           
class PassOn(object):
   
    def GET(self):
        content = 'Password Accepted.  &lta href = "/admin" &gtContinue&lt/a&gt ' + '\n STATUS TEST = ' + str(session.pass_bool)
        return render.login(content = content) #STATUS TEST is #just for testing and won't be in the final application.



class Admin(object):
   
    def GET(self):
        if session.pass_bool == True:
            content = adminpage.admingen()
            return render.admin(content = content)
        else:
            content = 'password is incorrect. &lta href = "/login"&gtReturn to log-in&lt/a&gt'
            return render.admin(content = content)
           
    def POST(self):
        wbc = web.input() #Construct the tuple x here and send to adminpage.adminpage_put(x) #wbc is a bad name.

        #Submit tuple needs to be (integer(1: blog, 2: #features), postnumber, title, author, date, body)

       date = time.localtime()[0:3]
       
       
        try:
            #For blog
            admintuple = (1, wbc.bpostn, wbc.btitle, wbc.bauthor, date, wbc.bbody)
        except:
            admintuple = (2, wbc.fpostn, wbc.ftitle, wbc.fauthor, date, wbc.fbody)
       
        finally:
            content = adminpage.adminpage_put(admintuple)
       
        return render.admin(content = content)       



class LogOut(object):
   
    def GET(self):
        session.passbool = False
        session.kill()   
        content = 'Logged out &lta href = "/login"&gtReturn to Log in&lt/a&gt'   
        return render.login(content = content)
               
               
class EditPage(object):
    #The edit page is not done because I'm not sure I need to use it.
   
    def GET(self):
        pass
       
    def POST(self):
        pass
               

application = app.wsgifunc()

if __name__ == "__main__":
    app.run()
 
</div></code> 	
The adminpage module (This is the heart of my problems and thus the heart of my problems):

<div class = "codebox"><code> 
import psycopg2, os, site, time
### Interation 1: Just get the inputs into the SQL database

def adminpage_put(submit_tuple):
    ''' Takes input tuple, parameterizes it, and places it inside SQL database.'''
    #Submit tuple needs to be (integer(1: blog, 2: features), postnumber, title, author, date, body)
  
  
    #Opens connection with the database.
  
    conn = psycopg2.connect("port = 0000 dbname = blargh password = caca user = postgres host = localhost")
    cur = conn.cursor()
  
    #Pulls into from the submission tuple
  
    post_number = submit_tuple[1]
    title = submit_tuple[2]
    author = submit_tuple[3]
    date = submit_tuple[4]
    body = submit_tuple[5]
  
  
    # Decides which database to put it into
    if submit_tuple[0] == 1:
        cur.execute('SELECT * FROM  "GP_blogs";\
                    INSERT INTO "GP_blogs"("post_num", "title", "author", "date", "body") VALUES \
         (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (str(post_number), title, author, date, body))
      
        conn.commit()
        cur.close()
        conn.close()

    elif submit_tuple[0] == 2:
        cur.execute('SELECT * FROM  "GP_features";\
                    INSERT INTO "GP_features"("post_num", "title", "author", "dte", "body") VALUES \
         (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\');' % (str(post_number), title, author, date, body))
      
        conn.commit()
        cur.close()
        conn.close()
  
    conn.close()
  
    return "Submission successful into %r &lta href = '/admin'&gtGo Back&lt/a&gt" % submit_tuple[0]
          

  


def adminpagedisplay():
    ''' Displays current posts on admin page to be edited. '''
  
    conn = psycopg2.connect("port = 0000 dbname = blargh password = caca user = postgres host = localhost")
    cur = conn.cursor()


def admingen():
  
    conn = psycopg2.connect("port = 0000 dbname = blargh password = caca user = postgres host = localhost")
    cur = conn.cursor()
  
    cur.execute('SELECT * FROM "GP_news"')
    news_posts = cur.fetchall()
        
          
  
    cur.execute('SELECT * FROM "GP_features"')
    features_posts = cur.fetchall()
  
    ''' Displays the input page for the admin '''
  
    return '''
  
    &lth2&gtNews Input:&lt/h2&gt

    Current: %r &ltbr/&gt
  
  
    &ltform action = "/admin" method = "POST"&gt
      
        Post class number: &ltinput type = "integer" name = "bpostn" value = "#" &gt&ltbr/&gt
        Title: &ltinput type = "text" name = "btitle" value= "Enter Title Here"&gt&ltbr/&gt
        Author: &ltinput type = "text" name = "bauthor" value = "Enter Author Here"&gt&ltbr/&gt
      
        &ltbr/&gt
        Body (Max 60,000 characters): &ltbr/&gt
            &lttextarea name = "bbody" rows = "15" cols = "40"&gt&lt/textarea&gt&ltbr/&gt
      
      
        &ltbr/&gt&ltinput type = "submit" value = "Save"&gt
    &lt/form&gt
    &ltbr/&gt
    &ltbr/&gt
  
    Current: %r &ltbr/&gt
  
    &lth2&gtFeatures Input:&lt/h2&gt
    &ltform action = "/admin" method = "POST"&gt
      
        Post class number: &ltinput type = "integer" name = "fpostn" value = "#" maxlength = "3"&gt&ltbr/&gt
        Title: &ltinput type = "text" name = "ftitle" value= "Enter Title Here" maxlength = "255"&gt&ltbr/&gt
        Author: &ltinput type = "text" name = "fauthor" value = "Enter Author Here" maxlength = "255"&gt&ltbr/&gt
      
        &ltbr/&gt
        Body (Max 60,000 characters): &ltbr/&gt
            &lttextarea name = "fbody" rows = "15" cols = "40" maxlength = "60000"&gt&lt/textarea&gt&ltbr/&gt
      
      
        &ltbr/&gt&ltinput type = "submit" value = "Save"&gt
    &lt/form&gt
  
    &lta href = '/logout' &gt Logout &lt/a&gt
 
  
  
  
''' % (news_posts, features_posts)

  
def adminedit(request):
    pass

</div></code> 


The problem:

So I think my problems start here.  

First, the whole thing isn't very well connected.  The 'module' is really just a smattering of functions that each serve a vague purpose.  One takes inputs from the application and injects it into a SQL table.  Another generates the page itself with its inputs.  None of them, however talk to each other and rely on getting data passed to them through the application.  This makes the module completely specialized and most of the code is not reusable for other aspects of the site since each function solves exactly one part of one problem.  For instance, every time I need to make requests to the database I have to use the psycopg2 module to open a connection and a cursor.   I think I need a more extensively OOP  approach as well as greater modularity where requests and data from the front end can be passed around and edited as it is needed. Perhaps 2 classes, one that generates the html and another that handles all SQL requests with a single connection and a single cursor.  The latter can take requests from the application as well as pass that info to the former SQL handling class which has a single connection to the database. This will also make edit and delete functions easier to implement because I can pull data, work with it then put it back with the same data scope and not have to worry about what data a function is working with since, right now, I have three or four tuples being thrown around in an entirely different module as my flow control. This should help clean up the dataflow of the whole program which leads to the next problem.  

Next, the data flow of this program is like a plate of spaghetti which is making creating delete and edit functions a pain.  Currently, I have to bounce between a bunch of different connections while the module has to juggle different groups of tuples.  I feel like this is really clumsy and also highly non-pythonic since I'm repeating myself a bunch.  In fact, not only do I repeat these connections a bunch I do so between two different modules.  As this gets bigger, I only see confusion about which set of user data is going where.  Ideally I will have the application which simply handles requests to the server and takes inputs but then the 'adminpage' module takes care of all the requests and places things into the database.  In fact, it may be cleaner to seperate the 'adminpage' module into two.  One that handles generating html, and one that actually handles data in a single class that makes a single connection to the database.

I could take the raw input from the front page, organize it in the class constructor then handle requests with functions in the class while also having only one set of data to work with.  This will definitely help with the edit function which is a slightly bigger pain.  This should also improve performance and is a cleaner OOP solution.

Last, The code itself is just plain messy.  I need to go back over my PEP8 guidelines and clean it up.  It took me far too long to parse through this to make this post. 

Conclusion:

I am aware that there are many other problems to consider than these three but I first want something that works period which then I will go back and improve upon.

I'm pretty sure if I gather my data better in one place, allow the passing of data more fluidly between functions (by using classes rather than free floating functions tied together in the application), clean up the syntax, and improve data flow, I can really make this work.  Hopefully the next (or, probably, second to next post) will be me explaining how I fixed it!  Next time though I think I am going to do a post about learning math since I am also currently in the middle of really overhauling the logic centers of my brain and I have some thoughts (or delusions) about relearning, unlearning, and discovering an entirely new skill. 
	"""
}



blogdic6 = {
	"Title":"Reinventing the wheel: Building an admin site from scratch.",
	"Author": "Tai Kersten",
	"Date" : "3/4/2015",
	"Content" : """ 
		
		One of the first tutorials I did for Python was Zed A. Shaw's
'Learn Python the Hardway' wherein he asserts that banging ones head
against a problem was an excellent way to learn how to program.  In this
tradition, I am setting about tackling an app that has been built
many times in the past for my own edification and to work on my own problem
solving skills.

    During the past month I have been working on building my second website
completely from scratch.  This means that I am not using any boilerplate,
bootstrapping, drag and drop, or pre made graphics.  I am attempting to build the entire site
by myself using text editors for code and gimp/inkblot for graphics.  As of currently, I have a working front end which pulls data from a database managed by postgresql.

I will supply a link and a write up on that as it starts looking less crappy.

    Currently, I need an admin site on the backend that can allow entries into the front
page's newsfeed as well as make entries into a longform 'features'  section
of the website.  It needs to be fully accessible from any area of the internet
while also limiting the users to a core group of administrators.

    I want to build an admin site that  can place and remove
elements of a database which will be displayed by
the front end.  It needs three items of core functionality with the ability
to be fully modular in the case that I want to add functionality or to accommodate
any growth on the front site.

The three core functions are:

1.) A log in front page using sessions and a store of encrypted passwords.
2.) The ability to view the contents of the site database.
3.) The ability to edit/add/delete contents from the database.

So essentially the admin is a wrapper for the back end of the
database.  It will make changes to the site that will be fully
visible to any user.

I will be building it with python.web.py/apache/html and should be extremely
simple to use.  More updates to follow as I bang my head against this one...
"""
	}
	
blogdic7 = {
	"Title":"Indroduction.",
	"Author": "Tai Kersten",
	"Date" : "2/24/2015",
	"Content" : """    
		Just to get this out of the way.  First post.

I am a new entrant into the world of programming.  I am currently working on learning python, postgresSQL, HTML, and CSS.  This seems to hint at a fascination with web design which isn't the case.  I just kind of wandered into doing that and it hasn't made me bored yet and I enjoy learning the stuff so far.

I do not have an academic background in computer science, nor do I have a really comprehensive background in mathematics or design or engineering or any other tangentially related field.  Rather, I have a Bachelors of Arts in Literature from Montana State University where I studied a general field of various writings from all about the canon.  For any engineers reading this and scoffing over your well honed math skills and ability to tell the difference between various polymers and functions and whatnot.  I understand.  Please carry on. This little Plebian is still going to try anyway.

For the rest, this blog is going to be a record of my screw ups and musings on various projects I decide to undertake as well as any other technology or engineering related nonsense I drudge up in my day - to - day.  Most of all though I hope for it to be a record of my growth as a thinker, problem solver, and a sounding board for my curiosity to steer itself.
"""
	}
	

blogtuple = [blogdic3,blogdic4,blogdic5,blogdic6,blogdic7] #no blogdic1 or 2
	
