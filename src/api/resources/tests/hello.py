from ...rest_core import (
    Resource,
)


class Hello(Resource):

    def get(self):
        print('Hello')
        return 'Hello'
