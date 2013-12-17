import web
import info
import info2

URLS = ('/convert', 'Index')

app = web.application(URLS, globals())
render = web.template.render('pages/')

class Index(object):
	def GET(self):
		return render.index(state = True)

	def POST(self):
		form = web.input(url=None)
		if form.url is not None:
			response = info2.info(form.url)
			if not response:
				return render.index(state = False)
			else:
				return render.response(response = response)

if __name__ == "__main__":
	app.run()