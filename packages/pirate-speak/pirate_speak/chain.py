import os
from dotenv import load_dotenv
from langchain.chat_models import ChatAnthropic
from langchain.prompts import ChatPromptTemplate

load_dotenv()

anthropic_Api_Key: str = os.environ["ANTHROPIC_API_KEY"]

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Translate user input into pirate speak",
        ),
        ("human", "{text}"),
    ]
)
_model = ChatAnthropic(anthropic_api_key=anthropic_Api_Key)

# if you update this, you MUST also update ../pyproject.toml
# with the new `tool.langserve.export_attr`
chain = _prompt | _model
