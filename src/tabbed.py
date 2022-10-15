# from curses import def_shell_mode
import streamlit as st
import webbrowser
import time

# USER Imports
from processImg import imageView


def start_tabs():
    tab1, tab2, tab3 = st.tabs(["Single File Upload", "Helpful Links", "Our Team"])

    with tab1:
        st.title("Upload a file to get started")
        with st.form("my_form", clear_on_submit=True):
            file = st.file_uploader(
                label="Upload a file",
                # label="",
                type=["jpg", "png", "JPG", "PNG", "jpeg", "JPEG"],
            )
            checkbox_val = st.checkbox("Is Annotation Available?")

            # Every form must have a submit button.
            submitted = st.form_submit_button("Start Analysis")
        if submitted:
            imageView(file)
            # spinner while inference is running
            with st.spinner(text="Inferencing..."):
                time.sleep(5)
            st.success("Done!")

    with tab2:
        url = "https://www.streamlit.io/"
        if st.button("Streamlit"):
            webbrowser.open_new_tab(url)
        url = "https://engineering.purdue.edu/Engr/Research/EURO"
        if st.button("EURO Homepage"):
            webbrowser.open_new_tab(url)
        url = "https://engineering.purdue.edu/Engr/Research/EURO/students/FAQ"
        if st.button("SURF Program Details"):
            webbrowser.open_new_tab(url)
        url = "https://engineering.purdue.edu/Engr/Research/EURO/surf-symposium"
        if st.button("SURF Symposium"):
            webbrowser.open_new_tab(url)

    with tab3:
        col51, col52, col53 = st.columns([1, 1, 1], gap="medium")
        with col51:
            st.image("media/varun.jpeg", caption="Varun", width=210)
            st.text("Founder")
        with col52:
            st.image("media/varun.jpeg", caption="Varun", width=210)
            st.text("CEO")
        with col53:
            st.image("media/varun.jpeg", caption="Varun", width=210)
            st.text("CFO")
        col54, col55, col56 = st.columns([1, 1, 1], gap="medium")
        with col54:
            st.image("media/varun.jpeg", caption="Varun", width=210)
            st.text("CCO")
        with col55:
            st.image("media/varun.jpeg", caption="Varun", width=210)
            st.text("EURO")
