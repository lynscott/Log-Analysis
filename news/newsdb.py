# "Database code" for the DB News.

import psycopg2

DBNAME = "news"


def get_top_articles():
    """Return the top articles from the 'database' with the amount of views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    articles = c.execute("select authors.name, count(log.path)"
                         "as num"
                         "from authors, log, articles"
                         "where log.path = concat('/article/', articles.slug)"
                         "and articles.author = authors.id"
                         "and log.status = '200 OK'"
                         "group by authors.name"
                         "order by num desc;")
    return articles
    db.close()


def get_top_authors():
    """Return top authors from the database with amount of views"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    authors = c.execute("select authors.name, count(log.path) as num"
                        "from authors, log, articles"
                        "where log.path = concat('/article/', articles.slug)"
                        "and articles.author = authors.id"
                        "and log.status = '200 OK'"
                        "group by authors.name"
                        "order by num desc;")
    return authors
    db.close()


def get_errors():
    """View days when HTTP response error exceeds 1%"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    error = c.execute("select date, round(100 * (errors * 1.0 / total), 1)"
                      "as percentage"
                      "from"
                      "(select date(time),"
                      "count(case when status = '404 NOT FOUND'"
                      "then 1 else null end)"
                      "as errors,"
                      "count(*)"
                      "as total"
                      "from log group by date(time)) as visits"
                      "where round(100* (errors * 1.0 / total),1) > 1.0;")
    return error
    db.close


get_top_articles()
get_top_authors()
get_errors()
