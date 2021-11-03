from django.core.management.base import BaseCommand
import requests
from tqdm import tqdm

from products.models import  Category,Product


class Command(BaseCommand):
    help = 'Populate database from api call to OpenFoodFact'
    
    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **kwargs):
        
        self._fill_categories_in_db()
        self._fill_products_in_db()


    def _get_categories_data(self):
        """
        Get all categories for the Api OpenFoodFact.
        
        return list of dictionnaries containing all datas of each category.
        """
        
        response = requests.get("https://fr.openfoodfacts.org/categories.json")
        data = response.json()
        return data
    
    def _clean_category_data(self):
        """Takes categories datas and extract only the name of each category

        Returns:
            list : a list containing all names of categories
        """
        
        datas = self._get_categories_data()
        list_of_categories = []
        for allcategories in tqdm(datas["tags"]):
            category = allcategories["name"]
            list_of_categories.append(category)
        return list_of_categories
       
    def _fill_categories_in_db(self):
        """
        Fill the DB table category with names of all categories.
        """
        categories = self._clean_category_data()
        for eachcategory in tqdm(categories):
            obj, created = Category.objects.get_or_create(
                name = f'{eachcategory}',
            )

    def _get_eight_categories(self):
        """
        Exctract 8 categories with the most products
        from the category datas from getcategory().

        Return a list.
        """
        all_categories = self._get_categories_data()
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

    def _get_products(self):
        """Makes an Api call to OpenFoodFact to get all products from 8categories.

        Returns:
            list: list of products, products are dict
        """
        categories = self._get_eight_categories()
        list_of_products = []
        for each_category in tqdm(categories):
            for page in tqdm(range(1,11)):
                response = requests.get(
                    f"https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={each_category}&fields=product_name_fr,image_nutrition_small_url,image_url,nutrition_grade_fr,categories,categories_old,url&page_size=100&json=true&page={page}"
                )
                data_products = response.json()
                if data_products["page_count"] is None:
                    continue
                else:
                    for items in data_products["products"]:
                        keys = ["product_name_fr","nutrition_grade_fr","image_url","url","image_nutrition_small_url","categories","categories_old"]
                        prod_keys = items.keys()
                        if set(keys) == set(prod_keys):
                            list_of_products.append(items)
                            
        return list_of_products
    
    
    def _fill_products_in_db(self):
        """With the list of products fill the DB.
        """
        all_products = self._get_products()
        for each_product in tqdm(all_products):
            print(each_product)           
            obj, created = Product.objects.get_or_create(
                name = f'{each_product["product_name_fr"]}',
                nutriScore = f'{each_product["nutrition_grade_fr"]}',
                linkToIMG = f'{each_product["image_url"]}',
                linkToURLOFF = f'{each_product["url"]}',
                linkToNutriForG = f'{each_product["image_nutrition_small_url"]}',
            )
            category = each_product["categories"].split(",")
            category_old = each_product["categories_old"].split(",")
            for items in category_old:
                if items not in category:
                    category.append(items)
            categories = Category.objects.filter(name__in=category)
            if obj:
                obj.category.add(*categories)
            else:
                created.category.add(*categories)