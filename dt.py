"""
  Timedelta arithmetics
"""

import sys
from datetime import timedelta
import re
import logging
import operator


LOGLEVEL=logging.DEBUG
logging.basicConfig(level=LOGLEVEL)

datestr = re.compile(r'^((?P<days>[+-]?\d+)d)?(?P<hours>\d+):(?P<minutes>\d+)$')


def usage():
  print("""
    Timedelta arithmetics. Only days, hours and minutes are supported. Negative
    values are normalized that time part is always positive.

    Usage:
      $python dt.py <expr>
    <expr>: expression with datetimes.

    Examples:
      1d 23:14 + 2d 12:11 = 4d 11:25
      1d 12:00 - 2d 00:00 = -1d 12:00 (minus 1 day plus 12 hours)
  """)
  sys.exit()


class Timedelta(object):
  """
    Dummy class incapsulate timedelta properties.
  """
  def __init__(self, days=0, hours=0, minutes=0, seconds=0):
    self.t = timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
    self.days = self.t.days
    self.seconds = self.t.seconds

  def __repr__(self):
    return repr(self.t)

  def __str__(self):
    s = self.t.seconds
    return "{}d {:02}:{:02}".format(self.days, s//3600, (s//60)%60)

  def __add__(self, other):
    t = self.t + other.t
    return Timedelta(days=t.days, seconds=t.seconds)


class DT(Timedelta):
  """
    Timedelta class with constructor from string
  """
  def __init__(self, string):
    m = datestr.search(string).groupdict()
    super(DT, self).__init__(**{k:int(v) for k, v in m.items()})


def calc(expr):
  try:
    return str(reduce(operator.add, [DT(x) for x in expr.strip().split(' ')]))
  except:
    logging.error('Failed to process expression "%s"' % expr)
    if LOGLEVEL > logging.DEBUG:
      sys.exit(-1)
    else:
      raise


def main():
  if len(sys.argv) != 2:
    usage()
  expr = sys.argv[1]
  logging.debug('Expression to evaluate: %s' % expr)
  expr = expr.replace(' ','')
  expr = expr.replace('-',' -')
  expr = expr.replace('+',' +')
  logging.debug('Processed expression: %s' % expr)
  print(calc(expr))


if __name__ == "__main__":
  main()
