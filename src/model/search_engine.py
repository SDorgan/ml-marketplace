from model.product import Product
from mongoengine import Q


class SearchEngine:

    def search(self, query):
        filter = Q()

        if query is not None:
            filter = filter & (Q(name__icontains=query) | Q(short_description__icontains=query) | Q(long_description__icontains=query))

        return Product.objects(filter)
