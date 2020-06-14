# Keskeisimmät käyttötapaukset

Tässä dokumentissa on esitelty sovelluksen keskeisimmät käyttötapaukset. Kaikki tässä listatut toiminnallisuudet on jo toteutettu sovellukseen.

## Käyttäjäroolit

Sovelluksessa on peruskäyttäjän ja pääkäyttäjän eli admin-käyttäjän roolit. Pääkäyttäjällä on peruskäyttäjää laajemmat oikeudet, ja hän voi esimerkiksi poistaa minkä tahansa viestin tai viestiketjun sovelluksesta.

## Ennen kirjautumista

### Käyttäjä voi luoda sovellukseen käyttäjätunnuksen

- käyttäjätunnukseen liittyy salasana
- sovellus ilmoittaa, mikäli käyttäjätunnus on jo käytössä
- sovellus ilmoittaa, mikäli salasana on liian lyhyt

Käyttäjätunnusta luotaessa tarkistetaan ensin, onko tunnus jo varattu (esim. tunnus _tsohauser_):

```sql
SELECT * FROM accounts
  WHERE username = 'tsohauser'
  LIMIT 1;
```

Mikäli tunnus on vapaana, tallennetaan käyttäjä tietokantaan kyselyllä:

```sql
INSERT INTO accounts (date_created, username, pw_hash, description, is_admin) VALUES (CURRENT_TIMESTAMP, 'tsohauser', ?, "", 0);
```

### Käyttäjä voi kirjautua sovellukseen antamalla oikean käyttäjätunnuksen ja salasanan

- sovellus ilmoittaa, mikäli käyttäjätunnus tai salasana on virheellinen

Kirjautumisessa hyödynnetään jälleen kyselyä:

```sql
SELECT * FROM accounts
  WHERE username = 'tsohauser'
  LIMIT 1;
```

## Kirjautumisen jälkeen

### Käyttäjä voi lisätä sovellukseen uuden viestiketjun

- viestiketjulle annetaan otsikko
- viestiketjuja voi merkitä aihetunnisteilla eli tageilla (1-3 kpl)
- viestiketjua luotaessa siihen lisätään samalla myös ensimmäinen viesti

Viestiketjun lisääminen toteutetaan käytännössä useilla kyselyillä, sillä myös ketjun ensimmäinen viesti ja mahdolliset uudet aihetunnisteet tulee tallentaa tietokantaan.

Varsinainen viestiketju:

```sql
INSERT INTO topics (date_created, date_modified, subject, author_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?);
```

Uudet aihetunnisteet:

```sql
INSERT INTO tags (date_created, date_modified, name) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?);
```

Aihetunnisteiden ja viestiketjujen liitostaulu:

```sql
INSERT INTO tag_topics (tag_id, topic_id) VALUES (?, ?);
```

Ensimmäinen viesti:

```sql
INSERT INTO posts (date_created, date_modified, body, topic_id, author_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?);
```

### Käyttäjä voi tarkastella listaa sovellukseen lisätyistä viestiketjuista

SQLAlchemy käyttää viestiketjujen hakemiseen seuraavaa kyselyä:

```sql
SELECT anon_1.topics_id AS anon_1_topics_id, anon_1.topics_date_created AS anon_1_topics_date_created, anon_1.topics_date_modified AS
  anon_1_topics_date_modified, anon_1.topics_subject AS anon_1_topics_subject, anon_1.topics_author_id AS anon_1_topics_author_id, accounts_1.id AS accounts_1_id, accounts_1.date_created AS accounts_1_date_created, accounts_1.username AS accounts_1_username, accounts_1.pw_hash AS accounts_1_pw_hash, accounts_1.description AS accounts_1_description, accounts_1.is_admin AS accounts_1_is_admin, posts_1.id AS posts_1_id, posts_1.date_created AS posts_1_date_created, posts_1.date_modified AS posts_1_date_modified, posts_1.body AS posts_1_body, posts_1.topic_id AS posts_1_topic_id, posts_1.author_id AS posts_1_author_id, tags_1.id AS tags_1_id, tags_1.date_created AS tags_1_date_created, tags_1.date_modified AS tags_1_date_modified, tags_1.name AS tags_1_name FROM (SELECT topics.id AS topics_id, topics.date_created AS topics_date_created, topics.date_modified AS topics_date_modified, topics.subject AS topics_subject, topics.author_id AS topics_author_id FROM topics ORDER BY topics.date_created DESC LIMIT ? OFFSET ?) AS anon_1
LEFT OUTER JOIN accounts AS accounts_1 ON accounts_1.id = anon_1.topics_author_id
LEFT OUTER JOIN posts AS posts_1 ON anon_1.topics_id = posts_1.topic_id
LEFT OUTER JOIN (tag_topics AS tag_topics_1 JOIN tags AS tags_1 ON tags_1.id = tag_topics_1.tag_id) ON anon_1.topics_id = tag_topics_1.topic_id
ORDER BY anon_1.topics_date_created DESC
```

