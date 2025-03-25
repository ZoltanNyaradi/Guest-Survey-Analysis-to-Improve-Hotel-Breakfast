import streamlit as st
import pandas as pd

def page_summary_body():
    
    df_survey_terms = pd.DataFrame({
        "Terms":["Breakfast",
                 "Appearance",
                 "Service",
                 "Staff",
                 "Variety",
                 "Price",
                 "Taste",
                 "Hotel"
                 ],
        "Question in the survey":[
                 "Did you have breakfast?",
                 "How do you rate the appearance of our restaurant?",
                 "How satisfied are you with the quality and speed of our service?",
                 "How frendly and helpful out staff?",
                 "How do you rate the variety in our breakfast?",
                 "How do you rate our price for the breakfast?",
                 "How does our breakfast taste/ looks like?",
                 "How do you rate your stay?"
                 ]
    })

    df_survey_terms = df_survey_terms.set_index("Terms")

    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terms & Jargon**\n"
        f" - A **Guest** is a person who has booked room in your hotel.\n"
        f" - The dataset is a survey filled by your guests.\n"
        f" - The terms from the survey and the related questions below.\n"
        f" - For **Breakfast** they could answer **No**,"
        f" **Yes, but next time I wouldn't**, **Yes, and I would again**.\n"
        f" - For the other questions they could answer from 1 to 10,"
        f"where 1 is the least satisfied and 10 is the most satisfied option."
    )

    st.table(df_survey_terms)
    
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/ZoltanNyaradi/Guest-Survey-Analysis-to-Improve-Hotel-Breakfast)."
    )

    st.success(
        f""
    )