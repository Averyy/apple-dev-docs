# imageDataFormat

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The format of the artwork image data that [`imageData`](./imagedata.md) returns.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var imageDataFormat: ITLibArtworkFormat { get }
```

```objc
@property (nonatomic, assign, readonly) ITLibArtworkFormat imageDataFormat;
```

## See Also

### Getting Artwork Info
- [var image: NSImage?](./image.md)
  The artwork image.
- [var imageData: Data?](./imagedata.md)
  The raw image data of the artwork in the format that [`imageDataFormat`](./imagedataformat.md) specifies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibartwork/imagedataformat)*