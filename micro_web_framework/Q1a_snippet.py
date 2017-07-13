import string
import urlparse

def httpFormat(headername):
	return string.capwords(headername[5:].replace('_', '-'), '-')

def extractHeaders(env):
	return { httpFormat(name): val for name, val in env.iteritems() if name.startswith('HTTP_') }

def get_req(env):
	r = HttpReq()
	r.url = env['PATH_INFO']
	r.method = env['REQUEST_METHOD']
	r.headers = extractHeaders(env)
	if r.method == 'GET':
		try:
			r.getparams = urlparse.parse_qs(env['QUERY_STRING'], True)
		except (ValueError):
			r.getparams = {}
	try:
		request_body_size = int(env.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	#print request_body_size
	if r.method == 'POST' and request_body_size > 0:
		req_body = env['wsgi.input'].read(request_body_size)
		#print req_body
		r.postparams = urlparse.parse_qs(req_body, True)
	return r
