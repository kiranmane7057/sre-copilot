from langchain.vectorstores import OpenSearchVectorSearch
from langchain.embeddings import OpenAIEmbeddings

retriever = OpenSearchVectorSearch(
    index_name="sre-logs",
    opensearch_url="http://localhost:9200",
    embedding=OpenAIEmbeddings()
)
