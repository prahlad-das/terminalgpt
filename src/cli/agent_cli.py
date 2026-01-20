import click
from audio.recorder import AudioRecorder
from agent.ollama_agent import ChatOllamaAgent

import os

@click.command('terminalagent', epilog='check readme in https://github.com/prahlad-das/terminalgpt for more details')
@click.argument('query', required=False)
def terminalagent(query):
    """
    Generate and execute MacOS terminal commands using Ollama LLM.
    If no QUERY is provided, audio input will be recorded and transcribed.

    \b
    Example usage:
    terminalgpt "list all files in the home directory"
    OR
    tg "list all files in the home directory"

    \b
    For audio input:
    terminalgpt (follow the instructions to speak your prompt)
    OR
    tg (follow the instructions to speak your prompt)
    """
    if not query:
        # no query provided
        audio_recorder = AudioRecorder()
        query = audio_recorder.run()
    
    command = ""
    if query:
        llm = ChatOllamaAgent(model_name="gpt-oss:20b")
        command = llm.run(query)
        click.secho(f"{command}", fg='green', bold=True)
    
    if command and click.confirm("Do you want to execute this command?"):
        script = f'tell application "Terminal" to do script "{command}" in front window'
        os.system(f"osascript -e '{script}'")

