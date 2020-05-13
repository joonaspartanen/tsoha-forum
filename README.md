# Tietokantasovellus, kesä 2020

Tämä on repositorio Helsingin yliopiston kurssille [Aineopintojen harjoitustyö: tietokantasovellus](https://materiaalit.github.io/tsoha-20/).

- [Arkkitehtuurikuvaus](https://github.com/joonaspartanen/tsoha-forum/blob/master/documentation/architecture.md)

## Yleistä

Harjoitustyön aiheena on keskustelufoorumi. Rekisteröityneet käyttäjät voivat luoda foorumille viestiketjuja, joihin he voivat lisätä viestejä. Käyttäjät voivat tykätä viesteistä.

Viestiketjuja on mahdollista luokitella käyttämällä aihetunnisteita. Foorumin hakutoiminto mahdollistaa viestiketjujen hakemisen mm. aihetunnisteiden ja ketjujen otsikoiden perusteella.

Tarkoituksena on luoda sovellukseen myös admin-käyttäjän rooli: admin-käyttäjä voi myös poistaa foorumilta viestejä ja viestiketjuja.

## Teknologiat

Sovellus on tehty Pythonin [Flask](https://flask.palletsprojects.com/en/1.1.x/)-kirjastolla. HTML-sivujen generointiin hyödynnetään ainakin [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)-kirjastoa. Ulkoasun tyylittelyyn käytetään jotain vielä määrittelemätöntä CSS-frameworkia.

Kehityksen alkuvaiheessa sovellus hyödyntää SQLite-tietokannanhallintajärjestelmää.

## Demo

Sovellukseen voi tutustua myös [Herokussa](https://tsoha-forum-app.herokuapp.com/).

## Asennusohjeet

Kloonaa ensin repositorio koneellesi ja siirry projektikansioon:

```
git clone https://github.com/joonaspartanen/tsoha-forum.git
cd tsoha-forum
```

Asenna sitten riippuvuudet komennolla `pip install -r requirements.txt`.

Voit käynnistää sovelluksen komennolla `python3 run.py`.

Voit nyt käyttää sovellusta osoitteessa `http://localhost:5000/`.
