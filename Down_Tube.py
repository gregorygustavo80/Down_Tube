import yt_dlp

def download_com_fallback(url, ydl_opts):
    tentativas = [
        ('edge',),
        ('chrome',),
        ('firefox',),
        None  
    ]

    for cookies in tentativas:
        try:
            if cookies:
                print(f"\n🍪 Tentando cookies do {cookies[0]}...")
                ydl_opts['cookiesfrombrowser'] = cookies
            else:
                print("\n🚫 Tentando sem cookies...")
                ydl_opts.pop('cookiesfrombrowser', None)

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            print("✅ Download concluído!\n")
            return

        except Exception as e:
            print("⚠️ Falha nesta tentativa.")

    print("❌ Não foi possível concluir o download.\n")


def baixar_video():
    video_url = input('Cole aqui o link do YouTube: ').strip()

    print("\nEscolha a resolução do vídeo:")
    print("1 - 1080p")
    print("2 - 720p")
    print("3 - 480p")
    print("4 - 360p")

    choice = input("Digite o número da resolução desejada: ").strip()

    resolutions = {
        '1': '1080',
        '2': '720',
        '3': '480',
        '4': '360'
    }

    resolution = resolutions.get(choice, '720')
    print(f"\n➡ Baixando vídeo em até {resolution}p...\n")

    ydl_opts = {
        'format': f'bestvideo[ext=mp4][height<={resolution}]+bestaudio[ext=m4a]/best[ext=mp4][height<={resolution}]',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'progress': True,
        'verbose': True,
    }

    download_com_fallback(video_url, ydl_opts)


def baixar_audio():
    video_url = input('Cole aqui o link do YouTube: ').strip()
    print("\n➡ Baixando áudio (mp3)...\n")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'progress': True,
        'verbose': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    download_com_fallback(video_url, ydl_opts)


def main():
    print("=== YouTube Downloader (yt-dlp) ===")

    while True:
        opcao = input("\n[V] Vídeo | [A] Áudio | [S] Sair: ").lower().strip()

        if opcao == 'v':
            baixar_video()
        elif opcao == 'a':
            baixar_audio()
        elif opcao == 's':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == '__main__':
    main()
