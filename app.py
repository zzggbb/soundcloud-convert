import web
import info

urls = (
  '/swag', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('pages/')

class Index(object):
	def GET(self):
		form = web.input(url=None)
		if form.url is not None:
			response = info.get_song(form.url)
			return render.index(response = response)
		else:
			return render.error()

if __name__ == "__main__":
	app.run()