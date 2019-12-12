import requests

class Person:
    '''
    '''
    def __init__(self, item):
        '''
        '''
        self.name = item.get('name')
        # self.created = item.get('created')
        # self.edited = item.get('edited')
        # self.birth_year = item.get('birth_year')
        self.eye_color = item.get('eye_color')
        # self.gender = item.get('gender')
        # self.hair_color = item.get('hair_color')
        # self.height = item.get('height')
        # self.homeworld = self.getHomeWorld(item.get('homeworld'))
        # self.films = self.getFilms(item.get('films'))
        # self.mass = item.get('mass')
        self.skin_color = item.get('skin_color')
        # self.species = self.getSpecies(item.get('species'))
        # self.starships = self.getStarShips(item.get('starships'))
        self.url = str(item.get('url')).strip('https://swapi.co/api/people')
        # self.vehicles = self.getVehicles(item.get('vehicles'))


    # @classmethod
    # def getVehicles(cls, carListUrl):
    #     '''
    #     '''
    #     carList = []
    #     for item in carListUrl:
    #         car = requests.get(item).json()
    #         if car:
    #             carList.append(car)
    #     return carList
    
    # @classmethod
    # def getHomeWorld(cls, homeWorldUrl):
    #     '''
    #     '''
    #     homeWorld = {}
    #     data = requests.get(homeWorldUrl).json()
    #     if data:
    #         homeWorld = data
    #     return homeWorld
    
    # @classmethod
    # def getStarShips(cls, starShipUrl):
    #     '''
    #     '''
    #     starShips = []
    #     for item in starShipUrl:
    #         data = requests.get(item).json()
    #         if data:
    #             starShips.append(data)
    #     return starShips
    
    # @classmethod
    # def getSpecies(cls, speciesList):
    #     '''
    #     '''
    #     speciesData = []
    #     for item in speciesList:
    #         species = requests.get(item).json()
    #         if species:
    #             speciesData.append(species)
    #     return speciesData
    
    # @classmethod
    # def getFilms(cls, filmsList):
    #     '''
    #     '''
    #     filmsDataList = []
    #     for item in filmsList:
    #         film = requests.get(item).json()
    #         if film:
    #             filmsDataList.append(film)
    #     return filmsDataList