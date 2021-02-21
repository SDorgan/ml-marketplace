from mongoengine import Document, StringField, IntField, ReferenceField
from model.product import Product

class Evaluation(Document):
    product = ReferenceField(Product)
    comment = StringField()
    rating = IntField()