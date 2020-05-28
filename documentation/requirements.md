# Vaatimusmäärittely

## Keskeisimmät käyttötapaukset

### Käyttäjäroolit

Sovellukseen on tarkoitus luoda peruskäyttäjän ja pääkäyttäjän roolit. Pääkäyttäjällä on peruskäyttäjää laajemmat oikeudet, ja hän voi esimerkiksi poistaa minkä tahansa viestin tai viestiketjun sovelluksesta. Pääkäyttäjän user storyt määritellään myöhemmin tarkemmin.

Peruskäyttäjä voi käyttää sovellusta ainakin seuraavilla tavoilla:

### Ennen kirjautumista

- käyttäjä voi luoda sovellukseen käyttäjätunnuksen (tehty)
  - käyttäjätunnukseen liittyy salasana (tehty)
  - sovellus ilmoittaa, mikäli käyttäjätunnus on jo käytössä (tehty)
  - sovellus ilmoittaa, mikäli salasana on liian lyhyt (tehty)
- käyttäjä voi kirjautua sovellukseen antamalla oikean käyttäjätunnuksen ja salasanan (tehty)
  - sovellus ilmoittaa, mikäli käyttäjätunnus tai salasana on virheellinen (tehty)

### Kirjautumisen jälkeen

- käyttäjä voi lisätä sovellukseen uuden viestiketjun (tehty)
  - viestiketjulle annetaan otsikko (tehty)
  - viestiketjuja voi merkitä aihetunnisteilla eli tageilla (1-3 kpl) (tehty)
  - viestiketjua luotaessa siihen lisätään samalla myös ensimmäinen viesti (tehty)
- käyttäjä voi tarkastella listaa sovellukseen lisätyistä viestiketjuista (tehty)
- viestiketjulistauksessa käyttäjä voi tarkastella kyseisen päivän tykätyimpien viestien listaa (tehty)
  - listaa ei näytetä, jos yhdestäkään kyseisen päivän viestistä ei ole tykätty (tehty)

- käyttäjä voi avata viestiketjun klikkaamalla ja tarkastella siihen lisättyjä viestejä (tehty)
- käyttäjä voi tykätä kustakin viestistä tasan yhden kerran (tehty)
- käyttäjä voi poistaa viestille antamansa tykkäyksen (tehty)
- käyttäjä voi poistaa sovellukseen lisäämänsä viestin
- käyttäjä voi poistaa sovellukseen lisäämänsä viestiketjun (tehty)
- käyttäjä voi muokata sovellukseen lisäämänsä viestiketjun otsikkoa (tehty)

- käyttäjä voi tarkastella omaa profiiliaan
  - profiilissa on esimerkiksi tieto käyttäjän sovellukseen lisäämien viestien ja niiden saamien tykkäyksien lukumäärästä

- käyttäjä voi hakea viestiketjuja mm. otsikon ja aihetunnisteiden avulla

- lisäksi sovelluksen pääkäyttäjät voivat poistaa minkä tahansa viestiketjun ja muokata niiden otsikoita (tehty)
