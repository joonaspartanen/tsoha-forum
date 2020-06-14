# Tietokantarakenteen kuvaus

## Tietokantakaavio

Sovelluksen tietokannan suunniteltua rakennetta kuvaa seuraava kaavio (päivitetty viikolla 4):

![Tietokantakaavio](https://raw.githubusercontent.com/joonaspartanen/tsoha-forum/master/documentation/images/db_structure.png)

Sovelluksen keskeisiä käsitteitä ovat siis _User_ (käyttäjä), _Topic_ (viestiketju), _Post_ (viesti) ja _Tag_ (aihetunniste).

Käsitteiden väliset suhteet ovat seuraavat:

- Kuhunkin viestiketjuun ja viestiin liittyy yksi ketjun tai viestin luonut käyttäjä. Kukin käyttäjä voi luoda useita viestiketjuja ja viestejä (yhden suhde moneen -yhteys).

- Kuhunkin viestiin voi liittyä useita käyttäjiä, jotka ovat tykänneet kyseisestä viestistä. Kukin käyttäjä voi tykätä useista viesteistä (monen suhde moneen -yhteys).

- Kuhunkin viestiketjuun voi liittyä useita viestejä, mutta kukin viesti voi liittyä vain yhteen viestiketjuun (yhden suhde moneen -yhteys).

- Viestiketjuja voidaan luokitella aihetunnisteilla eli tageilla. Kuhunkin viestiketjuun voi liittyä useita tunnisteita, ja kukin tunniste voi liittyä useaan viestiketjuun (monen suhde moneen -yhteys).

## CREATE TABLE -lauseet

```sql
CREATE TABLE tags (
    id INTEGER NOT NULL,
    date_created DATETIME,
    name VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);
```

```sql
CREATE TABLE accounts (
    id INTEGER NOT NULL,
    date_created DATETIME,
    username VARCHAR(100) NOT NULL,
    pw_hash VARCHAR(144) NOT NULL,
    description VARCHAR(1000),
    is_admin BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    CHECK (is_admin IN (0, 1))
);
CREATE UNIQUE INDEX ix_accounts_username ON accounts (username);
```

```sql
CREATE TABLE topics (
    id INTEGER NOT NULL,
    date_created DATETIME,
    date_modified DATETIME,
    subject VARCHAR(100) NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(author_id) REFERENCES accounts (id)
);
CREATE INDEX ix_topics_author_id ON topics (author_id);
```

```sql
CREATE TABLE posts (
    id INTEGER NOT NULL,
    date_created DATETIME,
    date_modified DATETIME,
    body VARCHAR(1000) NOT NULL,
    topic_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(topic_id) REFERENCES topics (id),
    FOREIGN KEY(author_id) REFERENCES accounts (id)
);
CREATE INDEX ix_posts_author_id ON posts (author_id);
CREATE INDEX ix_posts_topic_id ON posts (topic_id);
```

```sql
CREATE TABLE tag_topics (
    tag_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    FOREIGN KEY(tag_id) REFERENCES tags (id),
    FOREIGN KEY(topic_id) REFERENCES topics (id)
);
CREATE INDEX ix_tag_topics_topic_id ON tag_topics (topic_id);
CREATE INDEX ix_tag_topics_tag_id ON tag_topics (tag_id);
```

```sql
CREATE TABLE post_likes (
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(post_id) REFERENCES posts (id),
    FOREIGN KEY(user_id) REFERENCES accounts (id)
);
CREATE INDEX ix_post_likes_post_id ON post_likes (post_id);
CREATE INDEX ix_post_likes_user_id ON post_likes (user_id);
```

## Indeksit

SQLAlchemy luo taulujen pääavaimille automaattisesti indeksit. Kuten CREATE TABLE ja CREATE INDEX -lauseista näkyy, on myös viiteavaimille lisätty indeksit, sillä sovelluksessa tehdään paljon liitoskyselyjä, joissa käsitellään useita tauluja.

Tämän lisäksi käyttäjän _username_-sarakkeelle on lisätty indeksi, sillä sovelluksessa joudutaan usein hakemaan käyttäjiä käyttäjänimen perusteella.
