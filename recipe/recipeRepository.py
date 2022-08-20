import collections
import bson

from database import Database
from .models import Recipe
from bson.codec_options import CodecOptions
from bson.json_util import dumps
from bson.objectid import ObjectId

class RecipeRepository:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def insert(self, recipe):
        result = None

        recipes = self.__recipeCollection__()

        result = recipes.insert_one(recipe).inserted_id
        
        return str(result)
    
    def update(self, recipeId, recipe):
        result = 0

        recipes = self.__recipeCollection__()

        recipeIdObject = ObjectId(recipeId)

        result = recipes.replace_one({'_id': recipeIdObject}, recipe)

        assert(result.modified_count == 1), "Error when updating a Recipe"

        return result

    def delete(self, recipeId):
        result = 0

        recipes = self.__recipeCollection__()

        recipeIdObject = ObjectId(recipeId)

        result = recipes.delete_one({ '_id': recipeIdObject})

        assert(result.deleted_count == 1), "Error when deleting a Recipe"

        return result
 
    def query_recipes(self, id):
        result = []

        recipes = self.__recipeCollection__()

        if id is 0:
            for r in recipes.find():
                recipe = Recipe(r)
                
                result.append(recipe)

            return result

        # todo: verify this
        result = filter(lambda r: r.id == id, recipes)

        return result

    def __recipeCollection__(self):
        db = Database()

        recipes = db.col("recipe")

        return recipes