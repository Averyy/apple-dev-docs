# CICheckerboardGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a checkerboard generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CICheckerboardGenerator
```

## Topics

### Instance Properties
- [var center: CGPoint](cicheckerboardgenerator/3228105-center.md)
  The center of the effect as x and y coordinates.
- [var color0: CIColor](cicheckerboardgenerator/3228106-color0.md)
  A color to use for the first set of squares.
- [var color1: CIColor](cicheckerboardgenerator/3228107-color1.md)
  A color to use for the second set of squares.
- [var sharpness: Float](cicheckerboardgenerator/3228108-sharpness.md)
  The sharpness of the edges in the pattern.
- [var width: Float](cicheckerboardgenerator/3228109-width.md)
  The width of the squares in the pattern.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func checkerboardGenerator() -> any CIFilter & CICheckerboardGenerator](cifilter/3228279-checkerboardgenerator.md)
  Generates a checkerboard image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicheckerboardgenerator)*