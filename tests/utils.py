from case_conversion import separate_words
from difflib import Differ
from pretty_simple_namespace.fns import joinWith, passThrough
from .Results import Results

_d = Differ()


def runModuleTests(aModule):
    moduleName = separate_words(getModuleBasename(aModule))
    return aModule.runTests(Results(moduleName))


def getModuleBasename(m):
    return m.__name__.split(".")[-1]


def diff(left, right):
    result = _d.compare(
        left.splitlines(keepends=True), right.splitlines(keepends=True)
    )
    return passThrough(result, [list, joinWith("")])
