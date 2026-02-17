# title

**Framework**: WatchKit  
**Kind**: property

The title information for the audio file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var title: String? { get }
```

#### Discussion

If you do not set the title directly at initialization time, the asset object obtains the information from the audio file’s metadata. If the file does not contain any title metadata, the filename is used for the title.

## See Also

- [var url: URL](wkaudiofileasset/url.md)
  The URL of the audio file.
- [var duration: TimeInterval](wkaudiofileasset/duration.md)
  The duration (in seconds) of the audio file.
- [var albumTitle: String?](wkaudiofileasset/albumtitle.md)
  The album title information for the audio file.
- [var artist: String?](wkaudiofileasset/artist.md)
  The artist information for the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/title)*