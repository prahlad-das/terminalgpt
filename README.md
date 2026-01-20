# TerminalAgent ✅

A small macOS CLI tool that generates and (optionally) executes Terminal commands using an Ollama LLM and (optional) voice input.

- Uses LangChain + langchain_ollama's `ChatOllama` to generate Mac terminal commands from plain-language prompts.
- Provides a simple CLI entry point `terminalagent` (installed as a console script).
- Supports spoken prompts when invoked without an argument (uses the microphone + Google Speech Recognition via the `speech_recognition` package).

---

## 🔧 Features

- Generate macOS Terminal commands from natural-language queries.
- Record voice input and transcribe it to text when no query is passed.
- Show the generated command and ask for confirmation before executing it in the Terminal.

---

## 🚀 Quick start

Requirements:
- macOS (the tool uses AppleScript to run commands in Terminal.app)
- Python 3.10+ (recommended)
- Ollama installed with a compatible model available (the code defaults to `gpt-oss:20b`)

Installation (development / quick):

```bash
# From project root
python -m pip install -r requirements.txt
python -m pip install -e .
```

Or to install the package for use:

```bash
python -m pip install .
```

Note: `pyaudio` may require `portaudio` on macOS:

```bash
brew install portaudio
python -m pip install pyaudio
```

---

## Usage

Generate a command from a text prompt:

```bash
terminalagent "list all files in my home directory"
```

Record a voice prompt (invoke without arguments):

```bash
terminalagent
# Then speak when prompted; the tool will transcribe and pass the text to the LLM
```

Behavior:
- The generated command is printed in green.
- You are prompted to confirm execution; if you accept, Terminal.app will run the command using AppleScript.

**Security warning**: this tool executes commands on your machine. Carefully review generated commands before confirming execution.

---

## ⚙️ How it works (implementation notes)

- CLI: `src/cli/agent_cli.py` (console script `terminalagent`).
- LLM: `src/agent/ollama_agent.py` — uses `langchain_ollama.ChatOllama` and LangChain `create_agent` with a system prompt that instructs the model to return macOS command strings (no `bash` prefix).
- Audio: `src/audio/recorder.py` — wraps `speech_recognition` (Google recognizer) and `pyaudio` to capture and transcribe microphone input.
- Execution: `agent_cli` uses `osascript` to send the generated command to Terminal.app.

Configuration:
- The default model name is `gpt-oss:20b`. To change models, update the `model_name` argument when creating `ChatOllamaAgent` in `src/cli/agent_cli.py` or `src/agent/ollama_agent.py`.

---

## 🐛 Troubleshooting & Tips

- If microphone capture fails or `pyaudio` installation fails, ensure `portaudio` is installed and that your Python environment has access to audio devices.
- If transcription fails, you may see messages from `speech_recognition`; check network connectivity (Google recognizer) or replace with a different recognizer if required.
- If the model fails to generate meaningful commands, try a different Ollama model or lower the temperature in `ChatOllama` instantiation.
- If AppleScript execution does not work, check macOS Automation and Accessibility permissions for Terminal or the Python interpreter.

---

## 🧪 Development

- Tests live under `tests/` (add tests for new features).
- Run tests with `pytest`.
- Use `python -m pip install -e .` to work on the package in editable mode.

---

## 🤝 Contributing

Contributions are welcome — open an issue or a pull request. Follow the usual workflow:

1. Fork the repo
2. Create a branch for your change
3. Add tests where appropriate
4. Open a PR describing your change

---

## 📄 License

This project is licensed under the terms in `LICENSE`.

---

If you find a bug or want an improvement (e.g., additional models, non-Google transcription backing, or a `--model` CLI flag), please open an issue or PR. 💡

