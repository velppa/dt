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
    Timedelta arithmetics.
    Usage:
      $python dt.py <expr>

    <expr>: expression with datetimes.
    Examples:
      1d 23:14 + 2d 12:11
      -1d 23:14 - 2d 00:11
  """)
  sys.exit()


def str_to_timedelta(s):
  logging.debug("Converting %s to timedelta" % s)
  m = datestr.search(s).groupdict()
  td = timedelta(**{k:int(v) for k, v in m.items()})
  return td


def timedelta_to_str(td):
  s = td.seconds
  return "{}d {:02}:{:02}".format(td.days, s//3600, (s//60)%60)


def calc(expr):
  try:
    datetimes = [str_to_timedelta(x) for x in expr.strip().split(' ')]
    logging.debug(map(str, datetimes))
    result = sum(datetimes, timedelta())
    logging.debug("Result = %s" % str(result))
    return timedelta_to_str(result)
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
