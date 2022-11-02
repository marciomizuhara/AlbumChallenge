# Album Challenge
This is a Discord bot that I created for my discord music server. 
It was built around the idea of having a music challenge on the server, and it works as follows:
* Users can add album releases to the bot, which comprises all submitions into a list; 
* Then users can roll the dice and get an album randomly from the server. They have 24 hours to listen to this album and submit a review or a rating;
* The bot storages all data and, from that point on, is able to return some exploratory data analyses, such as return Top 10 rated albums, filter albums by year, genre, number of reviews, among others.

# How to Use
The bot was mainly developed to be used with Replit (replit.com/) as it's hosted there and uses Replit's Database. This is a key-value database type, so it could be easily adapted to other platforms.
Either way, this freeCodeCamp tutorial https://www.youtube.com/watch?v=SPTfmiYiuok&ab_channel=freeCodeCamp.org contains all information needed to host a discord bot on Replit.

# Commands
* **!roll 2022** -----> Rolls a random album from the 2022 releases list.
* **!newalbum** - ARTIST - ALBUM - SPOTIFY** -----> Adds a new album to the 2022 releases list.
* **!roll alltime** -----> Rolls a random album from the RYM best albums ever.
* **!roll 2022 only GENRE** -----> Rolls only albums tagged with the specified genre from the 2022 releases list.
* **!roll 2022 ignore GENRE** -----> Ignores the specified genre when rolling an album from the 2022 releases list.
* **!update** -----> Atualiza sua lista de álbuns ouvidos com o último álbum rollado.
* **!mystatus** -----> Exibe seus status no desafio.
* **!myratings** -----> Exibe seus álbuns ouvidos melhores avaliados.
* **!myreviews** -----> Exibe, por mensagem direta (DM), todas as resenhas que você já realizou no desafio.
* **!2022status** -----> Exibe a quantidade de álbuns da lista de lançamentos de 2022.
* **!list2022** -----> Exibe todos os álbuns já adicionados à lista de lançamentos de 2022.
* **!list LETRA** -----> Exibe todos os artistas adicionados na lista de lançamentos de 2022 que comecem com a LETRA escolhida.
* **!id NUMERO** -----> Exibe o álbum com o respectivo ID
* **!review ID TEXTO** -----> Salva o texto como a resenha para o álbum do respectivo ID
* **!rating ID NOTA** -----> Salva a nota para o álbum do respectivo ID
* **!getreviews ID** -----> Exibe todas as resenhas para o álbum do respectivo ID
* **!getratings ID** -----> Exibe todas as notas para o álbum do respectivo ID
* **!topalbums** -----> Exibe os álbuns mais bem avaliados do server
* **!users** -----> Exibe todos os usuários participantes do desafio.
* **leaderboard** -----> Exibe a leaderboard do desafio