Kyselyssä on huomionarvoista, että samalla kertaa haetaan myös viestiketjuihin liittyvät aihetunnisteet ja viestit sekä ketjun lisänneen käyttäjän tiedot. Tämä johtuu siitä, että viestiketjut listaavassa näkymässä näytetään myös näihin muihin entiteetteihin liittyviä tietoja. Mikäli haettaisiin vain viestiketjun tiedot, jouduttaisiin kutakin ketjua kohti tekemään myös uusi esim. käyttäjän tiedot hakea kysely (n+1 kyselyn ongelma).

Kysely hyödyntää myös sivutusta (LIMIT ja OFFSET-parametrit), jottei kysely muuttuisi liian raskaaksi viestiketjujen määrän kasvaessa.

### Viestiketjulistauksessa käyttäjä voi tarkastella kyseisen päivän tykätyimpien viestien listaa

- listaa ei näytetä, jos yhdestäkään kyseisen päivän viestistä ei ole tykätty

Toiminnallisuus on toteutettu seuraavalla yhteenvetokyselyllä:

```sql
SELECT Posts.id, Posts.date_created, Posts.date_modified, Posts.body, Post_likes.likes, Posts.topic_id, Posts.author_id, Accounts.username FROM Posts
JOIN
  (SELECT post_id, COUNT(post_id) AS likes FROM Post_likes GROUP BY post_id)
    AS Post_likes ON Posts.id = Post_likes.post_id
JOIN Accounts ON Posts.author_id = Accounts.id
  WHERE date(Posts.date_created) = date('now')
  ORDER BY likes DESC
  LIMIT 5;
```

### Käyttäjä voi avata viestiketjun klikkaamalla ja tarkastella siihen lisättyjä viestejä

Käytettävässä kyselyssä haetaan jälleen samalla kertaa myös muut näkymässä tarvittavat tiedot (aihetunnisteet, käyttäjät):

```sql
SELECT topics.id AS topics_id, topics.date_created AS topics_date_created, topics.date_modified AS topics_date_modified, topics.subject AS topics_subject,
  topics.author_id AS topics_author_id, accounts_1.id AS accounts_1_id, accounts_1.date_created AS accounts_1_date_created, accounts_1.username AS accounts_1_username,
  accounts_1.pw_hash AS accounts_1_pw_hash, accounts_1.description AS accounts_1_description, accounts_1.is_admin AS accounts_1_is_admin, posts_1.id AS posts_1_id,
  posts_1.date_created AS posts_1_date_created, posts_1.date_modified AS posts_1_date_modified, posts_1.body AS posts_1_body, posts_1.topic_id AS posts_1_topic_id,
  posts_1.author_id AS posts_1_author_id, tags_1.id AS tags_1_id, tags_1.date_created AS tags_1_date_created, tags_1.date_modified AS tags_1_date_modified, tags_1.name AS tags_1_name
FROM topics
LEFT OUTER JOIN accounts AS accounts_1 ON accounts_1.id = topics.author_id
LEFT OUTER JOIN posts AS posts_1 ON topics.id = posts_1.topic_id
LEFT OUTER JOIN (tag_topics AS tag_topics_1 JOIN tags AS tags_1 ON tags_1.id = tag_topics_1.tag_id) ON topics.id = tag_topics_1.topic_id
WHERE topics.id = ?;

```

### Käyttäjä voi tykätä kustakin viestistä tasan yhden kerran

```sql
INSERT INTO post_likes (post_id, user_id) VALUES (?, ?);
```

### Käyttäjä voi poistaa viestille antamansa tykkäyksen

```sql
DELETE FROM post_likes WHERE post_likes.post_id = ? AND post_likes.user_id = ?
```

### Käyttäjä voi poistaa sovellukseen lisäämänsä viestiketjun

Varsinaisen viestiketjun poistamisen lisäksi poistetaan muut siihen liittyvät tiedot (liitostaulujen rivit, viestit):

```sql
DELETE FROM tag_topics WHERE tag_topics.tag_id = ? AND tag_topics.topic_id = ?;
DELETE FROM post_likes WHERE post_likes.post_id = ? AND post_likes.user_id = ?;
DELETE FROM posts WHERE posts.id = ?;
DELETE FROM topics WHERE topics.id = ?;
```

### Käyttäjä voi muokata sovellukseen lisäämänsä viestiketjun otsikkoa

```sql
UPDATE topics SET date_modified=CURRENT_TIMESTAMP, subject=? WHERE topics.id = ?;
```

