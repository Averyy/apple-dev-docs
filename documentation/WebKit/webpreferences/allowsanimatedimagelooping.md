# allowsAnimatedImageLooping

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether or not the receiver allows animated images to loop.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var allowsAnimatedImageLooping: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsAnimatedImageLooping;
```

## Discussion

[`true`](../../Swift/true.md) if the web view should loop animated images, [`false`](../../Swift/false.md) otherwise.

If image looping is disabled, the web view displays it as a static image. The number of times that an image loops is determined by parameters of the image file itself and cannot be set in the web view.

## See Also

### Handling Images
- [var allowsAnimatedImages: Bool](./allowsanimatedimages.md)
  A Boolean that indicates whether or not the receiver allows animated images.
- [var loadsImagesAutomatically: Bool](./loadsimagesautomatically.md)
  A Boolean that indicates whether or not the web view allows images to be loaded automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/allowsanimatedimagelooping)*