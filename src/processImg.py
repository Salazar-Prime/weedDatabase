from unittest.util import _count_diff_all_purpose
import streamlit as st
import time


def imageView(img, weedList, userWeedCLass, checkbox_val=False):
    col11, col12 = st.columns([2, 1])
    with col11:
        st.image(img, caption="")
    with col12:
        if checkbox_val:
            st.write(f"User Weed Class: {userWeedCLass}")
        inferWeedClass, inferConfidence = inference(img)
        with st.spinner(text="Inferencing..."):
            time.sleep(2)
        if inferWeedClass == userWeedCLass and inferConfidence > 0.5 and checkbox_val:
            st.write(f"Predicted Class: {inferWeedClass}")
            st.write(f"Class Confidence: {inferConfidence}")
            return 1
        else:
            st.selectbox(
                label="Predicted Class",
                options=weedList,
                index=weedList.index(inferWeedClass),
            )
            st.write(f"Confidence: {inferConfidence}")
            if st.button("Save Image and Image Class", key="saveImg"):
                return 1
    return 0


def suc():
    # st.success("Image Saved Successfully")
    st.success("Analysis Complete and Image Saved")


def inference(img):
    inferConfidence = 0.4
    return "pigweed", inferConfidence
