import requests

try:
    conexao = requests.get("https://google.com", timeout=5)
    conexao.raise_for_status()  # força erro se status != 200

except requests.exceptions.ConnectionError:
    print("❌ Erro de conexão com a internet")

except requests.exceptions.Timeout:
    print("⏰ Tempo de conexão esgotado")

except requests.exceptions.HTTPError as erro:
    print(f"⚠️ Erro HTTP: {erro}")

except Exception as erro:
    print(f"❌ Erro inesperado: {erro}")

else:
    print(f"✅ Conexão feita com sucesso: {conexao.status_code}")

finally:
    print("🔚 Fim da verificação")
