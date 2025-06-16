import os
from openai import OpenAI
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()


client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 替换为您的 API Key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# model_id = "deepseek-r1"
model_id = "qwen3-235b-a22b"

enable_thinking = False
if model_id == "deepseek-r1":
    enable_thinking = True

completion = client.chat.completions.create(
    model=model_id,
    messages=[
        {'role': 'user', 'content': '9.9 和 9.11 谁大'}
    ],
    extra_body={"enable_thinking": enable_thinking}
)

if model_id == "deepseek-r1":
    print(" 思考过程：")
    print(completion.choices[0].message.reasoning_content)

print(" 最终答案：")
print(completion.choices[0].message.content)
