import hashlib
from __future__ import annotations
import zlib
class GitObject:
    def __init__(self, type: str, content: bytes):
        self.type = type
        self.content = content
    
    def hash(self)->str:
        header = f"{self.type} {len(self.content)}\0".encode()
        data = header + self.content
        return hashlib.sha1(data).hexdigest()
    
    def serialize(self)->bytes:
        header = f"{self.type} {len(self.content)}\0".encode()
        data = header + self.content
        return zlib.compress(data)
    @classmethod
    def deserialize(cls, data)->GitObject:
        decompressed = zlib.decompress(data)
        null_idx = decompressed.find(b"\0")
        header = decompressed[:null_idx]
        content = decompressed[null_idx+1:]
        obj_type, size = header.split(" ") 
        return cls(obj_type, content)