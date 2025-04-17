from pathlib import Path

# Define the full code content
code_content = '''
# AI Legal Analyst using Google’s Agent Development Kit (ADK)

import os
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

# --------------------------
# Setup Environment
# --------------------------

os.environ["GOOGLE_API_KEY"] = "your_google_api_key"
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"  # Optional

# --------------------------
# Tool Definitions
# --------------------------

def ingest_document(file_path: str) -> str:
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."

def extract_information(text: str) -> dict:
    print("Simulating entity extraction...")
    return {
        "Parties": ["Acme Corp", "Global Holdings"],
        "EffectiveDate": "2025-01-01",
        "Terms": ["Non-compete", "Payment Clause"]
    }

def summarize_document(text: str) -> str:
    print("Generating summary...")
    return "This contract outlines the terms between Acme Corp and Global Holdings..."

def detect_risks(text: str) -> list:
    print("Scanning for risks...")
    risks = []
    if "arbitration clause" not in text.lower():
        risks.append("Missing arbitration clause detected.")
    if "payment terms unclear" in text.lower():
        risks.append("Ambiguous payment terms found.")
    return risks or ["No significant risks found."]

# --------------------------
# Agent Configuration
# --------------------------

ingestion_agent = Agent("IngestionAgent", tools=[ingest_document], model="gemini-pro")
extraction_agent = Agent("ExtractionAgent", tools=[extract_information], model="gemini-pro")
summary_agent = Agent("SummarizationAgent", tools=[summarize_document], model="gemini-pro")
risk_agent = Agent("RiskAgent", tools=[detect_risks], model="gemini-pro")

coordinator_agent = Agent(
    name="CoordinatorAgent",
    sub_agents=[ingestion_agent, extraction_agent, summary_agent, risk_agent],
    model="gemini-pro"
)

# --------------------------
# Session Management
# --------------------------

session = InMemorySessionService()
print("Session initialized.")

# --------------------------
# Guardrail Example
# --------------------------

def before_tool_callback(tool_call):
    if "terminate" in tool_call.args.lower():
        raise ValueError("Use of restricted term: 'terminate'")
    return tool_call

# --------------------------
# Runner Function
# --------------------------

def run_legal_analyzer(filepath: str):
    print(f"\\nAnalyzing contract: {filepath}\\n")
    
    raw_text = coordinator_agent.tools["ingest_document"](filepath)
    if "Error" in raw_text:
        print(raw_text)
        return

    session.store("raw_text", raw_text)
    extracted_info = coordinator_agent.tools["extract_information"](raw_text)
    session.store("extracted_info", extracted_info)
    
    summary = coordinator_agent.tools["summarize_document"](raw_text[:500])
    session.store("summary", summary)

    risks = coordinator_agent.tools["detect_risks"](raw_text)
    session.store("risks", risks)

    print("\\nResults:")
    print(f"Key Info: {session.get('extracted_info')}")
    print(f"Summary: {session.get('summary')}")
    print(f"Risks: {session.get('risks')}")

# --------------------------
# Test Contract File
# --------------------------

with open("sample_contract.txt", "w") as f:
    f.write("Acme Corp and Global Holdings agree to terms on 2025-01-01. Payment terms unclear. No arbitration clause.")

run_legal_analyzer("sample_contract.txt")
'''

# Write to a file
file_path = Path("/mnt/data/adk_legal_analyst.py")
file_path.write_text(code_content)

file_path.name
