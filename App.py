import streamlit as st
import ollama

st.title("Translator")

text = st.text_area("Enter Text")
language = st.selectbox(
    "Translate To",
    ["Hindi", "Gujarati", "Marathi", "Tamil", "Telugu", "English"]
)

if st.button("Translate"):
    response = ollama.chat(
        model="phi3:mini",
        messages=[
            {
                "role": "user",
                "content": f"Translate this into {language}. Only return the translation:\n\n{text}"
            }
        ]
    )

    st.write(response["message"]["content"])
