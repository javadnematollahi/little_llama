import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama.settings import Settings
import argparse

# setting = Settings()

# parser = argparse.ArgumentParser()
# parser.add_argument('--data_path', type=str,default="./llama/data", help='Path of Your text file')
# parser.add_argument('--token', type=str,default=setting.OPENAI_API_KEY, help='Path of Your text file')
# parser.add_argument('--query', type=str,default="what is the content about?", help='Path of Your text file')
# opt = parser.parse_args()

# class Llama():
#     def __init__(self, path, token) -> None:
#          self.path = path
#          os.environ['OPENAI_API_KEY'] = token

#     def getquery(self, your_query):
#         documents = SimpleDirectoryReader(self.path).load_data()
#         index = VectorStoreIndex.from_documents(documents)
#         query_engine = index.as_query_engine()
#         response = query_engine.query(your_query)
#         return (response)

# if __name__=="__main__":
#     lama = Llama(opt.data_path, opt.token)
#     result = lama.getquery(opt.query)
#     print(result)


def main():
    setting = Settings()

    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str,default="./llama/data", help='Path of Your text file')
    parser.add_argument('--token', type=str,default=setting.OPENAI_API_KEY, help='Path of Your text file')
    parser.add_argument('--query', type=str,default="what is the content about?", help='Path of Your text file')
    opt = parser.parse_args()

    os.environ['OPENAI_API_KEY'] = opt.token

    documents = SimpleDirectoryReader(opt.data_path).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(opt.query)
    return (response)

