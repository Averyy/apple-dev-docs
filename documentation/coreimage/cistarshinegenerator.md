# CIStarShineGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a star-shine generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIStarShineGenerator
```

## Topics

### Instance Properties
- [var center: CGPoint](cistarshinegenerator/3228749-center.md)
  The x and y position to use as the center of the star.
- [var color: CIColor](cistarshinegenerator/3228750-color.md)
  The color to use for the outer shell of the circular star.
- [var crossAngle: Float](cistarshinegenerator/3228751-crossangle.md)
  The angle of the cross pattern.
- [var crossOpacity: Float](cistarshinegenerator/3228752-crossopacity.md)
  The opacity of the cross pattern.
- [var crossScale: Float](cistarshinegenerator/3228753-crossscale.md)
  The size of the cross pattern.
- [var crossWidth: Float](cistarshinegenerator/3228754-crosswidth.md)
  The width of the cross pattern.
- [var epsilon: Float](cistarshinegenerator/3228755-epsilon.md)
  The length of the cross spikes.
- [var radius: Float](cistarshinegenerator/3228756-radius.md)
  The radius of the star.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](cifilter/3228415-starshinegenerator.md)
  Generates a star-shine image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cistarshinegenerator)*