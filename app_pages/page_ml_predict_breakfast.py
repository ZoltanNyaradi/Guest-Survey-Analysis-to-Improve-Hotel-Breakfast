import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from src.data_management import load_survey, load_pkl_file
from src.machine_learning.evaluate_clf import clf_performance


def page_ml_predict_breakfast_body():

    version = 'v1'
    # load needed files
    breakfast_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_breakfast/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    breakfast_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_breakfast/{version}/clf_pipeline_model.pkl")
    breakfast_feat_importance = plt.imread(
        f"outputs/ml_pipeline/predict_breakfast/{version}/features_importance.png")
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_breakfast/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_breakfast/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_breakfast/{version}/y_train.csv").values
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_breakfast/{version}/y_test.csv").values

    st.write("### ML Pipeline: Predict Breakfast")
    # display pipeline training summary conclusions
    st.info(
        f"* The pipeline was tuned aiming at least 0.80 avarage Recall, "
        f"since we are interested in this project in understanding our guest.\n"
        f"* The pipeline performance on train and test set "
        f"is 0.82 and 0.77, respectively."
    )

    # show pipelines
    st.write("---")
    st.write("#### There are 2 ML Pipelines arranged in series.")

    st.write(" * The first is responsible for data cleaning and feature engineering.")
    st.write(breakfast_pipe_dc_fe)

    st.write("* The second is for feature scaling and modelling.")
    st.write(breakfast_pipe_model)

    # show feature importance plot
    st.write("---")
    st.write("* The features the model was trained and their importance.")
    st.write(X_train.columns.to_list())
    st.image(breakfast_feat_importance)

    # evaluate performance on train and test set
    st.write("---")
    st.write("### Pipeline Performance")
    
    clf_performance(X_train=X_train, y_train=y_train,
                    X_test=X_test, y_test=y_test,
                    pipeline=breakfast_pipe_model,
                    label_map=["No", "Yes", "Again"])
