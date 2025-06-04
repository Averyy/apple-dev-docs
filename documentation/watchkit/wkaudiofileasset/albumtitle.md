# albumTitle

**Framework**: WatchKit  
**Kind**: property

The album title information for the audio file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var albumTitle: String? { get }
```

#### Discussion

If you do not set the album title directly at initialization time, the asset object obtains the information from the audio file’s metadata.

## See Also

- [var url: URL](url.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/url))
  The URL of the audio file.
- [var duration: TimeInterval](duration.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/duration))
  The duration (in seconds) of the audio file.
- [var title: String?](title.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/title))
  The title information for the audio file.
- [var artist: String?](artist.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/artist))
  The artist information for the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/albumtitle)*