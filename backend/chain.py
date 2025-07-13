from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from retriever import retriever

llm = ChatOpenAI()
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def query_sre_logs(question: str):
    return qa.run(question)
