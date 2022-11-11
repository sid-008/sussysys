import json
import os
import shlex
import subprocess

import pandas as pd
import streamlit as st

st.write("""
    # Per Second syscalls
    ##SUSSYSYS##
         """)

df = pd.read_csv("data3.csv")
st.line_chart(df)
