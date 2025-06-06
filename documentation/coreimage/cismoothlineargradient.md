# CISmoothLinearGradient

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a smooth linear gradient filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CISmoothLinearGradient
```

## Topics

### Instance Properties
- [var color0: CIColor](cismoothlineargradient/3228723-color0.md)
  The first color to use in the gradient.
- [var color1: CIColor](cismoothlineargradient/3228724-color1.md)
  The second color to use in the gradient.
- [var point0: CGPoint](cismoothlineargradient/3228725-point0.md)
  The starting position of the gradient.
- [var point1: CGPoint](cismoothlineargradient/3228726-point1.md)
  The ending position of the gradient.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func smoothLinearGradient() -> any CIFilter & CISmoothLinearGradient](cifilter/3228407-smoothlineargradient.md)
  Generates a gradient that blends colors along a linear axis between two defined endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cismoothlineargradient)*