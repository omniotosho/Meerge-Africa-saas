from .base import *

# Django Xtensions
INSTALLED_APPS += [
    # extensions
    "django_extensions",
]
GRAPH_MODELS = {
    'app_labels': [
        "core",
        "cities_light",
        "restaurant",
        "geo",
        # "inventory",
        # "orders",
    ],
    'group_models': True,
}
