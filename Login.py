
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
    st.write("Log in or sign up to continue.")

    # Login form
    st.subheader("Login")
    username = st.text_input("Email", key="login_email")
    name = st.text_input("Name", key="login_name")
    Surname = st.text_input("Surname", key="login_surname")
    Phonenumber = st.text_input("Phone Number", key="login_phonenumber")
    password = st.text_input("Password", type="password", key="login_password")

    col1, col2, col3 = st.columns([1,7,1])  # Adjust column ratios as needed
    with col2:

            if user:
                st.session_state["user"] = user
                st.success("Logged in successfully!")
                st.switch_page("pages/Home.py")
    # Sign-up button
        if st.button("Signup", use_container_width=True):
            user = md.login(username, password)
            st.switch_page("pages/Finish.py")

# Handle page routing
main()
