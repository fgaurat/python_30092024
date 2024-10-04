import streamlit as st
from EmployeeDAO import EmployeeDAO

# streamlit run main_streamlit.py
def main():
    
    st.set_page_config(layout="wide")

    st.write("Hello, *World!* :sunglasses:")
    first_name = st.text_input("Prénom ?", "")
    if st.button("say Hello"):
        st.write("Hello", first_name)


    dao = EmployeeDAO("employees_db.db")
    employees = dao.find_all()
    st.table(employees)
    # if st.button("Say hello"):
    #     st.write("Why hello there")
    # else:
    #     st.write("Goodbye")

if __name__=='__main__':
    main()
