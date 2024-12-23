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

pip install discogs-client


## ⚙️ Configuração

1. Obtenha um token de autenticação da API Discogs.
2. No arquivo `discogs_get_data.py`, substitua o valor da variável `TOKEN` pelo seu token:


3. Por padrão, o script coleta dados do gênero "Rock". Você pode alterar o gênero editando a variável `GENRE` no mesmo arquivo:
GENRE = 'Pop' # Altere para o gênero desejado

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


---

## 🖥️ Executando no Google Colab

Se preferir executar os scripts diretamente no Google Colab, siga os passos abaixo:

1. **Acesse os scripts no Google Drive**:
   - [Script](https://drive.google.com/drive/folders/1NxVoFLBt3W_lR3uKUm5W4JiIx8XFQjsy?usp=drive_link)

2. **Monte o Google Drive no Colab**:
   Adicione o seguinte código no início da célula do notebook para montar seu Google Drive:


3. **Certifique-se de que os arquivos estão na mesma pasta**:
Para que os scripts funcionem corretamente, todos os arquivos necessários devem estar na **mesma pasta** no Google Drive. Por exemplo, se você estiver usando a pasta `Colab Notebooks`, os arquivos `discogs_get_data.py` e `tests.ipynb` devem estar localizados em `/content/drive/MyDrive/Colab Notebooks`.

4. **Adicione a pasta ao Python Path**:
No notebook, adicione o seguinte código para garantir que o Python consiga localizar os arquivos na pasta correta:


5. **Instale as dependências necessárias**:
Execute o comando abaixo para instalar a biblioteca `discogs-client`:


6. **Execute o script principal**:
Após navegar até o diretório correto e configurar o ambiente, execute o script principal diretamente no notebook:


7. **Execute os testes unitários**:
Para rodar os testes, execute o arquivo de testes da mesma forma:


---

### ⚠️ Atenção às pastas dos arquivos

- Certifique-se de que todos os arquivos necessários (como `discogs_get_data.py` e `tests.py`) estão na **mesma pasta** no Google Drive.
- Se você alterar a localização dos arquivos, atualize o caminho correspondente no Python Path com `sys.path.append('<novo_caminho>')`.
- Caso contrário, você verá erros como `ModuleNotFoundError: No module named 'discogs_get_data'`.

---

Se tiver dúvidas ou problemas, consulte a [documentação oficial da API Discogs](https://www.discogs.com/developers/) ou entre em contato com o mantenedor do projeto.
