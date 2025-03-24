Great, I’ll dive into the `browser-use` repository and Playwright documentation to improve the README. I’ll enhance clarity, add practical examples, insert relevant links to documentation, and ensure the usage of browser automation is well contextualized.

I’ll let you know when the updated version is ready.

# Browser Use – AI-Powered Browser Automation

 ([GitHub - browser-use/browser-use: Make websites accessible for AI agents](https://github.com/browser-use/browser-use)) *Figure: **Browser Use** enables AI agents to browse the web like a human, using the power of Playwright and LLMs.*

**Browser Use** is a Python package that lets AI agents (powered by Large Language Models, or LLMs) autonomously control a web browser. It bridges the gap between AI and web browsing by enabling agents to navigate sites, click links, fill forms, and extract information—just as a human user would ([Browser Use: An open-source AI agent to automate web-based tasks | InfoWorld](https://www.infoworld.com/article/3812644/browser-use-an-open-source-ai-agent-to-automate-web-based-tasks.html#:~:text=in%20digital%20interactions,step%20workflows)). Under the hood, it uses [Playwright](https://playwright.dev/python/) for browser automation and integrates with LLMs via [LangChain](https://python.langchain.com/) to interpret pages and decide actions. This means you can give your AI agent a high-level task, and **Browser Use** will handle the low-level browser interactions to accomplish it ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=Browser%20Use%20is%20a%20tool,as%20a%20human%20user%20would)) ([Browser Use: An open-source AI agent to automate web-based tasks | InfoWorld](https://www.infoworld.com/article/3812644/browser-use-an-open-source-ai-agent-to-automate-web-based-tasks.html#:~:text=in%20digital%20interactions,step%20workflows)).

## Features and Capabilities

- **Autonomous Web Interaction** – The agent reads page content, plans steps, and executes actions (clicks, typing, scrolling, etc.) on its own ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=AI)) ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=Browser%20Use%20leverages%20AI%20to,and%20execute%20those%20actions%20autonomously)). It extracts all interactive elements (buttons, inputs, links) and uses them to fulfill the given task, so you don’t have to write brittle DOM selectors yourself ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=The%20primary%20goal%20of%20Browser,AI%20agents%20to%20interact%20with)).  
- **Vision + DOM Understanding** – Combines visual context (screenshots) with HTML DOM parsing for robust element identification ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=Vision%20%2B%20HTML%20Extraction)). This dual approach helps the agent handle dynamic or unlabeled elements by “seeing” the page, improving reliability on modern web apps. (Vision can be toggled on/off depending on model support and cost considerations – e.g. GPT-4’s image analysis uses ~800-1000 tokens per image ([Agent Settings - Browser Use](https://docs.browser-use.com/customize/agent-settings#:~:text=,System%20Prompt%20for%20customization%20options)).)  
- **Multi-Tab Browsing** – Can operate multiple tabs or windows in parallel, enabling complex workflows across several pages at once (for example, comparing information or transferring data between sites) ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=Multi)). The agent keeps track of each tab’s state, which allows tasks like opening auxiliary pages for research or cross-checking.  
- **Custom Actions (Extensible Toolset)** – In addition to built-in browser actions (open URL, click element, type text, scroll, etc.), you can define your own **tools** for the agent via the `Controller`. For instance, you might add a custom action to solve CAPTCHAs, download a file, or query an API. The agent can then invoke these by name when needed ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=Custom%20Actions)). (See [Advanced Usage](#advanced-usage) for examples of adding custom controller actions.)  
- **Resilient Execution** – The system is designed to handle errors and adapt. If something goes wrong (a missing element, a timeout), the agent will try alternate strategies or retry up to a limit. This “self-healing” ability ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=input%20during%20specific%20steps%20in,the%20automation%20process)) helps complete tasks even when websites behave unexpectedly, and prevents simple hiccups from breaking the entire run.  
- **LLM Agnostic** – **Browser Use** supports a variety of language models through LangChain’s interface ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=Compatibility%20With%20Multiple%20LLMs)). You can plug in OpenAI’s GPT-4 (and GPT-3.5), Anthropic’s Claude, Google’s PaLM (Gemini), Meta’s LLaMA 2, or other chat models – including local models – as long as they support the required API or LangChain integration ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=Browser%20Use%20supports%20various%20LangChain,available%20in%20the%20LangChain%20documentation)) ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=Compatibility%20With%20Multiple%20LLMs)). This flexibility lets you choose cheaper or domain-specific models for your agent. *(OpenAI’s GPT-4 (denoted as “gpt-4o” in examples) currently gives the best results, achieving ~89% on a web automation benchmark ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=Model%20Recommendations)).)*

