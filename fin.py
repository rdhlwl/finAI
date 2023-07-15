from dotenv import load_dotenv
import tempfile
import pandas as pd
import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI


def main():

    load_dotenv()

    st.set_page_config(page_title="Fin.AI", page_icon="🤖")
    st.header("Fin.AI: Your AI-Powered Personal Finance Coach 💸")

    inputcsv = st.file_uploader("Upload your bank statement CSV", type = "csv")

    if inputcsv is not None:

        dataframe = pd.read_csv(inputcsv)
        del dataframe["Memo"]
        st.write(dataframe)

        process_df(dataframe)

        llm = OpenAI(temperature=0)
        agent = create_pandas_dataframe_agent(llm, dataframe, verbose = True)

        qchoice1 = st.button("Show me a chart of my expenses")
        qchoice2 = st.button("Breakdown my spending by category")
        qchoice3 = st.button("Give feedback on my spending")
    
        if qchoice1:
            st.write("📈1")
        if qchoice2:
            response = agent.run("Parse through the transactions in the dataframe and sum up all of the transactions and sort them into their respective spending categories and sort by highest amount spent to lowest.")
            st.write(response)


def process_df(dataframe):

    #this function removes the payments on the card and 
    #deletes all unnecessary columns from the dataframe such as dates

    

    return dataframe
    

        



if __name__ == "__main__":
    main()

