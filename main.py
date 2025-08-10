from langchain_openai import OpenAIEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import UnstructuredMarkdownLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

from langchain.schema.runnable import RunnableLambda, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatGroq(model = "openai/gpt-oss-120b")
e_model = OpenAIEmbeddings(model= "text-embedding-3-small")

#---------------------------------------- Utility functions -------------------------------
def getCompleteContext(ret_docs):
    context = ""
    for doc in ret_docs:
        context += doc.page_content
    return context
getContextRunnable = RunnableLambda(getCompleteContext)

def create_vector_store():
    loader = DirectoryLoader(
        path = 'data',
        glob = "**/*.md", 
        loader_cls=UnstructuredMarkdownLoader
    )
    docs = loader.load()
    print("created docs")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 5000,
        chunk_overlap = 300
    )
    split_docs = splitter.split_documents(docs)
    print("splitted docs")

    store = Chroma(
        embedding_function= e_model,
        persist_directory= "chroma_db",
    )
    store.add_documents(split_docs)
    print("vector store created successfully")

def query_vector_store(user_query):
    store = Chroma(
        persist_directory= "chroma_db",
        embedding_function= e_model
    )
    retriver = store.as_retriever(
        search_type = "mmr",
        search_kwargs = {
            "k": 4,
            "lambda_mult" : 0.5
        }
    )
    print("created retriver")

    input_prompt = PromptTemplate(
        template= """
            Hey you are a professional at answering the question by using only the context provided.
            If the question is out of context, no need of hallucinating the answer just tell them it is out of context question.

            quesry -> {query}\n\n
            context -> {context}
        """,
        input_variables= ['query', 'context']
    )

    parser = StrOutputParser()

    print("created chain")
    parallel_chain = RunnableParallel({
        "query" : RunnablePassthrough(),
        "context" : retriver | getContextRunnable
    })

    chain = parallel_chain | input_prompt | model | parser

    result = chain.invoke(user_query)
    return result

# create_vector_store()
# query_vector_store()