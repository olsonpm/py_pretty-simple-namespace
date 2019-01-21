from textwrap import dedent
from pretty_simple_namespace import wrapWith
from types import SimpleNamespace as o


def runTests(r):
    input = o(tabbed4spaces=True)
    wrapped = wrapWith(indent=4)
    expected = dedent(
        """\
        {
            tabbed4spaces: true
        }
        """
    )
    code = "wrapped.format(input)"
    actual = wrapped.format(input)
    if actual != expected:
        r.addError(code)

    return r
