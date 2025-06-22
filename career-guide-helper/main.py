import os
from dotenv import load_dotenv #type: ignore
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel #type: ignore


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

provider = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  
      
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,

)

agent = Agent(
    name="Career Helper",
    model=model,
    instructions="You are a Career Helper Agent.Guide users in career-related areas only: resume building, job search, interview prep, skill development, and career transitions.Respond with empathy, clarity, and encouragement. Ask follow-up questions if needed.Do not answer unrelated questions (e.g. health, food). Gently redirect users to career topics",
   
)

user_prompt= input("Enter your career-related question: ")
response = Runner.run_sync(agent, user_prompt)
print(f"Agent Response: {response.final_output}")



