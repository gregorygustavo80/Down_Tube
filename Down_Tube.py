import yt_dlp
import subprocess
import sys
import os
from datetime import date

def atualizar_ytdlp():
    flag_file = os.path.join(os.environ.get('TEMP', '/tmp'), 'ytdlp_updated')
    hoje = str(date.today())

    if os.path.exists(flag_file):
        with open(flag_file) as f:
            if f.read().strip() == hoje:
                return

    print("Atualizando yt-dlp...")
    subprocess.run([sys.executable, '-m', 'pip', 'install', '-U', 'yt-dlp', '--break-system-packages'],
                   capture_output=True)
    with open(flag_file, 'w') as f:
        f.write(hoje)
    print("yt-dlp atualizado!\n")

def get_ffmpeg_path():
    resultado = subprocess.run(['where.exe', 'ffmpeg'], capture_output=True, text=True)
    caminho = resultado.stdout.strip().splitlines()[0]
    return os.path.dirname(caminho) if caminho else None

def baixar_video(video_url, selected_resolution, ffmpeg_path):
    ydl_opts = {
        'format': f'bestvideo[height<={selected_resolution}]+bestaudio/best[height<={selected_resolution}]',
        'outtmpl': '%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'nooverwrites': True,
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'postprocessor_args': ['-c:a', 'aac', '-c:v', 'copy'],  # converte áudio para AAC
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def baixar_audio(video_url, ffmpeg_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'nooverwrites': True,
        'ffmpeg_location': ffmpeg_path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def main():
    atualizar_ytdlp()

    ffmpeg_path = get_ffmpeg_path()
    if not ffmpeg_path:
        print("AVISO: FFmpeg não encontrado. O merge de vídeo+áudio pode falhar.")
    else:
        print(f"FFmpeg encontrado em: {ffmpeg_path}\n")

    while True:
        resposta = input('\nDigite [V] para Vídeo, [A] para Áudio ou [S] para Sair: ').lower()

        if resposta == 's':
            print("Saindo...")
            break
        elif resposta not in ('v', 'a'):
            print('Opção inválida, tente novamente.')
            continue

        video_url = input('Cole o link do YouTube aqui: ').strip()
        if not video_url.startswith('http'):
            print("URL inválida.")
            continue

        try:
            if resposta == 'v':
                print("Escolha a resolução:\n1 - 1080p\n2 - 720p\n3 - 480p\n4 - 360p")
                choice = input("Digite o número: ")
                resolution = {'1': '1080', '2': '720', '3': '480', '4': '360'}.get(choice, '720')
                print(f"Baixando vídeo em {resolution}p...")
                baixar_video(video_url, resolution, ffmpeg_path)
            else:
                print("Baixando áudio em MP3...")
                baixar_audio(video_url, ffmpeg_path)

            print("Download concluído!")

        except yt_dlp.utils.DownloadError as e:
            print(f"Erro ao baixar: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == '__main__':
    main()