from marshmallow import Schema, fields as f

class BaseSchema(Schema):
    id = f.Integer()


class AuthorSchema(BaseSchema):
    name = f.Str()
    bio = f.Str()


class ReaderSchema(BaseSchema):
    username = f.Str()
    password = f.Str()
    role = f.Str()


class BookSchema(BaseSchema):
    name = f.Str()
    description = f.Str()
    content = f.Str()
    authors = f.Nested(AuthorSchema(many=True))
    readers = f.Nested(ReaderSchema(many=True))
