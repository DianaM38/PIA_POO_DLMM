#con esta libreria voy a hacer la prueba de unittest de enviaar una isntruccion, en el futuro cunaod mejore este proyecto hare mas
import unittest
from Conexion import ConexionSerial

# heredo de unittest.TestCase por los metodos que implementan los casos de prueba y por que asi lo dice la doc' 
class pruebaConexionSerial(unittest.TestCase):
    def test_mandar_instruccion(self):
        conexionSerial= ConexionSerial()
        conexionSerial.simular=None
        try:
            conexionSerial.enviar('V',6,180)
        except Exception:
            self.fail('fallo el metodo enviar')


if __name__=='__main__':
    unittest.main()

