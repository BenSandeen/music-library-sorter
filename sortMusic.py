from __future__ import print_function
import mutagen as m, os
import sys
import unicodedata as ud

prohibitedSymbolsInWindowsPaths = ["\\","/",":","\"","*","?","<",">","|"]
substituteSymbolsInWindowsPaths = ["--","--",";","'","_","_","(",")","_"]

class Song:
	def __init__(self):
		"""initializer function initializes data members to default values"""
		self.title = "No title info"
		self.artist = "No artist info"
		self.album = "No album info"
		self.albumartist = "No albumartist info"
		self.date = "No date info"
		self.tracknumber = "No tracknumber info"
		self.tracktotal = "No tracktotal info"

	def getTitle(self):
		return self.title

	def setTitle(self, title):
		self.title = title

	def getArtist(self):
		return self.artist

	def setArtist(self, artist):
		self.artist = artist

	def getAlbum(self):
		return self.album

	def setAlbum(self, album):
		self.album = album

	def getAlbumArtist(self):
		return self.albumartist

	def setAlbumArtist(self, albumartist):
		self.albumartist = albumartist

	def getDate(self):
		return self.date

	def setDate(self, date):
		self.date = date

	def getTrackNumber(self):
		return self.tracknumber

	def setTrackNumber(self, tracknumber):
		self.tracknumber = tracknumber

	def getTrackTotal(self):
		return self.tracktotal

	def setTrackTotal(self, tracktotal):
		self.tracktotal = tracktotal

a = Song()
a.setArtist("Poops McGee")
a.getArtist()

def removeBadSymbols(nameStr):
	if type(nameStr) == type(u'unicodeStr'):
		nameStr = ud.normalize("NFKD",nameStr).encode("ascii","ignore")
		# nameStr = repr(nameStr)
	for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
		if badSymbol in nameStr:
			nameStr = str(nameStr).replace(badSymbol,substituteSymbolsInWindowsPaths[idx])
	return nameStr

musicFileExtensions = ['.3gp','.aa','.aac','.aax','.act','.aiff','.amr','.ape','.au','.awb','.dct','.dss','.dvf','.flac','.gsm',
					   '.iklax','.ivs','.m4a','.m4b','.m4p','.mmf','.mp3','.mpc','.msv','.ogg','.oga','.mogg','.opus','.ra','.rm',
					   '.raw','.sln','.tta','.vox','.wav','.wma','.wv','.webm']