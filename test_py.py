#!python3.5
import sys
import matlab.engine
def generate_plant_response() :
    eng = matlab.engine.start_matlab()

    y = eng.generate_plant_response();
    eng.quit()
    return y
