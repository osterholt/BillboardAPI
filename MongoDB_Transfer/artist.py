class Song:
    def __init__(self, _ID: int, name: str) -> None:
        self._ID = _ID
        self.name = name
    def __str__(self) -> str:
        return '' #TODO: Fill with string format. 

class Album:
    def __init__(self, _ID: int, name: str, peak_pos: int = 201) -> None:
        self._ID = _ID
        self.name = name
        self.peak_pos = peak_pos
        self.songs = []
    def __str__(self) -> str:
        return f'\tPeak Pos: {det_peak_pos(self.peak_pos)} | Name: {self.name}, ID: {self._ID}'
    def __eq__(self, other) -> bool:
        return other != None and self._ID == other._ID and self.name == other.name
    def __ne__(self, other) -> bool:
        return not other != None and self._ID == other._ID and self.name == other.name
    def det_peak_pos(peak_pos: int):
        if(int == 201):
            return 'N/A'
        return peak_pos

class Artist:
    def __init__(self, _ID: str, name: str) -> None:
        self._ID = _ID
        self.name = name
        self.albums = []
        #TODO: Add photo URL
    def __str__(self) -> str:
        return f'{self.name}, ID: {self._ID}'
    
    def num_albums(self) -> int:
        return len(self.albums)
    
    def add_album(self, album: Album):
        if album == None:
            return
        for al in self.albums:
            if(al.__eq__(album)):
                return
        self.albums.append(album)
    
    def remove_album(self, album: Album):
        if album == None:
            return
        for al in self.albums:
            if(al.__eq__(album)):
                self.albums.remove(al)
    def remove_album(self, _ID: int):
        for al in self.albums:
            if(al._ID == _ID):
                self.albums.remove(al)