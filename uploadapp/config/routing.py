"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from pylons import config
from routes import Mapper

def make_map():
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    
    map.minimization = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    #map.connect('/error/{action}', controller='error')
    #map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('login', '/login', controller="upload", action="login");
    
    map.connect('/list/', 
        controller="upload", action="list", path="",
        conditions=dict(method=['GET']))
    
    map.connect('/list/*path',
        controller="upload", action="list",
        conditions=dict(method=['GET']))
    
    map.connect('/download/*path',
        controller="upload", action="download",
        conditions=dict(method=['GET']))
    
    map.connect('/list/', 
        controller="upload", action="upload", path="",
        conditions=dict(method=['PUT']))

    map.connect('/list/*path',
        controller="upload", action="upload",
        conditions=dict(method=['PUT']))
    
    map.connect('/list/',
        controller="upload", action="action", path="",
        conditions=dict(method=['POST']))

    map.connect('/list/*path',
        controller="upload", action="action",
        conditions=dict(method=['POST']))
    
    map.connect('/view/*path',
        controller="upload", action="view",
        conditions=dict(method=['GET']))
    
    map.redirect('/', '/list/', _redirect_code='301 Moved Permanently');
    return map
