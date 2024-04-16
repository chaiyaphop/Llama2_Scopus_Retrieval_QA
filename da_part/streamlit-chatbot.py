# get text input from Streamlit interface
import streamlit as st

prompt2 = st.text_area("Place the abstract of the research that captures your interest here")
if prompt2:
    st.write(prompt2)
    # embed
    from langchain.embeddings import HuggingFaceEmbeddings
    inference_api_key = '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'
    from langchain.embeddings import HuggingFaceInferenceAPIEmbeddings
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key=inference_api_key, model_name="morenolq/thext-cs-scibert"
    )
    query_result = embeddings.embed_query(prompt2)
    st.write(query_result)

