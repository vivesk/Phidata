from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

import phi.api
import phi
from phi.playground import Playground,serve_playground_app
# Load environment variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY is not set")

PHI_API_KEY = os.environ.get("PHI_API_KEY")
if PHI_API_KEY is None:
    raise ValueError("PHI_API_KEY is not set")

# Define Web Search Agent
websearch_agent = Agent(
    name="Web Search Agent",
    role="Search the web for relevant and accurate information.",
    backstory="You are an expert in web search, skilled at finding precise, reliable, and up-to-date information on any topic.",
    tools=[DuckDuckGo()],
    model=Groq(id="llama-3.3-70b-versatile", temperature=0.1),
    instructions=[
        "Provide detailed and accurate responses using reliable sources.",
        "When appropriate, include URLs and citations for any web-sourced information.",
    ],
    show_tool_calls=True,
    markdown=True,
)

# Define Financial Analysis Agent
financial_agent = Agent(
    name="Financial AI Agent",
    role="Provide comprehensive financial analysis, insights, and data visualization.",
    backstory="You are a financial expert capable of analyzing stock performance, summarizing news, and presenting key company information.",
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        stock_fundamentals=True,
        company_news=True,
        company_info=True
    )],
    model=Groq(id="llama-3.3-70b-versatile", temperature=0.1),
    instructions=[
        "Always include credible sources for financial data and news.",
        "Present information in tables for clarity, including stock price, analyst recommendations, and company fundamentals.",
        "Summarize company news in bullet points for quick readability.",
        "Ensure data and analysis are up-to-date and concise."
    ],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[websearch_agent,financial_agent]).get_app()


# Run a Query with Multi-Agent System
#multi_ai_agent.print_response("Summarize analyst recommendations, latest news, and stock price for Humana Inc", stream=True)

if __name__ == "__main__":
    serve_playground_app("playground:app",reload=True)   
