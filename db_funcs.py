## Database utility functions

def run_update(db, words):
    stored_words = get_stored_words(db)
    insert_query = "INSERT INTO words (word, frequency) VALUES"

    for (word, count) in words.items():
        if word in stored_words:
            db.execute("UPDATE words SET frequency=frequency+%s WHERE word = %s", count, word)            
        else:
            insert_query += "(\"%s\", \"%s\")," % (word, count)

    ## Run batch queries to increase throughput
    exc_insert_query = insert_query[:-1]
    db.execute(exc_insert_query)

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
