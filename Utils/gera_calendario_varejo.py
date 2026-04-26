import os
import pandas as pd
import requests
from datetime import datetime

def gera_calendario_varejo():
    anos = [2025]
    lista_final = []

    for ano in anos:
        # Busca feriados nacionais oficiais via API
        url = f"https://brasilapi.com.br/api/feriados/v1/{ano}"
        resposta = requests.get(url)
        if resposta.status_code == 200:
            feriados = resposta.json()
            for f in feriados:
                lista_final.append({'data': f['date'], 'evento': f['name'], 'tipo': 'feriado_oficial'})

        # Cálculo algorítmico de datas comerciais móveis
        
        # Dia das Mães: Segundo domingo de maio
        maio = pd.date_range(start=f'{ano}-05-01', end=f'{ano}-05-31', freq='W-SUN')
        lista_final.append({'data': maio[1].strftime('%Y-%m-%d'), 'evento': 'Dia das Mães', 'tipo': 'comercial'})

        # Dia dos Pais: Segundo domingo de agosto
        agosto = pd.date_range(start=f'{ano}-08-01', end=f'{ano}-08-31', freq='W-SUN')
        lista_final.append({'data': agosto[1].strftime('%Y-%m-%d'), 'evento': 'Dia das Pais', 'tipo': 'comercial'})

        # Black Friday: Quarta sexta-feira de novembro
        novembro = pd.date_range(start=f'{ano}-11-01', end=f'{ano}-11-30', freq='W-FRI')
        lista_final.append({'data': novembro[3].strftime('%Y-%m-%d'), 'evento': 'Black Friday', 'tipo': 'comercial'})

        # Datas comerciais fixas
        lista_final.append({'data': f'{ano}-06-12', 'evento': 'Dia dos Namorados', 'tipo': 'comercial'})
        lista_final.append({'data': f'{ano}-03-15', 'evento': 'Dia do Consumidor', 'tipo': 'comercial'})

    df_calendario = pd.DataFrame(lista_final)
    df_calendario['data'] = pd.to_datetime(df_calendario['data'])
    
    # Ordenação e remoção de duplicatas (ex: Natal que é feriado e comercial)
    df_calendario = df_calendario.sort_values('data').drop_duplicates(subset=['data'], keep='first')

    # Exportação para o diretório de dados estruturados
    os.makedirs('./Data/CSVs', exist_ok=True)
    df_calendario.to_csv('./Data/CSVs/calendario_varejo.csv', index=False)
    
    print("Calendário gerado e salvo em ./Data/CSVs/calendario_automatico_varejo.csv")

if __name__ == "__main__":
    gera_calendario_varejo()