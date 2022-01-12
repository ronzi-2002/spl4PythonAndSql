class Hat:
    def __init__(self, id, topping,supplier,quantity):
        self.id = id
        self.topping = topping
        self.supplier = supplier
        self.quantity = quantity

class Supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Order:
    def __init__(self, id, location,hat):
        self.id = id
        self.location = location
        self.hat = hat


class _Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""
               INSERT INTO hats (id, topping,supplier,quantity) VALUES (?,?,?,?)
           """, [hat.id, hat.topping, hat.supplier, hat.quantity])

    def findID(self,topping):
        c = self._conn.cursor()
        c.execute("""
                   SELECT *  FROM hats WHERE topping = ? order by supplier limit 1
               """, [topping] )
        return Hat(*c.fetchone())

    def updateQuntity(self,hat):
        c = self._conn.cursor()
        c.execute("""
                        UPDATE hats SET quantity=quantity-1 WHERE id = ? 
                       """, [hat.id])

    def delete(self,id):
        c = self._conn.cursor()
        c.execute("""
                                DELETE FROM hats WHERE id = ? 
                               """, [id])
    # def find(self, student_id):
    #     c = self._conn.cursor()
    #     c.execute("""
    #         SELECT id, name FROM students WHERE id = ?
    #     """, [student_id])
    #     return Student(*c.fetchone())

class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
               INSERT INTO suppliers (id, name) VALUES (?,?)
           """, [supplier.id, supplier.name])

class _Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
               INSERT INTO orders (id, location,hat) VALUES (?,?,?)
           """, [order.id, order.location,order.hat])
