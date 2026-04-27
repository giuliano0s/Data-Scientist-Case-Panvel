# Calibração de Metas Preditivas: Reduzindo o Burnout Organizacional

Este projeto resolve um problema crítico de gestão de vendas: a desconexão entre metas estipuladas e a capacidade real de entrega das filiais. Utilizando técnicas avançadas de Data Science e Machine Learning, o sistema migra de uma lógica de médias históricas estáticas para um motor de inferência estatística calibrado.

## Contexto do Problema

O modelo anterior apresentava falhas estruturais:
* **Burnout de Rede**: Aproximadamente 77% das filiais operavam com atingimento abaixo de 50%.
* **Desmotivação**: Metas inatingíveis geravam queda de esforço antes da metade do ciclo mensal.
* **Baixa Eficiência**: Apenas 8% das lojas atingiam a "Faixa Ideal" de Harvard (60% a 75% de atingimento).

## Solução Proposta

A solução utiliza **Gradient Boosting Models** para prever o faturamento real e aplica uma **Calibração via Z-Score** para ajustar a meta ao ponto de equilíbrio entre desafio e motivação.

### Fluxo de Desenvolvimento

1.  **Análise Exploratória (EDA)**: Identificação de padrões de sazonalidade semanal e tratamento de outliers (faturamento anômalo em 0.00019% dos tickets).
2.  **Engenharia de Features**:
    * Criação de **Lags** de 1, 7 e 8 dias (autocorrelação).
    * **Médias Móveis** de 7 e 30 dias.
    * **Clustering (K-Means)**: Agrupamento de 113 filiais em 5 clusters baseados em faturamento médio, volatilidade e peso do final de semana.
3.  **Modelagem**: Comparação entre Linear Regression, XGBoost e LightGBM.
4.  **Calibração Estatística**: Aplicação de Z-score negativo (média de -0.31) sobre a predição para posicionar a meta na zona de máximo engajamento.

## Resultados Obtidos (Holdout de Dezembro)

| Métrica | Modelo Anterior (Empírico) | Modelo Novo (Preditivo) | Impacto |
| :--- | :--- | :--- | :--- |
| Atingimento Médio | 31.4% | 55.7% | +77% de evolução |
| Lojas em Faixa Ideal (60-75%) | 9 | 40 | +344% de precisão |
| Lojas em Risco de Burnout (<50%) | 96 | 29 | -70% de redução |
| Regularidade de Batimento | 14.3% | 74.1% | Melhora drástica no moral |

## Arquitetura de Produção (MLOps)

O projeto foi desenhado para rodar na **Google Cloud Platform (GCP)**:
* **Data Warehouse**: BigQuery.
* **Orquestração**: Vertex AI Pipelines.
* **Feature Store**: Vertex AI Feature Store para gestão de Lags.
* **Serving**: Batch Prediction mensal para definição de metas de ciclo.

## Tecnologias Utilizadas

* **Linguagem**: Python 3.9+.
* **Manipulação de Dados**: Pandas, NumPy.
* **Machine Learning**: Scikit-learn, XGBoost, LightGBM.
* **Clustering**: K-Means.
* **Visualização**: Matplotlib, Seaborn, Plotly.

## Estrutura do Repositório

* `eda.ipynb`: Notebook de análise exploratória e limpeza.
* `feature_engineering.ipynb`: Criação de variáveis e clusterização de filiais.
* `modeling.ipynb`: Treinamento, tunagem de hiperparâmetros e validação.
* `calibracao_metas.pdf`: Documentação executiva da fundamentação teórica.

## Como Executar

1.  Clone o repositório:
    ```bash
    git clone https://github.com/Giuliano0s/Data-Scientist-Case-Panvel.git
    ```
2.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
3.  Execute os notebooks na ordem: `eda` > `feature_engineering` > `modeling`.

---
**Autor**: Giuliano  
**GitHub**: [Giuliano0s](https://github.com/Giuliano0s)  
**Especialidade**: Data Analytics & Cloud Infrastructure
