from unittest.util import _count_diff_all_purpose
import streamlit as st
import time

# USER IMPORTS
from inference import getInference


def imageView(img, classList, userSelectedClass, checkbox_val=False):
    col11, col12 = st.columns([2, 1])
    with col11:
        st.image(img, caption="")
    with col12:
        if checkbox_val:
            st.write(f"User Selected Class: {userSelectedClass}")
        inferenceMesasge, inferClass, _, inferConfidence = getInference(img)  # type: ignore
        with st.spinner(text="Loading..."):
            time.sleep(2)
        if inferClass == userSelectedClass and inferConfidence > 50 and checkbox_val:
            st.write(f"Predicted Class: {inferClass}")
            st.write(f"Class Confidence: {inferConfidence}")
            return 1, inferClass, inferConfidence
        else:
            finalClass = st.selectbox(
                label="Predicted Class",
                options=classList,
                index=classList.index(inferClass),
            )
            st.write(f"Confidence: {inferConfidence}")
            if st.button("Save Image and Image Class", key="saveImg"):
                return 1, finalClass, inferConfidence
    return 0, 0, 0


def suc():
    # st.success("Image Saved Successfully")
    st.success("Analysis Complete and Image Saved")
