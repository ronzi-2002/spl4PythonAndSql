import atexit
import sqlite3




# For Join query
class SupplierOfTopping:
    def __init__(self, hatId, supplierName):
        self.hatId =hatId
        self.supplierName = supplierName

# The Repository
from DAOsAndDTOs import _Hats, _Suppliers, _Orders


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.hats = _Hats(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.orders = _Orders(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def getHatIdWithSupllierName(self):
        c = self._conn.cursor()
        all = c.execute("""
               SELECT hats.id, suppliers.name 
               FROM hats
               JOIN suppliers ON hats.supplier = suppliers.id
           """).fetchall()
        return [SupplierOfTopping(*row) for row in all]

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE IF NOT EXISTS hats  (
            id      INT         PRIMARY KEY,
            topping    TEXT        NOT NULL,
            supplier  INT,
            quantity    TEXT        NOT NULL,
            
            FOREIGN KEY(supplier)     REFERENCES Supplier(id)
        );
    
        CREATE TABLE IF NOT EXISTS  suppliers (
            id      INT         PRIMARY KEY,
            name     TEXT    NOT NULL
        );
    
        CREATE TABLE IF NOT EXISTS orders (
            id      INT     PRIMARY KEY,
            location  TEXT     NOT NULL,
            hat           INT     NOT NULL,
            
    
            FOREIGN KEY(hat)     REFERENCES hats(id)
            
        );
    """)
        #self._conn.commit()

repo=_Repository()
atexit.register(repo._close)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
