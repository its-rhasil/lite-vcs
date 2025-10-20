from pathlib import Path
import json

class Repository: 
    def __init__(self, path="."):
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
    
