import hashlib
import zlib
class GitObject:
    def __init__(self, type: str, content: bytes):
        self.type = type
        self.content = content
    
    def hash(self):
        header = f"{self.type} {len(self.content)}\0".encode()
        data = header + self.content
        return hashlib.sha1(data).hexdigest()
    
    def serialize(self):
        header = f"{self.type} {len(self.content)}\0".encode()
        data = header + self.content
        return zlib.compress(data)


