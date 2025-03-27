import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_data
def load_survey():
    df = pd.read_csv("outputs/datasets/collection/BreakfastSurvey.csv")
    return df



def encode_breakfast(df):
    df["breakfast_encoded"] = df["breakfast"].replace({"Yes, again":2,
                                           "Yes, next time not":1,
                                           "No":0
                                           })

    return df


def load_pkl_file(file_path):
    return joblib.load(filename=file_path)