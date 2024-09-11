# YouTube Video & Audio Downloader

Este projeto permite baixar vídeos e áudios do YouTube utilizando as bibliotecas `yt_dlp` e `pytubefix`. O usuário pode escolher a resolução do vídeo a ser baixado ou optar por baixar apenas o áudio.

## Pré-requisitos

Certifique-se de que você tem as seguintes bibliotecas instaladas:

- `yt_dlp`: para download de vídeos em diferentes resoluções.
- `pytubefix`: para download de áudios.

Para instalar as dependências necessárias, use os seguintes comandos:

```bash
pip install yt-dlp
pip install pytubefix
````

## Funcionalidades
+ Baixar vídeo do YouTube em diferentes resoluções (1080p, 720p, 480p, 360p).
+ Baixar apenas o áudio do vídeo.


## Como Usar
Clone este repositório ou copie o código para um arquivo Python.



Execute o script: 
````
python Down_Tube.py
````

Escolha entre baixar vídeo ou áudio:
+ Digite V para vídeo.
+ Digite A para áudio.

Se a opção V for escolhida, você deverá selecionar a resolução do vídeo:
+ 1 para 1080p
+ 2 para 720p
+ 3 para 480p
+ 4 para 360p

O vídeo/áudio será baixado e salvo no diretório atual.

## Exemplo de Uso

### Baixando um vídeo
Ao iniciar o script e escolher a opção V (vídeo), o usuário deverá colar o link do vídeo do YouTube e escolher a resolução. O vídeo será baixado com o melhor áudio disponível.

### Baixando apenas o áudio
Se a opção A for escolhida, o usuário deverá colar o link do vídeo do YouTube. O script automaticamente baixa o áudio com a melhor qualidade disponível.

##Contribuições
Sinta-se à vontade para abrir uma issue ou enviar um pull request se encontrar algum problema ou quiser sugerir melhorias.