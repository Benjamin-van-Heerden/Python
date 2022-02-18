import streamlit as st

# displaying text
name = "benjamin"
st.text("This is text")
st.text("Hello World!")
st.text(f"My name is {name}")


# headers
st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")

# markdown
st.markdown("This is markdown")
st.markdown("It even has basic LaTex support $e^{i\pi} = -1$")

# bootstrap like text
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("This is and error")
st.exception("This is an exception")
