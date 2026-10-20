# sortTitle

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The title of the media item to use when sorting.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var sortTitle: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * sortTitle;
```

#### Discussion

If `nil`, iTunes uses [`title`](./title.md) when sorting media items.

## See Also

### Getting Media Item Info
- [var title: String](./title.md)
  The title of the media item.
- [var artist: ITLibArtist?](./artist.md)
  Information about the artist that iTunes associates with the media item.
- [var composer: String](./composer.md)
  The name of the composer that iTunes associates with the media item.
- [var sortComposer: String?](./sortcomposer.md)
  The name to use when sorting by composer.
- [var rating: Int](./rating.md)
  The rating of the media item.
- [var isRatingComputed: Bool](./isratingcomputed.md)
  A Boolean value that indicates whether iTunes computes the media item’s rating from its album rating.
- [var startTime: Int](./starttime.md)
  If nonzero, the actual time playback of the media item starts instead of 0:00 (in milliseconds).
- [var stopTime: Int](./stoptime.md)
  If nonzero, the actual time playback of the media item stops versus the total time (in milliseconds).
- [var album: ITLibAlbum](./album.md)
  The album of the media item.
- [var genre: String](./genre.md)
  The genre of the media item, if any.
- [var kind: String?](./kind.md)
  The kind of media item file, such as an MPEG audio file.
- [var mediaKind: ITLibMediaItemMediaKind](./mediakind.md)
  The kind of media item.
- [var totalTime: Int](./totaltime.md)
  The length of the media item in milliseconds.
- [var trackNumber: Int](./tracknumber.md)
  The position of the media item within its album.
- [var category: String?](./category.md)
  The podcast category of the media item, if the media item is a podcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitem/sorttitle)*