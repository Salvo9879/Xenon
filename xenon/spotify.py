
# Import internal modules
from xenon.models import ObjectScaffold, GetRequest, PutRequest, DeleteRequest
from xenon.helpers import convert_iso_to_dt

# Import external modules
import datetime


TOKEN = '' 



#* ====================================================================================================================================================================================================
#* MODELS



def _headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {TOKEN}"
    }

class Album(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def type_(self) -> str:
        """ The type of the album. """
        return self.get_data()['album_type']

    @property
    def total_tracks(self) -> int:
        """ The number of tracks in the album. """
        return self.get_data()['total_tracks']

    @property
    def available_markets(self) -> list:
        """ The markets in which the album is available: ISO 3166-1 alpha-2 country codes. NOTE: an album is considered available in a market when at least 1 of its tracks is available in that market. """
        return self.get_data()['available_markets']

    @property
    def external_urls(self) -> dict:
        """ Known external URLs for this album. """
        return self.get_data()['external_urls']

    @property
    def href(self) -> dict:
        """ A link to the Web API endpoint providing full details of the album. """
        return self.get_data()['href']

    @property
    def album_id(self) -> dict:
        """ The Spotify ID for the album. """
        return self.get_data()['id']
    
    @property
    def images(self) -> list:
        """ The cover art for the album in various sizes, widest first. """
        return self.get_data()['images']

    @property
    def name(self) -> str:
        """ The name of the album. In case of an album takedown, the value may be an empty string. """
        return self.get_data()['name']

    @property
    def release_date(self) -> datetime.datetime:
        """ The date the album was first released. """
        return convert_iso_to_dt(self.get_data()['release_date'])

    @property
    def release_date_precision(self) -> str:
        """ The precision with which `self.release_date` property is known. """

    @property
    def uri(self) -> str:
        """ The Spotify URI for the album. """
        return self.get_data()['uri']

    @property
    def album_artists(self) -> list:
        """ Returns a list of the artists. """
        artists_list = []
        for artist in self.get_data()['artists']:
            artists_list.append(Artist(artist))

        return artists_list

    @property
    def album_tracks(self) -> list:
        """ Returns a list of tracks """
        tracks_list = []
        for track in self.get_data()['tracks']['items']:
            tracks_list.append(Track(track))

        return tracks_list

class Artist(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def external_urls(self) -> dict:
        """ Known external URLs for this artist. """
        return self.get_data()['external_urls']

    @property
    def followers(self) -> int:
        """ The total numbers of followers. """
        return self.get_data()['followers']

    @property
    def genres(self) -> list:
        """ A list of the genres the artist is associated with. If not yet classified, the list is empty. """
        return self.get_data()['genres']

    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the artist. """
        return self.get_data()['href']

    @property
    def artist_id(self) -> str:
        """ The Spotify ID for this artist. """
        return self.get_data()['id']

    @property
    def images(self) -> list:
        """ Images of the artist in various sizes, widest first. """
        return self.get_data()['images']

    @property
    def name(self) -> str:
        """ The name of the artist. """
        return self.get_data()['name']

    @property
    def popularity(self) -> int:
        """ The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's tracks. """
        return self.get_data()['popularity']

    @property
    def type_(self) -> str:
        """ The type of the artist. """
        return self.get_data()['type']

    @property
    def uri(self) -> str:
        """ The Spotify URI of the artist. """
        return self.get_data()['uri']

class Show(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def available_markets(self) -> list:
        """ A list of the countries in which the show can be played, identified by their ISO 3166-1 alpha-2 code. """
        return self.get_data()['available_markets']

    @property
    def copyrights(self) -> list:
        """ The copyright statements of the show. """
        return self.get_data()['copyrights']

    @property
    def description(self) -> str:
        """ A description of the show. HTML tags are stripped away from this property, use html_description property in case HTML tags are needed. """
        return self.get_data()['description']

    @property
    def html_description(self) -> str:
        """ A description of the show. This field may contain HTML tags. """
        return self.get_data()['html_description']

    @property
    def explicit(self) -> bool:
        """ Whether or not the show has explicit content (`True` = yes it does; `False` = no it does not OR unknown). """
        return self.get_data()['explicit']

    @property
    def external_urls(self) -> dict:
        """ External URLs for this show. """
        return self.get_data()['external_urls']

    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the show. """
        return self.get_data()['href']

    @property
    def show_id(self) -> str:
        """ The Spotify ID of the show. """
        return self.get_data()['id']

    @property
    def images(self) -> str:
        """ The cover art for the show in various sizes, widest first. """
        return self.get_data()['images']

    @property
    def is_externally_hosted(self) -> bool:
        """ `True` if all of the shows episodes are hosted outside of Spotify's CDN. This property might be `None` in some cases. """
        return self.get_data()['is_externally_hosted']

    @property
    def languages(self) -> list:
        """ A list of the languages used in the show, identified by their ISO 639 code. """
        return self.get_data()['languages']

    @property
    def media_type(self) -> str:
        """ The media type of the show. """
        return self.get_data()['media_type']

    @property
    def name(self) -> str:
        """ The name of the show. """
        return self.get_data()['name']

    @property
    def publisher(self) -> str:
        """ The publisher of the show. """
        return self.get_data()['publisher']

    @property
    def type_(self) -> str:
        """ The type of the show """
        return self.get_data()['type']

    @property
    def uri(self) -> str:
        """ The Spotify URI of the show. """
        return self.get_data()['uri']

    @property
    def episodes(self) -> list:
        """ The episodes of the show. """
        episodes_list = []
        for episode in self.get_data()['episodes']['items']:
            episodes_list.append(Episode(episode))

        return episodes_list

    @property
    def total_episodes(self) -> int:
        """ The amount of total episodes that were created under this show name. """
        return self.get_data()['total_episodes']

class Episode(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def audio_preview_url(self) -> str:
        """ A URL to a 30 second preview (MP3 format) of the episode. `None` if not available.  """
        return self.get_data()['audio_preview_url']

    @property
    def description(self) -> str:
        """ A description of the episode. HTML tags are stripped away from this property, use `html_description` property in case HTML tags are needed. """
        return self.get_data()['description']

    @property
    def html_description(self) -> str:
        """ A description of the episode. This property may contain HTML tags. """
        return self.get_data()['html_description']

    @property
    def duration(self) -> int:
        """ The episode length in milliseconds. """
        return self.get_data()['duration_ms']

    @property
    def explicit(self) -> bool:
        """ Whether or not the episode has explicit content (`True` = yes it does; `False` = no it does not OR unknown). """
        return self.get_data()['explicit']

    @property
    def external_urls(self) -> dict:
        """ External urls for this episode. """
        return self.get_data()['external_urls']

    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the episode. """
        return self.get_data()['href']

    @property
    def episode_id(self) -> str:
        """ The Spotify ID of the episode. """
        return self.get_data()['id']

    @property
    def images(self) -> list:
        """ The cover art for the episode in various sizes, widest first. """
        return self.get_data()['images']

    @property
    def is_externally_hosted(self) -> bool:
        """ `True` if the episode is hosted outside of Spotify's CDN. """
        return self.get_data()['is_externally_hosted']

    @property
    def is_playable(self) -> bool:
        """ `True` if the episode is playable in the given market. Otherwise `False`. """
        return self.get_data()['is_playable']

    @property
    def languages(self) -> list:
        """ A list of the languages used in the episode, identified by their ISO 639-1 code. """
        return self.get_data()['languages']

    @property
    def name(self) -> str:
        """ The name of the episode. """
        return self.get_data()['name']

    @property
    def release_date(self) -> str:
        """ he date the episode was first released, for example "1981-12-15". Depending on the precision, it might be shown as "1981" or "1981-12". """
        return self.get_data()['release_date']

    @property
    def release_date_precision(self) -> str:
        """ The precision with which release_date value is known. Allowed values: "year" "month" "day" """
        return self.get_data()['release_date_precision']

    @property
    def resume_point(self) -> dict:
        """ The user's most recent position in the episode. Set if the supplied access token is a user token and has the scope `user-read-playback-position`. """
        return self.get_data()['resume_point']

    @property
    def type_(self) -> str:
        """ The type of the episode. """
        return self.get_data()['type']

    @property
    def uri(self):
        """ The Spotify URI of the episode. """
        return self.get_data()['uri']

    @property
    def restrictions(self):
        """ Included in the response when a content restriction is applied. See Restriction Object for more details.

        The reason for the restriction. Supported values:

        market - The content item is not available in the given market.
        product - The content item is not available for the user's subscription type.
        explicit - The content item is explicit and the user's account is set to not play explicit content.

        Additional reasons may be added in the future. Note: If you use this field, make sure that your application safely handles unknown values. """
        if 'restrictions' in self.get_data():
            return self.get_data()['restrictions']
        return None

    @property
    def linked_show(self) -> Show:
        """ Information about the show that the episode is released under. """
        return Show(self.get_data()['show'])

class Audiobook(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def authors(self) -> list:
        """ The author(s) for the audiobook. """
        return self.get_data()['authors']

    @property
    def available_markets(self) -> list:
        """ A list of the countries in which the audiobook can be played, identified by their ISO 3166-1 alpha-2 code. NOTE: Audiobooks are only available for the US, UK, Ireland, New Zealand and Australia markets."""
        return self.get_data()['available_markets']
    
    @property
    def copyrights(self) -> dict:
        """ The copyright statements of the audiobook. """
        return self.get_data()['copyrights']

    @property
    def description(self) -> str:
        """ A description of the audiobook. HTML tags are stripped away from this property, use html_description property in case HTML tags are needed. """
        return self.get_data()['description']

    @property
    def html_description(self) -> str:
        """ A description of the audiobook. This property may contain HTML tags. """
        return self.get_data()['html_description']

    @property
    def explicit(self) -> bool:
        """ Whether or not the audiobook has explicit content (`True` = yes it does; `False` = no it does not OR unknown). """
        return self.get_data()['explicit']

    @property
    def external_urls(self) -> dict:
        """ External URLs for this audiobook. """
        return self.get_data()['external_urls']

    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the audiobook. """
        return self.get_data()['href']

    @property
    def audiobook_id(self) -> str:
        """ The Spotify ID of the audiobook. """
        return self.get_data()['id']

    @property
    def images(self) -> list:
        """ The cover art for the audiobook in various sizes, widest first. """
        return self.get_data()['images']

    @property
    def languages(self) -> list:
        """ A list of the languages used in the audiobook, identified by their ISO 639 code. """
        return self.get_data()['languages']

    @property
    def media_type(self) -> str:
        """ The media type of the audiobook. """
        return self.get_data()['media_type']

    @property
    def narrators(self) -> dict:
        """ Information about the narrator(s) of the audiobook. """
        return self.get_data()['narrators']

    @property
    def publisher(self) -> str:
        """ The publisher of the audiobook. """
        return self.get_data()['publisher']

    @property
    def type_(self) -> str:
        """ The type of the audiobook. """
        return self.get_data()['type']

    @property
    def uri(self) -> str:
        """ The Spotify URI for the audiobook. """
        return self.get_data()['uri']

    @property
    def total_chapters(self) -> int:
        """ The number of total chapters in this audiobook. """
        return self.get_data()['total_chapters']

    @property
    def chapters(self) -> list:
        """ Returns a list of the chapters included in this audiobook. """
        chapters_list = []
        for chapter in self.get_data()['chapters']['items']:
            chapters_list.append(Chapter(chapter))

        return chapters_list

class Chapter(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def audio_preview_url(self) -> str:
        """ A URL to a 30 second preview (MP3 format) of the chapter. `None` if not available. """
        return self.get_data()['audio_preview_url']

    @property
    def chapter_number(self) -> int:
        """ The number of total chapters. """
        return self.get_data()['chapter_number']

    @property
    def description(self) -> str:
        """ A description of the chapter. HTML tags are stripped away from this `property`, use `html_description` property in case HTML tags are needed. """
        return self.get_data()['description']

    @property
    def html_description(self) -> str:
        """ A description of the chapter. This property may contain HTML tags. """
        return self.get_data()['html_description']

    @property
    def duration(self) -> int:
        """ The chapter length in milliseconds. """
        return self.get_data()['duration_ms']

    @property
    def explicit(self) -> bool:
        """ Whether or not the chapter has explicit content (`True` = yes it does; `False` = no it does not OR unknown). """
        return self.get_data()['explicit']

    @property
    def external_urls(self) -> dict:
        """ External URLs for this chapter. """
        return self.get_data()['external_urls']

    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the chapter. """
        return self.get_data()['href']

    @property
    def chapter_id(self) -> str:
        """ The Spotify ID for this chapter. """
        return self.get_data()['id']

    @property
    def images(self) -> list:
        """ The cover art for the chapter in various sizes, widest first. """
        return self.get_data()['images']

    @property
    def is_playable(self) -> bool:
        """ `True` if the chapter is playable in the given market. Otherwise `False`. """
        return self.get_data()['is_playable']

    @property
    def languages(self) -> list:
        """ A list of the languages used in the chapter, identified by their ISO 639-1 code. """
        return self.get_data()['languages']

    @property
    def name(self) -> str:
        """ The name of the chapter. """
        return self.get_data()['name']

    @property
    def release_date(self) -> str:
        """ The date the chapter was first released, for example "1981-12-15". Depending on the precision, it might be shown as "1981" or "1981-12". """
        return self.get_data()['release_date']

    @property
    def release_date_precision(self) -> str:
        """ The precision with which release_date value is known. Allowed values: "year" "month" "day". """
        return self.get_data()['release_date_precision']

    @property
    def resume_point(self) -> dict:
        """ The user's most recent position in the chapter. Set if the supplied access token is a user token and has the scope 'user-read-playback-position'. """
        return self.get_data()['resume_point']

    @property
    def type_(self) -> str:
        """ The type of chapter. """
        return self.get_data()['type_']

    @property
    def uri(self) -> str:
        """ The Spotify URI of the chapter. """
        return self.get_data()['uri']

    @property
    def restrictions(self) -> dict:
        """ Included in the response when a content restriction is applied. See Restriction Object for more details.

        The reason for the restriction. Supported values:

        market - The content item is not available in the given market.
        product - The content item is not available for the user's subscription type.
        explicit - The content item is explicit and the user's account is set to not play explicit content.

        Additional reasons may be added in the future. Note: If you use this field, make sure that your application safely handles unknown values. """
        if 'restrictions' in self.get_data():
            return self.get_data()['restrictions']
        return None

    @property
    def linked_audiobook(self) -> Audiobook:
        """ Information about the audiobook that the chapter is released under. """
        return Audiobook(self.get_data()['audiobook'])

class Track(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def linked_album(self) -> Album:
        """ Information about the album that the track is released under. """
        return Album(self.get_data()['album'])

    @property
    def artists(self) -> list:
        artists_list = []
        for artist in self.get_data()['artists']:
            artists_list.append(Artist(artist))
        
        return artists_list

    @property
    def available_markets(self) -> list:
        """ A list of the countries in which the track can be played, identified by their ISO 3166-1 alpha-2 code. """
        return self.get_data()['available_markets']

    @property
    def disc_number(self) -> int:
        """ The disc number (usually `1` unless the album consists of more than one disc). """
        return self.get_data()['disc_number']

    @property
    def duration(self) -> int:
        """ The track length in milliseconds. """
        return self.get_data()['duration_ms']

    @property
    def explicit(self) -> bool:
        """ Whether or not the track has explicit lyrics ( `True` = yes it does; `False` = no it does not OR unknown). """
        return self.get_data()['explicit']

    @property
    def external_ids(self) -> dict:
        """ Known external IDs for the track. """
        return self.get_data()['external_ids']

    @property
    def external_urls(self) -> dict:
        """ Known external URLs for this track. """
        return self.get_data()['external_urls']

    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the track. """
        return self.get_data()['href']

    @property
    def track_id(self) -> str:
        """ The Spotify ID of the track. """
        return self.get_data()['id']

    @property
    def is_playable(self) -> bool:
        """ Part of the response when Track Relinking is applied. If `True`, the track is playable in the given market. Otherwise `False`. """
        return self.get_data()['is_playable']

    @property
    def linked_from(self) -> dict:
        """ Part of the response when Track Relinking is applied, and the requested track has been replaced with different track. The track in the linked_from object contains information about the 
        originally requested track. """
        return self.get_data()['linked_from']

    @property
    def restrictions(self) -> None | dict:
        """ Included in the response when a content restriction is applied. See Restriction Object for more details. """
        if 'restrictions' in self.get_data():
            return self.get_data()['restrictions']
        return None
    
    @property
    def name(self) -> str:
        """ The name of the track. """
        return self.get_data()['name']

    @property
    def popularity(self) -> int:
        """ The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.
        The popularity of a track is a value between 0 and 100, with 100 being the most popular. The popularity is calculated by algorithm and is based, in the most part, on the total number of plays
        the track has had and how recent those plays are. Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. 
        Duplicate tracks (e.g. the same track from a single and an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. Note: the popularity 
        value may lag actual popularity by a few days: the value is not updated in real time. """
        return self.get_data()['popularity']

    @property
    def preview_url(self) -> str:
        """ A link to a 30 second preview (MP3 format) of the track. Can be `None`. """
        return self.get_data()['preview_url']

    @property
    def track_number(self) -> int:
        """ The number of the track. If an album has several discs, the track number is the number on the specified disc. """
        return self.get_data()['track_number']

    @property
    def type_(self) -> str:
        """ The type of track. """
        return self.get_data()['type']

    @property
    def uri(self) -> str:
        """ The spotify URI for the track. """
        return self.get_data()['uri']

    @property
    def is_local(self) -> bool:
        """ Whether or not the track is from a local file. """
        return self.get_data()['is_local']

class SearchItem(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def _get_data_by_identifier(self, identifier: str, obj: object) -> list:
        data_list = []
        for data_item in self.get_data()[identifier]['items']:
            data_list.append(obj(data_item))

        return data_list

    @property
    def albums(self) -> list:
        return self._get_data_by_identifier('albums', Album)

    @property
    def artists(self) -> list:
        return self._get_data_by_identifier('artists', Artist)

    @property
    def playlists(self) -> list:
        return self._get_data_by_identifier('playlists', Playlist)

    @property
    def tracks(self) -> list:
        return self._get_data_by_identifier('tracks', Track)

    @property
    def shows(self) -> list:
        return self._get_data_by_identifier('shows', Show)

    @property
    def episodes(self) -> list:
        return self._get_data_by_identifier('episodes', Episode)

    @property
    def audiobooks(self) -> list:
        return self._get_data_by_identifier('audiobooks', Audiobook)

class User(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def country(self) -> str:
        """ The country of the user, as set in the user's account profile. An ISO 3166-1 alpha-2 country code. """
        return self.get_data()['country']

    @property
    def username(self) -> str:
        """ The name displayed on the users profile. Returns the `email` property value if the display name is not available. """
        if not self.get_data()['display_name']:
            return self.email
        return self.get_data()['display_name']

    @property
    def email(self) -> str:
        """ The user's email address, as entered by the user when creating their account. NOTE: There is no proof that it actually belongs to the user. """
        return self.get_data()['email']

    @property
    def explicitly_settings(self) -> dict:
        """ The user's explicit content settings. """
        return self.get_data()['explicit_content']

    @property
    def external_urls(self) -> dict:
        """ Known external URLs for this user. """
        return self.get_data()['external_urls']

    @property
    def followers(self) -> int:
        """ The total amount of followers for this user. """
        return self.get_data()['followers']['total']

    @property
    def href(self) -> str:
        """ A link to the Web API endpoint for this user. """
        return self.get_data()['href']

    @property
    def user_id(self) -> str:
        """ The Spotify ID for the current user. """
        return self.get_data()['id']

    @property
    def images(self) -> list:
        """ The user's profile image. """
        return self.get_data()['images']

    @property
    def product(self) -> str:
        """ The user's Spotify subscription level: "premium", "free", etc. (The subscription level "open" can be considered the same as "free".) """
        return self.get_data()['product']

    @property
    def type_(self) -> str:
        """ The type of user. """
        return self.get_data()['type']

    @property
    def uri(self) -> str:
        """ The Spotify URI of the current user. """
        return self.get_data()['uri']
    



class Playlist(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)


#* ====================================================================================================================================================================================================



class AlbumRequests():
    class GetAlbum(GetRequest):
        """ Gets a Spotify album using an album id. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-album. """
        def __init__(self, album_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/albums/{album_id}"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = Album(self.get_data())

    class GetCurrentUsersSavedAlbums(GetRequest):
        """ Get a list of the albums saved in the current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-albums. """
        def __init__(self, limit: int = 50, offset: int = 0) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/albums'
            self.api_params = {
                'limit': limit,
                'offset': offset
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            album_list = []
            for album in self.get_data()['items']:
                album_list.append(Album(album['album']))

            self._data = album_list

    class SaveAlbumForCurrentUser(PutRequest):
        """ Saves 1 album to the current users library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-albums-user. """
        def __init__(self, album_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/albums'
            self.api_params = {
                'ids': album_id
            }
            self.api_headers = _headers()
            self.api_payload = {}

    class RemoveCurrentUsersSavedAlbum(DeleteRequest):
        """ Removes 1 album from the current users library. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-albums-user """
        def __init__(self, album_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/albums'
            self.api_params = {
                'ids': album_id
            }
            self.api_headers = _headers()

    class CheckCurrentUsersSavedAlbums(GetRequest):
        """ Check whether 1 album is already saved in the current users library. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-albums. """
        def __init__(self, album_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/albums/contains'
            self.api_params = {
                'ids': album_id
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = self.get_data()[0]

    class GetNewReleases(GetRequest):
        """ Gets a list of new album releases featured in Spotify. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-new-releases. """
        def __init__(self, limit: int = 50, offset: int = 0) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/browse/new-releases'
            self.api_params = {
                'limit': limit,
                'offset': offset
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = Album(self.get_data())

    

#* ====================================================================================================================================================================================================



class ArtistsRequests():
    class GetArtist(GetRequest):
        """ Get a Spotify artist using an id. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artist. """
        def __init__(self, artist_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/artists/{artist_id}"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = Artist(self.get_data())

    class GetArtistAlbums(GetRequest):
        """ Gets a list of albums linked to a Spotify artist. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-albums. """
        def __init__(self, artist_id: str, limit: int = 50, offset: int = 0, include_groups: str = None) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
            self.api_params = {
                'limit': limit,
                'offset': offset,
                'include_groups': include_groups,
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            albums_list = []
            for album in self.get_data()['items']:
                albums_list.append(Album(album))

            self._data = albums_list

    class GetArtistsTopTracks(GetRequest):
        """ Gets a list of the artists top tracks. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-top-tracks. """
        def __init__(self, artist_id: str, market: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
            self.api_params = {
                'market': market
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            tracks_list = []
            for track in self.get_data()['tracks']:
                tracks_list.append(Track(track))

            self._data = tracks_list

    class GetArtistsRelatedArtists(GetRequest):
        """ Gets information about artists similar to a given artist. Similarity is based on analysis of the Spotify community's listening history. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-related-artists. """
        def __init__(self, artist_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            artists_list = []
            for artist in self.get_data()['artists']:
                artists_list.append(Artist(artist))

            self._data = artists_list



#* ====================================================================================================================================================================================================



class ShowsRequests():
    class GetShow(GetRequest):
        """ Get a Spotify show using an id. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-a-show. """
        def __init__(self, show_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/shows/{show_id}"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = Show(self.get_data())

    class GetCurrentUsersSavedShows(GetRequest):
        """ Get a list of the shows saved in the current Spotify user's library. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-shows. """
        def __init__(self, limit: int = 50, offset: int = 0) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/shows'
            self.api_params = {
                'limit': limit,
                'offset': offset
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            shows_list = []
            for show in self.get_data()['items']:
                shows_list.append(Show(show['show']))

    class SaveShowForCurrentUser(PutRequest):
        """ Save 1 show to current user's Spotify library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-shows-user. """
        def __init__(self, show_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/shows'
            self.api_params = {
                'ids': show_id
            }
            self.api_headers = _headers()
            self.api_payload = {}

    class RemoveCurrentUsersSavedShow(DeleteRequest):
        """ Removes 1 show from the current users Spotify library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-shows-user. """
        def __init__(self, show_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/shows'
            self.api_params = {
                'ids': show_id
            }
            self.api_headers = _headers()

    class CheckCurrentUsersSavedShows(GetRequest):
        """ Check if 1 shows is already saved in the current users Spotify library. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-shows. """
        def __init__(self, show_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/shows/contains'
            self.api_params = {
                'ids': show_id
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = self.get_data()[0]



#* ====================================================================================================================================================================================================



class EpisodesRequests():
    class GetEpisode(GetRequest):
        """ Get a Spotify episode using a id. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-episode """
        def __init__(self, episode_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/episodes/{episode_id}"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = Episode(self.get_data())

    class GetCurrentUsersSavedEpisodes(GetRequest):
        """ Get a list of the episodes saved in the current user's Spotify library. This API endpoint is in beta and could change without warning. Please share any feedback that you have, or issues 
        that you discover, in our developer community forum. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-episodes. """
        def __init__(self, limit: int = 5, offset: int = 0) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/episodes'
            self.api_params = {
                'limit': limit,
                'offset': offset
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            episodes_list = []
            for episode in self.get_data()['items']:
                episodes_list.append(Episode(episode['episode']))

            self._data = episodes_list

    class SaveEpisodeForCurrentUser(PutRequest):
        """ Saves 1 episode to the current user's library. This API endpoint is in beta and could change without warning. Please share any feedback that you have, or issues that you discover, in our 
        developer community forum. """
        def __init__(self, episode_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/episodes'
            self.api_params = {
                'ids': episode_id
            }
            self.api_headers = _headers()
            self.api_payload = {}

    class RemoveUsersSavedEpisode(DeleteRequest):
        """ Remove one or more episodes from the current user's library. This API endpoint is in beta and could change without warning. Please share any feedback that you have, or issues that you 
        discover, in our developer community forum. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-episodes-user. """
        def __init__(self, episode_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/episodes'
            self.api_params = {
                'ids': episode_id
            }
            self.api_headers = _headers()

    class CheckUsersSavedEpisodes(GetRequest):
        """ Check if 1 episode is already saved in the current Spotify user's 'Your Episodes' library. This API endpoint is in beta and could change without warning. Please share any feedback that 
        you have, or issues that you discover, in our developer community forum. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-episodes. """
        def __init__(self) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/audiobooks'
            self.api_params = {}
            self.api_headers = _headers()



#* ====================================================================================================================================================================================================



class AudiobooksRequests():
    class GetAudiobook(GetRequest):
        """ Gets a Spotify audiobook using an id. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-audiobook. """
        def __init__(self, audiobook_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/audiobooks/{audiobook_id}"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = Audiobook(self.get_data())

    class GetCurrentUsersSavedAudiobooks(GetRequest):
        """ Get a list of audiobooks saved in the current users library. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-users-saved-audiobooks """

        """ BUG: No matter what, this api endpoint is always returning HTTP 403. I have reported this on the Spotify community forums. 
        https://community.spotify.com/t5/Spotify-for-Developers/Get-User-s-Saved-Audiobooks-always-returning-HTTP-403/m-p/5487560#M7620 
        
        NOTE: Due to this, the functionality of this api, is incomplete. When there is a fix, ensure to complete the code. """
        
        def __init__(self, limit: int = 50, offset: int = 0) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/audiobooks'
            self.api_params = {
                'limit': limit,
                'offset': offset
            }
            self.api_headers = _headers()

    class RemoveCurrentUsersSavedAudiobook(DeleteRequest):
        """ Removes 1 audiobook from the current users Spotify library. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-audiobooks-user. """
        def __init__(self, audiobook_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/audiobooks'
            self.api_params = {
                'ids': audiobook_id
            }
            self.api_headers = _headers()

    class CheckCurrentUsersSavedAudiobooks(GetRequest):
        """ Check if 1 audiobook is already saved onto the current users Spotify library. https://developer.spotify.com/documentation/web-api/reference/#/operations/check-users-saved-audiobooks. """
        def __init__(self, audiobook_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/audiobooks/contains'
            self.api_params = {
                'ids': audiobook_id
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = self.get_data()[0]



#* ====================================================================================================================================================================================================



class ChaptersRequests():
    class GetChapter(GetRequest):
        """ Gets a Spotify chapter using an id. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-a-chapter. """
        def __init__(self, chapter_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/chapters/{chapter_id}"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self) -> None:
            self._data = Chapter(self.get_data())



#* ====================================================================================================================================================================================================



class TracksRequests():
    class GetTrack(GetRequest):
        """ Gets a Spotify track using an id. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track. """
        def __init__(self, track_id: str) -> None:
            super().__init__() 

            self.api_url = f"https://api.spotify.com/v1/tracks/{track_id}"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = Track(self.get_data())

    class GetCurrentUsersSavedTracks(GetRequest):
        """ Get a list of tracks saved in the current users Spotify library. """
        def __init__(self, limit: int = 50, offset: int = 0) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/tracks'
            self.api_params = {
                'limit': limit,
                'offset': offset
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            tracks_list = []
            for track in self.get_data()['items']:
                tracks_list.append(Track(track['track']))

            self._data = tracks_list

    class SaveTrackForCurrentUser(PutRequest):
        """ Saves 1 track to the current users Spotify library. https://developer.spotify.com/documentation/web-api/reference/#/operations/save-tracks-user. """
        def __init__(self, track_id: str) -> None:
            super().__init__()
        
            self.api_url = 'https://api.spotify.com/v1/me/tracks'
            self.api_params = {
                'ids': track_id
            }
            self.api_headers = _headers()

    class RemoveUsersSavedTrack(DeleteRequest):
        """ Removes 1 track from the current users Spotify library. https://developer.spotify.com/documentation/web-api/reference/#/operations/remove-tracks-user. """
        def __init__(self, track_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/tracks'
            self.api_params = {
                'ids': track_id
            }
            self.api_headers = _headers()

    class CheckUsersSavedTracks(GetRequest):
        """ Check if 1 track is already saved in the current users Spotify library. """
        def __init__(self, track_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me/tracks/contains'
            self.api_params = {
                'ids': track_id
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = self.get_data()[0]

    class GetTrackAudioFeatures(GetRequest):
        """ Gets the audio features if a Spotify track using an id. https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features. """
        def __init__(self, track_id: str) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/audio-features'
            self.api_params = {
                'ids': track_id
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = self.get_data()['audio_features']



#* ====================================================================================================================================================================================================



class SearchRequests():
    class SearchForItem(GetRequest):
        """ Get items about albums, artists, playlists, tracks, shows, episodes or audiobooks that match a keyword string. https://developer.spotify.com/documentation/web-api/reference/#/operations/search. """
        def __init__(self, query: str, filters: list = ['album', 'artist', 'playlist', 'track', 'show', 'episode', 'audiobook'], limit: int = 50, offset: int = 0) -> None:
            super().__init__()

            self.filters_formatted = ','.join(filters)

            self.api_url = 'https://api.spotify.com/v1/search'
            self.api_params = {
                'q': query,
                'type': self.filters_formatted,
                'limit': limit,
                'offset': offset
            }
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = SearchItem(self.get_data())


#* ====================================================================================================================================================================================================



class UsersRequests():
    class GetCurrentUsersProfile(GetRequest):
        """ Get detailed profile information about the current user. """
        def __init__(self) -> None:
            super().__init__()

            self.api_url = 'https://api.spotify.com/v1/me'
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True
        
        def _config_data(self):
            self._data = User(self.get_data())

    class GetCurrentUsersTopItems(GetRequest):
        """ Get the current user's top artists or tracks based on calculated affinity. """
        def __init__(self, item_type: str, time_range: str = "medium_term", limit: int = 50, offset: int = 0) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/me/top/{item_type}"
            self.api_params = {
                'limit': limit,
                'offset': offset,
                'time_range': time_range
            }
            self.api_headers = _headers()

            self.cdq = True

            self.obj = Artist
            if item_type == 'tracks':
                self.obj = Track

        def _config_data(self):
            data_list = []
            for data_item in self.get_data()['items']:
                data_list.append(self.obj(data_item))

            self._data = data_list

    class GetUsersProfile(GetRequest):
        """ Get public profile information about a Spotify user. """
        def __init__(self, user_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/users/{user_id}"
            self.api_params = {}
            self.api_headers = _headers()

            self.cdq = True

        def _config_data(self):
            self._data = User(self.get_data())

    class FollowPlaylist(PutRequest):
        """ Add the current user as a follower of a playlist. """
        def __init__(self, playlist_id: str, public_query: bool) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/followers"
            self.api_params = {}
            self.api_headers = _headers()
            self.api_payload = {
                'public': public_query
            }

    class UnfollowPlaylist(DeleteRequest):
        """ Remove the current user as a follower of a playlist. """
        def __init__(self, playlist_id: str) -> None:
            super().__init__()

            self.api_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/followers"
            self.api_params = {}
            self.api_headers = _headers()

    class GetFollowedArtists(GetRequest):
        """ Get the current user's followed artists. """
        def __init__(self, limit) -> None:
            super().__init__()


#* ====================================================================================================================================================================================================



class PlaylistsRequests():
    pass
class CategoriesRequests():
    pass
class GenresRequests():
    pass
class PlayerRequests():
    pass
class MarketsRequests():
    pass