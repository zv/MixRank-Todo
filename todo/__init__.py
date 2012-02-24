from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view('scripts', 'scripts', cache_max_age=4000)
    config.add_static_view('assets', 'assets')
    config.add_route('home', '/')
    config.add_route('index', '/todos')
    config.add_route('update', '/todos/{todo_id}')
    config.scan()
    return config.make_wsgi_app()

