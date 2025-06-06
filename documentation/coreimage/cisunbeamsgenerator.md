# CISunbeamsGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a sunbeams generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CISunbeamsGenerator
```

## Topics

### Instance Properties
- [var center: CGPoint](cisunbeamsgenerator/3228767-center.md)
  The x and y position to use as the center of the sunbeam pattern.
- [var color: CIColor](cisunbeamsgenerator/3228768-color.md)
  The color of the sun.
- [var maxStriationRadius: Float](cisunbeamsgenerator/3228769-maxstriationradius.md)
  The radius of the sunbeams.
- [var striationContrast: Float](cisunbeamsgenerator/3228770-striationcontrast.md)
  The contrast of the sunbeams.
- [var striationStrength: Float](cisunbeamsgenerator/3228771-striationstrength.md)
  The intensity of the sunbeams.
- [var sunRadius: Float](cisunbeamsgenerator/3228772-sunradius.md)
  The radius of the sun.
- [var time: Float](cisunbeamsgenerator/3228773-time.md)
  The duration of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](cifilter/3228419-sunbeamsgenerator.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisunbeamsgenerator)*