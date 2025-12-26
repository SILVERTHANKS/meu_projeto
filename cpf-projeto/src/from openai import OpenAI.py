from openai import OpenAI
cli = OpenAI(api_key="SUA_CHAVE")
print(cli.models.list())

