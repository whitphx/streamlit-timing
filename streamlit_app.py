import streamlit as st

from streamlit_timing import delayed_rerun


if st.button("Rerun in 3 sec"):
    delayed_rerun(3)
