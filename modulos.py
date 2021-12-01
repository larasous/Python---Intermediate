"""
Módulos padrão do Python:
- Arquivos .py (que contém código python) e servem para expandir as
  funcionalidades padrão da linguagem
- Veja todos os módulos padrão do Python em:
  https://docs.python.org/3/py-modindex.html
"""
import sys  # Importa o módulo inteiro
print(sys.platform)

from sys import platform as pl # Importa um módulo específico
print(pl)

import random
print(random.randint(0,10))  # gerar um numero aleatorio de 0 a 10