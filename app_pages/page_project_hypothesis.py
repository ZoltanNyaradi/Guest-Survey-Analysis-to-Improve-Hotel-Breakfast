import streamlit as st



def page_project_hypothesis_body():

    st.write("### Project Hypotesis and Validation")

    st.success(
        f"* We suspect guests who rate taste and variaty higher, "
        f"would have breakfast next time: correct, "
        f"but the correlation not strong. The correlation study shows that.\n"
        f"* We suspected guests who had but next time wouldn't have breakfast, "
        f"they have generaly worst rating then thoes, "
        f"who didn't have breakfast at all: False."
        f"The studies show the opposite.\n"
        f"* We found that, that the 2 most important features are "
        f"**hotel** and **staff**."
    )