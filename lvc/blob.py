from objects import GitObject
class Blob(GitObject):
    def __init__(self, type, content):
        super().__init__(type, content)