
import streamlit as st
from supabase import create_client, Client
import Modules as md

# Hide Streamlit sidebar and other UI elements
st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    [data-testid="stSidebar"]{
        visibility: hidden;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Main app layout
def main():
    st.title("Lead Sync")
    st.write("sign up to continue.")

    # Login form
    st.subheader("Login")
    username = st.text_input("Email", key="login_email")
    idnumber = st.text_input("ID Number", key="login_idnumber")
    name = st.text_input("Name", key="login_name")
    Surname = st.text_input("Surname", key="login_surname")
    Phonenumber = st.text_input("Phone Number", key="login_phonenumber")


    col1, col2, col3 = st.columns([1,7,1])  # Adjust column ratios as needed
    with col2:
    # Sign-up button
        if st.button("Signup", use_container_width=True):
            user = md.login(username, password)
            st.switch_page("pages/Finish.py")

# Handle page routing
main()
