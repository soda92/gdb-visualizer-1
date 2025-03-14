from lldb_typeinfo import lldb

def function2(valobj: lldb.SBValue, internal_dict):
    height_val = valobj.GetChildMemberWithName("height")
    width_val = valobj.GetChildMemberWithName("width")
    height = height_val.GetValueAsUnsigned(0)
    width = width_val.GetValueAsUnsigned(0)
    area = height * width
    perimeter = 2 * (height + width)
    return "Area: " + str(area) + ", Perimeter: " + str(perimeter)


def s1():
    from pathlib import Path

    Path("build/t1.txt").write_text("aaa", encoding="utf8")
