import streamlit as st
import ollama

st.title("Simple Language Translator")

text = st.text_area("Enter Text")

languages = ["Hindi", "Gujarati", "Marathi", "Tamil", "Telugu", "Bengali", "Punjabi", "English"]

language = st.selectbox("Translate To", languages)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        response = ollama.chat(
            model="qwen2.5:3b",
            options={
                "temperature": 0,
                "top_p": 0.1
            },
            messages=[
                {
                    "role": "system",
                    "content": "You are a translation engine. Translate the user's text into " + language + ". Rules: output ONLY the translation in the native script. No transliteration. No romanization. No parentheses. No explanations. No extra lines. Just the single translated sentence."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        translation = response["message"]["content"].strip()

        translation = translation.split("\n")[0]
        translation = translation.split("(")[0].strip()

        st.text_area("Translation", value=translation)
st.success("Made By Bhavya S Solanki")
