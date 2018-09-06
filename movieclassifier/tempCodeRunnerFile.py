c.execute('CREATE TABLE review_db'\
        ' (review TEXT, sentiment INTEGER, date TEXT)')

example1 = 'I love this movie'
c.execute("INSERT INTO review_db"\
        " (review, sentiment, date) VALUES"\
        " (?, ?, DATETIME('now'))", (example1, 1))

example2 = 'I disliked this movie'
c.execute("INSERT INTO review_db"\
        " (review, sentiment, date) VALUES"\
        " (?, ?, DATETIME('now'))", (example2, 0))