### Käyttäjä voi lisätä sovellukseen viestejä

```sql
INSERT INTO posts (date_created, date_modified, body, topic_id, author_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?);
```

### Käyttäjä voi poistaa sovellukseen lisäämänsä viestin

```sql
DELETE FROM posts WHERE posts.id = ?;
```

### Käyttäjä voi muokata sovellukseen lisäämäänsä viestiä

```sql
UPDATE posts SET date_modified=CURRENT_TIMESTAMP, body=? WHERE posts.id = ?
```

### Käyttäjä voi tarkastella omaa tai muiden käyttäjien profiilia

- profiilissa on tieto käyttäjän sovellukseen lisäämien viestien ja niiden saamien tykkäyksien lukumäärästä
- profiilissa on tieto käyttäjän sovellukseen lisäämien viestiketjujen määrästä
- käyttäjäprofiilissa on käyttäjän kuvaus

Koska profiilinäkymään kuuluu monenlaisia tietoja, toteutetaan siihen liittyvä tiedonhaku laajana yhteenvetokyselynä:

```sql
SELECT Accounts.id, Accounts.username, Accounts.description, Accounts.is_admin, Accounts.date_created,
  Post_likes.likes, Posts.posts_amount, Topics.topics_amount FROM Accounts
LEFT JOIN (SELECT author_id, COUNT(post_id) AS likes FROM Post_likes
              LEFT JOIN Posts ON Post_likes.post_id = Posts.id
              GROUP BY author_id) AS Post_likes
                ON Post_likes.author_id = Accounts.id
LEFT JOIN (SELECT author_id, COUNT(id) AS posts_amount FROM Posts
  GROUP BY author_id) AS Posts
  ON Accounts.id = Posts.author_id
LEFT JOIN (SELECT author_id, COUNT(id) AS topics_amount FROM Topics
  GROUP BY author_id) AS Topics
  ON Accounts.id = Topics.author_id
WHERE Accounts.id = ?;
```

### Käyttäjä voi muokata omaa kuvaustaan

```sql
UPDATE accounts SET description=? WHERE accounts.id = ?;
```

### Käyttäjä voi hakea viestiketjuja otsikon ja kirjoittajan nimen avulla

Haku on toteutettu seuraavan SQL-kyselyn avulla. Kysely hakee myös kunkin ketjun ensimmäisen viestin, joka näytetään hakutulosnäkymässä:

```sql
SELECT Topics.id AS topic_id, Topics.date_created, Topics.date_modified,
  Topics.subject,Accounts.id AS author_id, Accounts.username, Initial_posts.body
FROM Topics
JOIN Accounts ON Accounts.id = Topics.author_id
JOIN (SELECT topic_id, body FROM Posts
        WHERE id IN(SELECT MIN(id) FROM Posts GROUP BY topic_id)) AS Initial_posts
  ON Topics.id=Initial_posts.topic_id
WHERE subject LIKE ? AND Accounts.username LIKE ?
ORDER BY Topics.date_created DESC;)
```

### Pääkäyttäjät voivat poistaa minkä tahansa viestiketjun ja muokata niiden otsikoita

Toiminnallisuudet käyttävät samoja kyselyjä kuin peruskäyttäjänkin tapauksessa.

### Pääkäyttäjät voivat poistaa minkä tahansa viestin tai muokata sitä

Toiminnallisuudet käyttävät samoja kyselyjä kuin peruskäyttäjänkin tapauksessa.

### Pääkäyttäjät voivat tarkastella listausta kaikista sovelluksen käyttäjistä

Käyttäjälistaus haetaan seuraavalla yhteenvetokyselyllä, joka hakee samalla kunkin käyttäjän sovellukseen lisäämien viestien ja viestiketjujen määrät:

```sql
SELECT accounts.id, accounts.username, accounts.date_created,
  accounts.is_admin, posts.posts_amount, topics.topics_amount
FROM accounts
LEFT JOIN (SELECT posts.author_id, COUNT(posts.id) AS posts_amount
          FROM posts
          GROUP BY author_id)
          AS posts
          ON posts.author_id = accounts.id
LEFT JOIN (SELECT topics.author_id, COUNT(topics.id) AS topics_amount
          FROM topics
          GROUP BY author_id)
          AS topics
          ON topics.author_id = accounts.id
ORDER BY accounts.username;
```

### Pääkäyttäjät voivat muokata muille käyttäjille myönnettyjä admin-oikeuksia

```sql
UPDATE accounts SET is_admin=? WHERE accounts.id = ?;
```

### Pääkäyttäjät voivat muokata muiden käyttäjien kuvauksia

Toiminnallisuus käyttää samoja kyselyjä kuin peruskäyttäjänkin tapauksessa.
