#! /
from __future__ import print_function
import unicodedata as ud
import song as Song
import os
import mutagen
import shutil
# import easygui as eg
try:
    from Tkinter import Tk
    from tkFileDialog import askdirectory
except:
    pass

class SortMusicFiles:
    def __init__(self):
        self.musicFilesLocation = ""
        self.outputFilesLocation = ""
        self.Songs = []
        self.firstSortingCriteria = "albumartist"
        self.secondSortingCriteria = "album"
        self.thirdSortingCriteria = ""

    def resetObjectToDefault(self):
        """Used only for testing, so we don't have to create a bunch of separate objects"""
        self.__init__()

    def setMusicFilesLocation(self, fileLoc):
        self.musicFilesLocation = fileLoc

    def setMusicFilesLocationFromUserInput(self):
        """This may be updated in the future with a GUI"""
        try:
            Tk().withdraw()
            location = askdirectory()
        except:
            doesPathExist = 0
            while not doesPathExist:
                location = raw_input("Enter path to your music:\t")
                if os._exists(location, os.R_OK): # can we `R`ead from the path?
                    doesPathExist = 1

        self.setMusicFilesLocation(location)
        # self.setMusicFilesLocation(self.removeBadSymbolsInPathName(raw_input("What is the path where your music is located?\t")))

    def getMusicFilesLocation(self):
        return self.musicFilesLocation

    def setOutputFilesLocation(self, fileLoc):
        self.outputFilesLocation = fileLoc

    def setOutputFilesLocationFromUserInput(self):
        """This may be updated in the future with a GUI"""
        try:
            Tk().withdraw()
            location = askdirectory()
        except:
            doesPathExist = 0
            while not doesPathExist:
                location = raw_input("Enter path to where you want your music to go:\t")
                if os._exists(location, os.W_OK): # can we `W`rite to the path?
                    doesPathExist = 1

        self.setOutputFilesLocation(location)

    def getOutputFilesLocation(self):
        return self.outputFilesLocation

    def findSongs(self):
        """Searches musicFilesLocation for music files, then puts it in Songs list"""
        if self.musicFilesLocation == "":
            self.setMusicFilesLocationFromUserInput()
            # raise IOError

        musicFileExtensions = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.amr',
                               '.ape', '.au', '.awb', '.dct', '.dss', '.dvf', '.flac',
                               '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf',
                               '.mp3', '.mpc', '.msv', '.ogg', '.oga', '.mogg', '.opus',
                               '.ra', '.rm', '.raw', '.sln', '.tta', '.vox', '.wav',
                               '.wma', '.wv', '.webm']
        # dirQueue = [] # queue for holding directories, so we can recurse into them
        for thing in os.walk(self.musicFilesLocation):
            # print("level 1")
            for ext in musicFileExtensions:
                # print("level 2")
                # thing is tuple: (pathname, dirs, files)
                # we want the files.  os.walk then recurses into any dirs, so we catch files in there too
                for possibleMusicFile in thing[2]:
                    # print("level 3")
                    if ext in possibleMusicFile:
                        # print("level 4")
                        # TODO: give this song object the correct data members
                        newSong = Song.Song()
                        metadata = mutagen.File(thing[0] +"/"+ possibleMusicFile)
                        # print("metadata:\t",metadata)
                        # print(mutagen.File(self.musicFilesLocation + "/"+thing))
                        newSong.setFileName(possibleMusicFile)
                        # print("PATH OF FILE:\t",self.musicFilesLocation + "/")
                        newSong.setFileLocation(thing[0] + "/") #self.musicFilesLocation + "/")
                        newSong.getSongInfoFromFile()
                        # try:
                        #     newSong.setTitle(metadata["title"][0])
                        # except KeyError as e:
                        #     print(e)
                        # try:
                        #     newSong.setArtist(metadata["artist"][0])
                        # except KeyError as e:
                        #     print(e)
                        # try:
                        #     newSong.setAlbum(metadata["album"][0])
                        # except KeyError as e:
                        #     print(e)
                        # try:
                        #     newSong.setAlbumArtist(metadata["albumartist"][0])
                        # except KeyError as e:
                        #     print(e)
                        # try:
                        #     newSong.setDate(metadata["date"][0])
                        # except KeyError as e:
                        #     print(e)
                        # try:
                        #     newSong.setTrackNumber(metadata["tracknumber"][0])
                        # except KeyError as e:
                        #     print(e)
                        # try:
                        #     newSong.setTrackTotal(metadata["tracktotal"][0])
                        # except KeyError as e:
                        #     print(e)

                        self.Songs.append(newSong)

    def getSortingCriteriaDataByCriteriaPriority(self, song, priority):
        """Gets data from Song object according to the music file sorter's first
        sorting criteria"""

        # switch statement allows us to obtain the appropriate data, depending on
        # what the sorting criteria is set to.  Not executing the functions (that's
        # why the parentheses at the end are omitted) should, in theory, reduce some
        # overhead of unnecessary function calls, but I don't know how much work that
        # is compared with doing what I did below
        switchStatement = {"artist": song.getArtist, "album": song.getAlbum,
                           "albumartist": song.getAlbumArtist, "title": song.getTitle,
                           "date": song.getDate, "tracknumber": song.getTrackNumber,
                           "tracktotal": song.getTrackTotal}
        # use a list, since we'll pass in an int as the priority
        criteriaByPriority = [self.firstSortingCriteria, self.secondSortingCriteria,
                              self.thirdSortingCriteria]

        # since some files don't have album artist metadata, but nearly all have artist metadata, we're first trying
        # to sort by album artist to prevent songs featuring other artists from being separated from the rest of
        # an album produced without that featured artist
        if (criteriaByPriority[priority] == "albumartist" and
                (switchStatement[criteriaByPriority[priority]]() == "No albumartist info")):
            print("No album artist info, using artist info instead")
            return switchStatement["artist"]()
        return switchStatement[criteriaByPriority[priority]]()

    def moveSong(self, song):
        """Moves a single song.  Makes sure not to create a folder if one by the same
        name already exists"""
        # TODO: split these lines up into separate try-excepts, because it is possible
        # TODO: that it will succeed at making the dirs but fail at moving the file,
        # TODO: and the code as it currently is would yield errors on the later
        # TODO: try-excepts, because the directory would already exist
        if self.thirdSortingCriteria != "":
            currentLocation = song.getFileLocation() + song.getFileName()
            destination = (self.outputFilesLocation + "/" +
                          self.getSortingCriteriaDataByCriteriaPriority(song,0) + "/" +
                          self.getSortingCriteriaDataByCriteriaPriority(song,1) + "/" +
                          self.getSortingCriteriaDataByCriteriaPriority(song,2))

            if os.path.exists(destination):
                shutil.move(currentLocation, destination)
            else:
                os.makedirs(destination)
                shutil.move(currentLocation, destination)
        else:
            # print("Song Artist:\t",song.getArtist())
            currentLocation = song.getFileLocation() + song.getFileName()
            destination = (self.outputFilesLocation + "/" +
                           self.getSortingCriteriaDataByCriteriaPriority(song, 0) + "/" +
                           self.getSortingCriteriaDataByCriteriaPriority(song, 1))

            if os.path.exists(destination):
                try:
                    shutil.move(currentLocation, destination)
                except Exception as e:
                    print("Current file location:\t", currentLocation)
                    print("File destination:\t", destination)
                    print(e)
            else:
                try:
                    os.makedirs(destination)
                except Exception as e:
                    print("Current file location:\t", currentLocation)
                    print("File destination:\t", destination)
                    print(e)

                try:
                    shutil.move(currentLocation, destination)
                except Exception as e:
                    print("Current file location:\t", currentLocation)
                    print("File destination:\t", destination)
                    print(e)

        #     shutil.move(song.getFileLocation() + song.getFileName(), self.musicFilesLocation + "/" +
        #                     self.getSortingCriteriaDataByCriteriaPriority(song,0) + "/" +
        #                     self.getSortingCriteriaDataByCriteriaPriority(song,1) + "/" +
        #                     self.getSortingCriteriaDataByCriteriaPriority(song,2))
        #         shutil.move(song.getFileLocation() + song.getFileName(), self.musicFilesLocation + "/" +
        #                     self.getSortingCriteriaDataByCriteriaPriority(song, 0) + "/" +
        #                     self.getSortingCriteriaDataByCriteriaPriority(song, 1))
        # else:
        #     # print(e)
        #     shutil.move(song.getFileLocation() + song.getFileName(), self.musicFilesLocation + "/" +
        #                 self.getSortingCriteriaDataByCriteriaPriority(song, 0) + "/" +
        #                 self.getSortingCriteriaDataByCriteriaPriority(song, 1))
        #
        # # if all directories have been made successfully
        # if os.access(self.musicFilesLocation + "/" +
        #              self.getSortingCriteriaDataByCriteriaPriority(song,0) + "/" +
        #              self.getSortingCriteriaDataByCriteriaPriority(song,1) + "/" +
        #              self.getSortingCriteriaDataByCriteriaPriority(song,2), os.F_OK):
        #     shutil.move(song.getFileLocation() + song.getFileName(),
        #                 self.musicFilesLocation + "/" +
        #                 self.getSortingCriteriaDataByCriteriaPriority(song,0) + "/" +
        #                 self.getSortingCriteriaDataByCriteriaPriority(song,1) + "/" +
        #                 self.getSortingCriteriaDataByCriteriaPriority(song,2))
        #
        # # if only first 2 were created
        # elif os.access(self.musicFilesLocation + "/" +
        #              self.getSortingCriteriaDataByCriteriaPriority(song,0) + "/" +
        #              self.getSortingCriteriaDataByCriteriaPriority(song,1), os.F_OK):
        #     shutil.move(song.getFileLocation() + song.getFileName(),
        #                 self.musicFilesLocation + "/" +
        #                 self.getSortingCriteriaDataByCriteriaPriority(song,0) + "/" +
        #                 self.getSortingCriteriaDataByCriteriaPriority(song,1))
        #
        # # if only first directory was created (shouldn't happen, but just in case)
        # elif os.access(self.musicFilesLocation + "/" +
        #              self.getSortingCriteriaDataByCriteriaPriority(song,0), os.F_OK):
        #     shutil.move(song.getFileLocation() + song.getFileName(),
        #                 self.musicFilesLocation + "/" +
        #                 self.getSortingCriteriaDataByCriteriaPriority(song,0))
        #
        # else:
        #     print("Something went dreadfully amiss, and we were unable to relocate your song.")

    def sortFiles(self):
        """Actually handles the sorting of the music files"""
        self.findSongs()
        if self.getOutputFilesLocation() == "":
            self.setOutputFilesLocationFromUserInput()
        numSongs = len(self.Songs)
        onePercentOfNumSongs = (numSongs / 100) + 1 # add 1 to avoid divide by 0 errors
        counter = 0
        print("Music Location:\t",self.getMusicFilesLocation())
        print("Output Location:\t",self.getOutputFilesLocation())
        print("songs:\t",self.Songs)
        print("Number of songs:\t", numSongs)
        print("Progress:\t",end="")
        for song in self.Songs:
            if counter % onePercentOfNumSongs == 0:
                print("-",end="")
            self.moveSong(song)
            counter += 1

        self.cleanup()

    def cleanup(self):
        """Asks user if they want to remove empty directories, and does it if they wish"""
        # TODO: prompt the user to decide this before running


    def removeBadSymbolsInPathName(self, path):
        """Removes symbols incompatible Windows's file system"""
        prohibitedSymbolsInWindowsPaths = ["\\", "/", ":", "\"", "*", "?", "<", ">", "|"]
        substituteSymbolsInWindowsPaths = ["--", "--", ";", "'", "_", "_", "(", ")", "_"]
        if type(path) == type(u'unicodeStr'):
            path = ud.normalize("NFKD", path).encode("ascii", "ignore")
        # nameStr = repr(nameStr)
        for idx, badSymbol in enumerate(prohibitedSymbolsInWindowsPaths):
            if badSymbol in path:
                path = str(path).replace(badSymbol, substituteSymbolsInWindowsPaths[idx])
        return path

    # def getSongInfoAndCreateSongObject(self):

##############################################################
# below is code to test basic things

s = SortMusicFiles()
# for thing in os.walk("/mnt/c/Users/Ben/Music/Test OGG Music/Music/"):
#     print(thing)

# s.setMusicFilesLocation("/mnt/a/Music/OGG Music")
# s.setOutputFilesLocation("/mnt/a/Music/testing")
s.setMusicFilesLocation("/mnt/a/Music/sample music for testing")
s.setOutputFilesLocation("/mnt/a/Music/testing")
# s.setMusicFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing")
# s.setOutputFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing_output")

s.sortFiles()

# s.Songs = ["hi"]
# s.resetObjectToDefault()
