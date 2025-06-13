import os
os.environ["OPIK_URL_OVERRIDE"] = "http://localhost:5173/api"
# Initialize the tracer
from opik.integrations.langchain import OpikTracer
opik_tracer = OpikTracer()
from langchain_openai import ChatOpenAI
# Create the LLM Chain using LangChain
import opik

client = opik.Opik()

# Get the most recent version of a prompt
prompt = client.get_prompt(name="call scoring")
print(prompt.metadata)
formatted_prompt = prompt.format(transcript="thanks for calling medical X how can I help you james", criteria="Proper Introduction")
llm = ChatOpenAI(
    model="gpt-4o-mini",
    base_url="http://localhost:4000/v1",
    api_key="sk-anything",
    callbacks=[opik_tracer]
)

response = llm.invoke(formatted_prompt)
print(response)
