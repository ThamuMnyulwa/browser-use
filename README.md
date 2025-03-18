# browser-use
Repo investigating browser use

**Examples**:

[0] Log onto twitter, use Grok to make an image. Download the image then upload the image into ... via the browser.

[1] Log onto .... download a picture then upload the picture onto .....

[2] Log onto Easy Speak (from Toastmasters) and download an agenda (pdf). Upload the agenda onto ....

**Use:**
Let me analyze what's happening based on the more detailed error messages you've provided.

The problem is that you're trying to install the `dotenv` package, but what you actually need is `python-dotenv` which is different. I notice from your previous output that `python-dotenv` is already listed as one of the packages installed by `uv sync`.

Here's what I recommend doing:

1. Python from your virtual environment:

```bash
source .venv/bin/activate
```

2. Run the login command:

```bash
python -m browser_use login
```

You could also try running one of the example scripts to see if they work:

```bash
.venv/bin/python examples/simple.py
```

The most reliable approach would be:

```bash
uv run python -m browser_use login
```

This should use the Python interpreter managed by UV along with all the dependencies that were correctly installed during your `uv sync` command.

Resources:

[1] [Github browser-use](https://github.com/browser-use/browser-use)
