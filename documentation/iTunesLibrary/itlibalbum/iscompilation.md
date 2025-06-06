# isCompilation

**Framework**: iTunes Library  
**Kind**: property

A Boolean value that indicates whether the album is a compilation.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var isCompilation: Bool { get }
```

#### Discussion

A  is an album with tracks from multiple sources.

## See Also

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
- [var albumArtist: String?](itlibalbum/albumartist.md)
  The name of the artist iTunes associates with the album.
- [var sortAlbumArtist: String?](itlibalbum/sortalbumartist.md)
  The name to use when sorting by album artist.
- [var persistentID: NSNumber](itlibalbum/persistentid.md)
  The unique identifier of the album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibalbum/iscompilation)*