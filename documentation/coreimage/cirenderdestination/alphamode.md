# alphaMode

**Framework**: Core Image  
**Kind**: property

The render destination’s representation of alpha (transparency) values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var alphaMode: CIRenderDestinationAlphaMode { get set }
```

#### Discussion

This property defaults to an appropriate value given the object with which you initialized the [`CIRenderDestination`](cirenderdestination.md).

## See Also

- [enum CIRenderDestinationAlphaMode](cirenderdestinationalphamode.md)
  Different ways of representing alpha.
- [var blendKernel: CIBlendKernel?](cirenderdestination/blendkernel.md)
  The destination’s blend kernel.
- [var blendsInDestinationColorSpace: Bool](cirenderdestination/blendsindestinationcolorspace.md)
  Indicator of whether to blend in the destination’s color space.
- [var colorSpace: CGColorSpace?](cirenderdestination/colorspace.md)
  The destination’s color space.
- [var width: Int](cirenderdestination/width.md)
  The render destination’s row width.
- [var height: Int](cirenderdestination/height.md)
  The render destination’s buffer height.
- [var isClamped: Bool](cirenderdestination/isclamped.md)
  Indicator of whether or not the destination clamps.
- [var isDithered: Bool](cirenderdestination/isdithered.md)
  Indicator of whether or not the destination dithers.
- [var isFlipped: Bool](cirenderdestination/isflipped.md)
  Indicator of whether the destination is flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirenderdestination/alphamode)*