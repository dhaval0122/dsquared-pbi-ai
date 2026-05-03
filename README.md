![Python](https://img.shields.io/badge/python-3.10+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![AI Powered](https://img.shields.io/badge/AI-Powered-purple)

# 🤖 AI Power BI Assistant

AI-powered tool that converts natural language into Power BI DAX measures and automatically applies them to Power BI using pbi-cli and OpenAI.

### Quick Start

```
git clone https://github.com/dhaval0122/pbi-ai-assistant
cd pbi-ai-assistant

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### Setup

```
cp .env.example .env
```

Add your OpenAI key inside .env.

### Run

```
python -m pbi_ai.main 
```

or

```
pbi-ai
```

---


Power BI Desktop must be open
Table name assumed: Sales
Column assumed: Amount
Internet required for OpenAI API

### Future Improvements

```
Auto-detect Power BI schema
Auto-create dashboards 
Web UI using Streamlit
Multi-table support
```

