# Discogs Data Fetcher

Este repositório contém scripts para coletar dados de artistas, álbuns e faixas do Discogs utilizando a API oficial. Ele também inclui testes unitários para validar as funcionalidades principais.

## 📋 Pré-requisitos

Certifique-se de ter o seguinte configurado antes de executar o projeto:

- **Python 3.7 ou superior**
- **Bibliotecas Python necessárias**:
  - `discogs_client`
  - `unittest`
  - `json`
  - `os`

Instale as dependências executando:


## ⚙️ Configuração

1. Obtenha um token de autenticação da API Discogs.
2. No arquivo `discogs_get_data.py`, substitua o valor da variável `TOKEN` pelo seu token:


3. Por padrão, o script coleta dados do gênero "Rock". Você pode alterar o gênero editando a variável `GENRE` no mesmo arquivo:


## 🚀 Como Executar

### Coleta de Dados

1. No terminal, navegue até o diretório onde os arquivos estão localizados.
2. Execute o script principal para iniciar a coleta de dados:


3. Os dados coletados serão salvos em um arquivo chamado `output.jsonl` no formato JSONL.

### Testes Unitários

Para garantir que as funções estão funcionando corretamente, execute os testes unitários incluídos no arquivo `tests.py`:


Os testes verificam:

- A normalização de texto (`normalize_text`)
- A coleta de dados de álbuns (`collect_album_data`)
- O salvamento de dados em formato JSONL (`save_to_jsonl`)

## 📂 Estrutura do Projeto

- **discogs_get_data.py**: Script principal para coletar dados da API Discogs.
- **tests.py**: Arquivo contendo testes unitários para validar as funções principais.

## 📝 Saída dos Dados

Os dados coletados serão salvos no formato JSONL (JSON Lines), onde cada linha representa um registro individual. O arquivo padrão é `output.jsonl`, mas você pode especificar outro nome alterando a chamada da função `save_to_jsonl`.

Exemplo de uma entrada no arquivo JSONL:

{"id": 1, "artist_name": "Nome do Artista", "albums": [{"album_name": "Nome do Álbum", "tracks": [{"track_number": "1", "track_title": "Nome da Faixa"}]}]}
