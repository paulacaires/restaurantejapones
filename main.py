import os
from dotenv import load_dotenv
from supabase import create_client, Client 

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

try:
    response = supabase.table("cliente").select("*").execute()
    
    dados_clientes = response.data
    
    print("\n✅ Consulta SELECT * from CLIENTE realizada com sucesso!")
    print("-------------------------------------------------")
    
    # Verifica e imprime os dados
    if dados_clientes:
        print(f"Total de clientes encontrados: {len(dados_clientes)}")
        print("Exemplo de dados (primeiro cliente):")
        # Imprime o primeiro registro para visualização
        print(dados_clientes[0]) 
    else:
        print("Nenhum registro encontrado na tabela 'cliente'.")

except Exception as e:
    print(f"\n❌ ERRO ao executar a consulta: {e}")