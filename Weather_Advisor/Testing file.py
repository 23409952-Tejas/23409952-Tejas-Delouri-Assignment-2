from ollama import Client

client = Client(
    host="https://ollama.com",
    headers={'Authorization': '6b7a9b80169a44cf92b1186fbbb37cd3.n_l-4T3p_Vo8IDtoBkR8jv4d'}
)

messages = [
  {
    'role': 'user',
    'content': 'What is your capacity to help me in my daily tasks?',
  },
]

for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
  print(part['message']['content'], end='', flush=True)