import os
from openai import OpenAI

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

completion = client.chat.completions.create(
    # model="deepseek-r1:7b",  # 可按需更换模型名称                                                                         
    model="qwen3:8b",  # 可按需更换模型名称                                                                                 
    messages=[
        {'role': 'user', 'content': '9.9 和 9.11 谁大'}
    ]
)

print(" 最终答案：")
print(completion.choices[0].message.content)
