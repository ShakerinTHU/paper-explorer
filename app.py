import streamlit as st
import json

# Set the page title
st.set_page_config(page_title="Paper Explorer")

# Load 10,000-paper subset
with open("ccf_10000.json", "r", encoding="utf-8") as f:
    subset = json.load(f)

# Load extracted PDF info (from separate JSON file)
try:
    with open("pdf_extracted_info.json", "r", encoding="utf-8") as f:
        extracted_info_list = json.load(f)
        extracted_info_dict = {
            item["file"]: item["extracted_info"]
            for item in extracted_info_list
        }
except FileNotFoundError:
    extracted_info_dict = {}

# Search bar
search_query = st.sidebar.text_input("🔎 Search papers by keyword (title/abstract):").lower()
if search_query:
    filtered_papers = [p for p in subset if search_query in p.get("title", "").lower() or search_query in p.get("abstract", "").lower()]
else:
    filtered_papers = subset

# Dropdown from filtered list
titles = [paper.get("title", "No Title") for paper in filtered_papers]
selected_title = st.sidebar.selectbox("📘 Select a paper to view details:", titles)
selected_paper = next((p for p in filtered_papers if p.get("title") == selected_title), None)

# Title
st.title("📄 Academic Paper Explorer")

# Display selected paper info
if selected_paper:
    st.header(selected_paper.get("title", "No Title"))
    st.subheader("Authors")
    st.write(", ".join(selected_paper.get("authors", [])))
    st.subheader("Abstract")
    st.write(selected_paper.get("abstract", "No abstract available"))
    st.subheader("Year")
    st.write(selected_paper.get("year", "Unknown"))

    # ✅ Check and show extracted PDF info if available
    if selected_paper.get("title") == "Degradation prediction and rolling predictive maintenance policy for multi-sensor systems based on two-dimensional self-attention":
        info = extracted_info_dict.get("sample_paper.pdf", {})
        if info:
            st.subheader("📘 Extracted Information (from PDF):")
            st.write("**Research Problem:**", info.get("research_problem", "N/A"))
            st.write("**Proposed Method:**", info.get("proposed_method", "N/A"))
            st.write("**Datasets Used:**", info.get("datasets", "N/A"))
            st.write("**Benchmark Tasks:**", info.get("benchmarks", "N/A"))
            st.write("**Code Links:**", info.get("code_links", "N/A"))
            st.write("**Key Results:**", info.get("key_results", "N/A"))
else:
    st.warning("No paper selected.")
