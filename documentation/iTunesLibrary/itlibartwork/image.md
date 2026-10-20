# image

**Framework**: iTunes Library  
**Kind**: property  
**Role**: Instance Property

The artwork image.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.13+

## Declaration

```swift
var image: NSImage? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) NSImage * image;
```

## See Also

### Getting Artwork Info
- [var imageData: Data?](./imagedata.md)
  The raw image data of the artwork in the format that [`imageDataFormat`](./imagedataformat.md) specifies.
- [var imageDataFormat: ITLibArtworkFormat](./imagedataformat.md)
  The format of the artwork image data that [`imageData`](./imagedata.md) returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ituneslibrary/itlibartwork/image)*