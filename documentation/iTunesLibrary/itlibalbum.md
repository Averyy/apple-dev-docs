# ITLibAlbum

**Framework**: iTunes Library  
**Kind**: class

This class provides information about an album in the iTunes library.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
class ITLibAlbum
```

#### Overview

A *media item* is a track that iTunes associates with an album. See [`ITLibMediaItem`](itlibmediaitem.md).

A *compilation* is an album with tracks from more than one source.

If an album is part of a *multiple-disc set*, [`discNumber`](itlibalbum/discnumber.md) is the index of the album in the set.

To retrieve an [`ITLibAlbum`](itlibalbum.md) instance, use the [`album`](itlibmediaitem/album.md) property of [`ITLibMediaItem`](itlibmediaitem.md).

## Topics

### Getting Album Info
- [var trackCount: Int](itlibalbum/trackcount.md)
  The number of tracks in the album.
- [var title: String?](itlibalbum/title.md)
  The title of the album.
- [var sortTitle: String?](itlibalbum/sorttitle.md)
  The title to use when sorting by album title.
- [var rating: Int](itlibalbum/rating.md)
  The rating of the album.
- [var isRatingComputed: Bool](itlibalbum/isratingcomputed.md)
  A Boolean value that indicates whether the system computes the rating of the album using the ratings of individual tracks in the album.
- [var isGapless: Bool](itlibalbum/isgapless.md)
  A Boolean value that indicates whether the album is gapless.
- [var discNumber: Int](itlibalbum/discnumber.md)
  The index (1, 2, 3, and so on) of the disc within an album that’s a multiple-disc set.
- [var discCount: Int](itlibalbum/disccount.md)
  The number of discs in a multiple-disc set.
- [var isCompilation: Bool](itlibalbum/iscompilation.md)
  A Boolean value that indicates whether the album is a compilation.
- [var albumArtist: String?](itlibalbum/albumartist.md)
  The name of the artist iTunes associates with the album.
- [var sortAlbumArtist: String?](itlibalbum/sortalbumartist.md)
  The name to use when sorting by album artist.
- [var persistentID: NSNumber](itlibalbum/persistentid.md)
  The unique identifier of the album.
### Deprecated
- [var artist: ITLibArtist?](itlibalbum/artist.md)
  The artist iTunes associates with the album.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class ITLibPlaylist](itlibplaylist.md)
  This class describes a playlist in the iTunes library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibalbum)*