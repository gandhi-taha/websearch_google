import streamlit as st
from googleapiclient.discovery import build
from google.cloud import aiplatform

def google_search(query, api_key, cx_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=cx_id, **kwargs).execute()
    return res['items']

def get_prediction(project, location, endpoint_id, content):
    client_options = {"api_endpoint": location+"-aiplatform.googleapis.com"}
    client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)
    endpoint = client.endpoint_path(project=project, location=location, endpoint=endpoint_id)
    response = client.predict(endpoint=endpoint, instances=[{"content": content}])
    return response.predictions[0]

def main():
    st.title('Gemini Chatbot')
    user_input = st.text_input("Please enter your query")
    if st.button('Send'):
        project = 'YOUR_PROJECT_ID'
        location = 'YOUR_LOCATION'
        endpoint_id = 'YOUR_ENDPOINT_ID'
        response = get_prediction(project, location, endpoint_id, user_input)
        st.write(response)
    if st.button('Search'):
        results = google_search(user_input, 'api-key', 'cxr', num=10)
        for result in results:
            st.write(result['title'])
            st.write(result['link'])
            st.write(result['snippet'])
            st.write('---')

if __name__ == "__main__":
    main()
