from agents import Agent, Runner
import traceback

agent = Agent(name="Assistant", instructions="You are a helpful assistant")
try:
    result = Runner.run_sync(agent, "What is the capital of France?")
    print(result.final_output)
except Exception as e:
    print("Ocurrio un error".join(traceback.format_exception(e)))

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.