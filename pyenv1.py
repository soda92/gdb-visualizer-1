import os


a = os.environ.get("PYTHONPATH")
print(a)

# test result: C:\src\gdb-visualizer-1;C:\Users\absdg\scoop\apps\llvm\current\Lib\site-packages
# env was appended even if you write `"PYTHONPATH": "${workspaceFolder}"`!
