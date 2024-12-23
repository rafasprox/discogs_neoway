import json
import unicodedata
from discogs_client import Client

# Configuração da API
USER_AGENT = "MyDiscogsApp/1.0"
TOKEN = "ZZItmlsEuhVmcrUtTRFpzHwYrPsTdlZacBJVWYuw"
client = Client(USER_AGENT, user_token=TOKEN)


def fetch_data(genre, max_artists=10, max_albums=10):
    data = []
    artists_collected = set()
    current_page = 1  # pagina inicial

    try:
        while len(artists_collected) < max_artists:
            print(f"Buscando na pagina {current_page}...")

            #filtrando por gênero e formato "Album"
            search_results = client.search(genre=genre, format='Album').page(current_page)

            if not search_results:  # Se não houver mais resultados
                print("Nenhum resultado encontrado em mais paginas.")
                break

            for release in search_results:
                if len(artists_collected) >= max_artists:
                    break

                # Verificar se o lançamento tem artistas associados
                if not hasattr(release, 'artists') or not release.artists:
                    continue

                artist = release.artists[0]  # Primeiro artista associado ao lançamento
                if artist.id in artists_collected:
                    continue

                artists_collected.add(artist.id)
                artist_name_normalized = normalize_text(artist.name)
                print(f"Coletando dados do artista: {artist_name_normalized}")

                # Dados básicos do artista
                artist_data = {
                    "id": artist.id,
                    "genre": genre,
                    "artist_name": artist_name_normalized,
                    "artist_members": [normalize_text(member.name) for member in getattr(artist, 'members', [])],
                    "artist_websites": getattr(artist, 'urls', []),
                    "albums": []
                }

                # Coletar álbuns do artista (limitado a max_albums)
                releases = client.artist(artist.id).releases.page(1)[:max_albums]
                for release in releases:
                    album_data = collect_album_data(release)
                    if album_data:
                        artist_data["albums"].append(album_data)

                data.append(artist_data)

            current_page += 1  # Avança para a próxima página

    except Exception as e:
        print(f"Erro ao buscar dados: {e}")

    return data

def collect_album_data(release):
    """Coleta dados de um album (MasterRelease ou Release simples)."""
    try:
        if hasattr(release, 'main_release'):  # Verifica se é MasterRelease
            master_release = client.master(release.id)
            album_name_normalized = normalize_text(master_release.title)
            print(f"Coletando album (Master Release): {album_name_normalized}")
            return {
                "album_name": album_name_normalized,
                "album_release_year": master_release.year,
                "album_label": [normalize_text(label.name) for label in getattr(master_release, 'labels', [])],
                "album_styles": getattr(master_release, 'styles', []),
                "tracks": [
                    {
                        "track_number": track.position,
                        "track_title": normalize_text(track.title),
                        "track_duration": track.duration
                    }
                    for track in master_release.tracklist
                ]
            }
        elif hasattr(release, 'artists'):  # Caso seja um Release simples com artistas
            album_name_normalized = normalize_text(release.title)
            print(f"Coletando album (Release): {album_name_normalized}")
            return {
                "album_name": album_name_normalized,
                "album_release_year": release.year,
                "album_label": [normalize_text(label.name) for label in getattr(release, 'labels', [])],
                "album_styles": getattr(release, 'styles', []),
                "tracks": [
                    {
                        "track_number": track.position,
                        "track_title": normalize_text(track.title),
                        "track_duration": track.duration
                    }
                    for track in release.tracklist
                ]
            }
        else:
            print("Lançamento ignorado: Nao e um album valido.")
            return None
    except Exception as e:
        print(f"Erro ao coletar dados do album: {e}")
        return None

def normalize_text(text):
    """Normaliza um texto removendo caracteres especiais e acentos."""
    try:
        # Remove acentos e normaliza para NFKD
        text = unicodedata.normalize('NFKD', text)
        # Remove caracteres não-ASCII
        text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
        # Remove espaços extras e caracteres invisíveis
        text = text.strip()
        return text
    except Exception as e:
        print(f"Erro ao normalizar texto: {e}")
        return text  # Retorna o texto original em caso de erro

def save_to_jsonl(data, filename="output.jsonl"):
    """Salva os dados em um arquivo JSONL."""
    if not data:
        print("Nenhum dado disponivel para salvar.")
        return

    try:
        with open(filename, 'w') as f:
            f.writelines(json.dumps(entry) + '\n' for entry in data)
        print(f"Dados salvos no arquivo {filename}")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

# Testar coleta e salvamento
if __name__ == "__main__":
    GENRE = "Rock"
    data = fetch_data(GENRE)

    if data:
        save_to_jsonl(data)
    else:
        print("Nenhum dado foi coletado.")
