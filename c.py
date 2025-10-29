from pathlib import Path
path = Path(".").resolve()
print(path)
obj_path = path / "obj"
obj_path.mkdir(exist_ok=True)
obj_file = obj_path / "rhasil.py"
if obj_file.exists(): 
    print("Hello World")
else:
    obj_file.write_text('print("Hello World")')