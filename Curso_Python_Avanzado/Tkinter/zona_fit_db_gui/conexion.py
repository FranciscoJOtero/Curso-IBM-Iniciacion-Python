# Este código se ha reutilizado de la App llamada zona_fit_db
from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = ''
    DB_PORT = '3306'
    HOST = 'localhost'
    POLL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    poll = None

    @classmethod
    def obtener_pool(cls):
        if cls.poll is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name = cls.POOL_NAME,
                    pool_size = cls.POLL_SIZE,
                    host = cls.HOST,
                    port = cls.DB_PORT,
                    database = cls.DATABASE,
                    user = cls.USERNAME,
                    password = cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrió un error al obtener pool: {e}')

        else:
            return cls.pool
        
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    
    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()


