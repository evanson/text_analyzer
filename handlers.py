import operator
import json
import logging
import tornado.web
import tornado.platform.twisted
tornado.platform.twisted.install()
from twisted.internet import threads

from tokenizer import tokenize
from db_funcs import run_update, get_word_frequencies

## Base class that has attributes common to all handlers
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

class HomeHandler(BaseHandler):
    def get(self):
        self.render("index.html")

    def post(self):
        text = self.get_argument("input_text")
        words = tokenize(text)
        word_count = {}
        for word in words:
            if word in word_count.keys():
                word_count[word] += 1
            else:
                word_count.setdefault(word, 1)

        ## Run db updates in thread to reduce response time
        d = threads.deferToThread(run_update, self.db, word_count)
        d.addErrback(catchError)

        sorted_words = sorted(word_count.iteritems(), key=operator.itemgetter(1))
        self.write(json.dumps(sorted_words))

class WordHandler(BaseHandler):
    def get(self):
        words = get_word_frequencies(self.db)
        sorted_words = sorted(words.iteritems(), key=operator.itemgetter(1))
        self.render("words.html", words=sorted_words)


def catchError(e):
    logging.error(str(e))

handlers = [
    (r"/", HomeHandler),
    (r"/words", WordHandler),
]
