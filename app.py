import streamlit as st

st.title("Student Application Form")

# -------- Sidebar --------
st.sidebar.title("Sidebar")
st.sidebar.text_input("Enter your email")
st.sidebar.selectbox("Select your country", ["India", "USA", "UK"])
st.sidebar.slider("Rate this app", 0, 5)

# -------- Tabs --------
tab1, tab2, tab3 = st.tabs(["Home", "Form", "Upload"])

# -------- Tab 1 --------
with tab1:
    st.header("Welcome Page")

    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", step=1)
    address = st.text_area("Enter your address")

    st.date_input("Select date")
    st.time_input("Select time")

    color = st.color_picker("Pick a color")
    st.write("Selected color:", color)

    st.checkbox("I agree")
    gender = st.radio("Select gender", ["Male", "Female", "Other"])
    st.write("Gender:", gender)

# -------- Tab 2 --------
with tab2:
    st.header("Registration Form")

    with st.form("form1"):
        col1, col2 = st.columns(2)

        with col1:
            st.text_input("First Name")

        with col2:
            st.text_input("Last Name")

        st.text_input("Email")
        st.text_input("Password", type="password")

        col1, col2 = st.columns(2)
        with col1:
            st.date_input("Start Date")

        with col2:
            st.date_input("End Date")

        st.text_area("Address")

        submit = st.form_submit_button("Submit")

        if submit:
            st.success("Form Submitted Successfully!")

# -------- Tab 3 --------
with tab3:
    st.header("File Upload")

    file = st.file_uploader("Upload a file", type=["jpg", "png", "pdf"])

    if file is not None:
        st.success("File uploaded successfully!")

        # Show image if uploaded
        if file.type.startswith("image"):
            st.image(file)

# -------- Columns --------
st.write("Columns Section")
col1, col2 = st.columns(2)

with col1:
    st.write("Column 1")
    st.text_input("Enter name in column 1")

with col2:
    st.write("Column 2")
    st.text_input("Enter name in column 2")

# -------- Button --------
if st.button("Final Submit"):
    st.success("Submitted Successfully!")

# -------- Link --------
st.write("[Google](https://www.google.com)")