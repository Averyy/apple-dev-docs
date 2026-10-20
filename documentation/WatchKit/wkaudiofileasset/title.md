# title

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The title information for the audio file.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
var title: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * title;
```

#### Discussion

If you do not set the title directly at initialization time, the asset object obtains the information from the audio file’s metadata. If the file does not contain any title metadata, the filename is used for the title.

## See Also

### Getting the Asset’s Properties
- [var url: URL](./url.md)
  The URL of the audio file.
- [var duration: TimeInterval](./duration.md)
  The duration (in seconds) of the audio file.
- [var albumTitle: String?](./albumtitle.md)
  The album title information for the audio file.
- [var artist: String?](./artist.md)
  The artist information for the audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/title)*