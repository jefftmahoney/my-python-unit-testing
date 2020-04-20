def my_assert(a, e, fp, ff, l):
    return fp(l) if a == e else ff(a, e, l)


def format_pass(l):
    return f"""
____________________
PASS:
{l}
____________________
    """

def format_fail(a, e, l):
    return f"""
####################
FAIL:
{l}
    expected => ({e})
    actual   => ({a})
####################
    """

def format_fail2(a, e, l):
    return f"""
!!!!!!!!!!!!!!!!!!!!
FAIL:
{l}
    expected => ({e})
    actual   => ({a})
!!!!!!!!!!!!!!!!!!!!
"""

def get_caller(s):
  if (s == 'double'):
    return lambda x : x*2
  elif (s == 'triple'):
    return lambda x : x*3
  elif (s == 'square'):
    return lambda x: x*x
  else:
    return lambda x: 'I do not know what you mean by "' + s + '"'

print(
    my_assert(
        get_caller('double')(4),
        123,
        format_pass,
        format_fail,
        'Factory Test #1a'
    )
