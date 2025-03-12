path = "LRLRLLRR"

# import lldb  # noqa: E402

try:
    from lldb_typeinfo import SBFrame
except ImportError as _e:
    exec("""
class SBFrame:
    pass
        """)
    pass


def py1(frame: SBFrame, bp_loc, internal_dict):
    global path
    if path[0] == "L":
        path = path[1:]
        thread = frame.GetThread()
        process = thread.GetProcess()
        process.Continue()
    else:
        print("Here is the problem. Going left, should go right!")


def py2(frame: SBFrame, bp_loc, internal_dict):
    global path
    if path[0] == "R":
        path = path[1:]
        thread = frame.GetThread()
        process = thread.GetProcess()
        process.Continue()
    else:
        print("Here is the problem. Going right, should go left!")
