import math

SEMIFACTOR = 2 ** (1 / 12)

BASENAMES = [
	("AX",),
	("BbX", "A#X"),
	("BX", "CbX"),
	("CX",),
	("DbX", "C#X"),
	("DX"),
	("EbX", "D#X"),
	("EX",),
	("FX", "E#X"),
	("GbX", "F#X"),
	("GX",),
	("AbX", "G#X")
]

FLAT = "b"
NATURAL = "N"
SHARP = "#"

class NoteName:
	def __init__(self, letter, accidental, number

class Key:
	def __init__(self, name):
		self.name = name
		self.frequency = 
