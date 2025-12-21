# CIDisintegrateWithMaskTransition

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a disintegrate-with-mask transition filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIDisintegrateWithMaskTransition : CITransitionFilter
```

## Topics

### Instance Properties
- [var maskImage: CIImage?](cidisintegratewithmasktransition/maskimage.md)
  An image that defines the shape to use when disintegrating from the source to the target image.
- [var shadowDensity: Float](cidisintegratewithmasktransition/shadowdensity.md)
  The density of the shadow the mask creates.
- [var shadowOffset: CGPoint](cidisintegratewithmasktransition/shadowoffset.md)
  The offset of the shadow the mask creates.
- [var shadowRadius: Float](cidisintegratewithmasktransition/shadowradius.md)
  The radius of the shadow the mask creates.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)
- [CITransitionFilter](citransitionfilter.md)

## See Also

- [class func disintegrateWithMaskTransition() -> any CIFilter & CIDisintegrateWithMaskTransition](cifilter-swift.class/disintegratewithmasktransition.md)
  Transitions between two images using a mask image.
- [protocol CITransitionFilter](citransitionfilter.md)
  The properties you use to configure a transition filter.
- [protocol CIBarsSwipeTransition](cibarsswipetransition.md)
  The properties you use to configure a bars swipe transition filter.
- [protocol CIAccordionFoldTransition](ciaccordionfoldtransition.md)
  The properties you use to configure an accordion fold transition filter.
- [protocol CICopyMachineTransition](cicopymachinetransition.md)
  The properties you use to configure a copy machine transition filter.
- [protocol CIDissolveTransition](cidissolvetransition.md)
  The properties you use to configure a dissolve transition filter.
- [protocol CIFlashTransition](ciflashtransition.md)
  The properties you use to configure a flash transition filter.
- [protocol CIModTransition](cimodtransition.md)
  The properties you use to configure a mod transition filter.
- [protocol CIPageCurlTransition](cipagecurltransition.md)
  The properties you use to configure a page curl transition filter.
- [protocol CIPageCurlWithShadowTransition](cipagecurlwithshadowtransition.md)
  The properties you use to configure a page-curl-with-shadow transition filter.
- [protocol CIRippleTransition](cirippletransition.md)
  The properties you use to configure a ripple transition filter.
- [protocol CISwipeTransition](ciswipetransition.md)
  The properties you use to configure a swipe transition filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidisintegratewithmasktransition)*