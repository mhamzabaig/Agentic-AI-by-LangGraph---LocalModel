from llama_cpp import Llama

# Path to your GGUF model
model_path = "claude2-alpaca-7b.Q4_K_M.gguf"

llm = Llama(model_path=model_path)

prompt = "Explain what is the differece between Corporation and a Simple Company."

output = llm(prompt=prompt, max_tokens=150)
print(output)
