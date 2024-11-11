# Context Processors
"""
It is in charge of changing context of navigation bar for all pages
so that it could prevent DRY (Don't Repeat Yourself) for every page

Just modified once when we need to change context for every page in same template


Args: request

Returns: dict

"""


def categories(request):
    categories = [
    "Programming",
    "Food",
    "Travel"
]   
    return {"categories": categories}



