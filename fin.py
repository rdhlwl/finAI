from dotenv import load_dotenv
import pandas as pd
import streamlit as st
from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import matplotlib


def main():

    load_dotenv()

    st.set_page_config(page_title="Fin.AI", page_icon="🤖")
    st.header("Fin.AI: Your AI-Powered Personal Finance Coach 💸")

    inputcsv = st.file_uploader("Upload your bank statement CSV", type = "csv")

    if inputcsv is not None:

        dataframe = pd.read_csv(inputcsv)
        

        process_df(dataframe)


        llm = OpenAI(temperature=0.7)
        agent = create_pandas_dataframe_agent(llm, dataframe, verbose = True)

        qchoice1 = st.button("Expand transaction history")
        qchoice2 = st.button("Breakdown my spending by category")
        qchoice3 = st.button("Give feedback on my spending")
    
        if qchoice1:
            st.write(dataframe)
        if qchoice2:
            response = agent.run("Parse through the transactions in the dataframe and sum up all of the transactions and sort them into their respective spending categories and sort by highest amount spent to lowest.")
            st.write(response)
        if qchoice3:
            response = agent.run("Give detailed feedback on how I can improve my spending and what categories I should spend less money on. Do not look at the transaction counts but instead the total amounts spent on each category. Multiple sentences.")
            st.write(response)

def process_df(df):

    #this function removes the payments on the card and 
    df.drop(df[df['Type'] == "Payment"].index, inplace=True)

    #multiplies amount column by -1
    df.Amount *= -1
    
    simpledf = df

    simpledf = simpledf.drop('Transaction Date', axis=1)
    simpledf = simpledf.drop('Post Date', axis=1)
    simpledf = simpledf.drop('Description', axis=1)
    simpledf = simpledf.drop('Type', axis=1)
    simpledf = simpledf.drop('Memo', axis=1)

    st.write(simpledf)

    newdict = simpledf.to_dict('index')

    #{0: {'Category': 'Shopping', 'Amount': 12.92}, 1: {'Category': 'Shopping', 'Amount': 0.53},...}

    simpledict = {}

    for index in newdict:
        nesteddict = newdict[index]
        for key in nesteddict:
            if key == "Category":
                category = nesteddict[key] #ex. category = shopping
                if category not in simpledict:
                    simpledict[category] = 0 #amount defaults to 0 
                simpledict[category] += nesteddict['Amount'] #aggregate all transactions into respective categories


    #now we have {category:TotalAmount} pairs

    st.write(simpledict)





    return df
    

        



if __name__ == "__main__":
    main()

