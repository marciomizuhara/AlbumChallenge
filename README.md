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
* **!roll 2022** -----> Rolls a random album from the 2022 releases list
* **!newalbum** - ARTIST - ALBUM - SPOTIFY** -----> Adds a new album to the 2022 releases list
* **!roll alltime** -----> Rolls a random album from the RYM best albums ever
* **!roll 2022 only GENRE** -----> Rolls only albums tagged with the specified genre from the 2022 releases list
* **!roll 2022 ignore GENRE** -----> Ignores the specified genre when rolling an album from the 2022 releases list
* **!update** -----> Updates you list of listened albums with the last rolled album
* **!mystatus** -----> Shows some information regarding your challenge status
* **!myratings** -----> Shows your listened albums sorted by the highest rated
* **!myreviews** -----> Receives a direct message from the bot with all your reviews submitted to the challenge
* **!2022status** -----> Shows some information regarding the 2022 releases list status
* **!list2022** -----> Shows all albums added to the 2022 releases list
* **!list LETTER** -----> Shows all artists added to the 2022 releses list starting with the LETTER specified
* **!id NUMBER** -----> Shows all information regarding the album with the specified NUMBER (id)
* **!review ID TEXT** -----> Saves the TEXT as the review for the specified album ID
* **!rating ID RATING** -----> Saves the RATING as the rating for the specified album ID
* **!getreviews ID** -----> Shows all reviews submitted for the specified album ID
* **!getratings ID** -----> Shows all ratings submitted for the specified album ID. It also returns the average rating for the album
* **!top NUMBER** -----> Shows the top NUMBER albums with the highest ratings on the challenge
* **!top NUMBER** -----> Shows the bottom NUMBER albums with the lowest ratings on the challenge
* **!users** -----> Shows all users participating in the challenge
* **leaderboard** -----> Show all users participating in the challenge, sorted by the ones with the most albums rolled.
