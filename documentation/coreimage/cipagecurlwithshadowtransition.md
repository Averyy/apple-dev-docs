# CIPageCurlWithShadowTransition

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a page-curl-with-shadow transition filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIPageCurlWithShadowTransition : CITransitionFilter
```

## Topics

### Instance Properties
- [var angle: Float](cipagecurlwithshadowtransition/angle.md)
  The angle of the curling page.
- [var backsideImage: CIImage?](cipagecurlwithshadowtransition/backsideimage.md)
  The image that appears on the back of the source image as the page curls to reveal the target image.
- [var extent: CGRect](cipagecurlwithshadowtransition/extent.md)
  The extent of the effect.
- [var radius: Float](cipagecurlwithshadowtransition/radius.md)
  The radius of the curl.
- [var shadowAmount: Float](cipagecurlwithshadowtransition/shadowamount.md)
  The strength of the shadow.
- [var shadowExtent: CGRect](cipagecurlwithshadowtransition/shadowextent.md)
  The rectagular portion of input image that casts a shadow.
- [var shadowSize: Float](cipagecurlwithshadowtransition/shadowsize.md)
  The maximum size, in pixels, of the shadow.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition](cifilter-swift.class/pagecurlwithshadowtransition.md)
  Simulates the curl of a page, revealing the target image with added shadow.
- [protocol CITransitionFilter](citransitionfilter.md)
  The properties you use to configure a transition filter.
- [protocol CIBarsSwipeTransition](cibarsswipetransition.md)
  The properties you use to configure a bars swipe transition filter.
- [protocol CIAccordionFoldTransition](ciaccordionfoldtransition.md)
  The properties you use to configure an accordion fold transition filter.
- [protocol CICopyMachineTransition](cicopymachinetransition.md)
  The properties you use to configure a copy machine transition filter.
- [protocol CIDisintegrateWithMaskTransition](cidisintegratewithmasktransition.md)
  The properties you use to configure a disintegrate-with-mask transition filter.
- [protocol CIDissolveTransition](cidissolvetransition.md)
  The properties you use to configure a dissolve transition filter.
- [protocol CIFlashTransition](ciflashtransition.md)
  The properties you use to configure a flash transition filter.
- [protocol CIModTransition](cimodtransition.md)
  The properties you use to configure a mod transition filter.
- [protocol CIPageCurlTransition](cipagecurltransition.md)
  The properties you use to configure a page curl transition filter.
- [protocol CIRippleTransition](cirippletransition.md)
  The properties you use to configure a ripple transition filter.
- [protocol CISwipeTransition](ciswipetransition.md)
  The properties you use to configure a swipe transition filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipagecurlwithshadowtransition)*