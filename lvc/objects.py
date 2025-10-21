# class GitObject:
#     def __init__(self, type: str, content: bytes):
#         self.type = type
#         self.content = content
    
#     def hash(self):
#         header = f"{self.type} {len(self.content)}\0".encode()
#         data = header + self.content
#         return hashlib
import hashlib
data = "Hello world".encode()
hashed = hashlib.sha1(data)
print(hashed.hexdigest())