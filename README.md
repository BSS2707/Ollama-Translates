# Simple Language Translator

A small Streamlit app that translates text into Hindi, Gujarati, Marathi, Tamil, Telugu, Bengali, Punjabi, or English using a local Ollama model.

## Requirements

- Python 3.9+
- [Ollama](https://ollama.com) installed and running locally
- The `qwen2.5:3b` model pulled in Ollama

## Setup

1. Install Ollama from https://ollama.com and make sure it's running.

2. Pull the model:
   ```
   ollama pull qwen2.5:3b
   ```

3. Install Python dependencies:
   ```
   pip install streamlit ollama
   ```

## Run

```
streamlit run simple_app.py
```

This opens the app in your browser, usually at `http://localhost:8501`.

## Usage

1. Type or paste text into the "Enter Text" box.
2. Choose a target language from the dropdown.
3. Click "Translate".
4. The translation appears in the "Translation" box below.

## Notes on accuracy

`qwen2.5:3b` is a small (3B parameter) model. It runs fast and needs little disk space (~1.9GB), but translation quality for Indic languages will still be inconsistent, especially for uncommon words or idioms. For more reliable results, consider:

- A larger local model such as `llama3.1:8b` (better multilingual quality, ~4.7GB)
- A dedicated translation API/service such as Google Translate, Bhashini, or IndicTrans2

## Changing the model

To try a different model, edit `simple_app.py` and change this line:

```python
model="qwen2.5:3b",
```

to any model name you have pulled in Ollama (check with `ollama list`).

## Files

- `simple_app.py` — the Streamlit application
