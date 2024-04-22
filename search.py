import streamlit as st
from googleapiclient.discovery import build

def google_search(query, api_key, cx_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=cx_id, **kwargs).execute()
    return res['items']

def main():
    st.title('Gemini Chatbot')
    user_input = st.text_input("Please enter your query")
    if st.button('Search'):
        results = google_search(user_input, 'api-key', 'cx_id', num=10)
        for result in results:
            st.write(result['title'])
            st.write(result['link'])
            st.write(result['snippet'])
            st.write('---')

if __name__ == "__main__":
    main()
