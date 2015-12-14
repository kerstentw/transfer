import site 

site.addsitedir("/home/tk/pprojects/webpy_blog")

import blog, articles

my_blog_page = blog.Blog(articles.blogtuple,0)

print my_blog_page.returnFullPage()
