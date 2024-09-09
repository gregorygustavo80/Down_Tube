from pytubefix import YouTube

def baixar_video():
    video_url = input('Cole o link do YouTube aqui: ')
    yt = YouTube(video_url)

    print("Baixando o vídeo...")
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download()
    print("Download do vídeo concluído!")


def baixar_audio():
    video_url = input('Cole o link do YouTube aqui: ')
    yt = YouTube(video_url)

    print("Baixando o áudio...")
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_stream.download()
    print("Download do áudio concluído!")
 

def main():
    while True:
        resposta = input('Digite [V] para baixar Vídeo ou [A] para baixar o áudio: ')
        if resposta.lower() == 'v':
            baixar_video()
        elif resposta.lower() == 'a':
            baixar_audio()
        else:
            print('Opção inválida, tente novamente.')

if __name__== '__main__':
    main()
