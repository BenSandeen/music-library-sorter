#### To be run using pytest testing library ####

import sortMusicFiles as SM
import song as Song
# import sys,
import os
import pytest
import mutagen

class TestClass:
    """pytest automatically finds and runs these tests.  The class is effectively a means
       of organizing the tests in logical compartments"""

    # def setup(self):
    #     self.song = Song.Song()

    def test_one(self):
        """Tests initialization of the song object"""
        self.song = Song.Song()
        assert self.song.getTitle() == "No title info"
        assert self.song.getArtist() == "No artist info"
        assert self.song.getAlbum() == "No album info"
        assert self.song.getAlbumArtist() == "No albumartist info"
        assert self.song.getDate() == "No date info"
        assert self.song.getTrackNumber() == "No tracknumber info"
        assert self.song.getTrackTotal() == "No tracktotal info"

        self.song.setTitle("Bohemian Rhapsody")
        self.song.setArtist("Queen")
        self.song.setAlbum("We Will Rock You")
        self.song.setAlbumArtist("Queen")
        self.song.setDate("1980")
        self.song.setTrackNumber("1")
        self.song.setTrackTotal("20")

        assert self.song.getTitle() == "Bohemian Rhapsody"
        assert self.song.getArtist() == "Queen"
        assert self.song.getAlbum() == "We Will Rock You"
        assert self.song.getAlbumArtist() == "Queen"
        assert self.song.getDate() == "1980"
        assert self.song.getTrackNumber() == "1"
        assert self.song.getTrackTotal() == "20"

        # TODO: make sure non-string inputs are converted to strings first

    musicSorter = SM.SortMusicFiles()

    # @pytest.fixture
    # def songObject(self, myTitle="", myArtist="", myAlbum="", myAlbumArtist="", myDate="",
    #                myTrackNumber="",myTrackTotal="", myFileLocation="", myFileName=""):
    #     mySong = Song.Song()
    #     print(mySong)
    #     mySong.setTitle(myTitle)
    #     mySong.setArtist(myArtist)
    #     mySong.setAlbum(myAlbum)
    #     mySong.setAlbumArtist(myAlbumArtist)
    #     mySong.setDate(myDate)
    #     mySong.setTrackNumber(myTrackNumber)
    #     mySong.setTrackTotal(myTrackTotal)
    #     mySong.setFileLocation(myFileLocation)
    #     mySong.setFileName(myFileName)
    #     return mySong

    # mySongObject = songObject

    def test_two(self):
        """Tests intitialization of SortMusicFiles object"""
        assert self.musicSorter.musicFilesLocation  == ""
        assert self.musicSorter.outputFilesLocation == ""
        assert self.musicSorter.Songs               == []
        self.musicSorter.resetObjectToDefault()


    # def test_three(self):
    #     """Tests getting user input and setting data appropriately"""
    #     path = "/mnt/c/Users/Ben/Music/Test OGG Music"
    #     with pytest.raises(IOError):
    #         self.musicSorter.findSongs()
    #     self.musicSorter.setMusicFilesLocation(path + "/testing")
    #     self.musicSorter.findSongs()
    #     assert self.musicSorter.Songs != []
    #     # print(mutagen.File("/mnt/c/Users/Ben/Music/Test OGG Music/testing/[Mix] One and a half hours of future bass, nu funk, electro, ect.ogg"))
    #     self.musicSorter.resetObjectToDefault()


    # @pytest.fixture#(scope="module")
    # def songObjectList(self, tmpdir):
    #     titles = ["Bohemian Rhapsody","Fireflies", "Sick Beats"]
    #     artists = ["Queen", "Owl City", "KKB"]
    #     albums = ["We Will Rock You", "Deer in the Headlights", "KKB"]
    #     albumArtists = ["Queen", "Adam Something", "Sarah Midori Perry, Augustus Lobban"]
    #     dates = [1980, 2011, 2016]
    #     trackNumbers = [1, 5, 8]
    #     trackTotals = [20, 14, 12]
    #     fileLocations = ["/mnt/c/Users/Ben/Music/Test OGG Music/testing/",
    #                      "/mnt/c/Users/Ben/Music/Test OGG Music/testing/",
    #                      "/mnt/c/Users/Ben/Music/Test OGG Music/testing/"]
    #     fileNames = ["Bohemian Rhapsody.ogg", "Fireflies.mp3", "Sick Beats.flac"]
    #
    #     myDir = tmpdir.mkdir("folder")
    #     # listOfSongObjects = []
    #     for i in xrange(len(titles)):
    #         mySong = Song.Song()
    #         mySong.setTitle(titles[i])
    #         mySong.setArtist(artists[i])
    #         mySong.setAlbum(albums[i])
    #         mySong.setAlbumArtist(albumArtists[i])
    #         mySong.setDate(dates[i])
    #         mySong.setTrackNumber(trackNumbers[i])
    #         mySong.setTrackTotal(trackTotals[i])
    #         mySong.setFileLocation(fileLocations[i])
    #         mySong.setFileName(fileNames[i])
    #
    #         musicFile = mutagen.MP3(fileNames[1], ID3=mutagen.easyid3.EasyID3)
    #         musicFile.save()
    #
    #         p = myDir.join(mySong.fileName)
    #         print("$$$$$$$$$$$$$$$$$$$$",os.tempnam())
    #         print(myDir.listdir())
    #     # self.musicSorter.musicFilesLocation(myDir.path())
    #         # listOfSongObjects.append(mySong)
    #     # return listOfSongObjects
    #     return myDir

    # @pytest.fixture(scope='session')
    # def makeMockDirectory(self, tmpdir_factory, songObjectList):
    #     myDir = tmpdir_factory.mktemp("folder")#.join("piss.txt")
    #     for song in songObjectList:
    #         myDir.join(song.fileName)
    #         # song.write(str(myDir + song.fileName))
    #     print(myDir.listdir())
    #     # assert 0 == 1
    #     return myDir

    # @pytest.fixture(scope='session')
    # def image_file(tmpdir_factory):
    #     img = compute_expensive_image()
    #     fn = tmpdir_factory.mktemp('data').join('img.png')
    #     img.save(str(fn))
    #     return fn


    # def test_four(self):#, songObjectList):
    #     """Tests finding music files in desired directory"""
    #
    #     # TODO: make a function to create mock music files so we can place them in
    #     # TODO: the tmpdir, rather than having to test with actual files
    #
    #     # myDir = self.makeMockDirectory(songObjectList)
    #     # assert (len(songObjectList.listdir())) != 0
    #     # location = "/mnt/c/Users/Ben/Documents/Computer Science/music_sorter/music-library-sorter"
    #     # p = tmpdir.mkdir(location + "test_output").join("hello.txt")
    #
    #     # filenames of songs in test directory
    #     titles = [u"[Mix] One and a half hours of future bass, nu funk, electro, ect",
    #               u"_bonnie_and_clyde", u"Title",
    #               u"A Mighty Fortress Is Our God",
    #               u"Amazing Grace (From ''Revival Tonight!'')",
    #               u"Outland Main Theme",
    #               u"Bach: Concerto in D major, BWV: III. Allegro (III. Allegro)",
    #               u"Keep It for Your Own"]
    #
    #     self.musicSorter.setMusicFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing")
    #     self.musicSorter.findSongs()
    #     # assert 0 == 1
    #     assert len(self.musicSorter.Songs) > 0
    #     for i in self.musicSorter.Songs:
    #         assert i.getTitle() in titles
    #         assert os.path.isfile(i.getFileLocation())
    #         # assert 0
    #
    #     self.musicSorter.resetObjectToDefault()


    def test_five(self):
        """"Tests to make sure files are moved correctly.  Currently, this requires
        the person testing the program to inspect the testing directory themselves
        to verify that the files were sorted properly"""

        self.musicSorter.setMusicFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/A")
        self.musicSorter.setOutputFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/Music")

        self.musicSorter.sortFiles()

        # self.musicSorter.setMusicFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing_output")
        # self.musicSorter.setOutputFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing")
        #
        # self.musicSorter.sortFiles()

        # there should be no files remaining in this directory
        # assert len(os.listdir("/mnt/c/Users/Ben/Music/Test OGG Music/testing")) == 0

        self.musicSorter.resetObjectToDefault()

    # def test_six(self):
    #     pass
    #
    # def test_seven(self):
    #     pass
    #
    # def test_eight(self):
    #     pass

    # def test_nine(self):
    #     pass
