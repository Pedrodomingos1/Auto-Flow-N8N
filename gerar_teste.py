import os

def criar_arquivo_teste():
    pasta = "pasta_monitorada"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    nome_arquivo = "2024-12-25_09-00_Teste de Automacao.jpg"
    caminho = os.path.join(pasta, nome_arquivo)
    
    print(f"📂 Criando arquivo simulado: {caminho}")
    
    with open(caminho, "wb") as f:
        f.write(b"conteudo binario de teste")
    
    print("✅ Arquivo criado! Verifique o terminal do 'monitoramento.py'.")

if __name__ == "__main__":
    criar_arquivo_teste()