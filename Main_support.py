import time                   
import streamlit as st

def progress_bar():
    progress_text="☕ Take a cup of Tea ☕☕"
    my_bar = st.progress(0, text=progress_text)
    st.markdown('<h3 style="color:red; ">Integration of Given Function</h3>', unsafe_allow_html=True)
    st.write("")

    for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty()


def to_respect_first_second(to_respect):
    if to_respect!=None:
        to_resp_var=None
        if to_respect=="dx":
               to_resp_var="x"
        if to_respect=="dy":
               to_resp_var="y" 
        if to_respect=="dz":
               to_resp_var="z"
        return to_resp_var
    
def lower_of_xyza(func_text):
    func_text_m=func_text
    if "X" in func_text:
       func_text_m=func_text.replace("X","x")
    if "Y" in func_text:
        func_text_m=func_text.replace("Y","y")
    if "Z" in func_text:
        func_text_m=func_text.replace("Z","z")
    if "A" in func_text:
        func_text_m=func_text.replace("A","a")
    return func_text_m