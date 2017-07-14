import inspect
import logging

def buildHandlerMap(clz):
	inst = clz()
	handlerMap = []
	for mname, handler in inspect.getmembers(inst, predicate=inspect.ismethod):
		if hasattr(handler, 'isHandler') and handler.isHandler:
			handlerMap.append((mname, handler.url, handler.method, handler))
			logging.info('Added route %s %s, handler %s', handler.method, handler.url, mname)
	return handlerMap

def dispatchReq(handlerMap, req):
	for handlerName, url, method, handler in handlerMap:
		if req.url == url and (req.method == method or method == 'ANY'):
			logging.debug('Req %s', handlerName)
			return handler(req)
	raise Exception('No route found')