## Installation

**Requirements:** Python 3.11+ ([Automate anything in the browser using AI  | by Nikhil Adiga | Mar, 2025 | Medium](https://nikhiladigaz.medium.com/automate-anything-in-the-browser-using-ai-2df80a968f03#:~:text=%3E%20browser,or%20above)) and an API key for your chosen LLM provider (e.g. OpenAI, Anthropic, etc.). Playwright supports Windows, macOS, and Linux, and can run browsers in headless or headed mode ([Browsers | Playwright Python](https://playwright.dev/python/docs/browsers#:~:text=Playwright%20can%20run%20tests%20on,desktop%2C%20tablet%20and%20mobile%20devices)). To install **Browser Use** and set up the browser environment:

1. **Install the package from PyPI**: 

   ```bash
   pip install browser-use
   ```

2. **Install a Playwright browser** (e.g. Chromium): 

   ```bash
   playwright install chromium
   ``` 

   This downloads the browser binary that Playwright will control. Playwright can automate Chromium (Chrome/Edge), Firefox, and WebKit (Safari) browsers ([Browsers | Playwright Python](https://playwright.dev/python/docs/browsers#:~:text=Playwright%20can%20run%20tests%20on,desktop%2C%20tablet%20and%20mobile%20devices)) – you can install other engines (replace `chromium` with `firefox` or `webkit`) if needed. By default, **Browser Use** will launch Chromium unless configured otherwise.

3. **Set up API keys** for LLMs: In a `.env` file or environment variables, add the credentials for your language model. For example, for OpenAI and Gemini:

   ```bash
   OPENAI_API_KEY=<your OpenAI API key>
   GEMINI_API_KEY=<your Google Gemini API key>
   ```
   
   Make sure to obtain these from your provider’s platform (e.g., the [OpenAI API Keys page](https://platform.openai.com/account/api-keys) or [Google AI Gemini console](https://ai.google.dev/gemini-api/docs)). **Browser Use** will load them at runtime (you can use [`python-dotenv`](https://pypi.org/project/python-dotenv/) as shown in examples to load from a `.env` file).

4. **(Optional) Virtual Environment**: It’s recommended to use a virtual environment (e.g. via `venv` or tools like [uv](https://docs.astral.sh/uv)) to isolate this package and its dependencies ([Automate anything in the browser using AI  | by Nikhil Adiga | Mar, 2025 | Medium](https://nikhiladigaz.medium.com/automate-anything-in-the-browser-using-ai-2df80a968f03#:~:text=Installing%20browser)) ([Automate anything in the browser using AI  | by Nikhil Adiga | Mar, 2025 | Medium](https://nikhiladigaz.medium.com/automate-anything-in-the-browser-using-ai-2df80a968f03#:~:text=%3E%20browser,or%20above)).

## Quick Start Example

Once installed, you can spin up an AI agent with just a few lines of code. In this example, we use OpenAI’s GPT-4 model to perform a simple task:

```python
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent

load_dotenv()  # loads OPENAI_API_KEY from .env

# Define the task for the agent
task = "Find the founders of Browser Use on its GitHub page and draft a short personalized message to thank them."

# Initialize the language model (LLM) – here using OpenAI GPT-4
llm = ChatOpenAI(model="gpt-4", temperature=0.0)

# Create the browser agent with the task and LLM
agent = Agent(task=task, llm=llm)

# Run the agent asynchronously
asyncio.run(agent.run())
```

**What happens:** The agent will launch a browser (Chromium by default), go to the Browser Use GitHub page, find information about the founders, and compose a message. All actions (navigation, clicking, reading text) are decided by the GPT-4 model in real-time. When `agent.run()` completes, it returns an `AgentHistoryList` containing the full execution history. You can get the final result content with `history.final_result()` or inspect other details (visited URLs, screenshots, errors, etc. – see [Agent History](#agent-history-and-logging)). 

For more complex scenarios, you might provide a multi-step instruction or goal. The agent will break it down and may open multiple tabs or perform a series of interactions to achieve the goal. *Example:* “**Read my resume from disk, search for relevant machine learning job postings, save top 5 listings to a CSV, then start applying to each job**” – the agent could open a local file or URL of the resume, summarize skills, search job sites in new tabs, collect results into a file, and even simulate clicking “Apply” on those sites (this would require login info or further guidance). **Browser Use** is capable of such multi-step workflows (some end-to-end examples are provided in the [use-cases](https://github.com/browser-use/browser-use/tree/main/examples/use-cases) examples).

## Examples and Use Cases

To see Browser Use in action on real-world tasks, check out the **[`examples/`](https://github.com/browser-use/browser-use/tree/main/examples)** directory in the repository. Notable examples include:

- **Job Applications** – [`find_and_apply_to_jobs.py`](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/find_and_apply_to_jobs.py): Reads your CV, searches for ML jobs, and automatically applies to them (opens new tabs for each application) as instructed.  
- **Social Media Automation** – [`post-twitter.py`](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/post-twitter.py): Posts a tweet on X (Twitter) with given content, handling login (see also `twitter_post_using_cookies.py` for using saved cookies to log in).  
- **Web Scraping & Data** – [`wikipedia_banana_to_quantum.py`](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/wikipedia_banana_to_quantum.py): An example agent that navigates Wikipedia (starting from “Banana”) and follows links step-by-step to reach the “Quantum mechanics” page (a playful navigation challenge).  
- **Form Filling and Checks** – [`check_appointment.py`](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/check_appointment.py): Checks for visa appointment slots on a government site by logging in and navigating a dashboard.  
- **Miscellaneous** – Solving CAPTCHAs (`captcha.py` with an external solver), using Google Sheets (`google_sheets.py`), even an **online coding agent** that writes and executes code in a browser IDE (`online_coding_agent.py`).  

There’s also a **Jupyter Notebook** example [📓 `agent_browsing.ipynb`](https://github.com/browser-use/browser-use/blob/main/examples/notebook/agent_browsing.ipynb) which demonstrates an interactive session with the agent. You can run it step by step to see how the agent plans and executes actions. For a quick demo with a UI, you can run the provided Gradio app (`examples/ui/gradio_demo.py`) to get a simple web interface for issuing tasks to the agent.

## Advanced Usage

Once you have the basics down, **Browser Use** offers many configuration options and extension points to tailor the agent’s behavior:

- **Agent Settings & Customization:** The `Agent` class provides knobs to adjust its operation. For example, you can enable/disable vision (`use_vision=True/False`), limit the number of steps (`max_steps`), or save transcripts (`save_conversation_path="logs/run.txt"`). You can also modify the system prompt that guides the agent – either by providing an override or using a custom prompt clas ([Agent Settings - Browser Use](https://docs.browser-use.com/customize/agent-settings#:~:text=,System%20Prompt%20for%20customization%20options))】 – to influence how the AI approaches tasks (e.g. adding company-specific instructions or formatting requirements). The agent’s reasoning process and memory management can be tuned via these settings (see the [documentation on Agent Settings](https://docs.browser-use.com/customize/agent-settings) for all options).  

- **Controller and Custom Actions:** The `Controller` is the component that defines what *actions* (tools) the agent can use. By default, it comes pre-loaded with all the essential browser actions (like clicking elements, navigating to URLs, typing text, scrolling, etc.), so you usually don’t need to configure it for basic task ([Custom Functions - Browser Use](https://docs.browser-use.com/customize/custom-functions#:~:text=return%20ActionResult))】. However, you can **extend** it with custom actions using the `@controller.action` decorator. For example, you could define an action to download a file via an API or to ask for human input mid-run:
  
  ```python
  from browser_use import Controller, ActionResult, Browser
  controller = Controller()

  @controller.action("Ask user for info")
  def ask_user(prompt: str) -> str:
      answer = input(f"{prompt}\n> ")
      return ActionResult(extracted_content=answer)

  @controller.action("Open website")
  async def open_site(url: str, browser: Browser):
      page = browser.get_current_page()
      await page.goto(url)
      return ActionResult(extracted_content="opened")
  ```

  Here we added a synchronous action that pauses and asks the user for input, and an asynchronous action that navigates the browser to a given URL (using the `browser` object). By passing this custom `controller` to the `Agent` (`Agent(..., controller=controller)`), the agent can now use these new actions in addition to the defaults. Custom actions are powerful for integrating external APIs, handling downloads, or any specialized logic – essentially serving as additional tools the LLM can invok ([Build an AI Browser Agent With LLMs, Playwright, Browser-Use](https://dzone.com/articles/build-ai-browser-agent-llms-playwright-browser-use#:~:text=Custom%20Actions))】. You can also **disable** or remove specific default actions via `Controller(exclude_actions=[...])` if you want to restrict the agent (for safety or focus).

- **File Uploads and Downloads:** Dealing with files is a common need in browser automation. **Browser Use** supports file uploads by allowing you to specify which local files the agent can access. When creating an agent, use the `available_file_paths` parameter to provide a list of file paths that the agent is allowed to attach (this acts as a sandbox, so the LLM can only use files you explicitly list). For example: `agent = Agent(task=..., llm=..., available_file_paths=["/path/to/resume.pdf"])`. Then, if a file input element is encountered on a page, the agent can choose one of these paths to upload (based on task context). For downloading files, Playwright can save files to disk if the browser context is configured appropriately. You may need to adjust the `BrowserConfig` – e.g., `BrowserConfig().new_context_config.accept_downloads = True` – to enable download ([how to download a file? · Issue #358 · browser-use/browser-use · GitHub](https://github.com/browser-use/browser-use/issues/358#:~:text=,browser_config.new_context_config.downloads_path%20%3D%20DOWNLOADS_DIR)) ([how to download a file? · Issue #358 · browser-use/browser-use · GitHub](https://github.com/browser-use/browser-use/issues/358#:~:text=,browser_config.new_context_config.downloads_path%20%3D%20DOWNLOADS_DIR))】. The downloaded files will be saved (by default in a temporary directory or as configured), but note that the agent’s LLM itself doesn’t automatically “open” or read the downloaded file. If you want the agent to utilize the file, you might follow up with an action to read it (if it’s a readable format) or implement a custom action (e.g., using Python `requests` as shown in an issue discussion) to fetch the file conten ([how to download a file? · Issue #358 · browser-use/browser-use · GitHub](https://github.com/browser-use/browser-use/issues/358#:~:text=%40controller,111111111111111111111111111111111111111111111111111111111111111111%2011111111111%29%20try%3A%20import%20requests)) ([how to download a file? · Issue #358 · browser-use/browser-use · GitHub](https://github.com/browser-use/browser-use/issues/358#:~:text=,write%28chunk))】. File download support is continually improving – currently it may require a bit of custom handling as shown.

- **Persistent Sessions (Browser Reuse):** By default, each `Agent.run()` will launch a fresh browser context to ensure a clean slate. If you need to maintain state (cookies, localStorage, etc.) across runs – for example, staying logged in to a site for a series of tasks – you can reuse a browser or context. **Browser Use** allows you to provide an existing `Browser` instance or a specific Playwright `BrowserContext` to the agen ([Agent Settings - Browser Use](https://docs.browser-use.com/customize/agent-settings#:~:text=Reuse%20Existing%20Browser%20Context)) ([Agent Settings - Browser Use](https://docs.browser-use.com/customize/agent-settings#:~:text=,Use%20persistent%20context))】. This way, multiple tasks can run in the same session. For instance:
  
  ```python
  from browser_use import Browser, Agent
  browser = Browser()  # launches a browser (with default config)
  agent1 = Agent(task="Login to example.com", llm=llm, browser=browser)
  await agent1.run()
  # The browser (and its context with login cookies) remains open.
  agent2 = Agent(task="Perform some action on example.com after login", llm=llm, browser=browser)
  await agent2.run()
  await browser.close()
  ```
  
  In this pattern, `agent2` will find itself already logged in because it’s using the same browser state as `agent1`. You can also manage contexts directly via Playwright (e.g., `browser.new_context()` with persistent storage) if finer control is neede ([Agent Settings - Browser Use](https://docs.browser-use.com/customize/agent-settings#:~:text=,Persistent%20Browser%20for%20more%20details)) ([Agent Settings - Browser Use](https://docs.browser-use.com/customize/agent-settings#:~:text=agent%20%3D%20Agent,Use%20persistent%20context))】. Remember to close the browser manually when reusing it, as the agent won’t auto-close a browser it didn’t launch.

- **Agent History and Logging:** After the agent finishes, you receive an **`AgentHistoryList`** object, which contains the step-by-step record of the run. You can use this for debugging or audit. For example, `history.action_names()` gives the list of actions taken, `history.urls()` the pages visited, `history.screenshots()` the screenshot image paths, and `history.errors()` any errors encountere ([Agent Settings - Browser Use](https://docs.browser-use.com/customize/agent-settings#:~:text=,run))】. You can also retrieve the agent’s thought process (the model’s reasoning messages) via `history.model_thoughts()`, or the final result content via `history.final_result( ([Agent Settings - Browser Use](https://docs.browser-use.com/customize/agent-settings#:~:text=The%20,methods%20to%20analyze%20the%20execution))】`. This rich history makes it easier to understand what the AI is doing at each step and to create reproducible scripts or reports. If you enabled `save_conversation_path`, the entire conversation (prompts and model outputs) is also saved to a file for review. Logging is configurable (the package uses Python’s logging library), and you can adjust verbosity or direct logs to a file if needed. 

For more advanced topics – such as customizing the system prompt template, integrating memory or vector DB for long tasks, or telemetry and analytics – refer to the [official documentation](https://docs.browser-use.com/) which covers these in depth. Browser Use is an active project (see the Roadmap in the docs for upcoming features like better DOM handling, improved planning, etc.), so you can expect additional capabilities over time.

## Supported Browsers and Platforms

Browser Use relies on **Playwright**, which supports automating **Chromium**, **Firefox**, and **WebKit** browsers. This means you can run your agents on Chrome/Edge, Firefox, or Safari engines, including headless mode (no GUI) or headed mode (visible browser ([Browsers | Playwright Python](https://playwright.dev/python/docs/browsers#:~:text=Playwright%20can%20run%20tests%20on,desktop%2C%20tablet%20and%20mobile%20devices))】. Playwright abstracts these differences with a single API, so most of the time you don’t need to worry about the specific browser – just install the one you want to use. By default, installing `browser-use` and running `playwright install chromium` is enough to get started with a headless Chromium. 

All major operating systems are supported (Windows, Linux, macOS ([Browsers | Playwright Python](https://playwright.dev/python/docs/browsers#:~:text=Playwright%20can%20run%20tests%20on,desktop%2C%20tablet%20and%20mobile%20devices))】. If you are running on Linux, ensure that [Playwright’s dependencies](https://playwright.dev/python/docs/cli#install-system-dependencies) are installed (you can run `playwright install-deps` for convenienc ([Browsers | Playwright Python](https://playwright.dev/python/docs/browsers#:~:text=System%20dependencies%20can%20get%20installed,is%20useful%20for%20CI%20environments))】). The package is designed to work both in local environments and in cloud or CI environments (where a virtual display may be needed for headed mode). 

*Note:* When running in headless mode, some websites might detect automation or behave differently. If you encounter issues, you can try `headless=False` in the `BrowserConfig` to run with a visible browser, or set `disable_security=True` to bypass certain browser security restrictions (e.g. for iframes ([Browser Settings - Browser Use](https://docs.browser-use.com/customize/browser-settings#:~:text=,websites%20may%20detect%20headless%20mode)) ([Browser Settings - Browser Use](https://docs.browser-use.com/customize/browser-settings#:~:text=,especially%20when%20visiting%20untrusted%20websites))】. Use such settings cautiously, especially with untrusted sites.

## Supported LLMs and Providers

**Browser Use** is model-agnostic as it delegates language understanding and planning to LangChain’s chat models interface. Any LLM that supports “function calling” (i.e. the ability to decide on tool usage) can potentially work. The project documentation highlights popular choices and how to configure the ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=Supported%20Models)) ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=OpenAI))】:

- **OpenAI GPT-4 / GPT-3.5:** Recommended for best results. Use `ChatOpenAI` from LangChain. Models like `"gpt-4"` (or the function-call enabled variant `"gpt-4-0613"` which Browser Use refers to as *GPT-4o*) work wel ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=OpenAI%E2%80%99s%20GPT,for%20best%20performance))】. Set your `OPENAI_API_KEY` and initialize `ChatOpenAI(model="gpt-4", temperature=0)` as shown above. *(Requires an OpenAI API account and access to the GPT-4 model.)*

- **Anthropic Claude:** Supported via LangChain’s `ChatAnthropic`. For example, `ChatAnthropic(model="claude-2", ... )`. Set `ANTHROPIC_API_KEY` in your environmen ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=And%20add%20the%20variable%3A))】. Claude can handle similar tasks, though it may have input size limits to consider.

- **Google Gemini (PaLM 2):** Supported via `ChatGoogleGenerativeAI` (LangChain integration for Google’s PaLM API). You’ll need a Google Cloud API key with access to the Generative AI (Gemini) service. Set `GEMINI_API_KEY ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=api_key%20%3D%20os.getenv%28))】 and instantiate with `ChatGoogleGenerativeAI(model="gemini-2.0-***", ...)` as per Google’s specs. (You may refer to Google’s [Gemini API docs](https://ai.google.dev/gemini-api/docs) for model IDs and usage details. At the time of writing, `gemini-2.0` models are in preview and free to us ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=We%20have%20yet%20to%20test,the%20community%20because%20it%20is))】.)

- **Azure OpenAI:** Use LangChain’s `AzureChatOpenAI` with your Azure endpoint and key. Browser Use supports it as well – just configure the environment variables that LangChain expects (e.g. `AZURE_OPENAI_KEY`, `AZURE_OPENAI_ENDPOINT`, etc. ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=Azure%20OpenAI)) ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=from%20langchain_openai%20import%20AzureChatOpenAI%20from,pydantic%20import%20SecretStr%20import%20os))】.

- **Local Models:** You can integrate local LLMs (like LLaMA 2 or others) via LangChain wrappers (such as HuggingFace pipelines or `ChatOllama` for an Ollama serve ([Playwright Chromium Executable Missing or Version Mismatch in ...](https://stackoverflow.com/questions/79530677/playwright-chromium-executable-missing-or-version-mismatch-in-python-vscode#:~:text=,from%20pydantic%20import%20SecretStr))】). The docs note that smaller models *can* work, but may sometimes produce outputs that don’t follow the expected format for actions, leading to error ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=We%20have%20yet%20to%20test,will%20improve%20significantly%20this%20year))】. Use local models with caution and expect to do some fine-tuning. The good news is that the framework is the same, so swapping in a different model is as easy as changing the LangChain class and providing the right interface (and hardware, if needed, for local inference).

Make sure to read the [LangChain documentation on chat models](https://python.langchain.com/docs/modules/model_io/models/chat) for any provider-specific setup (some require additional environment variables or config). All models require API keys or endpoints – if those are missing or incorrect, the agent will fail to start the conversation.

## Limitations and Tips

- **Not a Web Crawler:** Browser Use operates by actually rendering pages in a browser and is guided by an LLM. It’s not as fast or straightforward as a traditional web scraper on simple tasks. Expect it to be relatively resource-intensive (it’s running a browser and an AI model). For tasks where an official API or direct HTTP calls exist, those might be more efficient. Use Browser Use when you need true **end-to-end automation of a web UI** or when no simpler alternative is available (e.g., interacting with a site protected by Cloudflare or performing complex multi-step processes).

- **LLM Limitations:** The intelligence of the agent is bounded by the underlying LLM. If the model misinterprets the page or the instruction, the agent might take suboptimal actions or fail to complete the task. Increasing the model capability (GPT-4 over GPT-3.5, etc.) generally improves reliabilit ([Supported Models - Browser Use](https://docs.browser-use.com/customize/supported-models#:~:text=We%20have%20yet%20to%20test,will%20improve%20significantly%20this%20year))】. Giving clear, structured tasks (perhaps with sub-goals enumerated) in the `task` prompt can also help. **Browser Use** tries to mitigate some LLM issues (it validates the tool/action JSON outputs from the model and can retry on parsing errors), but it’s not foolproof. Always test your agent on the target websites and be prepared to tweak the prompt or add custom actions for tricky parts.

- **Website Compatibility:** Most modern websites work out-of-the-box, but very complex web apps (heavy SPAs with lots of asynchronous content) might challenge the agent. The agent does not have human-like intuition; it relies on the DOM snapshot and optional vision to understand the page. If an element is hidden or requires hovering, or if an action triggers a background AJAX call that the agent isn’t aware of, you may need to guide it (via task prompt or additional logic). You can often solve such issues by breaking the task into smaller steps or by using custom actions (e.g., an action that waits for a certain condition, or directly calls a JavaScript snippet via Playwright).

- **File Handling:** As noted, file downloads require enabling in the browser context and won’t automatically be read by the agent. File uploads are restricted to given paths for security. Be mindful of these when designing tasks (the agent won’t magically have access to your entire filesystem – you must grant specific file paths).

- **Security Considerations:** Running an AI agent that can browse the web and click links comes with risks. **Always review the tasks you give** to ensure they don’t cause unintended actions (like buying something or deleting data). The default system prompt instructs the agent not to do anything harmful, but it’s not a guarantee. It’s wise to supervise runs or use read-only modes if possible for critical scenarios. Also, avoid exposing sensitive data: if you do need to provide credentials or API keys for the agent to use on a website, know that these might end up in the prompt (and thus be seen by the LLM provider). Use test accounts when possible, or use the `sensitive_data` feature (which can mask certain substrings in the prompt for privacy).

## Community and Resources

- **Documentation:** See the official [Browser Use Docs 📖](https://docs.browser-use.com/) for detailed guides on each component, troubleshooting, and the latest updates. The docs cover additional topics like telemetry, advanced prompt customization, and contributing guidelines.
- **Examples Repository:** Beyond the built-in examples folder, you can find community-contributed recipes and projects on the Browser Use GitHub or linked in the Discord. The maintainers occasionally post new use-case scripts and notebooks demonstrating new features.
- **Discord Community:** Join the [Browser Use Discord](https://link.browser-use.com) to ask questions, share your agents, and see what others are building. It’s a great place to get support or inspiration for complex tasks.
- **Development Status:** Browser Use is an open-source project (MIT licensed) with an active development roadmap. You can check out the Issues and Discussions on GitHub for known issues or to file bug reports/feature requests. Contributions are welcome – if you have an improvement or a new action to add, feel free to open a pull request.

---

*Browser Use aims to make the web as accessible to AI agents as APIs a ([Browser Use: An open-source AI agent to automate web-based tasks | InfoWorld](https://www.infoworld.com/article/3812644/browser-use-an-open-source-ai-agent-to-automate-web-based-tasks.html#:~:text=in%20digital%20interactions,step%20workflows))7】. By leveraging the power of LLMs and a robust browser automation backend, it opens up countless possibilities for automating online tasks. Whether you want to build a personal web assistant, automate data entry, test webapps with AI, or create an agent that explores the internet, Browser Use provides the tools to get started.*