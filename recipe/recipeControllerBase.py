from .recipeService import RecipeService
from .recipeProvider import RecipeProvider

class RecipeControllerBase:
    def __init__(self):
        self.recipeService = RecipeService()
        self.recipeProvider = RecipeProvider()