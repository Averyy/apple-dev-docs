# sortSeries

**Framework**: iTunes Library  
**Kind**: property

The sorting name of the corresponding TV series, if the media item is an episode in a TV series.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var sortSeries: String? { get }
```

#### Discussion

This property is `nil` if the media item isn’t an episode in a TV series, or if the TV series doesn’t have a sorting name.

## See Also

- [var videoWidth: Int](itlibmediaitemvideoinfo/videowidth.md)
  The width of the video in pixels.
- [var videoHeight: Int](itlibmediaitemvideoinfo/videoheight.md)
  The height of the video in pixels.
- [var series: String?](itlibmediaitemvideoinfo/series.md)
  The name of the corresponding TV series, if the media item is an episode in a TV series.
- [var season: Int](itlibmediaitemvideoinfo/season.md)
  The corresponding TV season, if the media item is an episode of a TV series.
- [var isHD: Bool](itlibmediaitemvideoinfo/ishd.md)
  A Boolean value that indicates whether the video is high-definition.
- [var episode: String?](itlibmediaitemvideoinfo/episode.md)
  The name of the episode, if the media item is an episode of a TV series.
- [var episodeOrder: Int](itlibmediaitemvideoinfo/episodeorder.md)
  The numerical order of the episode, if the media item is an episode of a TV series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitemvideoinfo/sortseries)*