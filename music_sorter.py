from __future__ import print_function
import mutagen as m, os
import sys
import unicodedata as ud

prohibitedSymbolsInWindowsPaths = ["\\","/",":","\"","*","?","<",">","|"]
substituteSymbolsInWindowsPaths = ["--","--",";","'","_","_","(",")","_"]

def removeBadSymbols(nameStr):
	if type(nameStr) == type(u'unicodeStr'):
		nameStr = ud.normalize("NFKD",nameStr).encode("ascii","ignore")
		# nameStr = repr(nameStr)
	for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
		if badSymbol in nameStr:
			nameStr = str(nameStr).replace(badSymbol,substituteSymbolsInWindowsPaths[idx])
	return nameStr

artistDict = {"No artist info": {"No album info": [] } }

musicFileExtensions = ['.3gp','.aa','.aac','.aax','.act','.aiff','.amr','.ape','.au','.awb','.dct','.dss','.dvf','.flac','.gsm',
					   '.iklax','.ivs','.m4a','.m4b','.m4p','.mmf','.mp3','.mpc','.msv','.ogg','.oga','.mogg','.opus','.ra','.rm',
					   '.raw','.sln','.tta','.vox','.wav','.wma','.wv','.webm']

# have to use output of Windows 10's Ubuntu terminal's command `$ pwd`
path = "/mnt/c/Users/Ben/Music/Test OGG Music"
writePath = "/mnt/c/Users/Ben/test" # so as to prevent path lengths from exceeding system limit :/
for folder in os.listdir(path):
	numSongs = len(os.listdir(path + "/" + folder))
	try:
		incrementSize = numSongs // 30
		if numSongs < 30:
			incrementSize = -1
	except:
		incrementSize = -1
	counter = 0
	print("Progress in directory " + path + "/" + folder + ": ", end="")
	for song in os.listdir(path + "/" + folder):
		song = removeBadSymbols(song)
		# if counter >= 10:
		# 	break
		for musicFileExt in musicFileExtensions: # make sure it's an audio file
			if musicFileExt in song:
				if counter % (incrementSize) == 0: # displays progress
					print("-",end="")
					sys.stdout.flush()
				try:
					artist = ((m.File(path + "/" + folder + "/" + song))["artist"])[0] # without the `[0]`, artist is a list of a string
					artist = removeBadSymbols(artist)
					try:
						album = ((m.File(path + "/" + folder + "/" + song))["album"])[0]
						# for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
						# 	if badSymbol in album:
						# 		album = str(album).replace(badSymbol,substituteSymbolsInWindowsPaths[idx])
						album = removeBadSymbols(album)
						# print(album)
						if artist in artistDict.keys():
							if album in artistDict[artist].keys():
								artistDict[artist][album].append(song)
								# print("Pos. 1\ttype(artistDict)['No artist info']: ",type(artistDict['No artist info']))
							# TODO: the next two else statements can probably be combined if we combine the preceding two
							# if statements using an `and` operator, but I'm focused on getting things correct first
							else:
								artistDict[artist] = {album: [song]}
								# print("Pos. 2\ttype(artistDict)['No artist info']: ",type(artistDict['No artist info']))
						else:
							artistDict[artist] = {album: [song]}#[song]
							# print("\nalbum:\t", album,"\ttype(album):\t",type(album))
							print("Pos. 3\ttype(artistDict)[artist]: ",type(artistDict[artist]))

					except:
						if "No album info" in artistDict[artist].keys():
							artistDict[artist]["No album info"].append(song)
							print("Pos. 4\ttype(artistDict)['No artist info']: ",type(artistDict['No artist info']))
						else:
							artistDict[artist] = [artistDict[artist], {"No album info": [song]}]
							print("Pos. 5\ttype(artistDict)['No artist info']: ",type(artistDict['No artist info']))
				except:
					try:
						album = ((m.File(path + "/" + folder + "/" + song))["album"])[0]
						album = removeBadSymbols(album)
						if album in artistDict["No artist info"].keys():
							artistDict["No artist info"][album].append(song)
							print("Pos. 6\ttype(artistDict)['No artist info']: ",type(artistDict['No artist info']))
						# TODO: the next two else statements can probably be combined if we combine the preceding two
						# if statements using an `and` operator, but I'm focused on getting things correct first
						else:
							print("Pos. 7.0\ttype(artistDict)['No artist info']: ",type(artistDict['No artist info']))
							print("Pos. 7.0\ttype(artistDict)['No artist info'][album]: ",type(artistDict['No artist info'][album]))
							# print("\nalbum:\t", album,"\ttype(album):\t",type(album))
							print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHHHHHHEEEEEEEEEEEEERRRRRRRREEEEEEEEEEE")
									# artistDict[artist] = [artistDict[artist], {"No album info": [song]}]
							artistDict["No artist info"] = [artistDict["No artist info"], {album: [song]}]
							print("Pos. 7.1\ttype(artistDict)['No artist info']: ",type(artistDict['No artist info']))


					except:
						# print("NO NOTHING")
						print("Pos. 8\ttype(artistDict)['No artist info']: ",type(artistDict['No artist info']))
						# print()
						artistDict["No artist info"]["No album info"].append(song)
						# try:
						# 	if "No album info" in artistDict["No artist info"].keys():
						# 		artistDict["No artist info"]["No album info"].append(song)
						# 	else:
						# 		artistDict["No artist info"] = [artistDict["No artist info"], {"No album info": song}]
						# except:
						# 	artistDict["No artist info"] = [artistDict["No artist info"], {"No album info": song}]
		if counter == 3:
			print(artistDict)
		counter += 1

