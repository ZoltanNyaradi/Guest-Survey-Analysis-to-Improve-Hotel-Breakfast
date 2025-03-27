import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
from src.data_managment import load_survey, load_pkl_file


def page_ml_cluster_analysis_body():

    version = "v1"
    cluster_pipe = load_pkl_file(
        f"outputs/ml_pipeline/cluster_analysis/{version}/cluster_pipeline.pkl")
    cluster_silhouette = plt.imread(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_silhouette.png")
    features_to_cluster = plt.imread(
        f"outputs/ml_pipeline/cluster_analysis/{version}/features_define_cluster.png")
    cluster_profile = pd.read_csv(
        f"outputs/ml_pipeline/cluster_analysis/{version}/clusters_profile.csv")
    cluster_features = (pd.read_csv(f"outputs/ml_pipeline/cluster_analysis/{version}/TrainSet.csv")
                        .columns
                        .to_list()
                        )
    df_breakfast_vs_clusters = load_survey().filter(["breakfast"], axis=1)
    df_breakfast_vs_clusters["Clusters"] = cluster_pipe["model"].labels_

    st.write("### Page ML: Cluster Analysis")

    st.info(
        f"* We refitted the cluster pipeline using fewer variables, and it delivered equivalent "
        f"performance to the pipeline fitted using all variables.\n"
        f"* The pipeline average silhouette score is 0.50"
    )
    st.write("---")

    st.write("#### Cluster ML Pipeline steps")
    st.write(cluster_pipe)

    st.write("#### The features the model was trained with")
    st.write(cluster_features)

    st.write("#### Clusters Silhouette Plot")
    st.image(cluster_silhouette)

    cluster_distribution_per_variable(df=df_breakfast_vs_clusters, target='breakfast')

    st.write("#### Most important features to define a cluster")
    st.image(features_to_cluster)

    st.write("#### Cluster Profile")
    
    st.info(
        f"* We created two clusters, we could describe cluster 0 as"
        f"less satisfied guest and cluster 1 as more satisfied guest. \n"
        f"*  In cluster 1 the guest tend to more likely have breakfast,"
        f"and more likely that they would in the future again.\n"
        f"* The to most important variable to find these cluster are variety "
    )
   
    cluster_profile.index = [" "] * len(cluster_profile)
    st.table(cluster_profile)



def cluster_distribution_per_variable(df, target):

    df_bar_plot = df.groupby(["Clusters", target]).size().reset_index(name="Count")
    df_bar_plot.columns = ['Clusters', target, 'Count']
    df_bar_plot[target] = df_bar_plot[target].astype('object')

    st.write(f"#### Clusters distribution across {target} levels")
    fig = px.bar(df_bar_plot, x='Clusters', y='Count',
                 color=target, width=800, height=350)
    fig.update_layout(xaxis=dict(tickmode='array',
                      tickvals=df['Clusters'].unique()))
    
    st.plotly_chart(fig)

    df_relative = (df
                   .groupby(["Clusters", target])
                   .size()
                   .unstack(fill_value=0)
                   .apply(lambda x:  100*x / x.sum(), axis=1)
                   .stack()
                   .reset_index(name='Relative Percentage (%)')
                   .sort_values(by=['Clusters', target])
                   )
    df_relative.columns = ['Clusters', target, 'Relative Percentage (%)']

    st.write(f"#### Relative Percentage (%) of {target} in each cluster")
    fig = px.line(df_relative, x='Clusters', y='Relative Percentage (%)',
                  color=target, width=800, height=350)
    fig.update_layout(xaxis=dict(tickmode='array',
                      tickvals=df['Clusters'].unique()))
    fig.update_traces(mode='markers+lines')
    
    st.plotly_chart(fig)

