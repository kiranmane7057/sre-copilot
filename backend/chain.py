from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from retriever import retriever

llm = ChatOpenAI()
# qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def query_sre_logs(question: str) -> str:
    try:
        docs = retriever.similarity_search(question, k=3)
        if not docs:
            return "No relevant logs found"
        return "\n\n".join([doc.page_content for doc in docs])
    except Exception as e:
        return f"Error querying logs: {str(e)}"