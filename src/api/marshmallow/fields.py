from datetime import datetime
from marshmallow import (
    fields,
    ValidationError
)


class ErrorMessages(dict):

    def __getitem__(self, *args, **kwargs):
        value = super().__getitem__(*args, **kwargs)
        if callable(value):
            return value()
        return value


class BaseField:

    default_error_messages = {
        'required': 'Missing required field'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.error_messages = ErrorMessages(self.error_messages)


class Dict(BaseField, fields.Dict):
    pass


class Nested(BaseField, fields.Nested):
    pass


class Function(BaseField, fields.Function):
    pass


class List(BaseField, fields.List):
    pass


class Int(BaseField, fields.Int):
    pass


class Bool(BaseField, fields.Bool):
    pass


class Str(BaseField, fields.Str):
    pass


class Timestamp(BaseField, fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return value
        return value.timestamp()

    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return value
        return datetime.utcfromtimestamp(value)
