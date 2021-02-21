from marshmallow import Schema, fields

class CreateEvaluationSchema(Schema):
    comment = fields.Str(required=True)
    rating = fields.Int(required=True)


class EvaluationSchema(Schema):
    comment = fields.Str(required=True)
    rating = fields.Int(required=True)