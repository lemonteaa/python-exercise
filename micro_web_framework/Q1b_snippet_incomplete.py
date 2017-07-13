import inspect

class route:
	def __init__(self, url, method='ANY'):
		self.url = url
		self.method = method
	
	def __call__(self, f):
		#dependency injection
		args, _, _, defaults = inspect.getargspec(f)
		def wrapped_reqHandler(self, req):
			def bind_one_param(req, name):
				params = {}
				if req.method == 'GET' and hasattr(req, 'getparams'):
					params = req.getparams
				if req.method == 'POST' and hasattr(req, 'postparams'):
					params = req.postparams
				if not (name in params):
					return None
				vals = params[name]
				if len(vals) > 1:
					return vals
				else:
					return vals[0] #Really?
			args_val = { name: bind_one_param(req, name) for name in args }
			args_val['self'] = self #TODO for get param self
			return f(**args_val)
		# Stuffing additional attribute (different from dict!) to callable...
		# We will use that in later exercise
		wrapped_reqHandler.isHandler = True
		wrapped_reqHandler.url = self.url
		wrapped_reqHandler.method = self.method
		return wrapped_reqHandler
