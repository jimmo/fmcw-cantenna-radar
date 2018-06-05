import pyb
from array import array
dac = pyb.DAC(1, bits=12)
ramp = array('H', range(0, 2047, 5)) + array('H', range(2047, 0, -5))
dac.write(700)

from dftclass import DFTADC, FORWARD, POLAR, DB
mydft = DFTADC(4096, "X7")

#dac.write_timed(ramp, pyb.Timer(6, freq=len(ramp)*123), mode=pyb.DAC.CIRCULAR)

while True:
  mydft.run(FORWARD | POLAR | DB, 0.5)
  f = mydft.re[1:100]
  fmin = min(f)
  fmax = max(f)
  for i in range(0, len(f), 1):
    p = f[i]
    x = int(9*(p - fmin) / (fmax-fmin))
    if p == fmax and i not in (24, 49, 74):
      print('^', end='')
    elif x > 5 and i not in (24, 49, 74):
      print(x, end='')
    else:
      print(' ', end='')
  print()
