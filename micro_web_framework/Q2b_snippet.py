class microFrame:
	def __init__(self, clz):
		self.handlerMap = buildHandlerMap(clz)
	
	def app(self, env, start_response):
		req = get_req(env)
		try:
			res_body = dispatchReq(self.handlerMap, req)
			response_headers = [
				# For Testing
				# ('Content-Type', 'text/plain' if req.url != '/form' else 'text/html'),
				('Content-Type', 'text/html'),
				('Content-Length', str(len(res_body)))
			]
			start_response('200 OK', response_headers)
			return [res_body]
		except Exception as e:
			err_body = 'Error: ' + e.message
			response_headers = [
				('Content-Type', 'text/plain'),
				('Content-Length', str(len(err_body)))
			]
			start_response('500 Internal Server Error', response_headers)
			return [err_body]
