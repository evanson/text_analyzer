## Database utility functions
import logging
def run_update(db, words):
    stored_words = get_stored_words(db)
    insert_query = "INSERT INTO words (word, frequency) VALUES"
    temp_insert_query = "INSERT INTO temp_words (word, frequency) VALUES"
    insert = False
    update = False
    for (word, count) in words.items():
        if word in stored_words:
            update = True
            temp_insert_query += "(\"%s\", \"%s\")," % (word, count)
        else:
            insert = True
            insert_query += "(\"%s\", \"%s\")," % (word, count)


    ## Run batch queries to increase throughput
    if insert:
        exc_insert_query = insert_query[:-1]
        db.execute(exc_insert_query)

    if update:
        exc_temp_insert_query = temp_insert_query[:-1]
        db.execute("CREATE TABLE temp_words (word TEXT, frequency INT)")
        db.execute(exc_temp_insert_query)
        db.execute("UPDATE words w, temp_words tw SET w.frequency=w.frequency+tw.frequency WHERE w.word=tw.word")
        db.execute("DROP TABLE temp_words")

def get_stored_words(db):
    words = []
    for word in db.query("SELECT DISTINCT * FROM words"):
        words.append(str(word.word))
    return words

def get_word_frequencies(db):
    words = {}
    for word in db.query("SELECT DISTINCT * FROM words"):
       words.setdefault(str(word.word).capitalize(), int(word.frequency))
    return words
