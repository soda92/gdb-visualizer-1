## On building

need cmake, make, and TDM-GCC

## on Debugging

on command line, need to install llvm from scoop

also, need to install Python 3.10 (hard requirement), it's not included in LLVM, and is a lldb dependency

On VSCode, need not do that, and lldb is also not needed because the extension shipped with its own executable

## On Visiualizer

On VSCode

```json
"initCommands": ["command source ${workspaceFolder}/.lldbinit"]
```

If done in command line, need to ensure $Env:UserProfile/.lldbinit contains:
```
settings set target.load-cwd-lldbinit true
```

for `.lldbinit` in the source dir to load. See `init_home_lldbinit.py`.