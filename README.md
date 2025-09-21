# AI Text Extractor

This is a simple **AI-powered pipeline** that extracts structured information (like **Names** and **Dates**) from plain-text files using **spaCy** + **Streamlit**.
The results are displayed in a web interface and also saved to a CSV file.

---

## 📂 Project Structure

```
Extractor/
│
├── scribe_portal.py    # Main Streamlit app
├── harvest_log.csv     # Output file (auto-created after run)
```

---

## ⚡ Requirements

* Python 3.9+
* pip (Python package manager)

Dependencies:

* `streamlit`
* `spacy`
* `pandas`
* spaCy English model: `en_core_web_sm`

---

## 🔧 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/AI-data-extractor.git
cd AI-data-extractor/Extractor
```

### 2. Create a virtual environment (recommended)

#### On **Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

#### On **Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## 🚀 Running the App

Once inside the `Extractor` folder:

```bash
streamlit run scribe_portal.py
```

This will start a **local web server**.
Open the link shown in terminal (usually [http://localhost:8501](http://localhost:8501)).

---

## 📜 Usage

1. Upload the attached `.txt` file.
2. The app will extract **Names** and **Dates**.
3. Results are shown:

   * As JSON
   * As a table
   * Saved automatically in `harvest_log.csv`

---

## 📝 Example

**Input file (`sample_doc.txt`)**:

```
Meeting Notes

On 15th September 2025, John Smith met with Alice Johnson in New Delhi to discuss the upcoming product launch. 
The deadline for the first phase is October 2, 2025. 
A follow-up meeting is scheduled for next Monday with Dr. Robert Brown. 

Prepared by: Sarah Williams
```

**Extracted Output (CSV):**

```csv
Names,Dates
John Smith,September 2025
Alice Johnson,"October 2, 2025"
Robert Brown,next Monday
Sarah Williams,
```

---
