# Kpop API Eindproject Api-Development Documentatie

## Beschrijving van het gekozen thema
Ik heb voor het thema 'Kpop' gekozen, aangezien dit mijn favoriet muziekgenre is. Het leek me een tof idee om een API te bouwen die Kpop songs bevat en kan opvragen. Ik heb verdergebouwd op mijn vorige project.

[Link front-end](https://sooivervloessem-kpop-api.netlify.app/)  
[Link front-end repository (deze repo)](https://github.com/sooivervloessem/apidevelopment-eindproject)  
[Hosted API link](https://system-service-sooivervloessem.cloud.okteto.net/)  

## Uitbreidingen op het project:
In totaal heb ik voor 85 % van de punten gewerkt.
* Algemene eisen en documentatie = 50 %
* Front-end 3.1 = 15 %
* Front-end 3.1.1 = 10 %
* Front-end 3.1.2 = 10 %

## API functionaliteit van de Front-end
De volledige front-end ziet er als volgt uit:
![Image Frontend Setup](/images_readme/volledige_frontend.png)    

Ik toon de werking van alle onderdelen op de front-end.

### Get a token
Om een token te krijgen:
![Image Get a Token](/images_readme/frontend_get_a_token.png)  
Er komt 'logged in' te staan onder het form:
![Image logged in](/images_readme/frontend_logged_in.png)  

### Check user login
Nu we ingelogd zijn checken we onze user login gegevens
![Image check](/images_readme/frontend_check_user_login.png)  
Wanneer we niet ingelogd zijn krijgen we:
![Image check fail](/images_readme/frontend_check_user_login_fail.png)  

### Search user by id
Met de search user by id form kunnen we een user zoeken met zijn/haar id:
![Image search user by id](/images_readme/frontend_search_user_by_id.png)  
Wanneer we niet ingelogd zijn krijgen we:
![Image search user by id fail](/images_readme/frontend_search_user_by_id_fail.png)  

### Search Kpop group by id
Kpop groupen kunnen per id gezocht worden. Bij songs wordt enkel de titel weergegeven in een lijst element. In dit geval 'Circus' en 'Super Board'.  
![Image search kpop by id](/images_readme/frontend_search_kpop_group_by_id.png)  

### Search song by id
We kunnen ook nummers zoeken per id:  
![Image search song by id](/images_readme/frontend_search_song_by_id.png)  

### Add a Kpop song to the database
Nu is het tijd om de POSTS te tonen. De eerste is om een song aan te maken voor een bepaalde kpop group. Het is de bedoeling dat het id nummer van de Kpop group wordt meegegeven, zodat de relatie kan gemaakt worden in de database.  
![Image add a kpop song](/images_readme/frontend_add_a_kpop_song.png)  

De song is nu ook toegevoegd:  
![Image song is added](/images_readme/frontend_song_has_been_added.png)  

### Add a user to the database
Gebruikers kunnen aangemaakt worden met een email en een wachtwoord.
![Image add a user](/images_readme/frontend_add_a_user.png)  

We kunnen nu ook inloggen met deze gebruiker:
![Image login as new user](/images_readme/frontend_we_can_login_with_user.png)  
We checken de nieuwe gebruiker:  
![Image check new user](/images_readme/frontend_check_new_user.png)  

### Add a kpop group to the database
Als laatste voegen we een kpop group toe aan de database:
![Image add kpop group](/images_readme/frontend_add_a_kpop_group.png)  

Deze Kpop group kan nu opgevraagd worden. Het veld 'Songs' is nog leeg, aangezien er nog geen songs zijn toegevoegd:  
![Image check kpop group](/images_readme/frontend_check_kpop_group.png)  

We voegen een song toe ter illustratie:
![Image add song to new kpop group](/images_readme/frontend_add_song_to_new_kpop_group.png)  

Wanneer we de nieuwe group aanvragen staat de song nu in het veld 'Songs':
![Image check kpop group](/images_readme/frontend_check_kpop_group_with_song.png)  

In de backend kunnen er nog relaties gemaakt worden tussen de 3 entiteiten User, Song en KpopGroup. Ik heb dit op de frontend achterwegen gelaten, aangezien dit te ingewikkeld voor de gebruiker zou worden.
Wachtwoorden worden gehashed in de database opgeslagen en OAuth werkt op de endpoints waarvoor ik dit nodig achtte.


## FastAPI Docs
Vervolgens bekijken we de /docs endpoint van mijn API:
![Image DOCS](/images_readme/fastapi_docs.png)  


## Postman Screenshots
Nu we een idee hebben van de structuur van mijn API, gaan we over tot het tonen van de werking met Postman.


### POST /token
We geven onze username en password mee met de POST request om een token te ontvangen:
![Image postman /token](/images_readme/postman_post_token.png)  

### GET /users/
We kunnen onze token ingeven om geauthorizeerde toegang te krijgen tot de beveiligde endpoints. Vervolgens vragen we alle users op:
![Image get users](/images_readme/postman_get_users.png)  

### POST /users/
We maken een nieuwe gebruiker aan:
![Image add user](/images_readme/postman_add_user.png)  

### GET /users/me
We checken met onze token welke user er ingelogd is:
![Image get user me](/images_readme/postman_get_user_me.png)  

### GET /users/{user_id}
We vragen een user op door middel van het user_id:
![Image get user id](/images_readme/postman_get_user_by_id.png)  

### POST /listener/{listener_id}/{song_id}
We kunnen een gebruiker laten luisteren naar een song. Het relatieId is '1'. Het listener_id (wat gelijkstaat aan user_id) is ook '1'. song_id is 2. Deze POST heeft ervoor gezorgd dat user 1 naar song 2 luistert.  
![Image listener](/images_readme/postman_listener.png)  
Bij de gebruiker met id 1 is er nu een song relatie toegevoegd bij 'songs':
![Image listener user](/images_readme/postman_listener_link.png)  

### GET /kpop_groups/
Vraag alle kpop groups op:
![Image kpop groups](/images_readme/postman_get_kpop_groups.png)  
Zoals u kan zien, staat de relatie ook bij 'listeners' van de song met id '2', aangezien we deze daarstraks hebben opgezet.

### POST /kpop_groups/
We creëren een kpop group:
![Image create kpop group](/images_readme/postman_create_kpop_group.png)  

### GET /kpop_groups/{kpop_group_id}
We kunnen kpop groepen opvragen met hun id:
![Image check kpop group with id](/images_readme/postman_kpop_group_by_id.png)  

### POST /kpop_groups/{kpop_group_id}/songs/
We kunnen een song aanmaken voor een bepaalde Kpop groep. In ons geval geven we in de URL '3' mee, dit is de groep 'Itzy' die we daarnet hebben aangemaakt:
![Image add song](/images_readme/postman_add_song.png)  

### GET /songs/
Om alle songs op te vragen:
![Image get songs](/images_readme/postman_get_songs.png)  

### GET /songs/{song_id}
Om een specifieke song op te vragen met het song_id:
![Image get song by id](/images_readme/postman_get_song_by_id.png)  

### PUT /songs/{song_id}
Om een song aan te passen in de database kan men PUT gebruiken. Deze endpoint is beveiligd, aangezien anders iedereen aanpassingen kan maken aan songs. We starten vanaf deze song:
![Image before PUT](/images_readme/postman_before_put.png)  
We passen de naam aan met een PUT request:
![Image after PUT](/images_readme/postman_after_put.png)  
We checken met een GET request:
![Image after PUT 2](/images_readme/postman_after_put2.png)  

### DELETE /songs/{song_id}
Ten slotte hebben we nog een DELETE request. We maken eerst een foutieve song zodat we deze kunnen verwijderen:
![Image create wrong song](/images_readme/postman_create_wrong_song.png)  

Het Id van deze song is 6:
![Image get wrong song](/images_readme/postman_get_wrong_song.png)  

We verwijderen deze song:
![Image delete wrong song](/images_readme/postman_delete_wrong_song.png)  

We checken of deze verwijdert is:
![Image check deleted song](/images_readme/postman_song_is_deleted.png)  

Alle endpoints zijn via Postman getest en besproken.

## Volledige OpenAPI Docs screenshots
Nu toon ik mijn volledige OpenAPI Docs screenshots

### Login for Access Token
![Image openapi docs token](/images_readme/openapi_login_for_access_token.png)  

### Read Users
![Image openapi docs read users](/images_readme/openapi_read_users.png)  

### Create User
![Image openapi docs create user](/images_readme/openapi_create_user.png)  

### Read User Me
![Image openapi docs read user me](/images_readme/openapi_read_user_me.png)  

### Read User
![Image openapi docs read user](/images_readme/openapi_read_user.png)  

### Link Listener Song
![Image openapi docs link listener song](/images_readme/openapi_link_listener_song.png)  

### Read Kpop Groups
![Image openapi docs read kpop groups](/images_readme/openapi_read_kpop_groups.png)  

### Create Kpop Group
![Image openapi docs create kpop groups](/images_readme/openapi_create_kpop_group.png)  

### Read Kpop Group
![Image openapi docs read kpop group](/images_readme/openapi_read_kpop_group.png)  

### Create Song For Kpop Group
![Image openapi docs create song for kpop group](/images_readme/openapi_create_song_for_kpop_group.png)  

### Read Songs
![Image openapi docs read songs](/images_readme/openapi_read_songs.png)  

### Read Song
![Image openapi docs read song](/images_readme/openapi_read_song.png)  

### Update Song
![Image openapi docs update song](/images_readme/openapi_update_song.png)  

### Delete Song
![Image openapi docs delete song](/images_readme/openapi_delete_song.png)  

Alle endpoints zijn met openapi bekeken.

## Besluit
Het project is successvol ten einde gebracht. Ik heb opdrachten uitgevoerd voor een maximum van 85 %

- Algemene eisen & documentatie 50 %
- Frontend (3.1-3.1.1-3.1.2) 35 %
