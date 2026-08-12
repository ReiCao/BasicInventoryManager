import sqlite3

class InventoryManager:
    def __init__(self):
        self.inventory_path = "inventory.db"

        self.connect = sqlite3.connect(self.inventory_path)
        conn = self.connect

        self.cursor = conn.cursor()
        cursor = self.cursor

        cursor.execute("""CREATE TABLE IF NOT EXISTS inventory (
                            Id INTEGER PRIMARY KEY,
                            Name TEXT NOT NULL,
                            Amount INTEGER,
                            Price REAL
                            )""")

        conn.commit()

    def get_inventory(self) -> list:
        cursor = self.cursor

        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()

        return rows

    def is_valid_id(self, id_: int) -> bool:
        cursor = self.cursor

        cursor.execute("SELECT 1 FROM inventory WHERE Id = ?", (id_,))
        exists = cursor.fetchone() is not None

        if exists: return True
        else: return False

    def add_item(self, name: str, amount: int, price: float) -> None:
        cursor = self.cursor
        conn = self.connect

        cursor.execute("INSERT INTO inventory VALUES (NULL, ?, ?, ?)", (name, amount, price))

        conn.commit()

    def edit_name(self, id_: int, name: str) -> None:
        cursor = self.cursor
        conn = self.connect

        cursor.execute("UPDATE inventory SET Name = ? WHERE Id = ?", (name, id_,))

        conn.commit()

    def edit_amount(self, id_: int, amount: int) -> None:
        cursor = self.cursor
        conn = self.connect

        cursor.execute("UPDATE inventory SET Amount = ? WHERE Id = ?", (amount, id_,))

        conn.commit()

    def edit_price(self, id_: int, price: float) -> None:
        cursor = self.cursor
        conn = self.connect

        cursor.execute("UPDATE inventory SET Price = ? WHERE Id = ?", (price, id_,))

        conn.commit()

    def remove_item(self, id_: int) -> None:
        cursor = self.cursor
        conn = self.connect

        cursor.execute("DELETE FROM inventory WHERE Id = ?", (id_,))

        conn.commit()

    def end_connection(self) -> None:
        self.connect.close()