# artist

**Framework**: WatchKit  
**Kind**: property

The artist information for the audio file.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var artist: String? { get }
```

#### Discussion

If you do not set the artist name directly at initialization time, the asset object obtains the information from the audio file’s metadata.

## See Also

- [var url: URL](url.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/url))
  The URL of the audio file.
- [var duration: TimeInterval](duration.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/duration))
  The duration (in seconds) of the audio file.
- [var title: String?](title.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/title))
  The title information for the audio file.
- [var albumTitle: String?](albumtitle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/albumtitle))
  The album title information for the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/artist)*