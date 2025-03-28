"""Breakfast Predictor Page."""

import streamlit as st
import pandas as pd
from src.data_management import load_survey, load_pkl_file
from src.machine_learning.predictive_analysis_ui import (
    predict_breakfast,
    predict_cluster)


def page_breakfast_predictor_body():
    """Body of breakfast predictor page."""
    st.write("### Breakfast Predictor")

    # load predict breakfast files
    version = 'v1'
    breakfast_pipe_dc_fe = load_pkl_file(
        f'outputs/ml_pipeline/predict_breakfast/{version}/clf_pipeline_data_cleaning_feat_eng.pkl')
    breakfast_pipe_model = load_pkl_file(
        f"outputs/ml_pipeline/predict_breakfast/{version}/clf_pipeline_model.pkl")
    breakfast_features = (pd.read_csv(f"outputs/ml_pipeline/predict_breakfast/{version}/X_train.csv")
                      .columns
                      .to_list()
                      )

    version = 'v1'
    cluster_pipe = load_pkl_file(
        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
                        .columns
                        .to_list()
                        )
    cluster_profile = pd.read_csv(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")

    st.info(
        f"* The client is interested in determining whether or not a given prospect would have breakfast."
        f"If so, the client is interested to know when. In addition, the client is "
        f"interested in learning from which cluster this prospect will belong in the customer base. "
        f"Based on that, present potential factors that he should focus on."
    )
    st.write("---")

    X_live = DrawInputsWidgets()

    if st.button("Run Predictive Analysis"):
        breakfast_prediction = predict_breakfast(
            X_live, breakfast_features, breakfast_pipe_model)

        predict_cluster(X_live, cluster_features, cluster_pipe)


def check_variables_for_UI(breakfast_features, cluster_features):
    import itertools

    combined_features = set(
        list(
            itertools.chain(breakfast_features, cluster_features)
            )
    )
    st.write(
        f"* There are {len(combined_features)} features for the UI: \n\n {combined_features}")


def DrawInputsWidgets():

    df = load_survey()

    col1, col2, col3 = st.columns(3)

    X_live = pd.DataFrame([], index=[0])

    options = []
    for i in range(1,11):
        options.append(i)

    with col1:
        feature = "hotel"
        st_widget = st.selectbox(
            label=feature,
            options=options
        )
    X_live[feature] = st_widget

    with col2:
        feature = "service"
        st_widget = st.selectbox(
            label=feature,
            options=options
        )
    X_live[feature] = st_widget

    with col3:
        feature = "variety"
        st_widget = st.selectbox(
            label=feature,
            options=options
        )
    X_live[feature] = st_widget

    return X_live
