# season

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The corresponding TV season, if the media item is an episode of a TV series.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var season: Int { get }
```

```objc
@property (nonatomic, assign, readonly) NSUInteger season;
```

## Discussion

This property is `0` if the media item isn’t an episode of a TV series.

## See Also

### Getting Video Information
- [var videoWidth: Int](./videowidth.md)
  The width of the video in pixels.
- [var videoHeight: Int](./videoheight.md)
  The height of the video in pixels.
- [var series: String?](./series.md)
  The name of the corresponding TV series, if the media item is an episode in a TV series.
- [var sortSeries: String?](./sortseries.md)
  The sorting name of the corresponding TV series, if the media item is an episode in a TV series.
- [var isHD: Bool](./ishd.md)
  A Boolean value that indicates whether the video is high-definition.
- [var episode: String?](./episode.md)
  The name of the episode, if the media item is an episode of a TV series.
- [var episodeOrder: Int](./episodeorder.md)
  The numerical order of the episode, if the media item is an episode of a TV series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibmediaitemvideoinfo/season)*