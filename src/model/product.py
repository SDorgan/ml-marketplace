from mongoengine import Document, StringField, BooleanField, IntField, ReferenceField, FloatField


class Product(Document):
    name = StringField()
    short_description = StringField()
    long_description = StringField()
    seller = StringField(default='-')
    image = StringField(default='image.jpg')
    price = FloatField(default=100.0)
    avg_rating = FloatField(default=0.0)
    amount_rating = IntField(default=0)

