# Only need to run if run lldb in command line
# and this is not run before
# See [./DOC.md]

from pathlib import Path

file = Path.home().joinpath(".lldbinit")

content = file.read_text(encoding="utf8")
s = "settings set target.load-cwd-lldbinit true"
if s not in content:
    content += "\n" + s
    file.write_text(content, encoding="utf8")
