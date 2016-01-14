# -*- coding: utf-8 -*-

import sqlite3

db_path = 'stockindex.db'
conn = sqlite3.connect(db_path)

c = conn.cursor()

#
# Tabele
#
c.execute('''
          DROP TABLE StockIndexQuote
          ''')

c.execute('''
          DROP TABLE StockIndex
          ''')

c.execute('''
          CREATE TABLE StockIndex
          ( id INTEGER PRIMARY KEY,
            symbol VARCHAR(100) NOT NULL
          )
          ''')

c.execute('''
          CREATE TABLE StockIndexQuote
          ( value NUMERIC NOT NULL,
            value_date DATE NOT NULL,
            stockindex_id INTEGER,
            FOREIGN KEY(stockindex_id) REFERENCES StockIndex(id),
			PRIMARY KEY (value_date, stockindex_id))
          ''')
