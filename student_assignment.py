from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    
    # 使用 CharacterTextSplitter 將文本切割成塊
    text_splitter = CharacterTextSplitter(chunk_overlap=0)
    chunks = text_splitter.split_documents(docs)
    if chunks:
        return (chunks[-1])
    pass

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    
    # 合併所有頁面的文本
    full_text = "\n".join([doc.page_content for doc in docs])
    
    # 使用 RecursiveCharacterTextSplitter 將文本切割成塊
    text_splitter = RecursiveCharacterTextSplitter(
        separators = [
            r"第\s*[一二三四五六七八九十]+\s*章\s",
            r"\n第\s*\d+\s*條",
            r"\n第\s*\d+-\d+\s*條",
            r"第\s*\d+\s*條\n",
            r"第\s*\d+-\d+\s*條\n",
        ],
        chunk_size=5,
        chunk_overlap=0,
        is_separator_regex=True
    )
    chunks = text_splitter.split_text(full_text)

    if chunks:
        return (len(chunks))
    pass

'''if __name__ == "__main__":
     last_chunk = hw02_1(q1_pdf)
     print(last_chunk)
     chunk_count = hw02_2(q2_pdf)
     print(chunk_count)'''