from types import SimpleNamespace as o

expected = o()

expected.case1 = """\
{
  aKey: 'a val'
}
"""

expected.case2 = """\
[
  {
    aKey: 'a val'
  }
  {
    bKey: 'b val'
  }
]
"""

expected.case3 = """\
{
  anArray: [
    {
      aKey: 'a val'
    }
    {
      bKey: 'b val'
    }
  ]
  aDict: {
    cKey: c()
    dKey: 1
  }
}
"""

expected.case4 = """\
{
  name: 'bob'
  child: {
    name: 'billy'
    parent: <ref root>
  }
}
"""

expected.case5 = """\
{
  name: 'adam'
  child: {
    name: 'holdor'
    children: [
      {
        bob: {
          name: 'bob'
          child: {
            name: 'billy'
            parent: <ref root.child.children[0].bob>
          }
        }
      }
    ]
  }
}
"""

expected.case6 = """\
{
  someArray: []
  someDict: {}
}
"""

expected.case7 = """\
{
  child: {
    name: 'holdor'
    child: {
      name: 'bob'
      child: <ref root.superGrandChild>
    }
  }
  superGrandChild: {
    name: 'billy'
  }
  name: 'adam'
}
"""

expected.case8 = """\
[
  {
    complex: true
  }
  'simple'
]
"""
