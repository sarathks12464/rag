import chromadb
import google.generativeai as genai
from pypdf import PdfReader
genai.configure()

reader = PdfReader("cv3.pdf")
text = ""
for pages in reader.pages:
    page_text = pages.extract_text()

    if page_text:
        text = text +page_text


client = chromadb.Client()
collection = client.create_collection("knowledge")

collection.add(
    documents=
    [text]
,ids = ["1"])

question = input("ask : ")

result = collection.query(query_texts=[question],n_results=1)

context = result["documents"][0][0]

prompt = context,question
model = genai.GenerativeModel("gemini-2.5-flash")
response = model.generate_content(prompt)
print(response.text)
