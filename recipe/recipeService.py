import logging

from .models import Recipe
from .recipeRepository import RecipeRepository


class RecipeService:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def save_recipe(self, recipe):
        try:
            repo = RecipeRepository()

            result = repo.insert(recipe)

            saved = Recipe(recipe)

            saved.id = result

            return saved
        except Exception as e:
            raise e

    def update_recipe(self, recipeId, recipe):
        try:
            repo = RecipeRepository()

            result = repo.update(recipeId, recipe)

            return recipe
        except Exception as e:
            raise e

    def delete_recipe(self, recipeId):
        try:
            repo = RecipeRepository()

            result = repo.delete(recipeId)

            return recipeId
        except Exception as e:
            raise e

    def all_recipes(self):
        try:
            repo = RecipeRepository()

            result = repo.query_recipes(0)

            return result
        except Exception as e:
            raise e