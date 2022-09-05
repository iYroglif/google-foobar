from base64 import b64decode
from itertools import cycle

message = "DEIRGAINSxAcSldfQkoGHEsCG0pbRUUODgJCBg4KAgBFTVtOCQYcGRIADwgFSQJDSAgRAw0fFR0J Q1VNUAwMDhMLSgoNARJCTk1GD00LBggBAA8IDxoJQ1VNUBAMAQ4NRQYLSltFRR8ADEwKGx5QRVhN Rh1PBQpKW0VFCw4BCUNVTVASCwNASVM="
key = "webman.com"
for m, k in zip(b64decode(message), cycle(key)):
    print(chr(m ^ ord(k)), end="")
print()
