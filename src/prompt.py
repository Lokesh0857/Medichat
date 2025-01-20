import ollama # type: ignore
from IPython.display import display,Markdown,clear_output
prompt = "what is Acne?"
response_stream= ollama.chat(
    model='llama3.2',
    messages = [{'role':'user', 'content': prompt}],
    stream=True  
)

streamed_response = ""
for token in response_stream:
    streamed_response += token['message']['content']
    clear_output(wait=True)
    display(Markdown(f"**LLM Response (Streaming ):**\n\n{streamed_response}"))