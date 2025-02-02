from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY is not set")

PHI_API_KEY=os.environ.get("PHI_API_KEY")
if PHI_API_KEY is None:
    raise ValueError("PHI_API_KEY is not set")



websearch_agent = Agent(
    name="Web Search Agent",
    role="search the web for information.",
    #backstory="You are an expert in web search and can answer questions about any topic.",
    tools=[DuckDuckGo()],
    model=Groq(id="llama3-70b-8192", temperature=0.1),
    #allow_delegation=True,
    instructions=["Always include sources "],
    show_tool_calls=True,
    markdown=True,
)

## Financial Agent
financial_agent = Agent(
    name="Financial AI Agent",
    role="you are an expert in financial analysis.",
    #backstory="You are an expert in financial analysis and can answer questions about any topic.",
    tools=[YFinanceTools(stock_price=True,analyst_recommendations=True,stock_fundamentals=True,company_news=True,company_info=True)],
    model=Groq(id="llama3-70b-8192", temperature=0.1),
    #allow_delegation=True,
    instructions=[f"""Always include sources and Always use tables to present data, 
                    present current stock price, 
                    company news and 
                    company info"""],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    team=[websearch_agent,financial_agent],
    instructions=[f"""Always include sources , Always use tables to present data,
                    present current stock price, 
                    company news and 
                    company info"""],
    model=Groq(id="llama3-70b-8192", temperature=0.1),
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations, latest news, and stock price for starbucks", stream=True)