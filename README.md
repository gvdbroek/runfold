# runfold
Runfold – A structure-driven CLI runtime. Build command-line tools using folders and files, not frameworks. Drop in scripts, organize with directories, and run them instantly.


## PoC
This is currently just a PoC.
Currently supports very singular/simple structures, nothing too fancy.

### So what is it?
Inspired by Svelte & Pyrevit, this thing here allows you to build a routed CLI by just putting commands in folders.
The folder structure IS your CLI structure. So if you have any scripts you often have to run, but you don't want to create an alias for everything. This allows you to build some cli routing.

### Features
#### Passing overflow arguments as args to .command bundles
Say you have a command you want to execute `runfold cow moo --loud` , and your folder structure looks like `root/farm.route/cow.route/moo.command/command.py` we have an overflow of `--loud` , this will become an arg in the `command.sh` script

### Features I want to add
#### Allow for installation as a CLI tool
the main.py is just a PoC, the actual intent is to make this a CLI tool that can be added to `$path`

#### Support for Python Environments
Though technically you could just run your python tool through command.sh with any venv you want, I think a venv folder detection would be neat

## Usage (for now)
1. Clone
2. Put any path in replace (or add) any CLI root path to the CLI_PATHS variable.
3. Build out a cli structure using the Folder structure
4. run using `python main.py your argument list` (arguments are parsed using argv, so if you have spaces, add "")


### Folder structure
The folder structure is kept simple and clean
#### Command Bundle
A command bundle is a folder that is created that ends with .command
there's no concept of subcommands, subcommands etc should be handled by your own script
A .command folder MUST have a file that ends with command.sh or command.py.

#### Routes
Create folders with a .route extension and put .commands in them. This allows you to nest commands.


### Which Python Runtime is used?
Currently, for running python files, your global python runtime is used.
### Which Shell is used?
This PoC assumes you have `sh` installed. But will probably change to use your current shell.
