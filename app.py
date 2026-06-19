import streamlit as st

musicas = {
    "Oliver Tree": {
        "Life Goes On": "https://www.youtube.com/watch?v=8F2s8ivKXNY",
        "Miss You": "https://www.youtube.com/watch?v=BX0lKSa_PTk",
    },
    
      "Os Barões da Pisadinha" : {
        "Sou Favela": "https://www.youtube.com/watch?v=fZN1uFlpE-4",
        "Tá Complicado": "https://www.youtube.com/watch?v=ngw3hQwqXIE",
    },
    "João Gomes": {
        "MEU PEDAÇO DE PECADO": "https://www.youtube.com/watch?v=H1DEczvTjgE"
    },
}

st.sidebar.image("logo.png")
artista= st.sidebar.selectbox("selecione o artista", musicas.keys())
musicas_artista = musicas[artista]

st.title(artista)
video,sobre=st.tabs(['video','sobre'])
with video:

  for musica in musicas_artista.items():
    titulo, link = musica
    st.subheader(titulo)
    st.video(link)




with sobre:
    if artista == "Oliver Tree":
       st.title("Oliver Tree")
       st.markdown("Oliver Tree Nickell (nascido em 29 de junho de 1993, em Santa Cruz, Califórnia) foi um cantor, compositor, produtor musical e cineasta americano conhecido por seu estilo excêntrico, cabelo em formato de tigela, óculos escuros e videoclipes criativos.  " \
       " Informações mais importantes " \
       " Nome completo: Oliver Tree Nickell  " \
       " Nascimento: 29 de junho de 1993  " \
       " Origem: Santa Cruz, Califórnia, Estados Unidos " \
       " Profissões: Cantor, compositor, produtor musical, rapper e diretor de vídeos " \
       " Gêneros musicais: Alternative pop, rock alternativo, indie pop, hip-hop e música eletrônica.     " )
       st.image("olv.png")
    elif artista == "Os Barões da Pisadinha":
       st.title("Os Barões da Pisadinha")  
       st.markdown("Os Barões da Pisadinha são uma dupla brasileira de piseiro, forró e tecnobrega formada em 2015 pelos músicos Rodrigo Barão e Felipe Barão, naturais da Bahia. O grupo surgiu nas cidades de Heliópolis e Ribeira do Amparo e inicialmente era conhecido como Barões do Forró. Com o crescimento do ritmo da pisadinha, a dupla adotou o nome atual e se tornou um dos maiores fenômenos da música brasileira.  "
       "Entre os maiores sucessos do grupo estão Tá Rocheda, Basta Você Me Ligar, Recairei, Esquema Preferido, Já Que Me Ensinou a Beber, Chupadinha e Galera do Interior. Em 2021, a dupla alcançou um feito histórico ao colocar duas músicas simultaneamente no Top 50 Global do Spotify.")
       st.image("bar.png")
    elif artista ==  "João Gomes": 
       st.title("João Gomes")
       st.markdown("João Fernando Gomes Valério, conhecido artisticamente como João Gomes, nasceu em 31 de julho de 2002, na cidade de Serrita. É um cantor e compositor brasileiro de piseiro e forró que se tornou um dos maiores fenômenos da música brasileira. Sua carreira ganhou destaque nacional em 2021 com o álbum Eu Tenho a Senha, tornando-se o artista mais ouvido do Brasil naquele ano.")
       st.image("jg.png")




