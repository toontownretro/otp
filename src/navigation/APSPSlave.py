import pickle as pickle
from otp.navigation.NavMesh import NavMesh
import sys


# Custom: buffer in Python 3
args = sys.stdin.buffer.read()

filepath,filename,startRow,endRow = pickle.loads(args)

mesh = NavMesh(filepath, filename)
mesh.generatePathData((startRow,endRow))
mesh.printPathData()
sys.stdout.flush()
sys.stdout.close()
