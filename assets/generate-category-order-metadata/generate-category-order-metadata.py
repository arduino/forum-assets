import os
import requests
import json
import pathlib


def get_category_list(categories_data, level):
    category_list = ""
    for category_data in categories_data:
        if category_data["id"] in skip_list:
            continue

        category_list += "{indent}- {name}\n".format(indent="  " * level, name=category_data["name"])

        if "subcategory_list" in category_data:
            category_list += get_category_list(categories_data=category_data["subcategory_list"], level=level + 1)

    return category_list


response = requests.get(
    url="https://forum.arduino.cc/categories.json",
    params={"include_subcategories": "true"},
    headers={"Api-Key": os.environ["ARDUINO_FORUM_API_KEY"], "Api-Username": "system"},
)

script_location = pathlib.PurePath(os.path.dirname(os.path.realpath(__file__)))
with open(file=script_location.joinpath("category-skip-list.json"), encoding="utf-8") as skip_list_file:
    skip_list = json.load(fp=skip_list_file)

category_list = get_category_list(categories_data=response.json()["category_list"]["categories"], level=0)

with open(file="content/categories/order.md", mode="w", encoding="utf-8") as order_file:
    order_file.write(category_list)
