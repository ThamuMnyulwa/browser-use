import click
from browser_use_package import Agent, Browser, BrowserConfig


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Command-line interface for browser-use."""
    pass


@cli.command()
def version():
    """Show the version of browser-use"""
    click.echo("browser-use version 0.1.0")


@cli.command()
@click.argument("task")
@click.option("--headless", is_flag=True, help="Run the browser in headless mode.")
@click.option("--timeout", type=int, default=30, help="Browser timeout in seconds.")
@click.option("--user-agent", help="Custom user agent string.")
def run(task: str, headless: bool, timeout: int, user_agent: str | None):
    """Run a browser task."""
    try:
        config = BrowserConfig(
            headless=headless,
            timeout=timeout,
            user_agent=user_agent,
        )
        agent = Agent(task=task, browser_config=config)
        result = agent.run()
        print(f"Result: {result['action_results']}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    cli()
