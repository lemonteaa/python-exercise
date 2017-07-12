# Note: Just a suggestion, you are free to add log at whatever place you feel can help
# In part 1
	logging.info('Serving HTTP on port %s ...', PORT)
		logging.info('%s - %s', request_line.rstrip('\r\n'), client_address)
		if 'Content-Length' in headers:
			logging.debug('Content-Body: %s', content_body)

# In part 2
		logging.info('Server init\'ed')
		logging.info('Serving HTTP on port %s ...', self.server_port)
		
		# Log result
		logging.info('%s %s - %s', self.headers_set[0], request_line.rstrip('\r\n'), client_address)
		if 'Content-Length' in headers:
			logging.debug('Request Content-Body: %s', content_body)
