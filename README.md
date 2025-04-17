# 🧠 ADK Playground: LegalBot

This project is a  AI legal assistant powered by Google’s Agent Development Kit (ADK). It simulates how a multi-agent system can analyze legal contracts—extracting key details, summarizing content, and flagging potential legal risks—entirely in a local development environment.

## 📌 Repository: [baburam1985/adk-playground-legalbot](https://github.com/baburam1985/adk-playground-legalbot)

---

## 🔍 What It Does

- Reads raw legal text from contract files
- Extracts parties, dates, and terms
- Summarizes legal clauses into simple language
- Detects potential issues like missing arbitration clauses or vague terms

This is not a toy example—it mimics real-world legal workflows using a modular, extensible agent-based design.

---

## ⚙️ Local Setup

### 1. Clone the Repo

```bash
git clone https://github.com/baburam1985/adk-playground-legalbot.git
cd adk-playground-legalbot
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Your API Keys

```bash
export GOOGLE_API_KEY="your_google_api_key"
export OPENAI_API_KEY="your_openai_key"  # optional fallback
```

> 💡 Want to avoid exposing keys? Use `.env` + `python-dotenv` (optional setup).

### 5. Run It Locally

```bash
python adk_legal_analyst.py
```

---

## 🧪 Sample Output

```bash
Analyzing contract: sample_contract.txt

Step 1: Document ingested.
Step 2: Information extracted.
Step 3: Summary generated.
Step 4: Risks identified.

Results:
Key Info: {'Parties': ['Acme Corp', 'Global Holdings'], 'EffectiveDate': '2025-01-01'}
Summary: This contract outlines the terms between Acme Corp and Global Holdings...
Risks: ['Missing arbitration clause detected.', 'Ambiguous payment terms found.']
```

---

## 🧠 Agents in Action

| Agent                  | Role                                                  |
|------------------------|-------------------------------------------------------|
| `IngestionAgent`       | Reads contract files                                  |
| `InfoExtractionAgent`  | Identifies parties, dates, and terms                  |
| `SummarizationAgent`   | Generates plain-English summaries                     |
| `RiskDetectionAgent`   | Flags legal risks or missing clauses                  |
| `CoordinatorAgent`     | Orchestrates the entire flow between other agents     |


---

## 📚 References

- [Google ADK Docs](https://google.github.io/adk-docs)
- [Google Dev Blog – ADK Overview](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications)
- [Cloud Next 2025 Sessions](https://cloud.withgoogle.com/next)

---

> ⚖️ Built as an exploratory side project. Contributions, forks, and feedback are welcome!
