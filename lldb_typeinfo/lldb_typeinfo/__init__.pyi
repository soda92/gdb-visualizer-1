from lldb_typeinfo.lldb_typeinfo.process import SBProcess

class SBThread(object):
    def GetProcess(self) -> SBProcess:
        r"""GetProcess(SBThread self) -> SBProcess"""

class SBFrame(object):
    def GetThread(self) -> SBThread:
        r"""GetThread(SBFrame self) -> SBThread"""
