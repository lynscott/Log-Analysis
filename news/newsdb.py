#! /usr/bin/env python3
# "Database code" for the DB News.

import psycopg2


def connect(database_name="news"):
    """Connect to the database, create cursor for resuse in multiple f(x)s"""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error: Cannot connect to database")


def get_top_articles():
    """Return the top articles from the 'database' with the amount of views"""
    db, cursor = connect()
    top_articles = """SELECT articles.title, count(log.path) AS num
                      FROM articles LEFT JOIN log
                      ON log.path = concat('/article/', articles.slug)
                      AND log.status = '200 OK'
                      GROUP BY title
                      ORDER BY num DESC LIMIT 3;"""
    cursor.execute(top_articles)
    print("Most popular articles:" '\n')
    for (title, num) in cursor.fetchall():
        print("    {} - {} views".format(title, num))
    print("-" * 70)
    db.close()


def get_top_authors():
    """Return top authors from the database with amount of views"""
    db, cursor = connect()
    top_authors = """SELECT authors.name, count(log.path) AS num
                     FROM authors, log, articles
                     WHERE log.path = concat('/article/', articles.slug)
                     AND articles.author = authors.id
                     AND log.status = '200 OK'
                     GROUP BY authors.name
                     ORDER BY num DESC;"""
    cursor.execute(top_authors)
    print("Most popular authors:" '\n')
    for (name, num) in cursor.fetchall():
        print("    {} - {} views".format(name, num))
    print("-" * 70)
    db.close()


def get_errors():
    """View days when HTTP response error exceeds 1%"""
    db, cursor = connect()
    errors = """SELECT date, round(100* (errors * 1.0 / total),1) AS percentage
                FROM (select date(time),
                count(case when status = '404 NOT FOUND'
                THEN 1 else null end) AS errors,
                count(*) AS total
                FROM log group by date(time)) AS visits
                WHERE round(100* (errors * 1.0 / total),1) > 1.0;"""
    cursor.execute(errors)
    print("Days with more than 1% errors:" '\n')
    for (date, percentage) in cursor.fetchall():
        print("    {:%B %d, %Y} - {}% errors".format(date, percentage))
    print("-" * 70)
    db.close

if __name__ == "__main__":
    get_top_articles()
    get_top_authors()
    get_errors()
