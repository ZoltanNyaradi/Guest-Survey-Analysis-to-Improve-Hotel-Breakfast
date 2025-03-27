import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.data_managment import load_survey
from src.data_managment import encode_breakfast

def page_survey_study_body():
    
    st.write("### Survey Study")

    df = load_survey()
    df_encoded = encode_breakfast(df.copy())
    
    most_correlated_features = df_encoded.drop("breakfast", axis=1).corr(
        method="pearson")["breakfast_encoded"].drop(
            "breakfast_encoded").sort_values(key=abs, ascending=False)[:2]
    
    st.info(f"The survey was filled online "
            f"and on the hotel diveses in the lobby by the guest.\n"
            f"We collected rateings from {df.shape[0]} guests.\n"
            f"Here is a semple from the collected data bellow.")
    
    if st.checkbox("Inspect Survey's 10 first row"):
        
        st.table(df.head(10))

    st.info(f"We studied the pearson correlation between **breakfast** and "
            f"the feathers. "
            f"We found 2 features with medium correlation level, "
            f"**{most_correlated_features.index[0] }** with "
            f"**{most_correlated_features.iloc[0].round(2)}** and "
            f"**{most_correlated_features.index[1] }** with "
            f"**{most_correlated_features.iloc[1].round(2)}** respectively."
            )
    
    st.success(f"We made histogram diagram with these features.\n"
               f"- In the columns we can see the aswers "
               f" if they had breakfast.\n"
               f"- In each row represent a feature.\n"
               f"- And we can see on the histogram diagrams, "
               f"that how many guest and how they rated these features." 
    )

    if st.checkbox("Distribution of most correlated features"):
        plot_most_correlated_features(df_encoded,
                                      most_correlated_features.index)

    st.success(f"An we can inspect on heatmaps how their distributed in %.")

    if st.checkbox(
        f"Normalized distribution of {most_correlated_features.index[0]}"):
        plot_normalized_distribution(df_encoded,
                                     most_correlated_features.index[0])

    if st.checkbox(
        f"Normalized distribution of {most_correlated_features.index[1]}"):
        plot_normalized_distribution(df_encoded,
                                     most_correlated_features.index[1])
        

def plot_most_correlated_features(df, features):
    """
    Plot histograms from 2 features
    
    Take a DF and a series with 2 element with colom names from the df.
    Plot 6 histogram 3-3 with the 2 elements,
    2-2-2 with the uniqe values from 'breakfast' column.
    Each plot shows the distibution of the feature regarding the uniqe value.
    """
    breakfast_answers = order_answers(df) 
    
    fig, axes = plt.subplots(2, 3, figsize=(10, 6))

    for i_feature in range(0, 2):
        for i_answer in range(0, 3):
            
            df_same_answer = df[df["breakfast"]==breakfast_answers[i_answer]]

            sns.histplot(df_same_answer[features[i_feature]],
                         ax=axes[i_feature, i_answer],
                         binwidth=.8,
                         color="#22EE33")
            axes[i_feature, i_answer].set_xlabel("")
            axes[i_feature, i_answer].set_ylabel("")

            axes[i_feature, i_answer].set_title(
                f"{features[i_feature]} x {breakfast_answers[i_answer]}")
            
    plt.subplots_adjust(hspace=0.3, wspace=0.3)
    st.pyplot(fig)


def plot_normalized_distribution(df, feature):
    """
    Plot a normalized distrobtion heatmap
    
    Take a DF and a value, what is a column name in the DF.
    Plot a heatmap 3 columns and 10 rows.
    Each colum is a uniqe value from 'breakfast' column.
    Each row is a uniqe value from the colomn
    with the same name as the passed variable.
    The values are normalized by columns.
    """

    breakfast_answers = order_answers(df)

    df_normalized = pd.DataFrame()

    for i_answer in range(0, 3):

        df_answer = df[df["breakfast"]==breakfast_answers[i_answer]]
        ser = pd.Series()

        for index in range(0, 11):

            count = df_answer[df_answer[feature]==index].shape[0]
            ser = pd.concat([ser, pd.Series(count)])

        df_normalized[breakfast_answers[i_answer]]=ser/ser.sum()
    
    df_normalized.reset_index(inplace=True, drop=True)
    df_normalized = df_normalized.drop(index=0)

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df_normalized, annot=True, fmt=".2f", ax=ax)
    
    st.pyplot(fig)


def order_answers(df):
    """
    Gives an ordered list from uniqe vaules of 'breakfast'

    Take DF with 'breakfast' and 'encoded_breakfast'.
    Return list with 'breakfast' uniqes ordered by 'encoded_breakfast'.  
    """
    breakfast_answers_unordered=df["breakfast"].unique()
    breakfast_answers_encoded=df["breakfast_encoded"].unique()
    breakfast_answers=[0,0,0]

    for i_answer in range(0, 3):
        breakfast_answers[breakfast_answers_encoded[i_answer]]=(
            breakfast_answers_unordered[i_answer])

    return breakfast_answers

