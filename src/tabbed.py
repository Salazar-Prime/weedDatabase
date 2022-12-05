# from curses import def_shell_mode
import streamlit as st
import webbrowser
import time
import os
from PIL import Image

# USER Imports
import processImg
from utils import saveImg


checkbox_val = False
classList = []
userSelectedClass = ""
img = None
gbSubmit = False


def _callimagView():
    global img, classList, userSelectedClass, checkbox_val, gbSubmit
    processImg.imageView(img, classList, userSelectedClass, checkbox_val)


def start_tabs(cl):
    global img, classList, userSelectedClass, checkbox_val, gbSubmit
    classList = cl

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Single File Upload",
            "Search Database",
            "View Database",
            "Helpful Links",
            "Our Team",
        ]
    )
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
                userSelectedClass = st.selectbox(
                    label="Select the Class", options=classList
                )
        submitted = st.button("Start Analysis", key="startAnalysis")
        if submitted:
            gbSubmit = True

        if gbSubmit:
            suc, finalClass, _ = processImg.imageView(
                img, classList, userSelectedClass, checkbox_val
            )
            if suc == 1:
                saveImg(img, finalClass)
                st.success("Analysis Complete and Image Saved")
                gbSubmit = False
                time.sleep(3)

    with tab2:
        st.write("Search Database")
        query = st.text_input("Enter Search Query")
        if st.button("Search") and query:
            numberImages = [int(s) for s in str.split(query) if s.isdigit()]
            if len(numberImages) == 0:
                st.write("No Images Found, showing 1 image only")
                numberImages = [1]
            numberImages = numberImages[0]
            classForImage = query.split()
            for i in classForImage:
                if i in classList:
                    classForImage = i
                    break
            if type(classForImage) == list:
                st.write("No Images Found, showing images of cat")
                classForImage = "cat"
            # get list of files in folder
            imgList = os.listdir(f"database/{classForImage}")
            print(imgList)
            if len(imgList) > 0 and numberImages <= len(imgList) and numberImages > 0:
                st.write(f"Showing {numberImages} image for class {classForImage}")
                for i in range(numberImages):
                    print("Hello ---------", imgList[i])
                    img = Image.open(f"database/{classForImage}/{imgList[i]}")
                    img = img.resize((150, 150))
                    st.image(img)
            else:
                st.write(f"Insufficient images found for class {classForImage}")

    with tab3:
        col31, col32 = st.columns([1, 1])
        with col31:
            st.write("Feline Friend")
            imgList = os.listdir(f"database/{classList[0]}")
            if len(imgList) > 0:
                for i in range(len(imgList)):
                    img = Image.open(f"database/{classList[0]}/{imgList[i]}")
                    img = img.resize((150, 150))
                    st.image(img)
        with col32:
            st.write("Woof! Woof!")
            imgList = os.listdir(f"database/{classList[1]}")
            if len(imgList) > 0:
                for i in range(len(imgList)):
                    img = Image.open(f"database/{classList[1]}/{imgList[i]}")
                    img = img.resize((150, 150))
                    st.image(img)

    with tab4:
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

    with tab5:
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
