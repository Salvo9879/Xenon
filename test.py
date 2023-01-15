
from xenon.spotify import Album, Artist, Show, Episode, Audiobook, Chapter, Track, SearchItem, User
from xenon.spotify import ArtistsRequests as ar_r
from xenon.spotify import AlbumRequests as al_r
from xenon.spotify import ShowsRequests as sh_r
from xenon.spotify import EpisodesRequests as ep_r
from xenon.spotify import AudiobooksRequests as au_r
from xenon.spotify import ChaptersRequests as ch_r
from xenon.spotify import TracksRequests as tr_r
from xenon.spotify import SearchRequests as se_r
from xenon.spotify import UsersRequests as us_r

import json

# ALBUM: 2cWBwpqMsDJC1ZUwz813lo
# ARTIST: 7dGJo4pcD2V6oG8kP0tJRR
# SHOW: 0ofXAdFIQQRsCYj9754UFx
# EPISODE: 1dB8CTWkoYMEeCtGgA6CH1
# AUDIOBOOK: 7r556qBSQ8LTLddVQsx8IH
# CHAPTER: N/A
# TRACK: 26XaOsDMbl0e1cVKYfkz6w
# USER: nhqsksjhsj5gzj5kjjy1ygpfp
# PLAYLIST: 15sZyUgStYmvzm3QfdVDIp

ngr = us_r.UnfollowPlaylist('15sZyUgStYmvzm3QfdVDIp')
ngr.create_request()