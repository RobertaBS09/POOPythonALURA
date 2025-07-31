class Musica:
    nome=''
    artista=''
    duracao=int
    
musica1=Musica()
musica1.nome='Work Song'
musica1.artista='Hozier'
musica1.duracao=240

musica2=Musica()
musica2.nome='Ask Me Why'
musica2.artista='The Beatles'
musica2.duracao=120

musica3=Musica()
musica3.nome='Around you'
musica3.artista='Don Toliver'
musica3.duracao=180


print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')