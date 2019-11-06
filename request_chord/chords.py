
class RequestChord:

    def __init__(self, **kwargs):
        self.requests = kwargs.get('requests', [])

    def get_requests(self):
        return self.requests
