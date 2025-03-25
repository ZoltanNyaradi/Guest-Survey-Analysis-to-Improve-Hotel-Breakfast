import streamlit as st

class MultiPage:

    def __init__(self, app_name) -> None:
        self.page = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon=":croissant:"
        )


    def add_page(self, title, func) -> None: 
        self.page.append({"title": title, "function": func })


    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.page, format_func=lambda page: page['title'])
        page['function']() 

