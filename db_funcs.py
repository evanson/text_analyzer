## Database utility functions

def run_update(db, words):
    stored_words = get_stored_words(db)
    for (word, count) in words.items():
        if word in stored_words:
            db.execute("UPDATE words SET frequency=frequency+%s WHERE word = %s", count, word)
        else:
            db.execute("INSERT INTO words (word, frequency) VALUES (%s, %s)", word, count)

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
