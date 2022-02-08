from django.core.management.base import BaseCommand
import requests
from tqdm import tqdm

from products.models import Category, Product, Nutrimage


class Command(BaseCommand):
    help = "Populate database from api call to OpenFoodFact"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):

        self._save_nutriscore_images()
        self._fill_categories_in_db()
        self._fill_products_in_db()

    def _get_categories_data(self):
        """
        Get all categories for the Api OpenFoodFact.

        return list of strings containing all categories.
        """
        all_categories = []
        for iter in tqdm(range(1, 4)):
            response = requests.get(
                f"https://fr.openfoodfacts.org/categories.json/{iter}"
            )
            data = response.json()
            for eachcate in data["tags"]:
                category = eachcate["name"]
                all_categories.append(category)

        return all_categories

    def _fill_categories_in_db(self):
        """
        Fill the DB table category with names of all categories.
        """
        categories = self._get_categories_data()
        for eachcategory in tqdm(categories):
            obj, created = Category.objects.get_or_create(
                name=f"{eachcategory}",
            )

    def _get_eight_categories(self):
        """
        Exctract 8 categories with the most products
        from the category datas from getcategory().

        Return a list.
        """
        all_categories = self._get_categories_data()
        eightcategories = all_categories[:8]

        return eightcategories

    def _get_products(self):
        """Makes an Api call to OpenFoodFact to get all products from 8categories.

        Returns:
            list: list of products, products are dict
        """
        categories = self._get_eight_categories()
        list_of_products = []
        for each_category in tqdm(categories):
            for page in tqdm(range(1, 11)):
                response = requests.get(
                    f"""https://fr.openfoodfacts.org/cgi/search.pl?
                    action=process
                    &tagtype_0=categories
                    &tag_contains_0=contains
                    &tag_0={each_category}
                    &fields=
                        product_name_fr,
                        image_nutrition_small_url,
                        image_url,
                        nutrition_grade_fr,
                        categories,categories_old,
                        url
                    &page_size=100
                    &json=true
                    &page={page}"""
                )
                data_products = response.json()
                if data_products["page_count"] is None:
                    continue
                else:
                    for items in data_products["products"]:
                        keys = [
                            "product_name_fr",
                            "nutrition_grade_fr",
                            "image_url",
                            "url",
                            "image_nutrition_small_url",
                            "categories",
                            "categories_old",
                        ]
                        prod_keys = items.keys()
                        if set(keys) == set(prod_keys):
                            list_of_products.append(items)

        return list_of_products

    def _fill_products_in_db(self):
        """With the list of products fill the DB."""
        all_products = self._get_products()
        for each_product in tqdm(all_products):
            obj, created = Product.objects.get_or_create(
                name=f'{each_product["product_name_fr"]}',
                nutriScore=f'{each_product["nutrition_grade_fr"]}',
                linkToIMG=f'{each_product["image_url"]}',
                linkToURLOFF=f'{each_product["url"]}',
                linkToNutriForG=f'{each_product["image_nutrition_small_url"]}',
            )
            category = each_product["categories"].split(", ")
            category_old = each_product["categories_old"].split(", ")
            for items in category_old:
                if items not in category:
                    category.append(items)
            categories = Category.objects.filter(name__in=category)
            if obj:
                obj.category.add(*categories)
            else:
                created.category.add(*categories)

    def _save_nutriscore_images(self):
        nutri_a_url = "/static/images/nutriA.jpg"
        nutri_b_url = "/static/images/nutriB.jpg"
        nutri_c_url = "/static/images/nutriC.jpg"
        nutri_d_url = "/static/images/nutriD.jpg"
        nutri_e_url = "/static/images/nutriE.jpg"

        obj, created = Nutrimage.objects.get_or_create(
            name="a",
            link=nutri_a_url,
        )
        obj, created = Nutrimage.objects.get_or_create(
            name="b",
            link=nutri_b_url,
        )
        obj, created = Nutrimage.objects.get_or_create(
            name="c",
            link=nutri_c_url,
        )
        obj, created = Nutrimage.objects.get_or_create(
            name="d",
            link=nutri_d_url,
        )
        obj, created = Nutrimage.objects.get_or_create(
            name="e",
            link=nutri_e_url,
        )
