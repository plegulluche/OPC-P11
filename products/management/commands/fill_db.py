from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Populate database from api call to OpenFoodFact'
    
    def add_arguments(self, parser):
        parser.add_argument('total_categories', type=int, help='Indicate the number of categories we wanna fetch from the api call')
        parser.add_argument('total_products', type=int, help='Indicate the number of product per page')
        
        
    def handle(self, *args, **kwargs):
        total_categories = kwargs["total_categories"]
        total_products = kwargs["total_products"]
        self.stdout.write(f"test successful with {total_categories} and {total_products}")

class CustomAPIManager:
    
    def __init__(self):
        pass

    def __get_categories():
        
        response = requests.get("https://fr.openfoodfacts.org/categories.json")
        data = response.json()
        return data
        ["Aliments et boissons à base de végétaux","Aliments d'origine végétale","Snacks","Viandes","Snacks sucrés","Boissons"]
        
    def __geteightcategories(self):
        """
        Exctract 8 categories with the most products
        from the category datas from getcategory().

        Return a list.
        """
        all_categories = self.__get_categories()
        eightcategories = []

        sortedkeys = sorted(
            all_categories["tags"], key=lambda x: x["products"], reverse=True
        )
        for elems in sortedkeys[:8]:
            keys = ["name"]
            values = list(map(elems.get, keys))
            for items in values:
                eightcategories.append(items)

        return eightcategories


# url for products = "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=Aliments et boissons à base de végétaux&fields=product_name_fr,image_nutrition_small_url,image_url,nutrition_grade_fr,categories,categories_old&page_size=50&json=true&page=1"
# faire le tri des doublons dans les categories de chaque produit et regler le nombre de produits par pages.
#10k produits en tout suffisant. ( 8 cates 1000p/cate)