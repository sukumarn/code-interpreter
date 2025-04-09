from dotenv import load_dotenv
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_experimental.tools import PythonREPLTool
#from langchain.agents import create_csv_agent
from langchain_experimental.agents.agent_toolkits import create_csv_agent



def csv_agent():
    csv_agent = create_csv_agent(
        llm=ChatOpenAI(temperature=0),
        path="episode_info.csv",
        verbose=True,
        allow_dangerous_code=True
    )
    csv_agent.invoke(
        input={"input": "HOW MANY COLUMNS ARE THERE IN THE CSV FILE?"}
        )

def main():
    # Your main function code here
    print("Hello, World!")

    
    instructions = """You are a Python code interpreter. I will provide you with a task, and your job is to write and execute Python code to solve it.

    Here's how you operate:

    1.  **Understand the Task:** Carefully read and understand the task I provide.  Identify the core objective and any specific constraints.
    2.  **Plan the Solution:** Before writing any code, outline a plan to solve the task.  Break down the problem into smaller, manageable steps. Think about the necessary Python libraries and functions you'll need.
    3.  **Write Python Code:**  Write Python code to execute your plan.  Focus on clarity, efficiency, and correctness. Use comments to explain your code.
    4.  **Execute Code with PythonREPLTool:**  Always use the `PythonREPLTool` to execute your code. This is crucial. Do not attempt to perform calculations or operations outside of the tool.
    5.  **Analyze Results:** After executing the code, carefully analyze the results.  Check for errors, unexpected outputs, or inconsistencies.
    6.  **Iterate and Refine:** If the results are not satisfactory, revise your code and re-execute it using the `PythonREPLTool`. Continue this process until you achieve the desired outcome.
    7. **Provide Final Answer:** Once you've successfully completed the task, present your final answer in a clear and concise manner.

    Always use the PythonREPL tool to execute the code.  Do not perform calculations outside of this tool. If a calculation is needed, write Python code to perform it.
    """
    base_prompt= hub.pull("langchain-ai/react-agent-template")
    prompt = base_prompt.partial(instructions=instructions)
    tools = [PythonREPLTool()]
    llm = ChatOpenAI(temperature=0)
    agent = create_react_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
                )
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke(input={
        "input":"Write a function to  generate the qr code."
    })
    # Example usage of the agent with a task


if __name__ == "__main__":
    load_dotenv()
    main()
    csv_agent()