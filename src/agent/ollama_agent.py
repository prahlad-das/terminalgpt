from langchain.agents import create_agent
from langchain_ollama import ChatOllama
import click

class ChatOllamaAgent():
    def __init__(self, model_name: str = "gpt-oss:20b"):
        super().__init__()
        self.model = ChatOllama(model=model_name, temperature=0.7)
        self.agent = create_agent(model=self.model, system_prompt="You are a helpful MacOS terminal assistant who generates commands for the human message. Generate MacOS terminal commands in string without any 'bash' prefix. Return empty string if no command is generated.",)
        

    
    def run(self, query) -> str:
        click.echo("Agent is generating the command...")
        result = self.agent.invoke({"messages": [{"role": "user", "content": query}]})
        
        return result['messages'][1].content
    
if __name__ == "__main__":
    agent = ChatOllamaAgent("gpt-oss:20b")
    response = agent.run("list all files in the home directory")
    print(response)