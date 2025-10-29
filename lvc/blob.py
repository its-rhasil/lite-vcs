from objects import GitObject
class Blob(GitObject):
    def __init__(self, content:bytes):
        super().__init__("blob", content)