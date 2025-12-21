# currentEDRHeadroom

**Framework**: UIKit  
**Kind**: property

The screen’s current headroom when displaying extended dynamic range content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+

## Declaration

```swift
@MainActor
var currentEDRHeadroom: CGFloat { get }
```

#### Discussion

 is the ratio of the luminance of the screen’s brightest white to the luminance of standard dynamic range (SDR) white, in the screen’s native color space. The screen’s current headroom limits all rendered content, and can change depending on its configuration and whether it’s displaying extended dynamic range (EDR) content.

To display EDR content in a [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer), set the layer’s [`wantsExtendedDynamicRangeContent`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer/wantsExtendedDynamicRangeContent) property to [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var referenceDisplayModeStatus: UIScreen.ReferenceDisplayModeStatus](uiscreen/referencedisplaymodestatus-swift.property.md)
  The status of the screen’s reference display mode.
- [UIScreen.ReferenceDisplayModeStatus](uiscreen/referencedisplaymodestatus-swift.enum.md)
  Describes a screen’s reference display mode status.
- [var potentialEDRHeadroom: CGFloat](uiscreen/potentialedrheadroom.md)
  The screen’s maximum headroom when displaying extended dynamic range content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscreen/currentedrheadroom)*