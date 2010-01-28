"""The base Controller API

Provides the BaseController class for subclassing.
"""
import os
import grp

from pylons.controllers import WSGIController
from pylons.templating import render_mako as render

from pylons import request, config
from pylons import tmpl_context as c

from uploadapp.lib import fakeuser

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']

        if request.environ.has_key("HTTP_REMOTE_USER"):
            c.user = fakeuser.SystemUser(request.environ.get("HTTP_REMOTE_USER"));
        else:
            c.user = fakeuser.SystemUser("nobody", anonymous=True);
        
        c.group = grp.getgrnam(config["uploadapp.group"]);
        
        return WSGIController.__call__(self, environ, start_response)
