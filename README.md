# Tietokantasovellus, kesä 2020

Tämä on repositorio Helsingin yliopiston kurssille [Aineopintojen harjoitustyö: tietokantasovellus](https://materiaalit.github.io/tsoha-20/).

- [Tietokantarakenteen kuvaus](https://github.com/joonaspartanen/tsoha-forum/blob/master/documentation/db_description.md)

- [Käyttötapaukset](https://github.com/joonaspartanen/tsoha-forum/blob/master/documentation/requirements.md)

- [Käyttöohjeet](https://github.com/joonaspartanen/tsoha-forum/blob/master/documentation/user_instructions.md)

- [Asennusohjeet](https://github.com/joonaspartanen/tsoha-forum/blob/master/documentation/installation.md)

- [Jatkokehitysideoita](https://github.com/joonaspartanen/tsoha-forum/blob/master/documentation/future_development.md)

## Yleistä

Harjoitustyön aiheena on keskustelufoorumi. Rekisteröityneet käyttäjät voivat luoda foorumille viestiketjuja, joihin he voivat lisätä viestejä. Käyttäjät voivat tykätä viesteistä.

Viestiketjuja on mahdollista luokitella käyttämällä aihetunnisteita. Foorumin hakutoiminto mahdollistaa viestiketjujen hakemisen ketjujen otsikoiden ja niiden lisänneiden käyttäjien perusteella.

Hakutoiminnon lisäksi monimutkaisempia yhteenvetokyselyjä hyödynnetään käyttäjän omalla sivulla, jossa näytetään tilastotietoja käyttäjän toiminnasta foorumilla (viestien, ketjujen ja saatujen tykkäysten määrä).

Sovelluksessa on myös admin-käyttäjän rooli: admin-käyttäjä voi poistaa foorumilta kenen tahansa lisäämiä viestejä ja viestiketjuja.

## Demo

Sovellukseen voi tutustua myös [Herokussa](https://tsoha-forum-app.herokuapp.com/).

![Kuvakaappaus sovelluksen etusivusta](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/topics_list.png)

Oma tunnus on helppo tehdä, mutta myös seuraavia testitunnuksia voi käyttää:

Peruskäyttäjä:

- käyttäjätunnus: _tsohauser_
- salasana: _tsohauser_

Pääkäyttäjä:

- käyttäjätunnus: _tsohaadmin_
- salasana: _tsohaadmin_

## Teknologiat

Sovellus on tehty Pythonin [Flask](https://flask.palletsprojects.com/en/1.1.x/)-kirjastolla. HTML-sivujen generoinnissa hyödynnetään [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)-kirjastoa. Ulkoasun tyylittelyyn käytetään [Semantic UI:ta](https://semantic-ui.com/).

Sovellus käyttää paikallisesti tietokannanhallintajärjestelmänä [SQLiteä](https://www.sqlite.org/index.html) ja Herokussa [Postgresia](https://www.heroku.com/postgres).
