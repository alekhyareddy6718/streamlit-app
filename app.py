import streamlit as st

st.title("📄 Profile Preview App")

# Sidebar
st.sidebar.header("User Settings")
st.sidebar.text_input("Enter your email")
st.sidebar.selectbox("Select country", ["India", "USA", "UK"])

# Tabs
tab1, tab2 = st.tabs(["Profile Form", "Upload & Preview"])

# -------- TAB 1 --------
with tab1:
    st.header("Enter Your Details")

    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", step=1)
    address = st.text_area("Enter your address")

    gender = st.radio("Select gender", ["Male", "Female", "Other"])

    if st.button("Show Profile"):
        st.write("### Your Details")
        st.write("Name:", name)
        st.write("Age:", age)
        st.write("Address:", address)
        st.write("Gender:", gender)

# -------- TAB 2 --------
with tab2:
    st.header("Upload Your File")

    file = st.file_uploader("Upload Resume / ID", type=["jpg", "png", "pdf"])

    if file is not None:
        st.success("File uploaded successfully ✅")

        # Show image preview
        if file.type.startswith("image"):
            st.image(file, caption="Uploaded Image", width=300)
        else:
            st.write("PDF uploaded (preview not shown)")

# Columns
st.write("### Feedback Section")
col1, col2 = st.columns(2)

with col1:
    st.text_input("Enter your feedback")

with col2:
    rating = st.slider("Rate this app", 0, 5)
    st.write("Rating:", rating)