# init(url:)

**Framework**: WatchKit  
**Kind**: init

Returns an asset for the audio file at the specified URL.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(url URL: URL)
```

#### Return Value

An initialized asset object.

#### Discussion

This method creates an asset for the specified media file. The audio file’s title, album title, and artist information are derived from the metadata in the audio file itself.

## Parameters

- `URL`: This parameter must not be  .

## See Also

- [convenience init(url: URL, title: String?, albumTitle: String?, artist: String?)](init(url:title:albumtitle:artist:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/init(url:title:albumtitle:artist:)))
  Returns an audio file asset and sets the metadata for that item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/init(url:))*