# isRatingComputed

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the system computes the rating of the album using the ratings of individual tracks in the album.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var isRatingComputed: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isRatingComputed) BOOL ratingComputed;
```

#### Discussion

If the user rates tracks within the album individually, but hasn’t assigned a specific rating for the album, the album rating computes as the average of the rating of all tracks within the album (tracks with no rating don’t affect this average), and this property is `true`.

If the user has rated the album, this property is `false`.

If the user hasn’t rated the album and hasn’t rated any tracks on this album, the property is `false`.

## See Also

### Getting Album Info
- [var trackCount: Int](./trackcount.md)
  The number of tracks in the album.
- [var title: String?](./title.md)
  The title of the album.
- [var sortTitle: String?](./sorttitle.md)
  The title to use when sorting by album title.
- [var rating: Int](./rating.md)
  The rating of the album.
- [var isGapless: Bool](./isgapless.md)
  A Boolean value that indicates whether the album is gapless.
- [var discNumber: Int](./discnumber.md)
  The index (1, 2, 3, and so on) of the disc within an album that’s a multiple-disc set.
- [var discCount: Int](./disccount.md)
  The number of discs in a multiple-disc set.
- [var isCompilation: Bool](./iscompilation.md)
  A Boolean value that indicates whether the album is a compilation.
- [var albumArtist: String?](./albumartist.md)
  The name of the artist iTunes associates with the album.
- [var sortAlbumArtist: String?](./sortalbumartist.md)
  The name to use when sorting by album artist.
- [var persistentID: NSNumber](./persistentid.md)
  The unique identifier of the album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibalbum/isratingcomputed)*