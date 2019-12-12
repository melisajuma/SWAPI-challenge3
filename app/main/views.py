from flask import make_response, render_template, request, redirect, url_for, abort, flash, jsonify
from . import main
from ..requests import get_people, get_person
import os



@main.route('/')
def index():
    '''
    View root page function that returns the index page 
    '''
    people = get_people()
    title = 'Star Wars | Home.'
    response = make_response(render_template( 'main.html', people = people, title = title ))
    return response

@main.route('/person/<source>')
def person(source):
    '''
    '''
    result = get_person(source)
    title = result.name
    response = make_response(render_template('profile.html', title = title, result = result))
    return response