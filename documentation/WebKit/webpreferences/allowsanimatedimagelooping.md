# allowsAnimatedImageLooping

**Framework**: Webkit  
**Kind**: property

A Boolean that indicates whether or not the receiver allows animated images to loop.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var allowsAnimatedImageLooping: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the web view should loop animated images, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

If image looping is disabled, the web view displays it as a static image. The number of times that an image loops is determined by parameters of the image file itself and cannot be set in the web view.

## See Also

- [var allowsAnimatedImages: Bool](webpreferences/allowsanimatedimages.md)
  A Boolean that indicates whether or not the receiver allows animated images.
- [var loadsImagesAutomatically: Bool](webpreferences/loadsimagesautomatically.md)
  A Boolean that indicates whether or not the web view allows images to be loaded automatically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpreferences/allowsanimatedimagelooping)*