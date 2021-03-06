## PostgreSQL setup and tutorial

Let's get some data and start playing with it!


### Acquire data

First, we'll play with some tennis data from [here](https://archive.ics.uci.edu/ml/datasets/Tennis+Major+Tournament+Match+Statistics).

```bash
mkdir -p tennis/data
cd tennis/data
wget http://archive.ics.uci.edu/ml/machine-learning-databases/00300/Tennis-Major-Tournaments-Match-Statistics.zip
```

You may not have `unzip` installed yet.

```bash
sudo apt-get install unzip
unzip Tennis-Major-Tournaments-Match-Statistics.zip
```

**Data: acquired.**

Before we get into SQL, open up the files and poke around!


### Install PostgreSQL

(Mostly following the [Ubuntu directions](https://help.ubuntu.com/community/PostgreSQL).)

```bash
sudo apt-get install postgresql postgresql-contrib
```

This will install _and start up_ Postgres. You can check:

```bash
ps awx | grep post
```

On Ubuntu, servers are started and stopped mostly with [upstart](http://upstart.ubuntu.com/). Try:

```bash
sudo service postgresql status
sudo service postgresql stop
sudo service postgresql start
```

Installing Postgres also created a `postgres` user on your computer. But we want to be able to log in as ourselves. So:

```bash
sudo -u postgres createuser --superuser my_user_name
sudo -u postgres psql
# now in psql...
\password my_user_name
# exit psql...
sudo -u postgres createdb my_user_name
```

Now you can go to town with just `psql`! Explore a little with `help`, `\?`, `\l`, and `\d`.


### Getting the data into mysql database

You can create a new database with `CREATE DATABASE tennis;` -- if we use `\d`, we see there are not yet any tables (relations) in the database. So let's create one.


**Step 1: preparing the columns**

We have to specify the schema of our table, with detail about [data types](http://www.postgresql.org/docs/9.3/static/datatype.html).

```sql
CREATE TABLE  aus_ladies_2013(
      player1 VARCHAR(255),
      player2 VARCHAR(255),
      round INT,
      result INT,
      fnl1 DOUBLE PRECISION,
      fnl2 DOUBLE PRECISION,
      fsp_1 DOUBLE PRECISION,
      fsw_1 DOUBLE PRECISION,
      ssp_1 DOUBLE PRECISION,
      ssw_1 DOUBLE PRECISION,
      ace_1 INT,
      dbf_1 INT,
      wnr_1 INT,
      ufe_1 INT,
      bpc_1 INT,
      bpw_1 INT,
      npa_1 INT,
      npw_1 INT,
      tpw_1 INT,
      st1_1 INT,
      st2_1 INT,
      st3_1 INT,
      st4_1 INT,
      st5_1 INT,
      fsp_2 DOUBLE PRECISION,
      fsw_2 DOUBLE PRECISION,
      ssp_2 DOUBLE PRECISION,
      ssw_2 DOUBLE PRECISION,
      ace_2 INT,
      dbf_2 INT,
      wnr_2 INT,
      ufe_2 INT,
      bpc_2 INT,
      bpw_2 INT,
      npa_2 INT,
      npw_2 INT,
      tpw_2 INT,
      st1_2 INT,
      st2_2 INT,
      st3_2 INT,
      st4_2 INT,
      st5_2 INT);
```


**Step 2: filling the table with data**

The data has a mix of missing entries and entries that are the string `NA`. We'll use `sed` to fix that:

```bash
sed -i.bak s/NA//g AusOpen-women-2013.csv
```

Now we can load the data into Postgres.

```sql
copy aus_ladies_2013
    from '/home/my_user_name/tennis/data/AusOpen-women-2013.csv'
    delimiter ',' csv header;
```


#### Load the other tables

Hint that will save you pain: You can make a new table with the same schema as an existing table. For example:

```sql
create table aus_men_2013 (like aus_ladies_2013);
```

Extension: Can you make the tennis data tidy?


### Let's look around!

```sql
SELECT player1, player2, result FROM us_men_2013 LIMIT 5;

SELECT player1, result FROM us_men_2013 WHERE player1="Richard Gasquet";

SELECT player1, player2, result FROM us_men_2013 WHERE player1="Richard Gasquet";

SELECT player1, player2, result FROM us_men_2013 WHERE player1="Richard Gasquet" OR player2="Richard Gasquet";

SELECT COUNT(*) FROM us_men_2013;

SELECT player1, COUNT(*) FROM us_men_2013 GROUP BY player1;

SELECT player1, AVG(result) FROM us_men_2013 GROUP BY player1;

SELECT player1, player2, result FROM us_men_2013 WHERE result=1 LIMIT 5;

SELECT COUNT(*) FROM us_men_2013 WHERE result=1;

SELECT player1, player2, result FROM french_men_2013 WHERE result=1 LIMIT 5;

SELECT us_men_2013.player1, us_men_2013.tpw_1, french_men_2013.tpw_1 FROM us_men_2013, french_men_2013 WHERE us_men_2013.player1 = french_men_2013.player1;

SELECT us_men_2013.player1, us_men_2013.tpw_1, french_men_2013.tpw_1 FROM us_men_2013, french_men_2013 WHERE us_men_2013.player1 = french_men_2013.player1 GROUP BY us_men_2013.player1;

SELECT us_men_2013.player1, us_men_2013.tpw_1, french_men_2013.tpw_1, us_men_2013.tpw_1 + french_men_2013.tpw_1 AS total_points FROM us_men_2013, french_men_2013 WHERE us_men_2013.player1 = french_men_2013.player1 GROUP BY us_men_2013.player1;
```


### Python bindings

How can I access all this through python? Using the `psycopg2` module,
you can execute any query and get the results in python to do whatever
you want to them (put it in `pandas`, throw it into `sklearn`
algorithms, etc.)

Here again it will be easier to `apt-get install` than `pip install`:

```bash
sudo apt-get install python-psycopg2
```

```python
import psycopg2

db = psycopg2.connect(database='tennis')
cursor = db.cursor()

cur.execute("select * from aus_ladies_2013 limit 3")

for row in cursor.fetchall():
    print row
```
