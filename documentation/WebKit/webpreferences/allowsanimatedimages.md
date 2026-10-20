# allowsAnimatedImages

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether or not the receiver allows animated images.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var allowsAnimatedImages: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsAnimatedImages;
```

#### Discussion

Set to [`true`](../../Swift/true.md) if the web view should allow animated images, otherwise [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var autosaves: Bool](./autosaves.md)
  A Boolean that indicates whether or not the receiver’s attributes are automatically stored in the user defaults database.
### Handling Images
- [var allowsAnimatedImageLooping: Bool](./allowsanimatedimagelooping.md)
  A Boolean that indicates whether or not the receiver allows animated images to loop.
- [var loadsImagesAutomatically: Bool](./loadsimagesautomatically.md)
  A Boolean that indicates whether or not the web view allows images to be loaded automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/allowsanimatedimages)*