import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Stuffs",
        page_icon="👋",
    )

    st.write("# Bem vindo ao Stuffs! 👋")

    # st.sidebar.success("Select a demo above.")


if __name__ == "__main__":
    run()
