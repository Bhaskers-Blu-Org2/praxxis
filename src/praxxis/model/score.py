import os 
import warnings
import pandas as pd
import joblib
from keras.models import load_model
from tensorflow.compat.v1 import logging 

from numpy import array
from keras.preprocessing.sequence import pad_sequences


def encode(sequence, converter):
    newSeq = []
    for filename in sequence:
        if filename not in converter:
           newSeq.append(1) #<Unknown>
        else:
            newSeq.append(converter.index(filename))
    return newSeq

def pad_sequence(sequence, length, value=0):
    if len(sequence) <= length:
        padded = pad_sequences([sequence], maxlen=length, dtype=object, value=value)
        return padded[0].tolist()
    else:
        return sequence[(len(sequence) - length):]

def prep_input(sequence, converter, length):
    encoded = encode(sequence, converter)
    padded = pad_sequence(encoded, length)
    shaped = array(padded).reshape(1, length, 1)
    return shaped

def predict(sequence, model_path, converter_path):
    logging.set_verbosity(logging.ERROR)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 

    # load in model and converter
    converter = joblib.load(converter_path)
    model = load_model(model_path)

    # encode sequence, pad, reshape
    # TODO: get length from model shape
    prepped_in = prep_input(sequence, converter, length=5)
    
    # predict
    data = model.predict(prepped_in)
   
    # convert results into meaningful thing
    print(pd.Series(data[0], converter).sort_values(ascending=False))

def get_files(model_db):
    from src.praxxis.sqlite import sqlite_model

    paths = sqlite_model.get_current_model_paths(model_db)
    
    return paths
    
def get_predictions(sequence, model_db):
    model_path, converter_path = get_files(model_db)

    predict(sequence, model_path, converter_path)