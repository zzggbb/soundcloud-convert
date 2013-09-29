import web
import info
from random import choice

urls = (
  '/convert', 'Index'
)

lilb = ['http://content.animalnewyork.com/wp-content/uploads/lil_b_grammys_blocked_gig.jpg',
		'http://8tr.s3.amazonaws.com/i/000/460/481/Lil-B-9347.jpg',
		'http://1.bp.blogspot.com/-QDpiWZs2sKI/UdmNiWIywPI/AAAAAAAAAa4/Rqldr4IVENs/s640/maxresdefault.jpg',
		'http://25.media.tumblr.com/tumblr_m8xc441ezB1r899c9o1_1280.jpg']

app = web.application(urls, globals())

render = web.template.render('pages/')

class Index(object):
	def GET(self):
		form = web.input(url=None)
		swag = choice(lilb)
		if form.url is not None:
			response = info.get_song(form.url)
			return render.index(response = response, swag = swag)
		else:
			return render.error(swag = swag)

if __name__ == "__main__":
	app.run()