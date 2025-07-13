from langchain.vectorstores import OpenSearchVectorSearch
from langchain.embeddings import OpenAIEmbeddings
import os

openai_api_key=os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise EnvironmentError("OPENAI_API_KEY not found")

embedding_model = OpenAIEmbeddings(openai_api_key=openai_api_key)

retriever = OpenSearchVectorSearch(
    index_name="sre-logs",
    opensearch_url="http://localhost:9200",
    embedding=embedding_model,
)
