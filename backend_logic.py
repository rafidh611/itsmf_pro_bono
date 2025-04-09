import chromadb
from openai import OpenAI

# __import__('pysqlite3')
# import sys
# sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

#chromdb client
client = chromadb.PersistentClient("./collection")

collection = client.get_or_create_collection(name="ITSMF_RAG",
                                             metadata={"hnsw:space": "cosine"})


#OpenAI Model
openai_client = OpenAI()


def run_user_query(query):
    response = openai_client.chat.completions.create(
        model='gpt-4o',
        messages=[
           {"role": "system", "content": "You're a helpful assistant who looks up specific information about an organization called Information Technology Senior Management Forum (ITSMF) from user queries. If you are not able to answer the question, say 'I'm sorry, I don't have access to that information.'"},
           {"role": "user", "content": query},
        ]
    )

    return response.choices[0].message.content