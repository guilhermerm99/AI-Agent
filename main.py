import os
import gradio as gr
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
set_tracing_disabled(disabled=True)

proxy_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
client = AsyncOpenAI(base_url=proxy_url, api_key=os.getenv("TOKEN"))

agent = Agent(
    model=(OpenAIChatCompletionsModel(model="gemini-1.5-flash", openai_client=client)),
    name="Instrutor", 
    instructions="""
Você é um agente com propósito de ajudar usuários a criar agentes de IA
Seja educado e prestativo

Caso o usuário se desvie da finalidade lembre a ele que você é uma ferramenta de estudo
""",
    tools=[]
    )

async def agent_handler(message, history):
    trimmed_history = [{"role": h["role"], "content": h["content"]} for h in history ]
    message_with_history = trimmed_history + [{"role":"user", "content": message}]
    execution = await Runner.run(agent, message_with_history)
    return execution.final_output

demo = gr.ChatInterface(
    agent_handler,
    type="messages",
    save_history=True,
)

if __name__ == "__main__":
    demo.launch(share=True)