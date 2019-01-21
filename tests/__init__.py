from pretty_simple_namespace.fns import forEach, invokeAttr, map_, passThrough
from . import formatting, misc
from .utils import runModuleTests

modules = [formatting, misc]


def runTests():
    passThrough(
        modules, [map_(runModuleTests), forEach(invokeAttr("printResults"))]
    )
