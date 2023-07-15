import streamlit


def main():
    streamlit.set_page_config(page_title="Fin.AI", page_icon="🤖")
    streamlit.header("Fin.AI: Your AI-Powered Personal Finance Coach 💸")

    inputcsv = streamlit.file_uploader("Upload your bank statement CSV", type = "csv")



if __name__ == "__main__":
    main()

