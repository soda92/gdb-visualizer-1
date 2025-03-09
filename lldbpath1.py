def remove_quote(x):
    if x[0] == '"' or x[0] == "'":
        return x[1:-1]
    return x


def myfunc(frame, bp_loc, _a, _b):
    val0 = frame.FindVariable("vs").GetChildAtIndex(0).GetSummary()
    val0 = remove_quote(val0)
    if val0 == "hello0":
        thread = frame.GetThread()
        process = thread.GetProcess()
        process.Continue()
    else:
        print("Here is the problem!")
