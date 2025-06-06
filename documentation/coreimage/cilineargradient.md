# CILinearGradient

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a linear gradient filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CILinearGradient
```

## Topics

### Instance Properties
- [var color0: CIColor](cilineargradient/3228542-color0.md)
  The first color to use in the gradient.
- [var color1: CIColor](cilineargradient/3228543-color1.md)
  The second color to use in the gradient.
- [var point0: CGPoint](cilineargradient/3228544-point0.md)
  The starting position of the gradient.
- [var point1: CGPoint](cilineargradient/3228545-point1.md)
  The ending position of the gradient.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func linearGradient() -> any CIFilter & CILinearGradient](cifilter/3228351-lineargradient.md)
  Generates a color gradient that varies along a linear axis between two defined endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilineargradient)*