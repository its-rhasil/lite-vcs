from pathlib import Path
import json
from typing import Dict 
from .objects import GitObject
from .blob import Blob


class Repository: 
    def __init__(self, path : Path ="."):
        self.path = Path(path).resolve()
        #path for creating directories

        self.lvc_dir = self.path / ".lvc"
        self.objects_dir = self.lvc_dir / "objects"
        self.ref_dir = self.lvc_dir / "refs"
        self.heads_dir = self.ref_dir / "heads" 
        #Path for creating files

        self.head_file = self.lvc_dir / "head"
        self.index_file = self.lvc_dir / "index"
    def init(self):
        if self.lvc_dir.exists():
            return False            
        #Creating directories
        self.lvc_dir.mkdir()
        self.objects_dir.mkdir()
        self.ref_dir.mkdir()
        self.heads_dir.mkdir()
        #Head -> main branch
        self.head_file.write_text("ref: refs/heads/main\n")
        self.index_file.write_text(json.dumps({},indent=2))

        return True
    def load_index(self)->Dict[str, str]:
        if not self.index_file.exists():
            self.index_file.write_text(json.dumps({},indent=2))
            return {}
        try:
            return json.loads(self.index_file.read_text())
        except:
            return {}
        
    def store_object(self, obj:GitObject)-> str:
        obj_hash = obj.hash()
        obj_dir = self.objects_dir / obj_hash[:2]
        obj_file = obj_dir / obj_hash[2:]

        if not obj_file.exists():
            obj_dir.mkdir(exist_ok=True)
            obj_file.write_bytes(obj.serialize())

        return obj_hash
    def save_index(self,index: Dict[str,str]):
        self.index_file.write_text(json.dumps(index,indent=2))
    def add_file(self,file_path:Path):
        content = file_path.read_bytes()
        blob = Blob(content)
        hashed = self.store_object(blob)
        index = self.load_index()
        index[file_path.name] = hashed
        self.save_index(index)
        print(f"Added {file_path.name} to the staging area")

    def add_path(self, path: str)->None:
        absolute_path = self.path / path
        if not absolute_path.exists():
            raise FileNotFoundError(f"Path {absolute_path} not found!")
        if absolute_path.is_file():
            self.add_file(absolute_path)
        # elif absolute_path.is_dir():
        #     self.add_dir(absolute_path)
        else:
            raise ValueError("Neither a File nor a directory")