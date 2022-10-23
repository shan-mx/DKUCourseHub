from data import *
from helper import *
import streamlit as st

st.set_page_config(page_title='DKU Course Hub', page_icon='📚')
st.title('DKU Course Hub')

tab_search, cart, tab_timetable = st.tabs(['Search', 'Course Cart', 'Timetable'])
with tab_search:
    time_prompt = st.text_input('Time', '10:00-11:59,13:15-21:59')
    subject = st.selectbox('Subject', [''] + [each for each in subjects if subjects[each] != ''])
    datad = search_course(subject)
    section = st.selectbox('Section', get_sections(datad))
    datad = search_course(subject, section)
    instr = st.multiselect('Instructor', get_instr_names(datad))
    datad = search_course(subject, section, instr)
with tab_timetable:
    st.write(subject)

col_names = ['name', 'number', 'time', 'room', 'instructor']
for course_name, each_course in datad.items():
    cols = st.columns([1, 1, 2, 2, 2])
    with st.columns(1)[0]:
        st.write(course_name)
    for class_name, each_class in each_course.items():
        period_num = len(each_class['time'])
        with st.container():
            with cols[0]:
                st.write(class_name)
            with cols[1]:
                st.write(each_class['number'])
        for i in range(2, len(col_names)):
            with cols[i]:
                st.write(each_class[col_names[i]][0])
        if period_num > 1:
            with st.container():
                for i in range(2, len(col_names)):
                    for j in range(1, period_num):
                        with cols[i]:
                            st.write(each_class[col_names[i]][j])



