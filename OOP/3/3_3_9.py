class Recipe:
    def __init__(self, *args):
        self._recipe = list(args)

    def add_ingredient(self, ing):
        self._recipe.append(ing)

    def remove_ingredient(self, ing):
        self._recipe.remove(ing)

    def get_ingredients(self):
        return tuple(self._recipe)


class Ingredient:
    def __init__(self, name, volume, measure):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f"{self.name}: {self.volume}, {self.measure}."
