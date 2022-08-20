from .recipeControllerBase import RecipeControllerBase


class RecipeController(RecipeControllerBase):
    def get_recipes(self):
        return self.recipeService.all_recipes()

    def post_recipe(self, recipe):
        return self.recipeService.save_recipe(recipe)

    def put_recipe(self, recipeId, recipe):
        return self.recipeService.update_recipe(recipeId, recipe)

    def delete_recipe(self, recipeId):
        return self.recipeService.delete_recipe(recipeId)

    def fetch_recipes(self):
        return self.recipeProvider.recipes()