from agents import Agent, Runner
from connection import config

translater = Agent(
    name = 'Translator Agent',
    instructions= 
    """You are a translator agent. Your job is to translate user query as per their request."""
)

response = Runner.run_sync(
    starting_agent = translater,
    input = 'Translate in english, french, german, spanish, and russian "agar aap mehnat karoge toh kamyab ho jaoge"..',
    run_config = config
    )

print(response.final_output)
