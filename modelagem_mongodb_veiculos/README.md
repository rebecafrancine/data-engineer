# Projeto: Ingestão e Normalização de Dados de Veículos com MongoDB

Este projeto simula a ingestão de dados automotivos a partir de um CSV, utilizando MongoDB como banco de dados principal e Python para transformação e normalização dos dados.

## Estrutura de Entidades:
- **proprietarios**: um documento por CPF
- **veiculos**: um documento por veículo, referenciando seu proprietário

## Como executar:
1. Instale as dependências:
```bash
pip install -r requirements.txt
```
2. Certifique-se de que o MongoDB está rodando localmente ou na nuvem
3. Coloque no .env sua uri com o nome MONGODB_URI na pasta raiz
4. Execute o script de ingestão:
```bash
python scripts/ingestion.py
```