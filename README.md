# websearch_google

A small Streamlit app that pairs Google Programmable Search with a Vertex AI model prediction.

I built this as a quick experiment. It puts a text box on screen, then gives you two buttons. "Search" runs your query through the Google Custom Search API and lists the title, link and snippet for each result. "Send" passes your query to a model deployed on a Vertex AI endpoint and prints the prediction. It is a single file, `search.py`, and it was a way to try both APIs from one page.

## What's inside

- `search.py`: the whole app. `google_search()` calls the Custom Search API, `get_prediction()` calls a Vertex AI endpoint, and `main()` wires them to the Streamlit UI.

## Running it

You need your own Google Cloud setup: a Custom Search API key and search engine (cx) ID, and a Vertex AI endpoint. The project id, location and endpoint id are placeholders in `main()`, so fill those in first.

```
pip install streamlit google-api-python-client google-cloud-aiplatform
streamlit run search.py
```

Status: experiment, 2024, not maintained.
