class Book:
    def __init__(self):
        self.recipes = {}

    def write_recipe(self, path_file):
        if isinstance(path_file, list):
            path_file = path_file[0]

        with open(path_file, 'r', encoding='UTF-8') as datafile:
            lines = datafile.readlines()

        processing_list = []

        for line in lines:
            line = line.strip()

            if line == '':
                if processing_list:
                    recipe_name = processing_list[0]
                    ingredient_count = int(processing_list[1])
                    ingredients = []

                    for i in range(2, 2 + ingredient_count):
                        ingredient_split = processing_list[i].split('|')
                        ingredient = {
                            'ingredient_name': ingredient_split[0].strip(),
                            'quantity': ingredient_split[1].strip(),
                            'measure': ingredient_split[2].strip()
                        }
                        ingredients.append(ingredient)

                    if recipe_name in self.recipes:
                        self.recipes[recipe_name].extend(ingredients)
                    else:
                        self.recipes[recipe_name] = ingredients

                    processing_list = []
            else:
                processing_list.append(line)

        if processing_list:
            recipe_name = processing_list[0]
            ingredient_count = int(processing_list[1])
            ingredients = []

            for i in range(2, 2 + ingredient_count):
                ingredient_split = processing_list[i].split('|')
                ingredient = {
                    'ingredient_name': ingredient_split[0].strip(),
                    'quantity': ingredient_split[1].strip(),
                    'measure': ingredient_split[2].strip()
                }
                ingredients.append(ingredient)

            if recipe_name in self.recipes:
                self.recipes[recipe_name].extend(ingredients)
            else:
                self.recipes[recipe_name] = ingredients

        return self.recipes

    def get_shop_list_by_dishes(self, dishes, person_count):
        shop_list = {}
        for dish in dishes:
            for ingredient in self.recipes[dish]:
                if ingredient['ingredient_name'] in shop_list:
                    shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
                else:
                    shop_list[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'],
                        'quantity': int(ingredient['quantity']) * person_count
                    }
        return shop_list

book = Book()
book.write_recipe('recipes.txt')
book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Омлет'], 4)

