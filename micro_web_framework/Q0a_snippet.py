import contextlib
import socket

def parseHeader(headers, line):
	header_name, header_value = line.split(':', 1)
	headers[header_name] = header_value

with contextlib.closing(client_connection.makefile('r')) as client_file:
	request_line = client_file.readline()
	for line in client_file:
		if line in ['\n', '\r\n']:
			break
		parseHeader(headers, line)
	if 'Content-Length' in headers:
		content_body = client_file.read(int(headers['Content-Length']))
