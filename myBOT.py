from langchain_experimental.agents.agent_toolkits import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI
import streamlit as st

#OpenAI API key  (Use your KEY)
OPENAI_API_KEY = 'Use your key here'

def myBOT():
    # Check for OpenAIkey
    if OPENAI_API_KEY is None or OPENAI_API_KEY == "":
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")

    st.set_page_config(page_title="ASK ME ANYTHING")
    st.header("ASK ME ANYTHING ABOUT THE CSV FILE.")

    csv_file = st.file_uploader("Upload a CSV file", type="csv")
    if csv_file is not None:

        agent = create_csv_agent(
            OpenAI(api_key=OPENAI_API_KEY, temperature=0), csv_file, verbose=True)

        user_question = st.text_input("Ask any question related to the titanic incident: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    myBOT()
