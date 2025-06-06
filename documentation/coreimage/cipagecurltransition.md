# CIPageCurlTransition

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a page curl transition filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPageCurlTransition
```

## Topics

### Instance Properties
- [var angle: Float](cipagecurltransition/3228618-angle.md)
  The angle of the curling page.
- [var backsideImage: CIImage?](cipagecurltransition/3228619-backsideimage.md)
  The image that appears on the back of the source image as the page curls to reveal the target image.
- [var extent: CGRect](cipagecurltransition/3228620-extent.md)
  The extent of the effect.
- [var radius: Float](cipagecurltransition/3228621-radius.md)
  The radius of the curl.
- [var shadingImage: CIImage?](cipagecurltransition/3228622-shadingimage.md)
  An image that looks like a shaded sphere enclosed in a square.

## Relationships

### Inherits From
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func pageCurlTransition() -> any CIFilter & CIPageCurlTransition](cifilter/3228375-pagecurltransition.md)
  Simulates the curl of a page, revealing the target image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipagecurltransition)*