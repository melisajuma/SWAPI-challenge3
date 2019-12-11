class Person:
    '''
    '''
    def __init__(self, item):
        '''
        '''
        self.name = item.get('name')
        self.created = item.get('created')
        self.edited = item.get('edited')
        self.birth_year = item.get('birth_year')
        self.eye_color = item.get('eye_color')
        self.gender = item.get('gender')
        self.hair_color = item.get('hair_color')
        self.height = item.get('height')
        self.homeworld = item.get('homeworld')
        self.films = item.get('films')
        self.mass = item.get('mass')
        self.skin_color = item.get('skin_color')
        self.species = item.get('species')
        self.starships = item.get('starships')
        self.url = str(item.get('url')).strip('https://swapi.co/api/people')
        self.vehicles = item.get('vehicles')