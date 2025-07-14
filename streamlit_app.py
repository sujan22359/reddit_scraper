import streamlit as st
from reddit_scraper import scrape_user_content
from generate_persona import generate_persona, save_persona_file, improve_format, extract_username_from_url
import os

st.set_page_config(page_title="Reddit User Persona Generator", layout="centered")
st.title("🧠 Reddit User Persona Generator")

input_url = st.text_input("Enter Reddit Username or Profile URL:", "")

if st.button("Generate Persona"):
    if input_url.strip() == "":
        st.warning("Please enter a valid Reddit profile URL or username.")
    else:
        username = extract_username_from_url(input_url) if "reddit.com" in input_url else input_url
        st.info(f"🔍 Scraping Reddit user: `{username}`...")

        with st.spinner("Fetching user data..."):
            data = scrape_user_content(username)

        st.success(f"✅ Fetched {len(data['posts'])} posts and {len(data['comments'])} comments")

        with st.spinner("🧠 Generating persona using LLM..."):
            persona = generate_persona(data['posts'], data['comments'])
            txt_path = save_persona_file(username, persona)
            formatted_txt_path = improve_format(txt_path)

        st.success("🎉 Persona generation complete!")
        st.subheader("📄 User Persona:")
        st.markdown(persona)

        with open(formatted_txt_path, "r", encoding="utf-8") as f:
            st.download_button("📥 Download Persona (.txt)", f, file_name=f"{username}_persona.txt")
