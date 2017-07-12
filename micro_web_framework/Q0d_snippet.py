import multiprocessing

def app(environ, start_response):
	"""A barebones WSGI application.

	This is a starting point for your own Web framework :)
	"""
	status = '200 OK'
	response_headers = [('Content-Type', 'text/plain')]
	start_response(status, response_headers)
	return ['Hello world from a simple WSGI application!\n']


def runHttpd(app):
	httpd = make_server(SERVER_ADDRESS, app)
	httpd.serve_forever()

def start_daemon(app):
	p = multiprocessing.Process(target=runHttpd,args=(app,))
	p.daemon = True
	p.start()
	return p
