### this is the protoype
import sys, os, pathlib
from collections import defaultdict
from pathlib import Path

CLI_PATHS = [
    "./example.root"
]


def is_split(p:pathlib.Path)->bool:
    return str(p).endswith(".route")

def is_command(p:str)->bool:
    if str(p).endswith('.command'):
        return True
    return False


def get_all_commands(directory:pathlib.Path):
    dct = {}
    for d in os.listdir(directory):
        p = pathlib.Path(os.path.join(directory, d))
        if os.path.isdir(p):
            if is_split(p):
                sub_commands = get_all_commands(p)
                name = p.parts[-1].replace('.route', '')
                dct[name] = sub_commands
        if is_command(p):
            name = p.parts[-1].replace('.command', '')
            dct[name] = p
    return dct

def get_command_tree():
    tree = {}
    command_trees = []
    for cli_path in CLI_PATHS:
        cli_path = pathlib.Path(cli_path)
        cmds = get_all_commands(cli_path)
        command_trees.append(cmds)
        tree = {**tree, **cmds}
    return tree
    

def get_command(args: list[str]):
    command_tree = get_command_tree()
    
    for i, arg in enumerate(args):
        command_tree = command_tree.get(arg, None)
        if not command_tree:
            print("No subcommand found %s in %s" % (arg, args))
            return None, None

        if isinstance(command_tree, pathlib.Path):
            overflow = args[i+1:]
            return command_tree, overflow
            
    else:
        print("No such commmand in %s" % args)
        return None, None

def exec_command(folder: Path, args):
    assert isinstance(folder, Path)
    # print("Executing: %s" % folder)
    contents = os.listdir(folder)
    cmd = [c for c in contents if c.split('.')[0] == 'command']
    if not cmd:
        raise Exception("No command found in %s" % folder)
    cmd = cmd[0]
    cmd_path = Path(os.path.join(folder, cmd))
    cmd_type = cmd_path.suffix.lower()
    import subprocess
    if cmd_type == ".sh":
        subprocess.call(['sh', cmd_path])
    if cmd_type == '.py':
        subprocess.call(['python', cmd_path, *args])


    # print(cmd_path)
    
def main():
    args = list(sys.argv)
    arg_paths = args[1:]
    cmd, overflow_args = get_command(arg_paths)
    if not cmd:
        return
    exec_command(cmd, overflow_args)
    


if __name__ == '__main__':
    main()