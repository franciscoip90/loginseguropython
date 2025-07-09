import sqlite3
import bcrypt

class UsuarioDB:
    def __init__(self, db_name='usuarios.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._crear_tabla()

    def _crear_tabla(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS usuarios("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "username_hash TEXT UNIQUE NOT NULL,"
            "password_hash TEXT NOT NULL)"
            )
        self.conn.commit()

    def agregar_usuario(self, username_hash, password_hash):
        try:
            self.cursor.execute('INSERT INTO usuarios (username_hash, password_hash) VALUES (?, ?)',(username_hash, password_hash))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def obtener_password_hash_por_usuario(self, username):
        self.cursor.execute('SELECT username_hash, password_hash FROM usuarios')
        for username_hash, password_hash in self.cursor.fetchall():
            if bcrypt.checkpw(username.encode('utf-8'), username_hash):
                return password_hash
        return None
    
    def cerrar(self):
        self.conn.close()
