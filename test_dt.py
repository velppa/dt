
from dt import *

def test_timedelta_to_str():
  t = lambda d, h, m: timedelta(days=d, hours=h, minutes=m)
  assert timedelta_to_str(t(1, 2, 3)) == "1d 02:03"
  assert timedelta_to_str(t(0, 27, 37)) == "1d 03:37"
  assert timedelta_to_str(t(-1, 12, 30)) == "-1d 12:30"
  assert timedelta_to_str(t(0, -1, 0)) == "-1d 23:00"

def test_str_to_timedelta():
  assert str_to_timedelta("1d12:00") == timedelta(days=1, hours=12)
  assert str_to_timedelta("-11d03:12") == timedelta(days=-11, hours=3, minutes=12)
  assert str_to_timedelta("-2d12:00") == timedelta(days=-2, hours=12, minutes=0)

def test_calc():
  assert calc("3d00:00 -2d00:00") == "1d 00:00"
  assert calc("3d10:00 -2d00:00") == "1d 10:00"
  assert calc("3d12:00 -2d12:00") == "2d 00:00"
  assert calc("1d12:00 -5d00:00") == "-4d 12:00"
  assert calc("-5d12:00 +1d00:00") == "-4d 12:00"



