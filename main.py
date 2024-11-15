from dotenv import load_dotenv
from langchain import hub
from langchain)experimental.agents import create_csv_agent
from langchain)openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool

load_dotenv()

def main():
    print("Start...")

    instructions = """
    You are an agent designed to write and execute Python code to anser questions.
    You have acces to a python REPL, which you can use to execute python code.
    If you get an error, debug your code and try again.
    Only use the output of your code to answer the questtion.
    You might know the answer without running any code, but you should still run the code to get the answer.
    If it does not seem like you can write code to answer the question, just return 'I do not know' as the answer.
    """

    base_prompt = hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)

    tools = [PythonREPLTool()]

    agent = create_react_agent(
        prompt=prompt,
        llm=ChatOpenAI(temperature=0, model="gpt-4-turbo"),
        tools=tools,    
    )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    agent_executor.invoke(
        input={
            "input": """
                generate and save in current working directory 2 QR codes thath point to www.google.com you have qrcodepackage installed already
            """
            }
    )

if __name__ =="__main__":
    main()
