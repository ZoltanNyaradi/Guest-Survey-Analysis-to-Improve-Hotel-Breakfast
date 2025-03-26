import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_summary import page_summary_body
from app_pages.page_survey_study import page_survey_study_body

app = MultiPage(app_name = "Breakfast Survey")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Survey Study", page_survey_study_body)

app.run()
