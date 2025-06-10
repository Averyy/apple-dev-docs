# ITLibMediaItemMediaKind

**Framework**: iTunes Library  
**Kind**: enum

These constants specify the possible media kinds of a media item.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
enum ITLibMediaItemMediaKind
```

## Topics

### Media Kinds
- [ITLibMediaItemMediaKind.kindUnknown](itlibmediaitemmediakind/kindunknown.md)
  The media item kind is unknown.
- [ITLibMediaItemMediaKind.kindSong](itlibmediaitemmediakind/kindsong.md)
  The media item is a song.
- [ITLibMediaItemMediaKind.kindMovie](itlibmediaitemmediakind/kindmovie.md)
  The media item is a movie.
- [ITLibMediaItemMediaKind.kindPodcast](itlibmediaitemmediakind/kindpodcast.md)
  The media item is an audio or a video podcast.
- [ITLibMediaItemMediaKind.kindAudiobook](itlibmediaitemmediakind/kindaudiobook.md)
  The media item is an audiobook.
- [ITLibMediaItemMediaKind.kindPDFBooklet](itlibmediaitemmediakind/kindpdfbooklet.md)
  The media item is an unwrapped PDF file that’s part of a music album.
- [ITLibMediaItemMediaKind.kindMusicVideo](itlibmediaitemmediakind/kindmusicvideo.md)
  The media item is a music video.
- [ITLibMediaItemMediaKind.kindTVShow](itlibmediaitemmediakind/kindtvshow.md)
  The media item is a TV show.
- [ITLibMediaItemMediaKind.kindInteractiveBooklet](itlibmediaitemmediakind/kindinteractivebooklet.md)
  The media item is a QuickTime movie with embedded Flash.
- [ITLibMediaItemMediaKind.kindHomeVideo](itlibmediaitemmediakind/kindhomevideo.md)
  The media item is a non-iTunes Store movie.
- [ITLibMediaItemMediaKind.kindRingtone](itlibmediaitemmediakind/kindringtone.md)
  The media item is an iOS ringtone.
- [ITLibMediaItemMediaKind.kindDigitalBooklet](itlibmediaitemmediakind/kinddigitalbooklet.md)
  The media item is an iTunes Extra or an iTunes LP item.
- [ITLibMediaItemMediaKind.kindIOSApplication](itlibmediaitemmediakind/kindiosapplication.md)
  The media item is an iOS app.
- [ITLibMediaItemMediaKind.kindVoiceMemo](itlibmediaitemmediakind/kindvoicememo.md)
  The media item is a recorded voice memo.
- [ITLibMediaItemMediaKind.kindiTunesU](itlibmediaitemmediakind/kinditunesu.md)
  The media item is an iTunes U audio or video file.
- [ITLibMediaItemMediaKind.kindBook](itlibmediaitemmediakind/kindbook.md)
  The media item is an EPUB file or an iBooks Author book.
- [ITLibMediaItemMediaKind.kindPDFBook](itlibmediaitemmediakind/kindpdfbook.md)
  The media item is a PDF file that iTunes treats as a book unless the user overrides it.
- [ITLibMediaItemMediaKind.kindAlertTone](itlibmediaitemmediakind/kindalerttone.md)
  The media item is an audio tone that’s not a protected ringtone on an iOS device.
### Initializers
- [init?(rawValue: UInt)](itlibmediaitemmediakind/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitemmediakind)*