# phidata
Agentic Arch with Phidata
AI Agents for Web Search and Financial Analysis

# Overview

This project leverages the phi library to create AI agents that perform web search and financial analysis. The agents are integrated into a web-based playground using FastAPI, allowing users to interact with them in real-time.

# Features

  Web Search Agent: Uses DuckDuckGo to fetch accurate and relevant search results.

  Financial AI Agent: Provides financial analysis, stock performance insights, and company news using yfinance tools.

  Interactive Playground: Built with FastAPI, allowing users to interact with both agents in a user-friendly interface.

# Requirements

Ensure you have the following installed:

Python 3.8+

phi

dotenv

fastapi

uvicorn

yfinance

# Install dependencies using:

pip install -r requirements.txt

# Environment Variables

This project requires API keys for Groq and Phi. Store them in a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key
PHI_API_KEY=your_phi_api_key

# Usage

Running the Playground

Start the application by running:

python playground.py

Or using Uvicorn:

uvicorn playground:app --reload

The app will be available at http://localhost:7777.

# Agents

## Web Search Agent

Uses DuckDuckGo for web searches.

Provides accurate and well-cited information.

Model: llama-3.3-70b-versatile

## Financial AI Agent

Retrieves stock prices, company fundamentals, and news.

Uses yfinance for financial data analysis.

Presents information in tables and bullet points.

Model: llama-3.3-70b-versatile

# Flow Diagram

Below is the flow diagram representing the interactions between components:

  <img width="571" alt="image" src="https://github.com/user-attachments/assets/0d73ecdf-d4cd-486e-bef8-13d62b600f8c" />


# Contributing

Feel free to submit pull requests or open issues for improvements.

# License

This project is licensed under the MIT License.
