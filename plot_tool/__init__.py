import os
from PyQt5.QtCore import QProcessEnvironment
env = QProcessEnvironment.systemEnvironment()
base = os.path.dirname(__file__)
env.insert('PYTHONPATH', os.path.join(base, '../..'))
