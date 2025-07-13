# Task 3.1 – Conversational Loop with Telemetry

## Overview

This task implements a basic conversational loop using a local LLM API (OpenAI-compatible) with built-in telemetry and logging. The primary goal is to simulate and monitor the behaviour of a chat system capable of maintaining conversation state while tracking interactions for performance analysis and quality assurance.

The system is implemented as a simple command-line interface (CLI) where users can ask questions, and the system responds using a deployed language model. Each interaction is logged with metadata to enable analysis of usage patterns and model performance.

---

## Features

- Conversational CLI with stateful loop.
- Uses OpenAI-compatible `ChatCompletion` API.
- Automatically logs:
  - Prompt content
  - Model responses
  - Token usage
  - Latency
- Supports `.env` configuration for API key and model endpoint.
- Logs all telemetry data into a structured JSONL log file.

---

## Folder Structure


---

## Setup Instructions

### 1. Python Environment

Ensure you have Python 3.11 installed. Then create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate


---

## Setup Instructions

### 1. Python Environment

Ensure you have Python 3.11 installed. Then create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

pip install -r requirements.txt


### 3. Configure dependencies
OPENAI_API_KEY=your-api-key-here
OPENAI_API_BASE=https://your-api-endpoint.com/v1
MODEL_NAME=gpt-4

Example Ineraction

> Hello, who are you?
Assistant: I'm an AI assistant here to help you. How can I assist?

