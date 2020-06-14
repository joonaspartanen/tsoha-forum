# Käyttöohje

## Kirjautuminen ja rekisteröityminen

Kirjautumaton käyttäjä ohjataan aluksi kirjautumisnäkymään, jossa hän voi kirjautua syöttämällä käyttäjätunnuksensa ja salasanansa kirjautumislomakkeeseen:

![Kirjautumisnäkymä](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/login.png)

Mikäli käyttäjällä ei vielä ole käyttäjätunnusta, hän voi luoda sellaisen siirtymällä _Sign Up_-painikkeella rekisteröitymisnäkymään:

![Rekisteröitymisnäkymä](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/signup.png)

Sovellus ilmoittaa, mikäli haluttu käyttäjänimi on jo varattu tai mikäli käyttäjätunnus tai salasana eivät täytä vähimmäisvaatimuksia.

## Kaikki viestiketjut -näkymä

Kirjautumisen jälkeen käyttäjä ohjataan näkymään, josta löytyvät sovellukseen tallennetut viestiketjut aikajärjestyksessä (uusimmat ensin):

![Kaikki viestiketjut](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/topics_list.png)

Kustakin viestiketjusta näytetään sen luoneen käyttäjän nimi, luomisaika, ketjuun lisättyjen viestien määrä sekä ketjuun liittyvät aihetunnisteet. Samalla näytetään ketjun ensimmäinen, luomisen yhteydessä lisätty viesti.

Käyttäjän itse lisäämien viestiketjujen kohdalla näytetään myös kaksi toimintoikonia. Muokkausikonia (kynän kuva) painamalla käyttäjä voi muokata ketjun nimeä ja tallentaa uuden nimen painamalla enteriä. Poistamisikonia (ruksi) painamalla käyttäjä voi poistaa koko viestiketjun. Mikäli käyttäjällä on admin-oikeudet, hän voi muokata tai poistaa myös muiden käyttäjien lisäämiä viestiketjuja.

Käyttäjälle näytetään aina korkeintaan viisi viestiketjua. Mikäli sovellukseen on lisätty tätä enemmän ketjuja, voi käyttäjä tarkastella vanhempia ketjuja siirtymällä sivulta toiselle näkymän alareunaan ilmestyvien nuolinäppäinten avulla.

Näkymän oikeassa laidassa näytetään lisäksi _Most liked today_ -otsikon alla esikatselunäkymä viidestä eniten tykkäyksiä saaneesta ja tänään julkaistusta viestistä. Mikäli kyseisenä päivänä ei ole lisätty yhtään viestiä tai mikään niistä ei ole saanut tykkäyksiä, ei tätä osiota näytetä lainkaan. Viestien yhteydessä on _Reply_-linkki, jonka kautta käyttäjä pääsee tarkastelemaan kyseistä viestiä asiayhteydessään ja vastaamaan samaan ketjuun.

## Viestiketjun sisältö

Käyttäjä voi siirtyä tarkastelemaan ketjuun lisättyjä viestejä klikkaamalla ketjun otsikkoa:

![Viestiketjun sisältö](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/single_topic.png)

Näkymässä näytetään siis kaikki viestiketjuun lisätyt viestit ja niihin liittyvät metatiedot (kirjoittaja, lisäysaika, tykkäykset).

Käyttäjä voi tykätä viesteistä klikkaamalla niiden yhteydessä olevaan sydänpainiketta. Klikkaamalla painiketta uudelleen tykkäys on mahdollista poistaa.

Käyttäjällä on mahdollisuus muokata tai poistaa omia viestejään _Edit_ ja _Delete_-linkkien kautta. Admin-käyttäjä voi jälleen muokata tai poistaa kenen tahansa lisäämiä viestejä.

Näkymän alareunassa on myös tekstikenttä, johon käyttäjä voi kirjoittaa uuden viestin kyseiseen ketjuun. Viesti lähetetään _Add new post_ -painikkeella.

## Uuden viestiketjun lisääminen

Kirjautunut käyttäjä voi lisätä sovellukseen uuden viestiketjun siirtymällä päävalikon kautta _Add new topic_ -näkymään:

![Viestiketjun lisääminen](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/add_topic.png)

Käyttäjän tulee antaa viestiketjun otsikko, ensimmäinen viesti ja aihetunnisteet (1-3 kpl, max. 20 merkkiä).

Ketju lisätään _Add new topic_ -painikkeella. Mahdollisista validointivirheistä (esim. tyhjät kentät) ilmoitetaan käyttäjälle.

## Viestiketjujen hakeminen

Käyttäjä voi hakea viestiketjuja siirtymällä päävalikosta _Search topics_ -näkymään:

![Viestiketjujen hakeminen](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/search_topics.png)

Viestiketjuja voi hakea otsikon tai kirjoittajan (tai molempien) perusteella.

## Profiilinäkymä

Käyttäjä voi siirtyä tarkastelemaan omaa käyttäjäprofiiliaan päävalikon _My profile_ -linkistä. Lisäksi käyttäjä pääsee tarkastelemaan muiden käyttäjien profiileja klikkaamalla käyttäjän nimeä esimerkiksi foorumilla julkaistun viestin yhteydessä.

Profiilinäkymässä näytetään käyttäjän kuvaus, mahdollinen admin-status sekä tilastotietoa käyttäjästä, tämän kirjoittamista viesteistä ja niiden saamista tykkäyksistä:

![Profiilinäkymä](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/user_page.png)

_Edit profile_ -painikkeen avulla käyttäjä voi siirtyä muokkaamaan profiilikuvaustaan. Muokattu profiilikuvaus tallennetaan painamalla avautuvassa näkymässä olevaa _Save_-painiketta.

## Kaikki käyttäjät -näkymä

Sovelluksen admin-käyttäjät pääsevät päävalikon kautta myös kaikki sovelluksen käyttäjät listaavaan _All users_ -näkymään. Näkymässä tietoa kustakin käyttäjästä sekä painikkeet, joiden avulla voi muokata käyttäjille myönnettyjä admin-oikeuksia (_Give/Remove admin rights_) ja profiilikuvauksia (_Edit profile_):

![Profiilinäkymä](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/all_users.png)

## Uloskirjautuminen

Sovelluksesta voi kirjautua ulos klikkaamalla päävalikon _Log out_ -painiketta.
