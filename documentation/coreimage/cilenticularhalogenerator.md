# CILenticularHaloGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a lenticular halo generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CILenticularHaloGenerator
```

## Topics

### Instance Properties
- [var center: CGPoint](cilenticularhalogenerator/3228520-center.md)
  The x and y position to use as the center of the halo.
- [var color: CIColor](cilenticularhalogenerator/3228521-color.md)
  The color of the halo.
- [var haloOverlap: Float](cilenticularhalogenerator/3228522-halooverlap.md)
  The separation of colors in the halo.
- [var haloRadius: Float](cilenticularhalogenerator/3228523-haloradius.md)
  The radius of the halo.
- [var haloWidth: Float](cilenticularhalogenerator/3228524-halowidth.md)
  The width of the halo, from its inner radius to its outer radius.
- [var striationContrast: Float](cilenticularhalogenerator/3228525-striationcontrast.md)
  The contrast of the halo colors.
- [var striationStrength: Float](cilenticularhalogenerator/3228526-striationstrength.md)
  The intensity of the halo colors.
- [var time: Float](cilenticularhalogenerator/3228527-time.md)
  The current time of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func lenticularHaloGenerator() -> any CIFilter & CILenticularHaloGenerator](cifilter/3228345-lenticularhalogenerator.md)
  Generates a lenticular halo image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilenticularhalogenerator)*