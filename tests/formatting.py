# ------- #
# Imports #
# ------- #

from difflib import Differ
from pretty_simple_namespace import format
from pretty_simple_namespace.fns import forEach, joinWith, map_, passThrough
from simple_chalk import green, red, yellowBright
from .input import input
from .expected import expected as allExpected


# ---- #
# Init #
# ---- #

_d = Differ()
x = red("✘")
o = green("✔")
greenPlus = green("+")
redMinus = red("-")


# ---- #
# Main #
# ---- #


def runTests(r):
    def testCase(formatInput, case):
        actual = format(formatInput)
        expected = getattr(allExpected, case)
        if actual != expected:
            r.addError(case)
            # print()
            # print(f"  {case} {x}")
            # print()
            # # print("actual")
            # # print(actual.replace("\r", "\\r"))
            # # print()
            # # print("expected")
            # # print(expected.replace("\r", "\\r"))
            # print(diff(actual, expected))

    forEach(testCase)(input)
    return r


# ------- #
# Helpers #
# ------- #


def colorize(aLine):
    if aLine.startswith("+"):
        return greenPlus + aLine[1:]
    elif aLine.startswith("-"):
        return redMinus + aLine[1:]
    elif aLine.startswith("?"):
        return yellowBright(aLine)
    else:
        return aLine


def diff(left, right):
    result = _d.compare(
        left.splitlines(keepends=True), right.splitlines(keepends=True)
    )
    return passThrough(result, [list, map_(colorize), joinWith("")])
