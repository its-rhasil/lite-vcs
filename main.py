from lvc.repository import Repository
import argparse
import sys
def main():
    parse = argparse.ArgumentParser(description="LiteVCS: A Lightweight version control system inspired by Git.")
    subparse = parse.add_subparsers(dest="command",help="Available commands")
    #Creating Subparsers
    init_cmd = subparse.add_parser(name="init", help="Initialize a new Repository")
    
    args = parse.parse_args()
    if not args.command:
        parse.print_help()
        return
    try:
        if args.command == "init":
            repo = Repository()
            if repo.init():
               print(f"Initialized Empty Repository in {repo.lvc_dir}")
            else:
                print("Repository already exists!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()