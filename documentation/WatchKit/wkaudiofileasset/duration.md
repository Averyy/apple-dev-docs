# duration

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The duration (in seconds) of the audio file.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var duration: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval duration;
```

## Discussion

The duration of the audio file is obtained from the audio file itself.

## See Also

### Getting the Asset’s Properties
- [var url: URL](./url.md)
  The URL of the audio file.
- [var title: String?](./title.md)
  The title information for the audio file.
- [var albumTitle: String?](./albumtitle.md)
  The album title information for the audio file.
- [var artist: String?](./artist.md)
  The artist information for the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/duration)*