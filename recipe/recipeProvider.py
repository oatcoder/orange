import http.client
import ssl
import json

from config import Configuration

class RecipeProvider:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def recipes(self):
        config = Configuration()
        
        connection = http.client.HTTPSConnection(config.food_api(), context=ssl._create_unverified_context(), check_hostname=False)

        headers = {"Accept": "application/json", "Content-Type": "application/json"}

        connection.request("GET", "/food/recipes", headers=headers)
        
        response = connection.getresponse()

        assert(response.status == 200), "Error fetching Recipes"
        
        resp = json.loads(response.read())

        return resp