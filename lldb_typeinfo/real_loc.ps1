$a = $Env:USERPROFILE

$p = Join-Path -Path $a -ChildPath "scoop/apps/llvm/current/Lib/site-packages/lldb/__init__.py"

code $p