from marshmallow import Schema, fields


class CreateProductSchema(Schema):
    name = fields.Str(required=True)
    short_description = fields.Str(default='Short Description', required=True)
    long_description = fields.Str(default='Long Description', required=True)
    seller = fields.Str(default='-')
    image = fields.Str(default='image.jpg')
    price = fields.Float(default=100.0)
    avg_rating = fields.Float(default=0.0)
    amount_rating = fields.Int(default=0)

    class Meta:
        fields = ('name', 'short_description', 'long_description','seller', 'image', 'price', 'avg_rating', 'amount_rating')


class ProductDetailSchema(Schema):
    name = fields.Str(required=True)
    short_description = fields.Str(default='Short Description', required=True)
    long_description = fields.Str(default='Long Description', required=True)
    seller = fields.Str(default='-', required=True)
    image = fields.Str(default='image.jpg', required=True)
    price = fields.Float(required=True)
    avg_rating = fields.Float(required=False)
    amount_rating = fields.Int(required=False)

    class Meta:
        fields = ('id', 'name', 'short_description', 'long_description','seller', 'image', 'price', 'avg_rating', 'amount_rating')