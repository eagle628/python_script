#!python3.5
import sys
import matlab.engine
eng = matlab.engine.start_matlab()

print('hello')
print(sys.version)

tf = eng.isprime(37)
print(tf)

y = eng.generate_plant_response();
print(len(y))
eng.quit()
