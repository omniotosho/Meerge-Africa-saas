from .base import *

# Django Xtensions
INSTALLED_APPS += [
    # extensions
    "django_extensions",
]
GRAPH_MODELS = {
    'app_labels': [
        "core",
        # "restaurant",
        # "world",
        # "customers",
        # "inventory",
        # "orders",
    ],
    'group_models': True,
}
