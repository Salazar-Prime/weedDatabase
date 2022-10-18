# from curses import def_shell_mode
import streamlit as st
import webbrowser
import time

# USER Imports
import processImg

checkbox_val = False
weedList = []
userWeedCLass = ""
img = None
gbSubmit = False


def _callimagView():
    global img, weedList, userWeedCLass, checkbox_val, gbSubmit
    processImg.imageView(img, weedList, userWeedCLass, checkbox_val)


def start_tabs(wl):
    global img, weedList, userWeedCLass, checkbox_val, gbSubmit
    weedList = wl

    tab1, tab2, tab3 = st.tabs(["Single File Upload", "Helpful Links", "Our Team"])
    with tab1:
        img = st.file_uploader(
            label="Upload a file to get started",
            type=["jpg", "png", "JPG", "PNG", "jpeg", "JPEG"],
        )
        col11, col12 = st.columns([1, 2])
        with col11:
            checkbox_val = st.checkbox("Is Annotation Available?", key="checkboxAA")
        with col12:
            if checkbox_val:
                userWeedCLass = st.selectbox(label="Select the Class", options=weedList)
        submitted = st.button("Start Analysis", key="startAnalysis")
        if submitted:
            gbSubmit = True

        if gbSubmit:
            suc = processImg.imageView(img, weedList, userWeedCLass, checkbox_val)
            if suc == 1:
                st.success("Analysis Complete and Image Saved")
                time.sleep(3)

    with tab2:
        url = "https://www.streamlit.io/"
        if st.button("Streamlit"):
            webbrowser.open_new_tab(url)
        url = "https://scholar.google.com/"
        if st.button("Shoulder of Giants"):
            webbrowser.open_new_tab(url)
        # url = "https://engineering.purdue.edu/Engr/Research/EURO/students/FAQ"
        # if st.button("SURF Program Details"):
        #     webbrowser.open_new_tab(url)
        # url = "https://engineering.purdue.edu/Engr/Research/EURO/surf-symposium"
        # if st.button("SURF Symposium"):
        #     webbrowser.open_new_tab(url)

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
