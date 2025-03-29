from zhipuai import ZhipuAI

# Load extracted text
with open("extracted_text.txt", "r", encoding="utf-8") as f:
    file_content = f.read()

# Initialize client
client = ZhipuAI(api_key="dc96c4d8b4854fca88715d087e6516e2.3FOmstogBD8Fht2A")

# Build message prompt
message = (
    "Please extract the following from this paper:\n"
    "- Research Problem\n"
    "- Proposed Method\n"
    "- Datasets Used\n"
    "- Benchmark Tasks (if any)\n"
    "- Code Links (if any)\n"
    "- Key Results (in metrics)\n\n"
    f"{file_content}"
)

# Send to GLM-4-Flash
response = client.chat.completions.create(
    model="glm-4-long",
    messages=[{"role": "user", "content": message}]
)

# Print result
print("\n✅ Extracted Paper Information:\n")
print(response.choices[0].message.content)
