from ...rest_core import (
    Resource,
)


class TextText(Resource):

    def post(self):
        data = self.request.json
        if 'text' in data:
            print(f'Hello, {data["text"]}, how are you')
        return f'Hello, {data["text"]}, how are you'
