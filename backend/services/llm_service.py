import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:4b"


def ollama_generate(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama error: {response.text}")

    return response.json()["response"]


def generate_response(prompt: str):
    return ollama_generate(prompt)


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

Abstracts:
{combined_text}
"""
    return ollama_generate(prompt)


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
    return ollama_generate(prompt)

def generate_citations(papers, style):
    prompt = f"""
Format the following papers into {style} citations.

Papers:
{papers}
"""
    return ollama_generate(prompt)