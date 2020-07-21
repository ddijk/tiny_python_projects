#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './ask_for_int.py'



# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_Negative():
    """-1 -> Negative changed to zero"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


