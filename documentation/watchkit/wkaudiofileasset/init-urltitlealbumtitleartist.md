# init(url:title:albumTitle:artist:)

**Framework**: WatchKit  
**Kind**: init

Returns an audio file asset and sets the metadata for that item.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(url URL: URL, title: String?, albumTitle: String?, artist: String?)
```

#### Return Value

An initialized asset object.

## Parameters

- `URL`: This parameter must not be  .
- `title`: The title to use for the audio file asset. Specify   to use the title information from the file’s metadata. If you specify   and no title is found in the metadata, the title is set to the file’s name.
- `albumTitle`: The album title to use for the audio file asset. Specify   to use the album title information from the file’s metadata.
- `artist`: The artist to use for the audio file asset. Specify   to use the artist information from the file’s metadata.

## See Also

- [convenience init(url: URL)](init(url:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/init(url:)))
  Returns an asset for the audio file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/init(url:title:albumtitle:artist:))*