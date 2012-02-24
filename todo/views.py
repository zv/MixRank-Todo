from pyramid.view import view_config

from pyramid.renderers import render_to_response
import json

from .models import (
    DBSession,
    Todo,
    )


@view_config(route_name='home')
def home(request):
    return render_to_response('templates/index.pt', {}, request=request)

@view_config(renderer='json', route_name='index', request_method='GET')
def index(request):
    query = DBSession.query(Todo)
    results = query.all()
    todos = []
    for todo in results:
        todos.append(todo.to_dictionary())
    return todos

@view_config(renderer='json', route_name='index', request_method='POST')
def create(request):
    params = json.loads(request.body)
    todo = Todo(**params)
    DBSession.add(todo)
    return todo.to_dictionary()

@view_config(renderer='json', route_name='update', request_method='PUT')
def update(request):
    pass

@view_config(renderer='json', route_name='update', request_method='DELETE')
def destroy(request):
    DBSession.query(Todo).filter(Todo.id==request.matchdict['todo_id']).delete()
