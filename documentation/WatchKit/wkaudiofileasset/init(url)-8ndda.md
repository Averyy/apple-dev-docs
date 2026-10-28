# init(url:)

**Framework**: WatchKit  
**Kind**: init  
**Role**: Initializer

Returns an asset for the audio file at the specified URL.

**Availability**:
- watchOS 2.0+ - Deprecated in 6.0

## Declaration

```swift
convenience init(url URL: URL)
```

```objc
+ (instancetype) assetWithURL:(NSURL *) URL;
```

## Return Value

An initialized asset object.

## Discussion

This method creates an asset for the specified media file. The audio file’s title, album title, and artist information are derived from the metadata in the audio file itself.

## Parameters

- `URL`: A file-based URL that identifies the audio file. This URL must refer to a shared location that can be accessed by both the Watch app interface and the WatchKit extension. For more information, see [Sharing Data](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/SharingData.html#//apple_ref/doc/uid/TP40014969-CH29) in [App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969).

  This parameter must not be `nil`.

## See Also

### Creating an Asset
- [convenience init(url: URL, title: String?, albumTitle: String?, artist: String?)](./init%28url,title,albumtitle,artist%29-447fg.md)
  Returns an audio file asset and sets the metadata for that item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkaudiofileasset/init(url:)-8ndda)*