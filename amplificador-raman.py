# amplificador-raman.py

from binding_amplificador_raman import amplificador_raman
from pyangbind.lib.serialise import pybindIETFXMLEncoder
import pyangbind.lib.pybindJSON as pybindJSON

# Crear una instancia de AmplificadorRaman
amplificador = amplificador_raman()

# Configurar los atributos del amplificador
amplificador.amplificador_raman.potencia_bombeo = 500
amplificador.amplificador_raman.longitud_onda_bombeo = 1450.0
amplificador.amplificador_raman.longitud_onda_senal = 1550.0
amplificador.amplificador_raman.ganancia = 20

# Imprimir la representación XML y JSON del amplificador
print(pybindIETFXMLEncoder.serialise(amplificador))
#print(pybindJSON.dumps(amplificador))
