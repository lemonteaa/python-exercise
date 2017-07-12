# Split parse_request(self, text) into 
# parseHeader(self, headers, line) and parseRequestLine(self, request_line)

	def wsgiFormat(self, headername):
		return 'HTTP_' + headername.upper().replace('-', '_')
	
	def mergeHeaders(self, env, headers):
		env.update({ self.wsgiFormat(name): val for name, val in headers.iteritems()})
	
	def get_environ(self, headers, content_body):
		# omit...
		env['wsgi.input']        = StringIO.StringIO(content_body) if content_body else None
		# ...
		p = self.path.split('?', 1)
		env['PATH_INFO']         = p[0]                         # /hello
		env['QUERY_STRING']      = p[1] if len(p) > 1 else ''   #t=1&b=2
		# ...
		env['CONTENT_LENGTH']    = headers['Content-Length'] if 'Content-Length' in headers else '0'
		#Add request headers
		self.mergeHeaders(env, headers)
		# ...
