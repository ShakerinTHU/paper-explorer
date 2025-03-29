from zhipuai import ZhipuAI

client = ZhipuAI(api_key="dc96c4d8b4854fca88715d087e6516e2.3FOmstogBD8Fht2A")

response = client.chat.completions.create(
    model="glm-4",
    messages=[{"role": "user", "content": "What is Streamlit?"}]
)

print(response.choices[0].message.content)
