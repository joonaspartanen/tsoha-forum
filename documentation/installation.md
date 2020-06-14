# Asennusohje

## Esivaatimukset

Koneellasi tulee olla asennettuna [Pythonista](https://www.python.org/downloads/) vähintään versio 3.5. Lisäksi tarvitset [pip](https://packaging.python.org/key_projects/#pip)-paketinhallintaa projektin riippuvuuksien asentamiseen.

Sovellus käyttää paikallisesti tietokannanhallintajärjestelmänä [SQLiteä](https://www.sqlite.org/index.html) ja Herokussa [Postgresia](https://www.heroku.com/postgres).

## Paikallinen asennus

Kloonaa ensin repositorio koneellesi ja siirry projektikansioon:

```bash
git clone https://github.com/joonaspartanen/tsoha-forum.git
cd tsoha-forum
```

Asenna sitten riippuvuudet komennolla `pip install -r requirements.txt`.

Voit käynnistää sovelluksen komennolla `python3 run.py`.

Voit nyt käyttää sovellusta osoitteessa `http://localhost:5000/`.

## Julkaiseminen Herokussa

Julkaistaksesi sovelluksen [Heroku](https://www.heroku.com/)-pilvipalvelussa tarvitset Heroku-tilin ja [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) -komentorivityökalut.

Luo ensin uusi Heroku-sovellus komennolla

```bash
heroku create
```

Yhdistä sitten luomasi sovellus versionhallintaasi

```bash
git remote add heroku https://git.heroku.com/<sovelluksen-nimi>.git
```

Aseta vielä tarvittava ympäristömuuttuja

```bash
heroku config:set HEROKU=1
```

ja ota Postgres-tietokanta käyttöön

```bash
heroku addons:add heroku-postgresql:hobby-dev
```

Voit nyt julkaista sovelluksen committoimalla tekemäsi muutokset ja pushaamalla ne komennoilla

```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku master
```

## Käyttäjien luominen

Peruskäyttäjiä on helppo luoda sovelluksen käyttöliittymän kautta.

Ensimmäinen admin-käyttäjä täytyy kuitenkin luoda suoraan koodista. Sovelluksen _UserService_-luokassa on apumetodi create_testadmin_if_absent, jota voi käyttää hyväksi.
