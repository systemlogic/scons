#!/usr/bin/env python
# 
# __COPYRIGHT__
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__revision__ = "__FILE__ __REVISION__ __DATE__ __DEVELOPER__"

"""
Test that TargetSignatures and its associated warning flag
are definitely gone.
"""

import TestSCons

test = TestSCons.TestSCons()

test.file_fixture('SConstruct.method', 'SConstruct')
expect = """\
NameError: name 'TargetSignatures' is not defined:
  File "{}", line 2:
    TargetSignatures('MD5')
""".format(test.workpath('SConstruct'))
test.run(arguments='-Q -s', status=2, stdout=None, stderr=expect)

test.file_fixture('SConstruct.setopt', 'SConstruct')
test.run(arguments="-Q -s", status=0, stdout=None,
         stderr="""\
No warning type: 'deprecated-target-signatures'
No warning type: 'deprecated-target-signatures'
""")

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
