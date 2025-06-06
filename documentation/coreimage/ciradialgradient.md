# CIRadialGradient

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a radial gradient filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIRadialGradient
```

## Topics

### Instance Properties
- [var center: CGPoint](ciradialgradient/3228685-center.md)
  The center of the effect as x and y coordinates.
- [var color0: CIColor](ciradialgradient/3228686-color0.md)
  The first color to use in the gradient.
- [var color1: CIColor](ciradialgradient/3228687-color1.md)
  The second color to use in the gradient.
- [var radius0: Float](ciradialgradient/3228688-radius0.md)
  The radius of the starting circle to use in the gradient.
- [var radius1: Float](ciradialgradient/3228689-radius1.md)
  The radius of the ending circle to use in the gradient.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func radialGradient() -> any CIFilter & CIRadialGradient](cifilter/3228395-radialgradient.md)
  Generates a gradient that varies radially between two circles having the same center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciradialgradient)*