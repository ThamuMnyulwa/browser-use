# browser-use

A Python package for browser automation using AI agents. This tool allows you to programmatically control web browsers to perform tasks using natural language instructions.

## Installation

### Prerequisites

- Python 3.12 or higher
- Playwright (browser automation library)

### Install from PyPI

```bash
pip install browser-use
```

### Install from Source

Clone the repository and install in development mode:

```bash
git clone https://github.com/your-username/browser-use.git
cd browser-use
pip install -e .
```

### Installing Browser Binaries

Playwright (the browser automation library used by browser-use) needs to be installed.
You need to run the Playwright installation command:

```bash
playwright install
```

This will download and install the browser binaries that Playwright needs to function properly.

## Environment Setup

Create a `.env` file in your project root with the following variables:

```
OPENAI_API_KEY=<your_openai_api_key>
GEMINI_API_KEY=<your_gemini_api_key>
```

## Usage

### Command Line Interface

```bash
# Run a browser task
browser-use run "Go to Google and search for Python"

# Get version information
browser-use --version

# Get help
browser-use --help
```

### Python API

```python
import asyncio
from langchain_openai import ChatOpenAI
from browser_use_package import Agent, Browser, BrowserConfig

# Initialize the language model
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Configure browser
config = BrowserConfig(
    headless=False,  # Set to True to run without visible browser
    timeout=30
)

# Initialize browser
browser = Browser(config=config)

async def main():
    # Create agent with a task
    agent = Agent(
        task="Go to Wikipedia and search for Python programming language",
        llm=llm,
        browser=browser,
        generate_gif=False,
    )
    
    # Run the agent
    result = await agent.run()
    
    # Process results
    for action in result.action_results():
        print(action.extracted_content)
    
    # Close the browser when done
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
```

## Examples

The repository includes several example use cases that demonstrate the capabilities of browser-use:

### 1. Simple Example

Basic browser automation example demonstrating web search and information extraction.

```bash
python examples/simple_example.py
```

### 2. Agent Browsing

Interactive Jupyter notebook demonstrating browser agent functionality.

```bash
jupyter notebook examples/agent_browsing.ipynb
```

### 3. Download and Upload

The `examples/download_and_upload` directory contains examples showing how to:
- Download images and files from websites
- Upload files through browser interfaces

## Configuration Options

### Browser Configuration

`BrowserConfig` provides several options to customize browser behavior:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| headless | bool | False | Run browser without GUI |
| timeout | int | 30 | Timeout for browser operations in seconds |
| user_agent | str | None | Custom user agent string |

### Agent Configuration

When creating an Agent, you can customize its behavior:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| task | str | - | Natural language task to perform |
| llm | LLM | - | Language model for reasoning |
| browser | Browser | - | Browser instance |
| generate_gif | bool | False | Generate GIF of browser actions |

## Advanced Features

### File Downloads

The package supports downloading files from websites:

```python
browser = Browser(
    config=BrowserConfig(
        new_context_config=BrowserContextConfig(
            save_downloads_path="/path/to/downloads"
        )
    )
)
```

### File Uploads

For file uploads, you can use the Controller with custom actions:

```python
controller = Controller()

@controller.action('Upload file to interactive element with file path')
async def upload_file(index: int, path: str, browser: BrowserContext, available_file_paths: list[str]):
    # Implementation details...
    pass
```

## Development

To set up the development environment:

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"

# Install playwright browsers
playwright install
```

## License

[Include license information here]
