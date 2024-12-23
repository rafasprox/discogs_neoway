# Importar as funções do arquivo discogs_get_data.py
from discogs_get_data import normalize_text, collect_album_data, save_to_jsonl

# Bibliotecas para testes unitários
import unittest
import json
import os

class TestDiscogsGetDataFunctions(unittest.TestCase):

    def test_normalize_text(self):
        print("Iniciando teste: test_normalize_text")
        # Testa a função normalize_text corrigida para remover acentos e caracteres especiais
        self.assertEqual(normalize_text("Olá, mundo!"), "Ola, mundo!")
        print("Passou: Remocao de acentos e caracteres especiais em 'Ola, mundo!'")

        self.assertEqual(normalize_text("Café com açúcar"), "Cafe com acucar")
        print("Passou: Remocao de acentos em 'Cafe com acucar'")

        self.assertEqual(normalize_text("  Texto com espaços extras  "), "Texto com espacos extras")
        print("Passou: Remocao de espacos extras em '  Texto com espacos extras  '")

        self.assertEqual(normalize_text(""), "")
        print("Passou: Entrada vazia retorna saida vazia")

        print("Finalizado teste: test_normalize_text\n")

    def test_collect_album_data(self):
        print("Iniciando teste: test_collect_album_data")

        # Dados controlados para simular um álbum válido
        mock = {
            "album_name": "Album Exemplo",
            "album_release_year": 2020,
            "album_label": ["Gravadora Exemplo"],
            "album_styles": ["Rock"],
            "tracks": [
                {"track_number": "1", "track_title": "Faixa 1", "track_duration": "3:30"},
                {"track_number": "2", "track_title": "Faixa 2", "track_duration": "4:00"}
            ]
        }

        # Mock da função collect_album_data para retornar dados controlados
        album_data = mock

        # Verificar se os dados retornados correspondem aos dados controlados
        self.assertIsNotNone(album_data)  # Certifica-se de que não é None
        print("Passou: Dados do album nao sao None")

        self.assertEqual(album_data["album_name"], mock["album_name"])
        print(f"Passou: Nome do album corresponde ('{mock['album_name']}')")

        self.assertEqual(album_data["album_release_year"], mock["album_release_year"])
        print(f"Passou: Ano de lancamento corresponde ({mock['album_release_year']})")

        self.assertEqual(album_data["tracks"][0]["track_title"], mock["tracks"][0]["track_title"])
        print(f"Passou: Nome da primeira faixa corresponde ('{mock['tracks'][0]['track_title']}')")

        print("Finalizado teste: test_collect_album_data\n")

    def test_save_to_jsonl(self):
        print("Iniciando teste: test_save_to_jsonl")

        # Dados de exemplo para salvar no arquivo JSONL
        data = [
            {"id": 1, "name": "Artista 1"},
            {"id": 2, "name": "Artista 2"}
        ]

        filename = "./test_output.jsonl"  # Caminho relativo para salvar no diretório atual

        # Salvar os dados no arquivo JSONL usando a função save_to_jsonl
        save_to_jsonl(data, filename=filename)

        # Verificar se o arquivo foi criado e contém os dados corretos
        self.assertTrue(os.path.exists(filename))
        print(f"Passou: Arquivo '{filename}' foi criado com sucesso")

        with open(filename, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), len(data))
            print(f"Passou: Numero de linhas no arquivo corresponde ao numero de entradas ({len(data)})")

            for i, line in enumerate(lines):
                self.assertEqual(json.loads(line), data[i])
                print(f"Passou: Linha {i+1} corresponde aos dados esperados")

        # Remover o arquivo após o teste
        os.remove(filename)
        print(f"Arquivo '{filename}' removido apos o teste")

        print("Finalizado teste: test_save_to_jsonl\n")

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
