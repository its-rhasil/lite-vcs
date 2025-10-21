from lvc.repository import Repository
import argparse
import sys
def main():
    parse = argparse.ArgumentParser(description="LiteVCS: A Lightweight version control system inspired by Git.")
    subparse = parse.add_subparsers(dest="command",help="Available commands")
    #Creating Subparsers 
    #lvc init
    init_cmd = subparse.add_parser(name="init", help="Initialize a new Repository")
    #lvc add _path
    add_cmd = subparse.add_parser(name="add",help="Adds files or directories to staging area")
    add_cmd.add_argument("path",nargs='+',help="Files and directories to add")


    args = parse.parse_args()
    if not args.command:
        parse.print_help()
        return
    repo = Repository()
    try:
        if args.command == "init":
            if repo.init():
               print(f"Initialized Empty Repository in {repo.lvc_dir}")
            else:
                print("Repository already exists!")
        elif args.command == "add":
            if not repo.lvc_dir.exists():
                print("Repository is not initialized!")
                return
            for path in args.path:
                print(path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()