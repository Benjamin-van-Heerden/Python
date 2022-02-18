import streamlit as st
from PIL import Image
import pandas as pd
import docx2txt
import pdfplumber
from PyPDF2 import PdfFileReader
from os.path import join, dirname


@st.cache()
def load_image(image_file):
    img = Image.open(image_file)
    return img


def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        text += page.extractText()
    return text


def save_uploaded_file(file):
    with open(join(dirname(__file__), f"./saved_files/saved_{file.name}"), "wb",) as f:
        f.write(file.getbuffer())
        st.success(
            f"Saved file to {join(dirname(__file__), f'./saved_files/saved_{file.name}')}"
        )


def main():
    st.title("File Upload App")

    menu = ["Image", "Dataset", "Document File", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Image":
        st.subheader("Image")
        image_files = st.file_uploader(
            "Upload Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True
        )
        # for images multiple files are allowed
        if image_files:
            for image_file in image_files:
                file_details = {
                    "file_name": image_file.name,
                    "file_type": image_file.type,
                    "file_size": image_file.size,
                }
                st.json(file_details)
                st.image(load_image(image_file), width=400)
                # saving file
                if st.button("Save File", key=f"button_{file_details['file_name']}"):
                    save_uploaded_file(image_file)

    elif choice == "Dataset":
        st.subheader("Dataset")
        dataset_file = st.file_uploader("Upload CSV", type=["csv"])
        if dataset_file is not None:
            file_details = {
                "file_name": dataset_file.name,
                "file_type": dataset_file.type,
                "file_size": dataset_file.size,
            }
            st.json(file_details)
            df = pd.read_csv(dataset_file)
            st.dataframe(df)

            # saving file
            if st.button("Save File"):
                save_uploaded_file(dataset_file)

    elif choice == "Document File":
        st.subheader("Document File")
        document_file = st.file_uploader(
            "Upload Document File", type=["PDF", "docx", "txt"]
        )
        if document_file is not None:
            file_details = {
                "file_name": document_file.name,
                "file_type": document_file.type,
                "file_size": document_file.size,
            }
            st.json(file_details)
            if file_details["file_type"] == "text/plain":
                text = document_file.read().decode("utf8")
                st.write(text)
            elif file_details["file_type"] == "application/pdf":
                # # using pdfplumber
                # try:
                #     with pdfplumber.open(document_file) as pdf:
                #         pages = pdf.pages[0]
                #         st.write(pages.extract_text())
                # except Exception as e:
                #     st.exception(e)

                # using PyPDF2
                try:
                    text = read_pdf(document_file)
                    st.write(text)
                except Exception as e:
                    st.exception(e)
            else:
                text = docx2txt.process(document_file)
                st.write(text)

            # saving file
            if st.button("Save File"):
                save_uploaded_file(document_file)

    else:
        st.subheader("About")


if __name__ == "__main__":
    main()
