import sqlite3

db_path = 'stockindex.db'

#
# Wyjątek używany w repozytorium
#
class RepositoryException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors

class StockIndex():
    """Pojedynczy indeks akcji"""
    def __init__(self, id, symbol):
        self.id = id
        self.symbol = symbol

    def __repr__(self):
        
