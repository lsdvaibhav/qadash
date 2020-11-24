import streamlit as st

def login():
  """login form"""
  st.title("qaDash")
  st.subheader("Login")
  username = st.text_input("Username")
  password = st.text_input("Enter a password", type="password")
  if st.button("Login"):
    if  password == '123': 
      st.success("logged in")
    
if __name__ == "__main__":
  login()
