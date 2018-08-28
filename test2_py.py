#!python3.6
import test_py
import sys
import matplotlib.pyplot as plt
print(sys.version)

import matlab.engine
eng = matlab.engine.start_matlab()

print(sys.version)

y = test_py.generate_plant_response(eng)

t = range(len(y))

fig = plt.figure(figsize=(12,8))

ax = fig.add_axes([0,0,1,1])
ax.plot(t,y,label="test")

plt.legend()

plt.show()
