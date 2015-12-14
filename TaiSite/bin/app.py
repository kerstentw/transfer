 #!/usr/bin/python
 # -*- coding: <'utf-8'> -*-

import web, site

site.addsitedir("/home/tk/pprojects/TaiSite/bin")
import TaiApp, blog, articles


urls = (
"/index","Index",
"/about","About",
"/blog/(.*)", "Blog",
"/design", "Design",
"/links", "Links",
"/favicon.ico","Icon",
) # All templates are the ClassName.html'

render = web.template.render(
						"/home/tk/pprojects/TaiSite/templates", 
						base = "layout"
						)

class Icon(object):
	def GET(self):
		raise web.seeother("/static/favicon.ico")

class Index(object):
	
	def __init__(self):
		pass
		
	def GET(self):
		My_FrontPage = TaiApp.FrontPage()
		content = My_FrontPage.generateFrontPage()
		return render.Index(content = content)
		
	def POST(self):
		pass
	

class About(object):
	
	def __init__(self):
		pass
	
	def GET(self):
		content = "Applinked"
		return render.About(content = content)
		
		
		
class Blog(object):
	
	def __init__(self):
		pass
		
	def GET(self,pagenum):
		
		blog_page = blog.Blog(articles.blogtuple,pagenum)
		content = blog_page.returnFullPage()
		
		return render.Blog(content = content)
	
	def POST(self):
		pass
	
	
		
class Design(object):
	
	def __init__(self):
		pass
		
	def GET(self):
		content = "Applinked"
		return render.Design(content = content)
		
	def POST(self):
		pass
	
	
	
class Links(object):
	
	def __init__(self):
		pass
	
	def GET(self):
		content = "Applinked"
		return render.Links(content = content)
		
	def POST(self):
		pass
		
app = web.application(urls, globals())
app.wsgifunc()
		

		
if __name__ == "__main__":
	app.run()
