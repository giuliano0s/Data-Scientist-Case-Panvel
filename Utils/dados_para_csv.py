import pandas as pd
import glob
import os

def converter_arquivos_para_csv_estruturado():
    """
    Converte arquivos .parquet e .xlsx na pasta 'Data' para .csv,
    salvando na subpasta 'Data/CSVs'.
    """
    pasta_origem = "Data"
    pasta_destino = os.path.join(pasta_origem, "CSVs")
    
    # Cria diretório de destino caso não exista
    os.makedirs(pasta_destino, exist_ok=True)
    
    # Busca arquivos dinamicamente
    arquivos_parquet = glob.glob(os.path.join(pasta_origem, '*.parquet'))
    arquivos_excel = glob.glob(os.path.join(pasta_origem, '*.xlsx'))
    
    # Unifica lista de arquivos
    todos_arquivos = arquivos_parquet + arquivos_excel
    
    if not todos_arquivos:
        print(f"Nenhum arquivo encontrado no diretório '{pasta_origem}'.")
        return

    print(f"Encontrados {len(todos_arquivos)} arquivo(s) para conversão.\n")

    for arquivo in todos_arquivos:
        # Extrai nome e extensão do arquivo
        nome_base = os.path.basename(arquivo)
        nome_sem_extensao, extensao = os.path.splitext(nome_base)
        novo_nome = f"{nome_sem_extensao}.csv"
        
        # Monta caminho final
        caminho_final = os.path.join(pasta_destino, novo_nome)
        
        try:
            print(f"Lendo: {nome_base}...")
            
            # Carrega dataframe conforme a extensão
            if extensao.lower() == '.parquet':
                df = pd.read_parquet(arquivo)
            elif extensao.lower() == '.xlsx':
                df = pd.read_excel(arquivo)
            
            print(f"Exportando para: {caminho_final}...")
            
            # Salva em formato csv
            df.to_csv(caminho_final, index=False, sep=';', encoding='utf-8')
            
            print("Sucesso!\n")
            
        except Exception as e:
            print(f"Erro ao converter {nome_base}: {e}\n")
            
    print("Pipeline de conversão finalizado")

if __name__ == "__main__":
    converter_arquivos_para_csv_estruturado()