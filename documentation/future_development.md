# Jatkokehitysideoita ja sovellukseen jääneitä puutteita

Sovelluksen keskeisimmät ominaisuudet tulivat toteutetuiksi harjoitustyön aikana. Joistain toiminnallisuuksista nousee kuitenkin esiin selkeitä kehitysideoita:

## Haku

Hakutoiminnallisuus jäi hieman tyngäksi eli esimerkiksi aihetunnisteita ei vielä hyödynnetä haussa. Hakua voisi kehittää myös niin, että hakiessa voisi valita, hakeeko avainsanoja vain viestiketjun otsikosta vai myös viestien sisällöstä. Lisäksi haku palauttaa tällä hetkellä esimerkiksi kaikki ketjut, joiden kirjoittajan nimessä esiintyy hakusanana käytetty käyttäjänimi – olisi hyvä, jos käyttäjä voisi hakea myös täsmällisemmin juuri yhden käyttäjän lisäämät ketjut.

## Käyttäjäroolit

Käyttäjän rooli määritellään tällä hetkellä vain boolean-tyyppisellä _is_admin_-muuttujalla. Tämä yksinkertainen ratkaisu riittää tässä vaiheessa mainiosti, mutta jatkossa sovellukseen olisi syytä luoda erillinen rooli-entiteetti, joka mahdollistaisi käyttäjäoikeuksien monipuolisemman hallinnan. Tällä hetkellä ongelmallista on esimerkiksi se, että admin-käyttäjät voivat vapaasti poistaa toisiltaan admin-oikeudet. Olisi parempi, että sovelluksessa olisi erikseen varsinaiset pääkäyttäjät, jotka voisivat antaa ylimääräisiä oikeuksia vaikkapa viestejä hallinnoiville moderaattoreille.

## HTML

Eristin joitain usein toistuvia elementtejä erillisiksi template-tiedostoiksi, mutta sovelluksen HTML-sivuissa on edelleen jonkin verran toistoa. HTML-tiedostot olisikin syytä pilkkoa pienempiin, modulaarisiin osiin.

## Sovelluksen arkkitehtuuri

Sovelluksen kontrollerikerroksessa on – kurssimateriaalia seuraten – paljon sovelluslogiikkaa, joka olisi ehkä hyvä siirtää erilliseen kerrokseen. Samalla olisi helpompi poistaa kontrollereissa jonkin verran toistuvaa koodia.
