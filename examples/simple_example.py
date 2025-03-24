# This import is required only for jupyter notebooks, since they have their own eventloop
import nest_asyncio
import os
from langchain_openai import ChatOpenAI
import dotenv
from browser_use_package import Agent, Browser
from browser_use_package import BrowserConfig
import asyncio

# Apply nest_asyncio for async support
nest_asyncio.apply()

# Load environment variables
dotenv.load_dotenv()

# Get the API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the language model
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Basic configuration for the browser
config = BrowserConfig(
    headless=True,  # Run in headless mode
    # disable_security=True  # Uncomment if you want to disable security
)

# Initialize the browser with the specified configuration
browser = Browser(config=config)


async def main():
    # Initialize the agent with the task and language model
    agent = Agent(
        task="Tell me about Unathi Skosana",
        llm=llm,
        browser=browser,
        generate_gif=False,  # Disable GIF generation
    )

    # Run the agent and get results asynchronously
    result = await agent.run()

    # Process results token-wise
    for action in result.action_results():
        if action.is_done:
            print(action.extracted_content)
            print("\n")

    # Close the browser after completion
    await browser.close()


# Run the asynchronous main function
if __name__ == "__main__":
    asyncio.run(main())
