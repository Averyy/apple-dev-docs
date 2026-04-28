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

- `URL`: A file-based URL that identifies the audio file. This URL must refer to a shared location that can be accessed by both the Watch app interface and the WatchKit extension. For more information, see [`Sharing Data`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/SharingData.html#//apple_ref/doc/uid/TP40014969-CH29) in [`App Programming Guide for watchOS`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969). This parameter must not be `nil`.
- `title`: The title to use for the audio file asset. Specify `nil` to use the title information from the file’s metadata. If you specify `nil` and no title is found in the metadata, the title is set to the file’s name.
- `albumTitle`: The album title to use for the audio file asset. Specify `nil` to use the album title information from the file’s metadata.
- `artist`: The artist to use for the audio file asset. Specify `nil` to use the artist information from the file’s metadata.

## See Also

- [convenience init(url: URL)](wkaudiofileasset/init(url:)-8ndda.md)
  Returns an asset for the audio file at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/init(url:title:albumtitle:artist:)-447fg)*