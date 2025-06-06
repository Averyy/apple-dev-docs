# ITLibMediaItemLyricsContentRating

**Framework**: iTunes Library  
**Kind**: enum

These constants specify the possible ratings of media item lyrics.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
enum ITLibMediaItemLyricsContentRating
```

## Topics

### Media Item Lyric Content Ratings
- [ITLibMediaItemLyricsContentRating.none](itlibmediaitemlyricscontentrating/none.md)
  There is no rating information for the media item lyrics.
- [ITLibMediaItemLyricsContentRating.explicit](itlibmediaitemlyricscontentrating/explicit.md)
  The media item lyrics contain explicit language.
- [ITLibMediaItemLyricsContentRating.clean](itlibmediaitemlyricscontentrating/clean.md)
  The media item lyrics don’t contain explicit language.
### Initializers
- [init?(rawValue: UInt)](itlibmediaitemlyricscontentrating/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var title: String](itlibmediaitem/title.md)
  The title of the media item.
- [var sortTitle: String?](itlibmediaitem/sorttitle.md)
  The title of the media item to use when sorting.
- [var artist: ITLibArtist?](itlibmediaitem/artist.md)
  Information about the artist that iTunes associates with the media item.
- [var composer: String](itlibmediaitem/composer.md)
  The name of the composer that iTunes associates with the media item.
- [var sortComposer: String?](itlibmediaitem/sortcomposer.md)
  The name to use when sorting by composer.
- [var rating: Int](itlibmediaitem/rating.md)
  The rating of the media item.
- [var isRatingComputed: Bool](itlibmediaitem/isratingcomputed.md)
  A Boolean value that indicates whether iTunes computes the media item’s rating from its album rating.
- [var startTime: Int](itlibmediaitem/starttime.md)
  If nonzero, the actual time playback of the media item starts instead of 0:00 (in milliseconds).
- [var stopTime: Int](itlibmediaitem/stoptime.md)
  If nonzero, the actual time playback of the media item stops versus the total time (in milliseconds).
- [var album: ITLibAlbum](itlibmediaitem/album.md)
  The album of the media item.
- [var genre: String](itlibmediaitem/genre.md)
  The genre of the media item, if any.
- [var kind: String?](itlibmediaitem/kind.md)
  The kind of media item file, such as an MPEG audio file.
- [var mediaKind: ITLibMediaItemMediaKind](itlibmediaitem/mediakind.md)
  The kind of media item.
- [var totalTime: Int](itlibmediaitem/totaltime.md)
  The length of the media item in milliseconds.
- [var trackNumber: Int](itlibmediaitem/tracknumber.md)
  The position of the media item within its album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitemlyricscontentrating)*