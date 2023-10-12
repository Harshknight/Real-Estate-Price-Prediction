import json
import pickle

import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(locations,sqft,bhk,bath):
    try:
        loc_index =__data_columns.index(locations.lower())
    except:
        loc_index =-1

    x= np.zeros(len(__data_columns))
    x[0] =sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >=0:
        x[loc_index] =1

    return round(__model.predict([x])[0],2)


def get_location_names():
    return __locations
def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    try:
        with open("./artifacts/columns.json", 'r') as f:
            data = json.load(f)
            __data_columns = data.get('data_columns', [])
            __locations = __data_columns[3:]  # Extract location names
    except Exception as e:
        print("Error loading columns.json:", str(e))

    global __model
    try:
        with open("./artifacts/bangalore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    except Exception as e:
        print("Error loading the model:", str(e))

    print("Loading saved artifacts...done")

load_saved_artifacts()  # Add this line to load the artifacts and print location names
print("Location Names:", __locations)



