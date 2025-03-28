import streamlit as st



def page_project_hypothesis_body():

    st.write("### Project Hypotesis and Validation")
    
    st.write("#### Hypotesis 1")

    st.info(
        f"We suspected that guests who rated taste and variety higher "
        f"would have breakfast next time, and this is also the best predictor"
        )
    
    st.error(
        f"We found in the survey summary that there was a positive "
        f"correlation between these features and the breakfast variable, "
        f"but not a strong one and certainly not the most significant one."
    )

    st.write("---")

    st.write("#### Hypotesis 2")
    
    st.info(
        f"We suspected that guests who had breakfast "
        f"but didn't want it the next time would generally rate lower "
        f"than those who didn't have breakfast at all."
    )

    st.error(
        f"It is wrong: the ML prediction shows the opposite."
    )

    st.write("---")

    st.write("#### Hypotesis 3")

    st.info(
        f"From the correlation analysis, we suggest that the two most "
        f"important characteristics are 'hotel' and 'staff'."
    )

    st.success(
        f"The ML model confirms this. So the data suggests that if the client "
        f"wants to improve breakfast sales, perhaps the best way to do so is "
        f"to focus on improving the overall stay experience and the way the "
        f"crew treats guests."
    )