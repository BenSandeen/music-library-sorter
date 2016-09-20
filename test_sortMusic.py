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

    musicSorter = SM.SortMusicFiles()

    def test_two(self):
        """Tests intitialization of SortMusicFiles object"""
        assert self.musicSorter.musicFilesLocation  == ""
        assert self.musicSorter.outputFilesLocation == ""
        assert self.musicSorter.Songs               == []
        self.musicSorter.resetObjectToDefault()

    def test_three(self):
        """Tests getting user input and setting data appropriately"""
        path = "/mnt/c/Users/Ben/Music/Test OGG Music"
        with pytest.raises(IOError):
            self.musicSorter.findSongs()
        self.musicSorter.setMusicFilesLocation(path + "/testing")
        self.musicSorter.findSongs()
        assert self.musicSorter.Songs != []
        print(mutagen.File("/mnt/c/Users/Ben/Music/Test OGG Music/testing/[Mix] One and a half hours of future bass, nu funk, electro, ect.ogg"))
        self.musicSorter.resetObjectToDefault()

    def test_four(self, tmpdir):
        """Tests sorting and writing files to directory"""
        # location = "/mnt/c/Users/Ben/Documents/Computer Science/music_sorter/music-library-sorter"
        # p = tmpdir.mkdir(location + "test_output").join("hello.txt")

        # filenames of songs in test directory
        titles = ["[Mix] One and a half hours of future bass, nu funk, electro, ect.ogg",
                  "001_bonnie_and_clyde.ogg", "001_Title.ogg",
                  "01 - A Mighty Fortress Is Our God.ogg",
                  "01 - Amazing Grace (From ''Revival Tonight!'').ogg",
                  "01 - Ari Pulkkinen - Outland Main Theme.ogg",
                  "01 - Bach_ Concerto in D major, BWV_ III. Allegro (III. Alle.ogg",
                  "01 - Keep It for Your Own.ogg"]

        self.musicSorter.setMusicFilesLocation("/mnt/c/Users/Ben/Music/Test OGG Music/testing")
        print("song files:\t", os.listdir(self.musicSorter.getMusicFilesLocation()))
        print("Songs:\t", self.musicSorter.Songs)
        self.musicSorter.findSongs()
        print("Songs:\t", self.musicSorter.Songs)
        assert len(self.musicSorter.Songs) > 0

        # myDir = tmpdir.mkdir("sub")
        # p = []

        # for song in titles:
        #     p.append(myDir.join(song))
        #
        # print(tmpdir.listdir())
        # assert len(tmpdir.listdir()) == 1

        self.musicSorter.resetObjectToDefault()

    def test_five(self):
        pass

    def test_six(self):
        pass

    def test_seven(self):
        pass

    def test_eight(self):
        pass

    def test_nine(self):
        pass
