# Sovelluksen arkkitehtuurikuvaus

## Tietokantakaavio

Sovelluksen tietokannan suunniteltua rakennetta kuvaa seuraava kaavio:
![Tietokantakaavio](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/erdiagram.png)

Sovelluksen keskeisiä käsitteitä ovat siis _User_ (käyttäjä), _Topic_ (viestiketju), _Post_ (viesti) ja _Tag_ (aihetunniste).

Käsitteiden väliset suhteet ovat seuraavat:

- Kuhunkin viestiketjuun ja viestiin liittyy yksi käyttäjä, ja kukin käyttäjä voi luoda useita viestiketjuja ja viestejä (yhden suhde moneen -yhteys).

- Kuhunkin viestiketjuun voi liittyä useita viestejä, mutta kukin viesti voi liittyä vain yhteen viestiketjuun (yhden suhde moneen -yhteys).

- Viestiketjuja voidaan luokitella aihetunnisteilla eli tageilla. Kuhunkin viestiketjuun voi liittyä useita tunnisteita, ja kukin tunniste voi liittyä useaan viestiketjuun (monen suhde moneen -yhteys).
