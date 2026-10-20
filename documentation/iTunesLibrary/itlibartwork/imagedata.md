# imageData

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The raw image data of the artwork in the format that [`imageDataFormat`](./imagedataformat.md) specifies.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var imageData: Data? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSData * imageData;
```

## See Also

### Getting Artwork Info
- [var image: NSImage?](./image.md)
  The artwork image.
- [var imageDataFormat: ITLibArtworkFormat](./imagedataformat.md)
  The format of the artwork image data that [`imageData`](./imagedata.md) returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibartwork/imagedata)*