"""
Streamlit UI for Queue Optimization Agent with OpenAI Key Loader, Prompt Templates,
FAISS Memory (fallback to JSON), and Decision Logging.
"""
import streamlit as st
import pandas as pd
from datetime import datetime
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.prompts import PromptTemplate
from langchain.tools.python.tool import PythonREPLTool
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import VectorStoreRetrieverMemory
import os, json
import tempfile

# OpenAI Key
st.sidebar.subheader("🔐 API Configuration")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
if not api_key:
    st.warning("Please provide your OpenAI API Key in the sidebar.")
    st.stop()

# Upload simulation CSV
st.set_page_config(page_title="🧠 Queue Optimization Agent")
st.title("🧠 Autonomous Queue Optimization Agent")
uploaded_file = st.file_uploader("Upload Simulation CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Simulation Data")
    st.dataframe(df)

    # Prompt Template
    prompt_template = PromptTemplate(
        input_variables=["data", "question"],
        template="Analyze this queue data:
{data}

Question: {question}"
    )

    # Memory: FAISS or fallback to in-memory
    tmpdir = tempfile.mkdtemp()
    retriever_memory = VectorStoreRetrieverMemory(
        retriever=FAISS.from_texts(["Start of memory"], embedding=OpenAIEmbeddings(openai_api_key=api_key)).as_retriever()
    )

    # LangChain tools + agent
    tools = [
        Tool(
            name="PythonTool",
            func=PythonREPLTool().run,
            description="Useful for queue analysis"
        )
    ]
    llm = ChatOpenAI(temperature=0, openai_api_key=api_key)
    agent = initialize_agent(
        tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=retriever_memory, verbose=True
    )

    st.subheader("💬 Ask the Agent")
    user_input = st.text_area("Prompt", "What should we change to reduce wait time?")
    if st.button("🔍 Run Agent"):
        prompt = prompt_template.format(data=df.to_csv(index=False), question=user_input)
        with st.spinner("Analyzing..."):
            response = agent.run(prompt)

        # Log to JSON
        log_path = "logs/agent_decisions.json"
        os.makedirs("logs", exist_ok=True)
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "input": user_input,
            "template_prompt": prompt,
            "response": response
        }
        if os.path.exists(log_path):
            with open(log_path, "r+") as f:
                logs = json.load(f)
                logs.append(log_entry)
                f.seek(0)
                json.dump(logs, f, indent=2)
        else:
            with open(log_path, "w") as f:
                json.dump([log_entry], f, indent=2)

        st.success("✅ Response:")
        st.markdown(response)
