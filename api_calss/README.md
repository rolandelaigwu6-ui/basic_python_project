# Gemini API setup and progress

This guide records the Python Gemini API setup from creating a key through saving a model response to a text file. The project also has a TypeScript example; the steps below use Python because that is the version we have run successfully.

## 1. Create a Gemini API key in Google AI Studio

1. Open [Google AI Studio API keys](https://aistudio.google.com/apikey) and sign in.
2. Create an API key and copy it.
3. Keep the key private. Do not paste it into source code, commit it to Git, or share it in chat.

The Gemini API has a free tier for some models, with usage limits. Google says free-tier content may be used to improve its products, so avoid sending sensitive or private data. Check [Google's current pricing and free-tier details](https://ai.google.dev/gemini-api/docs/pricing) before relying on a model or quota.

## 2. Create and activate a Python virtual environment

Run these commands from the project root (`~/basic_python_project`):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

The `(.venv)` marker in the terminal prompt means the virtual environment is active. It keeps this project's Python packages separate from the system Python installation.

## 3. Install the Google GenAI SDK

```bash
python -m pip install --upgrade pip
python -m pip install google-genai
```

An SDK (Software Development Kit) is a library that handles much of the work of communicating with an API. Here, `google-genai` provides the Python client used by `main.py`.

## 4. Provide the API key to Python

In the same terminal where you will run the script, enter:

```bash
read -s GEMINI_API_KEY
```

Paste your key when the terminal waits, then press **Enter**. The input is hidden. Next, export it so programs launched from this terminal can read it:

```bash
export GEMINI_API_KEY
```

Check that a value is set without printing the key:

```bash
test -n "$GEMINI_API_KEY" && echo "API key is set"
```

The key is available only in this terminal session. In a new terminal, enter it again. Never use `echo "$GEMINI_API_KEY"` because that displays the secret.

## 5. Choose the model and run the first API call

The script reads `GEMINI_MODEL` if it is set. Otherwise, `main.py` defaults to `gemini-3.8-flash`. Our first request reached Google but returned `503 UNAVAILABLE` because that model was experiencing high demand. This was a temporary service response, not a Python syntax error or missing key.

We selected the lighter model that then returned a successful response:

```bash
export GEMINI_MODEL="gemini-3.1-flash-lite"
python api_calss/main.py
```

The model selection is also only set for this terminal session. If a request returns `503`, the model may be busy; waiting and retrying, or trying another currently available model, can help. Free-tier availability and limits can vary.

## 6. What the Python API call does

The key parts of `api_calss/main.py` are:

```python
import os
from google import genai

client = genai.Client()
MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

response = client.models.generate_content(
    model=MODEL,
    contents="What is a neural network in one sentence?",
)

print(response.text)
```

- `genai.Client()` creates the SDK client. It reads `GEMINI_API_KEY` from the environment.
- `MODEL` selects the model from `GEMINI_MODEL`, or uses its fallback if that variable is unset.
- `generate_content(...)` sends the prompt to the Gemini API.
- `response.text` is the generated text returned by the SDK.

The SDK sends an HTTP `POST` request under the hood. In a raw HTTP request, the model name and `:generateContent` operation appear in the URL, the key is sent in the `x-goog-api-key` header, and the prompt is sent as JSON in the request body. See Google's [text-generation and REST examples](https://ai.google.dev/gemini-api/docs/generate-content/text-generation).

## 7. Save the answer to `api.txt`

The current Python script writes the response to a file instead of printing the full answer:

```python
# print(response.text)
with open("api.txt", "a") as file:
    content = file.write(response.text)
    print("write to api file sucessfully")
```

- `open("api.txt", "a")` opens the file in append mode, creating it if needed. Each run adds the new answer to the end.
- `file.write(response.text)` writes Gemini's answer. The returned character count is assigned to `content`, but that value is not currently used.
- The short status message is printed in the terminal. The full answer goes into the file.
- Because the path is relative, `api.txt` is created in the directory from which you run Python. Running the command above from the project root writes to `~/basic_python_project/api.txt`.
- To replace the file's contents on every run, change append mode `"a"` to write mode `"w"`. To keep answers separate, add a newline after each response.

At the current stage, the prompt in `main.py` says “explain what every code here does” but does not include any code. Gemini therefore asked for the code to explain. Put the code you want explained into the `contents` string, for example:

```python
contents="Explain this code: print('Hello, world!')"
```

Then run the script again and inspect `api.txt`.

## Common issues we encountered

- **`No API key was provided`:** the key had not been read/exported correctly. Use the exact variable name `GEMINI_API_KEY`, then check it with the safe `test -n` command above.
- **`503 UNAVAILABLE`:** Google reported temporary high demand for the selected model. Trying `gemini-3.1-flash-lite` worked in our run.
- **Command typos:** run `python api_calss/main.py` to launch the script. `read` is only for entering the hidden API key; it is not part of the Python run command.

## TypeScript example

`api_call.tsx` uses the TypeScript SDK, which is separate from the Python SDK. Install it from the project root with:

```bash
npm install @google/genai
```

It also needs `GEMINI_API_KEY` in the environment. The TypeScript file is included as an example; the successful run recorded above was the Python script.

## Official references

- [Create and manage Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key)
- [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/get-started)
- [Gemini API pricing and free tier](https://ai.google.dev/gemini-api/docs/pricing)
- [Text generation and raw REST request](https://ai.google.dev/gemini-api/docs/generate-content/text-generation)
