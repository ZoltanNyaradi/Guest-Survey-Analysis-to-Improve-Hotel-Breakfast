import streamlit as st

def predict_breakfast(X, features, pipeline_model):
       
    X_breakfast = X.filter(features)
    
    breakfast_prediction = pipeline_model.predict(X_breakfast)
    breakfast_prediction_proba = pipeline_model.predict_proba(X_breakfast)

    breakfast_proba = breakfast_prediction_proba[
        0, breakfast_prediction][0]*100
    
    breakfast_answer = ""
    if breakfast_prediction == 0:
        breakfast_answer = "didn't have breakfast"
    elif breakfast_prediction == 1:
        breakfast_answer = "had breakfast but next time wouldn't"
    else:
        breakfast_answer = "had breakfast and would again"

    statement =(
        f"### A guest with these answers most likely {breakfast_answer}. "
        f"And it has a probability {breakfast_proba.round(1)}%.")

    st.write(statement)



def predict_cluster(X, features, pipeline):

    X_cluster = X.filter(features)       
    
    cluster_prediction = pipeline.predict(X_cluster)

    if cluster_prediction[0]==0:
        
        cluster_name = "less satisfied guests"
        
        cluster_answer_probabilities = "'No': 86% , 'Yes, next time not': 13% , 'Yes, again': 1% "

        cluster_rates = ["1.0 -- 2.0","2.0 -- 3.0"]

    else:
        
        cluster_name = "more satisfied guests"
        
        cluster_answer_probabilities = "'No': 58% , 'Yes, next time not': 29% , 'Yes, again': 13%"

        cluster_rates = ["3.0 -- 6.0","4.0 -- 6.0"]


    statement = (
    f"### The guest is expected to belong to **cluster {cluster_prediction[0]}**. "
    f"This class we can describe as **{cluster_name}**."
    )
    st.write("---")
    st.write(statement)

    statement = (
        f"The probabilities for this cluster is the next: \n"
        f"{cluster_answer_probabilities}"
        )
    st.info(statement)
    
    statement = (f"Cluster {cluster_prediction[0]} has guests, "
        f"who rated food variaty between {cluster_rates[0]} "
        f"and the hotel overall {cluster_rates[1]}.")

    st.success(statement)
    
