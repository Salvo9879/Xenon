
# Import internal modules
from xenon.models import ObjectScaffold

""" MODIFIED ATTR:
1. id
2. restrictions
3. uri
4. description
5. explicit
6. is_externally_hosted
7. is_playable
"""

class FollowingRequest(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def items(self) -> list:
        """ The requested content """
        return self.get_data()['items']

    @property
    def limit(self) -> int:
        """ The maximum number of items in the response (as set in the query or by default). """
        return self.get_data()['limit']

    @property
    def offset(self) -> int:
        """ The offset of the items returned (as set in the query or by default) """
        return self.get_data()['offset'] + self.limit

    @property
    def after(self) -> str:
        """ The cursor to use as key to find the next page of items. """
        return self.get_data()['cursors']['after']

class Album(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def type_(self) -> str:
        """ The object type. """
        return self.get_data()['album_type']

    @property
    def total_tracks(self) -> int:
        """ The number of tracks in the album. """
        return self.get_data()['total_tracks']

    @property
    def available_markets(self) -> list:
        """ The markets in which the album is available: ISO 3166-1 alpha-2 country codes. NOTE: an album is considered available in a market when at least 1 of its tracks is available in that 
        market. """
        return self.get_data()['available_markets']

    @property
    def external_urls(self) -> dict:
        """ Known external URLs for this album. """
        return self.get_data()['external_urls']

    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the album. """
        return self.get_data()['href']

    @property
    def album_id(self) -> str:
        """ The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the album. """
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
    def release_date(self) -> str:
        """ The date the album was first released. """
        return self.get_data()['release_date']

    @property
    def release_date_precision(self) -> str:
        """ The precision with which release_date value is known. Allowed values: "year", "month", "day". """
        return self.get_data()['release_date_precision']

    @property
    def restrictions(self) -> dict | None:
        """ Included in the response when a content restriction is applied. If no restrictions are applied then returns `None`. """
        if 'restrictions' in self.get_data():
            return self.get_data()['restrictions']
        return None

    @property
    def uri(self) -> str:
        """ The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the album. """
        return self.get_data()['uri']

    @property
    def artists(self) -> list:
        """ The artists of the album. Each artist object includes a link in `href` to more detailed information about the artist. """
        return self.get_data()['artists']

    @property
    def tracks_metadata(self) -> None:
        """ Returns a `FollowingRequest()` for the tracks of the album. """
        return FollowingRequest(self.get_data()['tracks'])   

class Artist(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def external_urls(self) -> dict:
        """ Known external URLs for this artist. """
        return self.get_data()['external_urls']

    @property
    def followers(self) -> int:
        """ The total number of followers. """
        return self.get_data()['followers']['total']

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
        """ The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the artist. """
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
        """ The popularity of the artist. The value will be between 0 and 100, with 100 being the most popular. The artist's popularity is calculated from the popularity of all the artist's 
        tracks. """
        return self.get_data()['popularity']

    @property
    def type_(self) -> str:
        """ The object type. """
        return self.get_data()['type']

    @property
    def uri(self) -> str:
        """ The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the artist. """
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
        """ A description of the show. HTML tags are stripped away from this property, use `html_description` property in case HTML tags are needed. """
        return self.get_data()['description']

    @property 
    def html_description(self) -> str:
        """ A description of the show. This field may contain HTML tags. """
        return self.get_data()['html_description']

    @property   
    def is_explicit(self) -> bool:
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
        """ The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the show. """
        return self.get_data()['id']
        
    @property
    def images(self) -> list:
        """ The cover art for the show in various sizes, widest first. """
        return self.get_data()['images']
        
    @property
    def is_externally_hosted(self) -> bool:
        """ `True` if all of the shows episodes are hosted outside of Spotify's CDN. This field might be `None` in some cases. """
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
        """ The name of the episode. """
        return self.get_data()['name']
        
    @property
    def publisher(self) -> str:
        """ The publisher of the show. """
        return self.get_data()['publisher']
        
    @property
    def type_(self) -> str:
        """ The object type. """
        return self.get_data()['type']
        
    @property
    def uri(self) -> str:
        """ The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the show. """
        return self.get_data()['uri']

    @property 
    def episodes(self) -> None:
        """ Returns a `FollowingRequest()` for the episodes of the show. """
        return FollowingRequest(self.get_data()['episodes'])

class Episode(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def audio_preview_url(self) -> str:
        """ A URL to a 30 second preview (MP3 format) of the episode. `None` if not available. """
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
    def duration_ms(self) -> int:
        """ The episode length in milliseconds. """
        return self.get_data()['duration_ms']
        
    @property
    def is_explicit(self) -> bool:
        """ Whether or not the episode has explicit content (`True` = yes it does; `False` = no it does not OR unknown). """
        return self.get_data()['explicit']
        
    @property
    def external_urls(self) -> dict:
        """ External URLs for this episode. """
        return self.get_data()['external_urls']
        
    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the episode. """
        return self.get_data()['href']
        
    @property
    def episode_id(self) -> str:
        """ The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the episode. """
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
        """ The date the episode was first released, for example `1981-12-15`. Depending on the precision, it might be shown as `1981` or `1981-12`. """
        return self.get_data()['release_date']
        
    @property
    def release_date_precision(self) -> str:
        """ The precision with which `release_date` value is known. Allowed values: "year", "month", "day" """
        return self.get_data()['release_date_precision']
        
    @property
    def resume_point(self) -> dict:
        """ The user's most recent position in the episode. Set if the supplied access token is a user token and has the scope `user-read-playback-position`. """
        return self.get_data()['resume_point']
        
    @property
    def type_(self) -> str:
        """ The object type. """
        return self.get_data()['type']
        
    @property
    def uri(self) -> str:
        """ The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the episode. """
        return self.get_data()['uri']
    @property
    def linked_show(self) -> Show:
        """ The show in which the episode is released under. NOTE: This property returns a `Show()` object. It will not include the property `episodes`. """
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
        """ A list of the countries in which the audiobook can be played, identified by their ISO 3166-1 alpha-2 code. """
        return self.get_data()['available_markets']
        
    @property
    def copyrights(self) -> list:
        """ The copyright statements of the audiobook. """
        return self.get_data()['copyrights']
    
    @property
    def description(self) -> str:
        """ A description of the audiobook. HTML tags are stripped away from this property, use `html_description` property in case HTML tags are needed. """
        return self.get_data()['description']
        
    @property
    def html_description(self) -> str:
        """ A description of the audiobook. This field may contain HTML tags. """
        return self.get_data()['html_description']

    @property
    def is_explicit(self) -> bool:
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
        """ The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the audiobook. """
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
    def name(self) -> str:
        """ The name of the audiobook. """
        return self.get_data()['name']

    @property
    def narrators(self) -> list:
        """ A list of the narrators of the audiobook. """
        return self.get_data()['narrators']

    @property
    def publisher(self) -> str:
        """ The publisher of the audiobook. """
        return self.get_data()['publisher']

    @property
    def type(self) -> str:
        """ The object type. """
        return self.get_data()['type']

    @property
    def uri(self) -> str:
        """ The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the audiobook. """
        return self.get_data()['uri']

    @property
    def total_chapters(self) -> int:
        """ The number of chapters in this audiobook. """
        return self.get_data()['total_chapters']

    @property
    def chapters(self) -> list:
        """ Returns a `FollowingRequest()` for the chapters of the audiobook. """
        return FollowingRequest(self.get_data()['chapters'])

class Chapter(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def audio_preview_url(self) -> str:
        """ A URL to a 30 second preview (MP3 format) of the episode. `None` if not available. """
        return self.get_data()['audio_preview_url']

    @property
    def chapter_number(self) -> int:
        """ The number of the chapter """
        return self.get_data()['chapter_number']
        
    @property
    def description(self) -> str:
        """ A description of the episode. HTML tags are stripped away from this property, use `html_description` property in case HTML tags are needed. """
        return self.get_data()['description']

    @property        
    def html_description(self) -> str:
        """ A description of the episode. This field may contain HTML tags. """
        return self.get_data()['html_description']

    @property        
    def duration(self) -> int:
        """ The episode length in milliseconds. """
        return self.get_data()['duration_ms']

    @property        
    def is_explicit(self) -> bool:
        """ Whether or not the episode has explicit content (`True` = yes it does; `False` = no it does not OR unknown). """
        return self.get_data()['explicit']

    @property        
    def external_urls(self) -> dict:
        """ External URLs for this episode. """
        return self.get_data()['external_urls']

    @property       
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the episode. """
        return self.get_data()['href']
        
    @property   
    def chapter_id(self) -> str:
        """ The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the episode. """
        return self.get_data()['id']
        
    @property   
    def images(self) -> list:
        """ The cover art for the episode in various sizes, widest first. """
        return self.get_data()['images']
        
    @property   
    def is_playable(self) -> bool:
        """ True if the episode is playable in the given market. Otherwise `False`. """
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
        """ The date the episode was first released, for example "1981-12-15". Depending on the precision, it might be shown as "1981" or "1981-12". """
        return self.get_data()['release_date']
        
    @property   
    def release_date_precision(self) -> str:
        """ The precision with which release_date value is known. Allowed values: "year", "month", "day" """
        return self.get_data()['release_date_precision']
        
    @property   
    def resume_point(self) -> dict:
        """ The user's most recent position in the episode. Set if the supplied access token is a user token and has the scope `user-read-playback-position`. """
        return self.get_data()['resume_point']
        
    @property   
    def type_(self) -> str:
        """ The object type. """
        return self.get_data()['type']
        
    @property   
    def uri(self) -> str:
        """ The [Spotify URI](per.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the episode. """
        return self.get_data()['uri']
        
    @property   
    def restrictions(self) -> dict | None:
        """ Included in the response when a content restriction is applied. If no restrictions are applied then returns `None`. """
        if 'restrictions' in self.get_data():
            return self.get_data()['restrictions']
        return None
        
    @property   
    def linked_audiobook(self) -> Audiobook:
        """ The audiobook in which the chapter is released under. NOTE: This property returns a `Audiobook()` object. It will not include the property `chapters`. """
        return self.get_data()['audiobook']
        
class Track(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property   
    def linked_album(self) -> Album:
        """ The album in which the track is released under. NOTE: This property returns a `Album()` object. It will not include the property `episodes`. """
        return Album(self.get_data()['album'])

    @property   
    def artists(self) -> list:
        """ The artists who performed the track. Each artist object includes a link in `href` to more detailed information about the artist. """
        return self.get_data()['artists']

    @property   
    def available_markets(self) -> list:
        """ A list of the countries in which the track can be played, identified by their ISO 3166-1 alpha-2 code. """
        return self.get_data()['available_markets']
        
    @property   
    def disc_number(self) -> int:
        """ The disc number (usually 1 unless the album consists of more than one disc). """
        return self.get_data()['disc_number']
        
    @property   
    def duration(self) -> int:
        """ The disc number (usually 1 unless the album consists of more than one disc). """
        return self.get_data()['duration_ms']

    @property   
    def is_explicit(self) -> bool:
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
        """ The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the track. """
        return self.get_data()['id']
        
    @property    
    def is_playable(self) -> bool:
        """ `True` if the track is playable in the given market. Otherwise `False`. """
        return self.get_data()['is_playable']
        
    @property    
    def restrictions(self) -> dict | None:
        """ Included in the response when a content restriction is applied. If no restrictions are applied then returns `None`. """
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
        the track has had and how recent those plays are.
        
        Generally speaking, songs that are being played a lot now will have a higher popularity than songs that were played a lot in the past. Duplicate tracks (e.g. the same track from a single and 
        an album) are rated independently. Artist and album popularity is derived mathematically from track popularity. Note: the popularity value may lag actual popularity by a few days: the value 
        is not updated in real time. """
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
        """ The object type. """
        return self.get_data()['type']
        
    @property    
    def uri(self) -> str:
        """ The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the track. """
        return self.get_data()['uri']
        
    @property    
    def is_local(self) -> bool:
        """ Whether or not the track is from a local file. """
        return self.get_data()['is_local']
        
class AudioFeatures(ObjectScaffold):
    @property
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def acousticness(self) -> float:
        """ A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. """
        return self.get_data()['audio_features']['acousticness']
    
    @property
    def analysis_url(self) -> str:
        """ A URL to access the full audio analysis of this track. An access token is required to access this data. """
        return self.get_data()['audio_features']['analysis_url']
    
    @property
    def danceability(self) -> float:
        """ Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable. """
        return self.get_data()['audio_features']['danceability']
    
    @property
    def duration(self) -> int:
        """ The duration of the track in milliseconds. """
        return self.get_data()['audio_features']['duration_ms']
    
    @property
    def energy(self) -> float:
        """ Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy. """
        return self.get_data()['audio_features']['energy']
    
    @property
    def audio_feature_id(self) -> str:
        """ The Spotify ID for the track. """
        return self.get_data()['audio_features']['id']
    
    @property
    def instrumentalness(self) -> float:
        """ Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0. """
        return self.get_data()['audio_features']['instrumentalness']
    
    @property
    def key(self) -> int:
        """ The key the track is in. Integers map to pitches using standard [Pitch Class notation](https://en.wikipedia.org/wiki/Pitch_class). E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1. """
        return self.get_data()['audio_features']['key']
    
    @property
    def liveness(self) -> float:
        """ Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live. """
        return self.get_data()['audio_features']['liveness']
    
    @property
    def loudness(self) -> float:
        """ The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db. """
        return self.get_data()['audio_features']['loudness']
    
    @property
    def mode(self) -> int:
        """ Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0. """
        return self.get_data()['audio_features']['mode']
    
    @property
    def speechiness(self) -> float:
        """ Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks. """
        return self.get_data()['audio_features']['speechiness']
    
    @property
    def tempo(self) -> float:
        """ The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration. """
        return self.get_data()['audio_features']['tempo']
    
    @property
    def time_signature(self) -> int:
        """ An estimated time signature. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure). The time signature ranges from 3 to 7 indicating time signatures of "3/4", to "7/4". """
        return self.get_data()['audio_features']['time_signature']
    
    @property
    def track_href(self) -> str:
        """ A link to the Web API endpoint providing full details of the track. """
        return self.get_data()['audio_features']['track_href']
    
    @property
    def type_(self) -> str:
        """ The object type. """
        return self.get_data()['audio_features']['type_']
    
    @property
    def uri(self) -> str:
        """ The Spotify URI for the track. """
        return self.get_data()['audio_features']['uri']
    
    @property
    def valence(self) -> float:
        """ A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry). """
        return self.get_data()['audio_features']['valence']

class SearchResults(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)
    
        
    @property
    def tracks(self) -> FollowingRequest:
        """ Tracks related to the search query. Returns `None` if it wasn't declared by the filters query at the get request. """
        if 'tracks' in self.get_data():
            return FollowingRequest(self.get_data()['tracks'])
        return None
    
    @property
    def artists(self) -> FollowingRequest:
        """ Artists related to the search query. Returns `None` if it wasn't declared by the filters query at the get request. """
        if 'artists' in self.get_data():
            return FollowingRequest(self.get_data()['artists'])
        return None
    
    @property
    def albums(self) -> FollowingRequest:
        """ Albums related to the search query. Returns `None` if it wasn't declared by the filters query at the get request. """
        if 'albums' in self.get_data():
            return FollowingRequest(self.get_data()['albums'])
        return None
    
    @property
    def playlists(self) -> FollowingRequest:
        """ Playlists related to the search query. Returns `None` if it wasn't declared by the filters query at the get request. """
        if 'playlists' in self.get_data():
            return FollowingRequest(self.get_data()['playlists'])
        return None
    
    @property
    def shows(self) -> FollowingRequest:
        """ Shows related to the search query. Returns `None` if it wasn't declared by the filters query at the get request. """
        if 'show' in self.get_data():
            return FollowingRequest(self.get_data()['shows'])
        return None
    
    @property
    def episodes(self) -> FollowingRequest:
        """ Episodes related to the search query. Returns `None` if it wasn't declared by the filters query at the get request. """
        if 'episodes' in self.get_data():
            return FollowingRequest(self.get_data()['episodes'])
        return None
    
    @property
    def audiobooks(self) -> FollowingRequest:
        """ Audiobooks related to the search query. Returns `None` if it wasn't declared by the filters query at the get request. """
        if 'audiobooks' in self.get_data():
            return FollowingRequest(self.get_data()['audiobooks'])
        return None

class User(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    @property
    def display_name(self) -> str | None:
        """ The name displayed on the user's profile. `None` if not available. """
        return self.get_data()['display_name']

    @property
    def external_urls(self) -> dict:
        """ Known public external URLs for this user. """
        return self.get_data()['external_urls']

    @property  
    def total_followers(self) -> int:
        """ The total number of followers. """
        return self.get_data()['followers']['total']
    @property   
    def href(self) -> str:
        """ A link to the Web API endpoint for this user. """
        return self.get_data()['href']

    @property  
    def user_id(self) -> str:
        """ The [Spotify user ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for this user. """
        return self.get_data()['id']

    @property   
    def images(self) -> list:
        """ The user's profile image. """
        return self.get_data()['images']
        
    @property
    def type_(self) -> str:
        """ The object type. """
        return self.get_data()['type']
        
    @property
    def uri(self) -> str:
        """ The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for this user. """
        return self.get_data()['uri']

class Playlist(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def is_collaborative(self) -> bool:
        """ True if the owner allows other users to modify the playlist. """
        return self.get_data()['collaborative']

    @property
    def description(self) -> str | None:
        """ The playlist description. Only returned for modified, verified playlists, otherwise `None`. """
        return self.get_data()['description']
        
    @property
    def external_urls(self) -> dict:
        """ Known external URLs for this playlist. """
        return self.get_data()['external_urls']
        
    @property
    def total_followers(self) -> int:
        """ The total number of followers. """
        return self.get_data()['followers']['total']
        
    @property
    def href(self) -> str:
        """ A link to the Web API endpoint providing full details of the playlist. """
        return self.get_data()['href']
        
    @property
    def playlist_id(self) -> str:
        """ The [Spotify ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the playlist. """
        return self.get_data()['id']
        
    @property
    def images(self) -> list:
        """ Images for the playlist. The list may be empty or contain up to three images. The images are returned by size in descending order. See [Working with Playlists](https://developer.spotify.com/documentation/general/guides/working-with-playlists/). NOTE: If returned, the source URL for the image (url) is temporary and will expire in less than a day. """
        return self.get_data()['images']
        
    @property
    def name(self) -> str:
        """ The name of the playlist. """
        return self.get_data()['name']
        
    @property
    def owner(self) -> User:
        """ The user who owns the playlist. """
        return User(self.get_data()['owner'])
        
    @property
    def is_public(self) -> bool:
        """ The playlist's public/private status: `True` the playlist is public, `False` the playlist is private, `None` the playlist status is not relevant. For more about public/private status, see [Working with Playlists](https://developer.spotify.com/documentation/general/guides/working-with-playlists/) """
        return self.get_data()['public']
        
    @property
    def tracks(self) -> list:
        """ Returns a `FollowingRequest()` for the tracks of the playlist. """
        return FollowingRequest(self.get_data()['tracks'])
        
    @property
    def type_(self) -> str:
        """ The object type. """
        return self.get_data()['type']
        
    @property
    def uri(self) -> str:
        """ The [Spotify URI](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) for the playlist. """
        return self.get_data()['uri']

class Category(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def href(self) -> str:
        """ A link to the Web API endpoint returning full details of the category. """
        return self.get_data()['href']

    def icons(self) -> list:
        """ The category icon, in various sizes. """
        return self.get_data()['icons']

    def category_id(self) -> str:
        """ The [Spotify category ID](https://developer.spotify.com/documentation/web-api/#spotify-uris-and-ids) of the category. """
        return self.get_data()['id']

    def name(self) -> str:
        """ The name of the category. """
        return self.get_data()['name']

class Device(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def device_id(self) -> str:
        """ The device ID. """
        return self.get_data()['id']

    @property
    def is_active(self) -> bool:
        """ If this device is the currently active device. """
        return self.get_data()['is_active']

    @property
    def is_in_private_session(self) -> bool:
        """ If this device is currently in a private session. """
        return self.get_data()['is_private_session']

    @property
    def is_restricted(self) -> bool:
        """ Whether controlling this device is restricted. At present if this is `True` then no Web API commands will be accepted by this device. """
        return self.get_data()['is_restricted']

    @property
    def name(self) -> str:
        """ A human-readable name for the device. Some devices have a name that the user can configure (e.g. "Loudest speaker") and some devices have a generic name associated with the manufacturer or device model. """
        return self.get_data()['name']

    @property
    def type_(self) -> str:
        """ Device type, such as "computer", "smartphone" or "speaker". """
        return self.get_data()['type']

    @property
    def volume(self) -> int:
        """ The current volume in percent. 0 <= v <= 100"""
        return self.get_data()['volume_percent']

class Queue(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def currently_playing(self) -> Track:
        """ Information about the track that is currently playing. """
        return Track(self.get_data()['currently_playing'])

    def queue(self) -> list:
        """ The tracks or episodes in the queue. Can be empty. """
        items_list = []
        for item in self.get_data()['queue']:
            if item['type'] == 'episode':
                items_list.append(Episode(item))
            elif item['type'] == 'track':
                items_list.append(Track(item))
            else:
                raise AttributeError(f"Item in queue was not track or episode. Returned {item['type']} instead.")
        return items_list

class PlaybackState(ObjectScaffold):
    def __init__(self, data: dict) -> None:
        super().__init__(data)

    def device(self) -> Device:
        """ The device that is currently active. """
        return Device(self.get_data()['device'])
    
    @property
    def repeat_state(self) -> str:
        """ The shuffle state of the device. """
        return self.get_data()['repeat_state']
    
    @property
    def shuffle_state(self) -> bool:
        """ If shuffle is on or off. """
        return self.get_data()['shuffle_state']
    
    @property
    def context(self) -> dict | None:
        """ The context of which the item is being played from. Can be `None`. """
        return self.get_data()['context']
    
    @property
    def timestamp(self) -> int:
        """ Unix Millisecond Timestamp when data was fetched. """
        return self.get_data()['timestamp']
    
    @property
    def progress(self) -> int | None:
        """ Progress into the currently playing track or episode. Can be `None`. """
        return self.get_data()['progress_ms']
    
    @property
    def is_playing(self) -> bool:
        """ If something is currently playing, return `True`. """
        return self.get_data()['is_playing']
    
    @property
    def item(self) -> Track | Episode:
        """ The item that is currently playing. """
        if self.type_ == 'track':
            return Track(self.get_data()['item'])
        if self.type_ == 'episode':
            return Episode(self.get_data()['item'])
        return self.get_data()['item']
    
    @property
    def type_(self) -> str:
        """ The object type of the currently playing item. Can be one of `track`, `episode`, `ad` or `unknown`. """
        return self.get_data()['currently_playing_type']
    
    @property
    def actions(self) -> dict:
        """ Allows to update the user interface based on which playback actions are available within the current context. """
        return self.get_data()['actions']