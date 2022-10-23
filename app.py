from data import *
from helper import *
import streamlit as st

st.set_page_config(page_title='Better DKU Hub', page_icon='❤️')
st.title('Better DKU Hub')
tab_search, cart, tab_timetable = st.tabs(['Search', 'Course Cart', 'Timetable'])
with tab_search:
    time_prompt = st.text_input('Time', '10:00-11:59,13:15-21:59')
    subject = st.selectbox('Subject', [''] + [each for each in subjects if subjects[each] != ''])
    datad = search_by_subject(subject)
    section = st.selectbox('Section', get_sections(datad))
    instr = st.multiselect('Instructor', get_prof_names(datad))
with tab_timetable:
    st.write(subject)


with st.container():
    cols = st.columns(7)
    col_names = ['number', 'name', 'time', 'room', 'instructor']
    for each_col in cols:
        with each_col:
            st.write('s02')