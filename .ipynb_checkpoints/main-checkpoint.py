from ase import Atoms
from ase.visualize import view

# Создание молекулы NaCl
NaCl = Atoms('NaCl', positions=[(0, 0, 0), (0.5, 0.5, 0.5)])

# Визуализация молекулы
view(NaCl, viewer='x3d')