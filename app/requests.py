from .models import Person
import requests, json


def get_people():
    '''
    '''
    data = requests.get('https://swapi.co/api/people').json()
    response = []
    res = data['results']
    if res:
        response = [ Person(item) for item in res ]
    return response


def get_person(source):
    '''
    '''
    data = requests.get('https://swapi.co/api/people/'+source).json()
    # print(data)
    response = {}
    if data:
        response = Person(data)
        return response