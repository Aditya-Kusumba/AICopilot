from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="qwen3:4b",
    base_url="http://localhost:11434"
)

def generate_response(prompt: str):
    return llm.invoke(prompt)

def generate_response(prompt: str):
    return llm.invoke(prompt)

def generate_literature_review(texts: list):
    combined_text = "\n\n".join(texts[:10])  # limit size

    prompt = f"""
You are a research assistant.

Given multiple research paper abstracts, generate a structured literature review with:
- Introduction
- Key Themes
- Methods
- Findings
- Trends

{texts}
"""

    return llm.invoke(prompt)

def generate_research_gap(text: str):
    prompt = f"""
Analyze this research paper abstract.

Identify:
- Limitations
- Missing aspects
- Future work

Abstract:
{text}
"""
    return llm.invoke(prompt)

def generate_citations(papers, style):
    prompt = f"""
Format the following papers into {style} citations.

Papers:
{papers}
"""
    return llm.invoke(prompt)