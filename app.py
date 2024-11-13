import autogen
import os
from dotenv import load_dotenv

load_dotenv()

config_list = [
    {
        'model': 'gpt-4',
        'api_key': os.environ['OPENAI_API_KEY']
    }
]

llm_config = {
    # 'request_timeout': 600,
    'seed': 42,
    'config_list': config_list,
    'temperature': 0
}

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="TERMINATE",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, if not solved yet."""
)

user_proxy.initiate_chat(
    assistant,
    message=input()
)

