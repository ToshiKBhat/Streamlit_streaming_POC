import streamlit as st
import httpx
import asyncio

async def fetch_stream(url):
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            async for chunk in response.aiter_text():
                yield chunk

async def main():
    st.title("Streamlit with Streaming API")

    url = "http://127.0.0.1:8000/stream"  # URL of your FastAPI streaming endpoint

    if st.button("Start Streaming"):
        placeholder = st.empty()
        text = ""

        async for chunk in fetch_stream(url):
            text += chunk
            placeholder.text(text)

if __name__ == "__main__":
    asyncio.run(main())