# print("\nartistDict: ", artistDict)
# print("\nartistDict.keys(): ",artistDict.keys())
# for artist in artistDict.keys():
# 	print("artist: ", artist, "\tNumber of songs: ", len(artistDict[artist]))
songCounter = 0

# print(artistDict["Anael & Bradfield"])

while (os.getcwd() != "/mnt/c/Users/Ben"):
	os.chdir(writePath)
	for artist in artistDict.keys():
		# for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
		# 	if badSymbol in artist:
		# 		artist = str(artist).replace(badSymbol,substituteSymbolsInWindowsPaths[idx])
		# artist = removeBadSymbols(artist)
		print("Artist:\t",artist)
		if (os.path.exists(artist) == False):
			try:
				os.mkdir(artist)
			except IOError as e:
				if e.errno == errno.ENOENT:
					os.mkdir(repr(artist))
		os.chdir(artist)
		try:
			for album in artistDict[artist].keys():
				# for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
				# 	if badSymbol in album:
				# 		album = str(album).replace(badSymbol,substituteSymbolsInWindowsPaths[idx])
				# album = removeBadSymbols(album)
				print("Album:\t",album)
				e = -1
				if (os.path.exists(album) == False):
					try:
						os.mkdir(album)
					except IOError as e:
						print("We found an error!!!!!!!!!!!!!!")
						if e.errno == errno.ENOENT:
							print("We found an error!!!!!!!!!!!!!!")
							os.mkdir(repr(album))
				if e == -1:
					os.chdir(album)
				else:
					os.chdir(repr(album))
				for song in artistDict[artist][album]:
					# for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
					# 	if badSymbol in song:
					# 		song = str(song).replace(badSymbol,substituteSymbolsInWindowsPaths[idx])
					# song = removeBadSymbols(song)
					print("Song:\t",song)
					with open(song + ".txt", 'w') as outfile:
						outfile.write("Test")
					songCounter += 1
				os.chdir("..")
			os.chdir("..")
		except:
			for song in artistDict[artist]:
				# for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
				# 	if badSymbol in song:
				# 		song = str(song).replace(badSymbol,substituteSymbolsInWindowsPaths[idx])
				# song = removeBadSymbols(song)
				print("Pos 1:\tSong:\t",song)
				with open(song + ".txt", 'w') as outfile:
					outfile.write("Test")
				songCounter += 1
	break

print("Number of songs actually recorded: ", songCounter)