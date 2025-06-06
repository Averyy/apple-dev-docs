# CIGaussianGradient

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a Gaussian gradient filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIGaussianGradient
```

## Topics

### Instance Properties
- [var center: CGPoint](cigaussiangradient/3228467-center.md)
  The center of the effect as x and y coordinates.
- [var color0: CIColor](cigaussiangradient/3228468-color0.md)
  The first color to use in the gradient.
- [var color1: CIColor](cigaussiangradient/3228469-color1.md)
  The second color to use in the gradient.
- [var radius: Float](cigaussiangradient/3228470-radius.md)
  The radius of the Gaussian distribution.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func gaussianGradient() -> any CIFilter & CIGaussianGradient](cifilter/3228332-gaussiangradient.md)
  Generates a gradient that varies from one color to another using a Gaussian distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cigaussiangradient)*