import streamlit as st
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import os
from zipfile import ZipFile
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(page_title="AI WEBSITE CREATION", page_icon="🤖")
st.title("AI AUTOMATION WEBSITE CREATION")

prompt = st.text_area("write here about your website")

if st.button("Generate Website"):
    message= [("system",""" you are a expert website developer mainly in frontend development so create html,css and java scripts code for creating a frontend based on the user prompt
               
               the output should be  in the below format
               
               ---html--
               [html code]
               --html--
               
               --css--
               [css code]
               --css--
               
               --js--
               [java script code]
               --js-- """)]

    message.append(("user",prompt))
    
    model= ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    response=model.invoke(message)
    
    with open("file.txt","w") as file:
        file.write(response.content)
        
    with open("index.html","w") as file:
        file.write(response.content.split("--html--")[1])
        
    with open("style.css","w") as file:
        file.write(response.content.split("--css--")[1]) 

    with open("script.js","w") as file:
        file.write(response.content.split("--js--")[1])
    
    from zipfile import ZipFile

    with ZipFile("website.zip", "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    st.download_button("Click to Download your Website",data=open("website.zip","rb"),file_name="website.zip")

    st.success("Website Generated Successfully")
    
    