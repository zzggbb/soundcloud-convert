import web
import info

URLS = ('/convert', 'Index')

app = web.application(URLS, globals())
render = web.template.render('pages/')

class Index(object):
	def GET(self):
		return render.index()

	def POST(self):
		form = web.input(url=None)
		if form.url is not None:
			response = info.info(form.url)
			if not response:
				return render.error()
			else:
				return render.response(response = response)

if __name__ == "__main__":
	app.run()