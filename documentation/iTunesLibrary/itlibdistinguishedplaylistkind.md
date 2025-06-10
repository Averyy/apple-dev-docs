# ITLibDistinguishedPlaylistKind

**Framework**: iTunes Library  
**Kind**: enum

These constants specify the possible kinds of distinguished playlists.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
enum ITLibDistinguishedPlaylistKind
```

## Topics

### Distinguished Playlist Kinds
- [ITLibDistinguishedPlaylistKind.kindNone](itlibdistinguishedplaylistkind/kindnone.md)
  The playlist isn’t a distinguished playlist.
- [ITLibDistinguishedPlaylistKind.kindMovies](itlibdistinguishedplaylistkind/kindmovies.md)
  The playlist contains all the movies in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindTVShows](itlibdistinguishedplaylistkind/kindtvshows.md)
  The playlist contains all the TV shows in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindMusic](itlibdistinguishedplaylistkind/kindmusic.md)
  The playlist contains all the music items in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindAudiobooks](itlibdistinguishedplaylistkind/kindaudiobooks.md)
  The playlist contains all the audiobooks in the iTunes library.
- [static var kindBooks: ITLibDistinguishedPlaylistKind](itlibdistinguishedplaylistkind/kindbooks.md)
  The playlist contains all the audiobooks in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindRingtones](itlibdistinguishedplaylistkind/kindringtones.md)
  The playlist contains all the iOS ringtones in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindPodcasts](itlibdistinguishedplaylistkind/kindpodcasts.md)
  The playlist contains all the podcasts in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindVoiceMemos](itlibdistinguishedplaylistkind/kindvoicememos.md)
  The playlist contains all the voice memos in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindPurchases](itlibdistinguishedplaylistkind/kindpurchases.md)
  The playlist contains all the user’s purchases from the iTunes Store.
- [ITLibDistinguishedPlaylistKind.kindiTunesU](itlibdistinguishedplaylistkind/kinditunesu.md)
  The playlist contains all the user’s iTunes U items.
- [ITLibDistinguishedPlaylistKind.kind90sMusic](itlibdistinguishedplaylistkind/kind90smusic.md)
  The default Smart Playlist that iTunes creates of the user’s music from the 1990s.
- [ITLibDistinguishedPlaylistKind.kindMyTopRated](itlibdistinguishedplaylistkind/kindmytoprated.md)
  The default Smart Playlist that iTunes creates of the user’s top rated media items.
- [ITLibDistinguishedPlaylistKind.kindTop25MostPlayed](itlibdistinguishedplaylistkind/kindtop25mostplayed.md)
  The default Smart Playlist that iTunes creates of the user’s 25 most played media items.
- [ITLibDistinguishedPlaylistKind.kindRecentlyPlayed](itlibdistinguishedplaylistkind/kindrecentlyplayed.md)
  The default Smart Playlist that iTunes creates of the user’s most recently played media items.
- [ITLibDistinguishedPlaylistKind.kindRecentlyAdded](itlibdistinguishedplaylistkind/kindrecentlyadded.md)
  The default Smart Playlist that iTunes creates of the user’s most recently added media items.
- [ITLibDistinguishedPlaylistKind.kindMusicVideos](itlibdistinguishedplaylistkind/kindmusicvideos.md)
  The default Smart Playlist that iTunes creates of the user’s music videos.
- [ITLibDistinguishedPlaylistKind.kindClassicalMusic](itlibdistinguishedplaylistkind/kindclassicalmusic.md)
  The default Smart Playlist that iTunes creates of the user’s classical music.
- [ITLibDistinguishedPlaylistKind.kindLibraryMusicVideos](itlibdistinguishedplaylistkind/kindlibrarymusicvideos.md)
  The playlist contains all the music videos in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindHomeVideos](itlibdistinguishedplaylistkind/kindhomevideos.md)
  The playlist contains all the user’s home videos in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindApplications](itlibdistinguishedplaylistkind/kindapplications.md)
  The playlist contains all the user’s iOS apps in the iTunes library.
- [ITLibDistinguishedPlaylistKind.kindLovedSongs](itlibdistinguishedplaylistkind/kindlovedsongs.md)
  The playlist contains all the user’s loved music.
- [ITLibDistinguishedPlaylistKind.kindMusicShowsAndMovies](itlibdistinguishedplaylistkind/kindmusicshowsandmovies.md)
  The default Smart Playlist that iTunes creates of the user’s music shows and movies.
### Initializers
- [init?(rawValue: UInt)](itlibdistinguishedplaylistkind/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var name: String](itlibplaylist/name.md)
  The name or title of the playlist.
- [var items: [ITLibMediaItem]](itlibplaylist/items.md)
  The media items (tracks) in the playlist.
- [var parentID: NSNumber?](itlibplaylist/parentid.md)
  The unique persistent identifier of the playlist’s parent playlist.
- [var isPrimary: Bool](itlibplaylist/isprimary.md)
  A Boolean value that indicates whether the playlist is the primary playlist.
- [var isVisible: Bool](itlibplaylist/isvisible.md)
  A Boolean value that indicates whether the playlist is visible to the user in iTunes.
- [var distinguishedKind: ITLibDistinguishedPlaylistKind](itlibplaylist/distinguishedkind.md)
  An indication of whether the playlist has a special distinction.
- [var kind: ITLibPlaylistKind](itlibplaylist/kind.md)
  An indication of the type of playlist.
- [enum ITLibPlaylistKind](itlibplaylistkind.md)
  These constants specify the possible kinds of playlists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibdistinguishedplaylistkind)*