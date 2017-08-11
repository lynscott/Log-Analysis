#! /usr/bin/env python3
# "Database code" for the DB News.

import psycopg2


def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")


def get_top_articles():
    """Return the top articles from the 'database' with the amount of views"""
    db, cursor = connect()
    top_articles = "select title from articles, log count(path) "
    "as num "
    "from articles left join log "
    "on log.path = concat('/article/', articles.slug) "
    "and log.status = '200 OK' "
    "group by title "
    "order by num desc limit 3; "
    cursor.execute(top_articles)
    print("Most popular articles")
    for (title, num) in cursor.fetchall():
        print("    {} - {} views".format(title, num))
        print("-" * 70)
    db.close()


def get_top_authors():
    """Return top authors from the database with amount of views"""
    db, cursor = connect()
    top_authors = "select name from authors, log count(path) as num "
    "from authors, log, articles "
    "where log.path = concat('/article/', articles.slug) "
    "and articles.author = authors.id "
    "and log.status = '200 OK' "
    "group by authors.name "
    "order by num desc; "
    cursor.execute(top_authors)
    print("Most popular authors")
    for (name, num) in c.fetchall():
        print("    {} - {} views".format(name, num))
        print("-" * 70)
    db.close()


def get_errors():
    """View days when HTTP response error exceeds 1%"""
    db, cursor = connect()
    errors = "select date, round(100 * (errors * 1.0 / total), 1) "
    "as percentage from "
    "(select date(time), "
    "count(case when status = '404 NOT FOUND' "
    "then 1 else null end) as errors, "
    "count(*) as total "
    "from log group by date(time)) as visits "
    "where round(100* (errors * 1.0 / total),1) > 1.0; "
    cursor.execute(top_articles)
    print("Days with more than 1% errors:")
    for (date, percentage) in cursor.fetchall():
        print("    {} - {} errors".format(date, percentage))
        print("-" * 70)
    db.close

if __name__ == "__main__":
    get_top_articles()
    get_top_authors()
    get_errors()
