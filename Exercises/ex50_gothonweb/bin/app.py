import web

urls = (
	'/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/') # render object knows how to load .html files out of templates/ because we pass that as a parameter

class Index(object):
	def GET(self):
		greeting = "Hello World"
		return render.index(greeting = greeting) # render object sees we're asking for index, goes to templates/, looks for index.html, then renders it
		
if __name__ == "__main__":
	app.run()