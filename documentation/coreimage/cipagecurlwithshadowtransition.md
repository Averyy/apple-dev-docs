# CIPageCurlWithShadowTransition

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a page-curl-with-shadow transition filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPageCurlWithShadowTransition
```

## Topics

### Instance Properties
- [var angle: Float](cipagecurlwithshadowtransition/3228624-angle.md)
  The angle of the curling page.
- [var backsideImage: CIImage?](cipagecurlwithshadowtransition/3228625-backsideimage.md)
  The image that appears on the back of the source image as the page curls to reveal the target image.
- [var extent: CGRect](cipagecurlwithshadowtransition/3228626-extent.md)
  The extent of the effect.
- [var radius: Float](cipagecurlwithshadowtransition/3228627-radius.md)
  The radius of the curl.
- [var shadowAmount: Float](cipagecurlwithshadowtransition/3228628-shadowamount.md)
  The strength of the shadow.
- [var shadowExtent: CGRect](cipagecurlwithshadowtransition/3228629-shadowextent.md)
  The rectagular portion of input image that casts a shadow.
- [var shadowSize: Float](cipagecurlwithshadowtransition/3228630-shadowsize.md)
  The maximum size, in pixels, of the shadow.

## Relationships

### Inherits From
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition](cifilter/3228376-pagecurlwithshadowtransition.md)
  Simulates the curl of a page, revealing the target image with added shadow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipagecurlwithshadowtransition)*