import streamlit as st
import spacy
import pandas as pd

# Load spaCy model
seer = spacy.load("en_core_web_sm")

st.title("📄 Information Extractor")
st.write("Upload a text file and extract structured **Names** and **Dates**.")

uploaded_scroll = st.file_uploader("Choose a .txt file", type=["txt"])

def distill_entities(text):
    doc = seer(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    dates = [ent.text for ent in doc.ents if ent.label_ in ["DATE", "TIME"]]
    return {"names": names, "dates": dates}

if uploaded_scroll:
    text = uploaded_scroll.read().decode("utf-8")
    st.subheader("📜 Input Text")
    st.write(text)

    entities = distill_entities(text)

    st.subheader("🧾 Extracted Entities (JSON)")
    st.json(entities)

    st.subheader("📊 Table View")
    ledger = pd.DataFrame({
        "Names": entities["names"],
        "Dates": entities["dates"]
    })
    st.dataframe(ledger)

    # Save results
    ledger.to_csv("harvest_log.csv", index=False)
    st.success("Results saved to harvest_log.csv ✅")
