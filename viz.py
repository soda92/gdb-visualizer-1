if "gdb" not in locals():
    gdb = False


class MyClassPrinter:
    "Print a MyNamespace::MyClass"

    def __init__(self, val):
        self.val = val

    def to_string(self):
        return "MyClass: member1 = {}, member2 = {}".format(
            self.val["member1"], self.val["member2"]
        )


def lookup_function(val):
    if str(val.type) == "MyNamespace::MyClass":
        return MyClassPrinter(val)
    return None


gdb.pretty_printers.append(lookup_function)
