import streamlit as st

@st.cache(allow_output_mutation=True)
def get_data():
    return []


btns = [st.button("Select", key=i) for i in range(5)]
for i in range(5):
    if btns[i]:
        get_data().append(i)

if st.button("Reset"):
    get_data().clear()
st.write(get_data())
