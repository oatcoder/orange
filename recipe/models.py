import bson


class Recipe:
    def __init__(self, data):
        if data is not None:
            self.id = str(data["_id"])

            if 'name' in data:
                self.name = data["name"]

            if 'description' in data:
                self.description = data['description']

    def set_id(self, val):
        self.id = val

    def set_name(self, val):
        self.name = val

    def set_description(self, val):
        self.description = val
