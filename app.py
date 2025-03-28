import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_survey_study import page_survey_study_body
from app_pages.page_breakfast_predictor import page_breakfast_predictor_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_predict_breakfast import page_ml_predict_breakfast_body
from app_pages.page_ml_cluster_analysis import page_ml_cluster_analysis_body

app = MultiPage(app_name = "Breakfast Survey")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Survey Study", page_survey_study_body)
app.add_page("Breakfast Predictor", page_breakfast_predictor_body)
app.add_page("Project Hypotesis and Validation", page_project_hypothesis_body)
app.add_page("ML: Predict Breakfast", page_ml_predict_breakfast_body)
app.add_page("ML: Cluster Analysis", page_ml_cluster_analysis_body)

app.run()
