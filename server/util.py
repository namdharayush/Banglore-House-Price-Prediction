import json
import pickle
import numpy as np
__locations = []
__data_columns = []
__model = None



def get_estimated_price(location,sqft,bath,bhk):
    global __data_columns
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if location.lower() in __data_columns:
        try:
            loc_index = __data_columns.index(location.lower())
            x[loc_index] = 1
        except:
            loc_index = -1

    return round(__model.predict([x])[0],2)
def get_location_name():
    return __locations

def load_saved_artifacts():
    global __locations
    global __data_columns
    global  __model

    print("Started....")
    with open('./artifacts/columns.json','r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    print("Locations Extracted ....")
    with open('./artifacts/banglore_home_prices_model.pickle','rb') as f:
        __model = pickle.load(f)

    print("Model Fetched ...")
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_name())