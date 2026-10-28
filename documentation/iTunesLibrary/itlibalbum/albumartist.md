# albumArtist

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The name of the artist iTunes associates with the album.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var albumArtist: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * albumArtist;
```

## Discussion

If the artist is unknown, this property is `nil`.

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
- [var isRatingComputed: Bool](./isratingcomputed.md)
  A Boolean value that indicates whether the system computes the rating of the album using the ratings of individual tracks in the album.
- [var isGapless: Bool](./isgapless.md)
  A Boolean value that indicates whether the album is gapless.
- [var discNumber: Int](./discnumber.md)
  The index (1, 2, 3, and so on) of the disc within an album that’s a multiple-disc set.
- [var discCount: Int](./disccount.md)
  The number of discs in a multiple-disc set.
- [var isCompilation: Bool](./iscompilation.md)
  A Boolean value that indicates whether the album is a compilation.
- [var sortAlbumArtist: String?](./sortalbumartist.md)
  The name to use when sorting by album artist.
- [var persistentID: NSNumber](./persistentid.md)
  The unique identifier of the album.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibalbum/albumartist)*