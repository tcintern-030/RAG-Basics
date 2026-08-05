import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

"""
loader = TextLoader("sample_directory/sample.txt")
documents = loader.load()

print(documents)
"""

dir_loader = DirectoryLoader(
    "sample_directory", 
    glob="*.txt",
    loader_cls=TextLoader
)
directory = dir_loader.load()

print("\n\nDocuments from directory:")
print(directory)

def split_documents(documents, chunk_size=1000, chunk_overlap=0):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return text_splitter.split_documents(documents)

chunks = split_documents(directory)

print("\n\nChunks:")

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}:")
    print(chunk)
    print("\n")

