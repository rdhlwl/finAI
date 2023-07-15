from dotenv import load_dotenv
import tempfile
import csv
import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI


def main():

    load_dotenv()

    st.set_page_config(page_title="Fin.AI", page_icon="🤖")
    st.header("Fin.AI: Your AI-Powered Personal Finance Coach 💸")

    inputcsv = st.file_uploader("Upload your bank statement CSV", type = "csv")

    if inputcsv is not None:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as f:
            f.write(inputcsv.getvalue())

            llm = OpenAI(temperature=0)
            agent = create_csv_agent(llm, f.name, verbose = True)

            qchoice1 = st.button("Show me a chart of my expenses")
            qchoice2 = st.button("Breakdown my spending by category")
            qchoice3 = st.button("Breakdown and give feedback on my spending")
        
            if qchoice1:
                st.write("📈1")
            if qchoice2:
                response = agent.run("Parse through the transactions in the CSV file and sum up all of the transactions and sort them into their respective spending categories and sort by highest amount spent to lowest.")
                st.write(response)

# def process_csv(inputfile):
#     with open(inputfile, 'r') as input

        



if __name__ == "__main__":
    main()

