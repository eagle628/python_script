#!python3.6
def generate_plant_response(eng) :
    #import matlab.engine
    #eng = matlab.engine.start_matlab()
    y = eng.generate_plant_response()
    eng.quit()
    return y
